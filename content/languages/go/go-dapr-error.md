---
title: "[Solution] Go Dapr Error — How to Fix"
description: "Fix Go Dapr errors. Handle sidecar connection, service invocation, state management, and pub/sub."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Dapr Error

Fix Go Dapr errors. Handle sidecar connection, service invocation, state management, and pub/sub.

## Why It Happens

- Dapr sidecar is not running causing connection refused errors
- Service invocation fails because of wrong app-id or port configuration
- State store operations fail because of incorrect key configuration
- Pub/sub messages are not being received because of missing subscription

## Common Error Messages

```
dapr: connection refused
```
```
dapr: service not found
```
```
dapr: state store not configured
```
```
dapr: pub/sub subscription not registered
```

## How to Fix It

### Solution 1: Connect to Dapr sidecar

```go
import "github.com/dapr/go-sdk/client"

ctx := context.Background()
c, err := client.NewClient()
if err != nil { log.Fatal(err) }
defer c.Close()
```

### Solution 2: Invoke service

```go
resp, err := c.InvokeMethodWithContent(ctx, "myapp", "/api/method", "post",
    &client.DataContent{ContentType: "application/json", Data: []byte(payload)},
)
```

### Solution 3: Manage state

```go
// Save state
err := c.SaveState(ctx, "statestore", "key1", []byte("value1"))
// Get state
state, err := c.GetState(ctx, "statestore", "key1")
// Delete state
err := c.DeleteState(ctx, "statestore", "key1")
```

### Solution 4: Subscribe to pub/sub

```go
import "github.com/dapr/go-sdk/service"

func main() {
    srv := service.New("myapp")
    srv.Subscribe("pubsub", "topic1", "sub1", func(ctx context.Context, e *service.TopicEvent) error {
        log.Printf("received: %s", e.Data)
        return nil
    })
    srv.Start()
}
```

## Common Scenarios

- Dapr sidecar is not running because daprd is not started
- Service invocation fails because the target app-id does not exist
- Pub/sub messages are not delivered because subscriptions are not registered

## Prevent It

- Ensure Dapr sidecar is running with daprd or dapr run
- Register pub/sub subscriptions before starting the service
- Use correct app-id and port when invoking services
