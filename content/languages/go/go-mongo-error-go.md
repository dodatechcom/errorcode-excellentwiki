---
title: "[Solution] Go MongoDB Error — How to Fix"
description: "Fix Go MongoDB errors. Handle connection failures, BSON marshaling, index creation, transaction issues, and change streams."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go MongoDB Error

Fix Go MongoDB errors. Handle connection failures, BSON marshaling, index creation, transaction issues, and change streams.

## Why It Happens

- MongoDB server is not reachable or the connection string is incorrect
- BSON marshaling fails because of unsupported types or circular references
- Index creation fails because of duplicate index definitions
- MongoDB transactions require a replica set but standalone server is used

## Common Error Messages

```
mongo: no documents in result
```
```
mongo: connection pool exhausted
```
```
mongo: server selection timeout
```
```
Invalid document: Field cannot be used in element specification
```

## How to Fix It

### Solution 1: Configure MongoDB client properly

```go
clientOpts := options.Client().
    ApplyURI("mongodb://localhost:27017").
    SetMaxPoolSize(100).
    SetConnectTimeout(10 * time.Second)
client, err := mongo.Connect(ctx, clientOpts)
```

### Solution 2: Handle BSON marshaling errors

```go
type Record struct {
    ID        primitive.ObjectID `bson:"_id,omitempty" json:"id"`
    Name      string             `bson:"name"`
    Timestamp time.Time          `bson:"timestamp"`
}
```

### Solution 3: Create indexes properly

```go
indexModel := mongo.IndexModel{
    Keys:    bson.D{{Key: "email", Value: 1}},
    Options: options.Index().SetUnique(true),
}
_, err := collection.Indexes().CreateOne(ctx, indexModel)
```

### Solution 4: Use transactions with replica set

```go
session, _ := client.StartSession()
defer session.EndSession(ctx)
session.WithTransaction(ctx, func(sessCtx mongo.SessionContext) (interface{}, error) {
    _, err := collection1.InsertOne(sessCtx, doc1)
    _, err = collection2.InsertOne(sessCtx, doc2)
    return nil, err
})
```

## Common Scenarios

- A MongoDB query returns no documents because the collection name is wrong
- A BSON marshaling error occurs because a struct field has an unsupported type
- A MongoDB transaction fails because the deployment is not a replica set

## Prevent It

- Always check for mongo.ErrNoDocuments instead of nil document
- Use primitive types (ObjectID, DateTime) for MongoDB-specific types
- Ensure MongoDB replica set is configured before using transactions
