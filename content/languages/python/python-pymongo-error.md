---
title: "[Solution] Python PyMongo Error — How to Fix"
description: "Fix Python PyMongo errors. Resolve connection, authentication, and query failures in MongoDB operations."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python PyMongo Error

A `pymongo.errors.ConnectionFailure` or `pymongo.errors.OperationFailure` occurs when PyMongo fails to connect to MongoDB, encounters authentication errors, or when queries reference non-existent indexes.

## Why It Happens

PyMongo is the official Python driver for MongoDB. Errors arise when the MongoDB server is unreachable, when authentication credentials are wrong, when the database requires replica set read preference, or when document schemas do not match expected formats.

## Common Error Messages

- `ConnectionFailure: [Errno 111] Connection refused`
- `OperationFailure: authentication failed`
- `ServerSelectionTimeoutError: No servers found yet`
- `PyMongoError: ns not found`

## How to Fix It

### Fix 1: Configure connection properly

```python
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Wrong — no timeout or retry configuration
# client = MongoClient("mongodb://localhost:27017")

# Correct — configure connection parameters
client = MongoClient(
    "mongodb://localhost:27017",
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000,
    socketTimeoutMS=5000,
    maxPoolSize=100,
    retryWrites=True,
)

# Test connection
try:
    client.admin.command("ping")
    print("Connected to MongoDB")
except ConnectionFailure as e:
    print(f"Connection failed: {e}")
```

### Fix 2: Handle authentication

```python
from pymongo import MongoClient
from pymongo.errors import OperationFailure

# Wrong — no authentication
# client = MongoClient("mongodb://localhost:27017")

# Correct — use authentication
client = MongoClient(
    "mongodb://admin:password@localhost:27017/?authSource=admin"
)

try:
    client.admin.command("ping")
    db = client["mydatabase"]
    print(f"Connected to database: {db.name}")
except OperationFailure as e:
    print(f"Authentication failed: {e}")
```

### Fix 3: Use proper query patterns

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["testdb"]
collection = db["users"]

# Wrong — unindexed query
# collection.find({"email": "test@example.com"})

# Correct — create index first
collection.create_index("email", unique=True)

# Insert document
collection.insert_one({"name": "Alice", "email": "alice@example.com"})

# Query with index
user = collection.find_one({"email": "alice@example.com"})
print(f"User: {user['name']}")

# Use projection to limit fields
user = collection.find_one(
    {"email": "alice@example.com"},
    {"name": 1, "_id": 0}
)
print(f"Name only: {user}")
```

### Fix 4: Handle bulk operations

```python
from pymongo import MongoClient, InsertOne, UpdateOne
from pymongo.errors import BulkWriteError

client = MongoClient("mongodb://localhost:27017")
db = client["testdb"]
collection = db["users"]

# Wrong — individual inserts are slow
# for user in users:
#     collection.insert_one(user)

# Correct — use bulk operations
operations = [
    InsertOne({"name": "Alice", "email": "alice@example.com"}),
    InsertOne({"name": "Bob", "email": "bob@example.com"}),
    UpdateOne({"name": "Alice"}, {"$set": {"age": 25}}),
]

try:
    result = collection.bulk_write(operations, ordered=False)
    print(f"Inserted: {result.inserted_count}")
except BulkWriteError as bwe:
    print(f"Bulk write errors: {bwe.details}")
```

## Common Scenarios

- **Connection refused** — MongoDB server not running on the expected port.
- **Authentication failure** — Wrong username/password or auth database.
- **Replica set required** — Operations that require majority read concern need a replica set.

## Prevent It

- Always use `serverSelectionTimeoutMS` to avoid long hangs when the server is down.
- Create indexes before running queries that will be executed frequently.
- Use `bulk_write()` for multiple operations to reduce round trips.

## Related Errors

- [ConnectionFailure](/languages/python/connectionerror/) — cannot connect to server
- [OperationFailure](/languages/python/operation-error/) — database command failed
- [ServerSelectionTimeoutError](/languages/python/server-timeout/) — no server found
