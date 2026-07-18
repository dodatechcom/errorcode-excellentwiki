---
title: "[Solution] Go RabbitMQ Error — How to Fix"
description: "Fix Go RabbitMQ errors. Handle AMQP connection failures, channel errors, message acknowledgment, and prefetch configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go RabbitMQ Error

Fix Go RabbitMQ errors. Handle AMQP connection failures, channel errors, message acknowledgment, and prefetch configuration.

## Why It Happens

- RabbitMQ server is not reachable or credentials are incorrect
- Channel error causes the channel to be closed requiring reconnection
- Messages are redelivered because of incorrect acknowledgment handling
- Prefetch count is not set causing consumer to be overwhelmed

## Common Error Messages

```
amqp: connection closed
```
```
amqp: channel closed
```
```
amqp: connection refused
```
```
delivery tag not found
```

## How to Fix It

### Solution 1: Configure AMQP connection with proper settings

```go
conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
if err != nil { return fmt.Errorf("dial: %w", err) }
defer conn.Close()
ch, err := conn.Channel()
```

### Solution 2: Handle channel errors with reconnection

```go
func connectWithRetry(urls []string) (*amqp.Connection, error) {
    for _, url := range urls {
        for attempt := 0; attempt < 5; attempt++ {
            conn, err := amqp.Dial(url)
            if err == nil { return conn, nil }
            time.Sleep(time.Duration(attempt) * time.Second)
        }
    }
    return nil, fmt.Errorf("all attempts failed")
}
```

### Solution 3: Set QoS prefetch count

```go
err = ch.Qos(10, 0, false)
```

### Solution 4: Handle message acknowledgment correctly

```go
for msg := range msgs {
    if err := process(msg.Body); err != nil {
        msg.Nack(false, true)
    } else {
        msg.Ack(false)
    }
}
```

## Common Scenarios

- A RabbitMQ consumer is overwhelmed because prefetch is not configured
- A message is processed multiple times because acknowledgment is not sent on success
- The AMQP channel closes because of a protocol error requiring full reconnection

## Prevent It

- Set QoS prefetch count to limit unacknowledged messages per consumer
- Always acknowledge messages on success and nack on failure with requeue
- Implement connection and channel recovery with automatic reconnection
