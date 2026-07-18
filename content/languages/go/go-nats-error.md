---
title: "[Solution] Go NATS Error — How to Fix"
description: "Fix Go NATS errors. Handle connection, pub/sub, request-reply, and JetStream."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go NATS Error

Fix Go NATS errors. Handle connection, pub/sub, request-reply, and JetStream.

## Why It Happens

- NATS connection fails because of wrong server URL
- Subscription does not receive messages because of wrong subject
- JetStream publish fails because stream is not configured
- NATS connection drops and is not automatically reconnected

## Common Error Messages

```
nats: connection refused
```
```
nats: no servers available
```
```
nats: timeout
```
```
nats: stream not found
```

## How to Fix It

### Solution 1: Connect to NATS

```go
import "github.com/nats-io/nats.go"

nc, err := nats.Connect("nats://localhost:4222")
if err != nil { log.Fatal(err) }
defer nc.Drain()
```

### Solution 2: Publish and subscribe

```go
nc.Subscribe("orders.new", func(msg *nats.Msg) {
    fmt.Printf("Received: %s\n", string(msg.Data))
})
nc.Publish("orders.new", []byte("order-123"))
```

### Solution 3: Request-reply

```go
nc.Subscribe("api.getUser", func(msg *nats.Msg) {
    msg.Respond([]byte(`{"name":"Alice"}`))
})
resp, _ := nc.Request("api.getUser", []byte(`{"id":1}`), time.Second)
```

### Solution 4: Use JetStream

```go
js, _ := nc.JetStream()
js.AddStream(&nats.StreamConfig{Name: "ORDERS", Subjects: []string{"orders.*"}})
js.Publish("orders.new", []byte("order-123"))
sub, _ := js.Subscribe("orders.new", handler)
```

## Common Scenarios

- NATS connection fails because server is not running
- JetStream messages are not delivered because stream is not created
- Request times out because no subscriber is listening

## Prevent It

- Handle connection errors with reconnection callbacks
- Create JetStream streams before publishing
- Use nc.Drain() to cleanly disconnect
