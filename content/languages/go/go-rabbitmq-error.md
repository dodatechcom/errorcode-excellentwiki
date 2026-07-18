---
title: "[Solution] Go RabbitMQ Error — How to Fix"
description: "Fix Go RabbitMQ errors. Handle connection, channel, publish, consume, and queue configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go RabbitMQ Error

Fix Go RabbitMQ errors. Handle connection, channel, publish, consume, and queue configuration.

## Why It Happens

- RabbitMQ connection fails because of wrong URL or credentials
- Channel is closed because of prefetch count issues
- Publish fails because exchange is not declared
- Consumer does not receive messages because queue is not bound

## Common Error Messages

```
amqp: connection refused
```
```
amqp: channel closed
```
```
amqp: exchange not found
```
```
amqp: queue not found
```

## How to Fix It

### Solution 1: Connect to RabbitMQ

```go
conn, _ := amqp.Dial("amqp://guest:guest@localhost:5672/")
defer conn.Close()
ch, _ := conn.Channel()
defer ch.Close()
```

### Solution 2: Declare queue and publish

```go
q, _ := ch.QueueDeclare("orders", true, false, false, false, nil)
ch.Publish("", q.Name, false, false, amqp.Publishing{
    ContentType: "application/json",
    Body:        body,
})
```

### Solution 3: Consume messages

```go
msgs, _ := ch.Consume(q.Name, "", false, false, false, false, nil)
for msg := range msgs {
    process(msg.Body)
    msg.Ack(false)
}
```

### Solution 4: Declare exchange

```go
ch.ExchangeDeclare("logs", "topic", true, false, false, false, nil)
ch.QueueBind(q.Name, "logs.*", "logs", false, nil)
```

## Common Scenarios

- RabbitMQ connection fails because of wrong URL format
- Messages are not delivered because exchange is not declared
- Consumer stops receiving messages because channel is closed

## Prevent It

- Always declare exchanges and queues before publishing
- Use message acknowledgments to prevent message loss
- Set up connection recovery with notify
