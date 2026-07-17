---
title: "[Solution] mongo-go: Server Selection Timeout Fix"
description: "Fix mongo-go driver server selection timeout errors. Handle replica set issues, DNS resolution, and connection pool configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# mongo-go: Server Selection Timeout

This error occurs when the mongo-go driver cannot select a server from the topology within the configured timeout. It is the MongoDB driver's equivalent of a connection timeout.

## What This Error Means

Common error messages:

- `server selection timeout: topology closed`
- `server selection timeout: context deadline exceeded`
- `server selection timeout: dial tcp 127.0.0.1:27017: connect: connection refused`
- `no eligible servers`

The mongo-go driver maintains a topology view of the MongoDB deployment. When it cannot find a suitable server for the requested operation within the timeout, it returns this error.

## Common Causes

```go
// Cause 1: MongoDB not running
client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://localhost:27017"))

// Cause 2: Wrong replica set name
opts := options.Client().ApplyURI("mongodb://rs0/mongo1:27017,mongo2:27017/?replicaSet=wrong-name")

// Cause 3: Short server selection timeout
opts := options.Client().SetServerSelectionTimeout(100 * time.Millisecond)

// Cause 4: DNS resolution failure
client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://mongo-cluster:27017"))

// Cause 5: All nodes in replica set are down
```

## How to Fix

### Fix 1: Set appropriate server selection timeout

```go
clientOpts := options.Client().
    ApplyURI("mongodb://localhost:27017").
    SetServerSelectionTimeout(10 * time.Second).
    SetConnectTimeout(10 * time.Second)

client, err := mongo.Connect(ctx, clientOpts)
if err != nil {
    log.Fatal(err)
}
```

### Fix 2: Configure connection pool

```go
clientOpts := options.Client().
    ApplyURI("mongodb://localhost:27017").
    SetMaxPoolSize(100).
    SetMinPoolSize(10).
    SetMaxConnIdleTime(5 * time.Minute)

client, err := mongo.Connect(ctx, clientOpts)
```

### Fix 3: Verify connection on startup

```go
func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    defer cancel()

    client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://localhost:27017"))
    if err != nil {
        log.Fatal(err)
    }

    if err = client.Ping(ctx, nil); err != nil {
        log.Fatal("MongoDB is not reachable:", err)
    }
    defer client.Disconnect(ctx)

    log.Println("Connected to MongoDB")
}
```

### Fix 4: Handle replica set topology

```go
// For replica set, include all members in the URI
uri := "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=myrs"

clientOpts := options.Client().
    ApplyURI(uri).
    SetServerSelectionTimeout(15 * time.Second).
    SetDirect(false)

client, err := mongo.Connect(ctx, clientOpts)
```

### Fix 5: Add health monitoring

```go
func monitorTopology(ctx context.Context, client *mongo.Client) {
    ticker := time.NewTicker(30 * time.Second)
    for range ticker.C {
        if err := client.Ping(ctx, nil); err != nil {
            log.Printf("MongoDB ping failed: %v", err)
        }
    }
}

go monitorTopology(ctx, client)
```

## Examples

```
server selection timeout: topology closed
```

```go
// Fix: wrap operations with context timeout
func findUser(ctx context.Context, collection *mongo.Collection, id string) (*User, error) {
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()

    var user User
    err := collection.FindOne(ctx, bson.M{"_id": id}).Decode(&user)
    if err != nil {
        if errors.Is(err, mongo.ErrNoDocuments) {
            return nil, fmt.Errorf("user not found: %s", id)
        }
        return nil, err
    }
    return &user, nil
}
```

## Related Errors

- [go-mongo-error]({{< relref "/languages/go/go-mongo-error" >}}) — basic MongoDB error
- [context-deadline]({{< relref "/languages/go/context-deadline" >}}) — context deadline exceeded
- [go-postgres-error-v2]({{< relref "/languages/go/go-postgres-error-v2" >}}) — PostgreSQL connection error
