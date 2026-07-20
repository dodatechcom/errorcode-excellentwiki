---
title: "[Solution] mongo-go-driver Server Selection Timeout Fix"
description: "Fix MongoDB Go driver server selection timeout. Handle replica sets, sharded clusters, and connection pooling."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# mongo-go-driver Server Selection Timeout

The MongoDB Go driver fails to select a server from the cluster within the configured timeout. This occurs when the connection string is wrong, MongoDB is down, DNS resolution fails for replica set hosts, or the driver cannot reach any cluster member.

## Common Causes

```go
// Cause 1: Wrong connection string or host unreachable
client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://wrong-host:27017"))
// server selection error: context deadline exceeded

// Cause 2: DNS resolution failure for replica set hosts
client, err := mongo.Connect(ctx, options.Client().ApplyURI(
    "mongodb://rs0/node1.example.com:27017,node2.example.com:27017",
))
// server selection error: lookup node1.example.com: no such host

// Cause 3: Authentication failure blocks server selection
client, err := mongo.Connect(ctx, options.Client().ApplyURI(
    "mongodb://user:wrongpass@localhost:27017/mydb",
))
// auth error: authentication failed

// Cause 4: TLS certificate issues
opts := options.Client().ApplyURI("mongodb://localhost:27017").
    SetTLSConfig(&tls.Config{InsecureSkipVerify: false})
// tls: certificate signed by unknown authority

// Cause 5: Server selection timeout too short
opts := options.Client().
    ApplyURI("mongodb://localhost:27017").
    SetServerSelectionTimeout(1 * time.Millisecond)
```

## How to Fix

### Fix 1: Validate connection and test with ping

```go
import (
    "context"
    "fmt"
    "time"

    "go.mongodb.org/mongo-driver/v2/mongo"
    "go.mongodb.org/mongo-driver/v2/mongo/options"
)

func connectMongo() (*mongo.Client, error) {
    opts := options.Client().
        ApplyURI("mongodb://localhost:27017").
        SetServerSelectionTimeout(10 * time.Second).
        SetConnectTimeout(10 * time.Second)

    client, err := mongo.Connect(opts)
    if err != nil {
        return nil, fmt.Errorf("mongo connect: %w", err)
    }

    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    defer cancel()

    if err := client.Ping(ctx, nil); err != nil {
        return nil, fmt.Errorf("mongo ping: %w", err)
    }
    return client, nil
}
```

### Fix 2: Configure replica set connection properly

```go
uri := "mongodb://user:pass@mongo1:27017,mongo2:27017,mongo3:27017/mydb?replicaSet=rs0&authSource=admin"

opts := options.Client().ApplyURI(uri).
    SetServerSelectionTimeout(15 * time.Second).
    SetDirect(false)

client, err := mongo.Connect(opts)
```

### Fix 3: Enable retryable reads and writes

```go
opts := options.Client().
    ApplyURI("mongodb://localhost:27017").
    SetRetryWrites(true).
    SetRetryReads(true)

client, err := mongo.Connect(opts)
```

## Examples

```go
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "go.mongodb.org/mongo-driver/v2/bson"
    "go.mongodb.org/mongo-driver/v2/mongo"
    "go.mongodb.org/mongo-driver/v2/mongo/options"
)

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    defer cancel()

    client, err := mongo.Connect(options.Client().
        ApplyURI("mongodb://localhost:27017").
        SetServerSelectionTimeout(10*time.Second))
    if err != nil {
        log.Fatal(err)
    }
    defer client.Disconnect(ctx)

    if err := client.Ping(ctx, nil); err != nil {
        log.Fatalf("Cannot reach MongoDB: %v", err)
    }

    coll := client.Database("mydb").Collection("users")
    result, err := coll.InsertOne(ctx, bson.M{"name": "Alice", "age": 30})
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Inserted:", result.InsertedID)
}
```

## Related Errors

- [context-deadline-exceeded]({{< relref "/languages/go/context-deadline" >}}) — server selection timeout
- [net-dns-lookup]({{< relref "/languages/go/net-dns-lookup" >}}) — DNS resolution fails for MongoDB hosts
- [connection-refused]({{< relref "/languages/go/net-dial" >}}) — TCP connection to MongoDB port fails
