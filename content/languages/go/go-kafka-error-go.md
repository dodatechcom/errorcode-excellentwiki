---
title: "[Solution] Go Kafka Error — How to Fix"
description: "Fix Go Kafka errors. Handle broker connection, producer retries, consumer group rebalancing, and message serialization."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Kafka Error

Fix Go Kafka errors. Handle broker connection, producer retries, consumer group rebalancing, and message serialization.

## Why It Happens

- Kafka broker is not reachable or the bootstrap server address is wrong
- Producer retries are exhausted because of persistent broker unavailability
- Consumer group rebalancing causes offset reset and duplicate processing
- Message serialization fails because the serializer does not match the schema

## Common Error Messages

```
kafka: failed to reach broker
```
```
kafka: max retries exceeded
```
```
kafka: commit failed: topic not initialized
```
```
kafka: no available broker
```

## How to Fix It

### Solution 1: Configure Kafka producer with retries

```go
producer, _ := sarama.NewSyncProducer(brokers, sarama.NewConfig()
    Producer.Return.Successes = true,
    Producer.Retry.Max = 5,
    Producer.Retry.Backoff = 100 * time.Millisecond,
)
```

### Solution 2: Handle consumer group rebalancing

```go
group, _ := sarama.NewConsumerGroup(brokers, "my-group", config)
handler := &ConsumerGroupHandler{Ready: make(chan bool)}
go func() {
    for {
        if err := group.Consume(ctx, []string{"topic"}, handler); err != nil {
            log.Printf("consumer error: %v", err)
        }
    }
}()
```

### Solution 3: Handle message serialization

```go
type Event struct {
    Type    string    `json:"type"`
    Payload []byte    `json:"payload"`
    Time    time.Time `json:"time"`
}
encoded, _ := json.Marshal(event)
producer.SendMessage(&sarama.ProducerMessage{
    Topic: "events", Value: sarama.ByteEncoder(encoded),
})
```

### Solution 4: Handle producer errors

```go
partition, offset, err := producer.SendMessage(msg)
if err != nil {
    if errors.Is(err, sarama.ErrOutOfBrokers) {
        log.Println("no brokers available")
    }
}
```

## Common Scenarios

- A Kafka producer fails because the broker is temporarily unavailable
- A consumer group resets offsets because it was inactive for too long
- Message serialization fails because producer and consumer use different schemas

## Prevent It

- Configure producer retries and backoff for temporary broker failures
- Set appropriate session timeout and heartbeat interval for consumer groups
- Use a schema registry to ensure producer and consumer schema compatibility
