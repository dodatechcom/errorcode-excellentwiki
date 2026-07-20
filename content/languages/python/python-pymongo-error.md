---
title: "[Solution] Python PyMongo Error — MongoDB Driver Failures"
description: "Fix Python PyMongo errors like PyMongoError, ConnectionFailure, OperationFailure, timeout, and bulk write errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 429
---

# Python PyMongo Error — MongoDB Driver Failures

PyMongo errors occur when the driver cannot connect to MongoDB, operations fail due to invalid queries, indexes are missing, or bulk writes encounter errors. These are common in data-driven applications.

## Common Causes

```python
# ConnectionFailure: cannot connect to MongoDB
from pymongo import MongoClient
client = MongoClient("mongodb://invalid-host:27017", serverSelectionTimeoutMS=1000)
client.admin.command("ping")

# OperationFailure: invalid query or index
from pymongo import MongoClient
client = MongoClient()
db = client["mydb"]
db.collection.find({"$invalidOperator": 1})  # bad query operator

# OperationFailure: duplicate key on insert
db.collection.insert_one({"_id": "duplicate", "name": "test"})
db.collection.insert_one({"_id": "duplicate", "name": "test2"})  # duplicate key

# BulkWriteError: partial failure in bulk operation
from pymongo import InsertOne
ops = [InsertOne({"_id": i}) for i in range(10)]
db.collection.bulk_write(ops, ordered=False)  # some may fail

# InvalidOperation: cursor already exhausted
cursor = db.collection.find()
for doc in cursor:
    pass
next(cursor)  # cursor exhausted
```

## How to Fix

### Fix 1: Verify Connection with Timeout
Always set a server selection timeout and verify connectivity.
```python
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

client = MongoClient(
    "mongodb://localhost:27017",
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000,
)

try:
    client.admin.command("ping")
    print("Connected to MongoDB")
except ConnectionFailure:
    print("Cannot connect to MongoDB server")
```

### Fix 2: Handle Duplicate Key Errors
Catch DuplicateKeyError when inserting documents.
```python
from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError

client = MongoClient()
db = client["mydb"]

try:
    db.users.insert_one({"email": "user@example.com", "name": "User"})
except DuplicateKeyError:
    print("User with this email already exists")
```

### Fix 3: Use Bulk Write with Error Handling
Handle partial failures in bulk operations.
```python
from pymongo import MongoClient, InsertOne
from pymongo.errors import BulkWriteError

client = MongoClient()
db = client["mydb"]

ops = [InsertOne({"_id": i, "name": f"item_{i}"}) for i in range(100)]
try:
    result = db.collection.bulk_write(ops, ordered=False)
    print(f"Inserted: {result.inserted_count}")
except BulkWriteError as bwe:
    print(f"Partial failure: {bwe.details}")
```

### Fix 4: Set Read/Write Concern for Reliability
Configure appropriate read and write concerns.
```python
from pymongo import MongoClient, ReadConcern, WriteConcern

client = MongoClient()
db = client["mydb"]
collection = db.get_collection(
    "mycollection",
    read_concern=ReadConcern("majority"),
    write_concern=WriteConcern(w="majority", wtimeout=5000),
)
collection.insert_one({"key": "value"})
```

### Fix 5: Use Context Managers for Cursors
Ensure cursers are properly closed after use.
```python
from pymongo import MongoClient

client = MongoClient()
db = client["mydb"]

with db.collection.find() as cursor:
    for doc in cursor:
        print(doc)
```

## Examples

```python
# Complete MongoDB operations with error handling
from pymongo import MongoClient
from pymongo.errors import (
    ConnectionFailure,
    OperationFailure,
    DuplicateKeyError,
    BulkWriteError,
)

class MongoDBClient:
    def __init__(self, uri="mongodb://localhost:27017"):
        self.client = MongoClient(uri, serverSelectionTimeoutMS=5000)

    def connect(self):
        try:
            self.client.admin.command("ping")
            return True
        except ConnectionFailure:
            return False

    def insert_document(self, db_name, collection_name, document):
        try:
            result = self.client[db_name][collection_name].insert_one(document)
            return result.inserted_id
        except DuplicateKeyError:
            raise ValueError("Document with this _id already exists")
        except OperationFailure as e:
            raise RuntimeError(f"Insert failed: {e}")

    def find_documents(self, db_name, collection_name, query=None):
        try:
            return list(self.client[db_name][collection_name].find(query or {}))
        except OperationFailure as e:
            raise RuntimeError(f"Find failed: {e}")
```

## Related Errors

- [Python redis-py Error](/languages/python/python-redis-py-error/)
- [Python Elasticsearch Error](/languages/python/python-elasticsearch-error/)
- [Python kafka-python Error](/languages/python/python-kafka-python-error/)
