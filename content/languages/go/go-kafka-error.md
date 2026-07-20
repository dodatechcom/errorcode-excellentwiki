---
title: "[Solution] sarama/kafka-go No Brokers Available Fix"
description: "Fix Kafka Go client errors when no brokers are available. Handle broker discovery, SASL auth, and topic configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# sarama/kafka-go No Brokers Available

The Kafka Go client (sarama or kafka-go) fails to connect to any Kafka broker due to wrong broker addresses, network issues, TLS misconfiguration, or the broker not being ready. Kafka uses a metadata exchange to discover brokers, so the initial seed broker must be reachable.

## Common Causes

```go
// Cause 1: Wrong broker address
config := sarama.NewConfig()
config.Producer.Return.Successes = true
producer, err := sarama.NewSyncProducer([]string{"wrong-host:9092"}, config)
// dial tcp: lookup wrong-host: no such host

// Cause 2: Kafka not ready — broker starting up
producer, err := sarama.NewSyncProducer([]string{"kafka:9092"}, config)
// not available: server not ready yet

// Cause 3: SASL authentication missing
config := sarama.NewConfig()
config.Net.SASL.Enable = true
// missing SASL username/password configuration

// Cause 4: TLS required but not configured
config.Net.TLS.Enable = true
// missing config.Net.TLS.Config with certificates

// Cause 5: Topic does not exist and auto-create is disabled
msg := &sarama.ProducerMessage{Topic: "nonexistent-topic", Value: sarama.StringEncoder("hello")}
producer.SendMessage(msg)
// kafka: failed to produce: topic not authorized
```

## How to Fix

### Fix 1: Configure producers with retry and proper broker list

```go
import (
    "fmt"
    "log"
    "time"

    "github.com/IBM/sarama"
)

func createProducer() (sarama.SyncProducer, error) {
    config := sarama.NewConfig()
    config.Producer.Return.Successes = true
    config.Producer.Timeout = 10 * time.Second
    config.Producer.Retry.Max = 3
    config.Metadata.Retry.Max = 5
    config.Metadata.RefreshFrequency = 10 * time.Minute

    brokers := []string{"kafka1:9092", "kafka2:9092", "kafka3:9092"}
    producer, err := sarama.NewSyncProducer(brokers, config)
    if err != nil {
        return nil, fmt.Errorf("create producer: %w", err)
    }
    return producer, nil
}
```

### Fix 2: Configure consumers with proper offset handling

```go
func createConsumer() (sarama.Consumer, error) {
    config := sarama.NewConfig()
    config.Consumer.Return.Errors = true
    config.Consumer.Offsets.Initial = sarama.OffsetOldest

    consumer, err := sarama.NewConsumer([]string{"kafka1:9092", "kafka2:9092"}, config)
    if err != nil {
        return nil, fmt.Errorf("create consumer: %w", err)
    }
    return consumer, nil
}
```

### Fix 3: Use cluster consumer for group-based consumption

```go
func consumeGroup() {
    config := sarama.NewConfig()
    config.Consumer.Group.Rebalance.Strategy = sarama.BalanceStrategyRoundRobin
    config.Consumer.Offsets.Initial = sarama.OffsetOldest

    group, err := sarama.NewConsumerGroup([]string{"kafka1:9092"}, "my-group", config)
    if err != nil {
        log.Fatal(err)
    }
    defer group.Close()

    handler := &ConsumerGroupHandler{}
    for {
        if err := group.Consume(context.Background(), []string{"my-topic"}, handler); err != nil {
            log.Printf("consume error: %v", err)
        }
    }
}

type ConsumerGroupHandler struct{}

func (h *ConsumerGroupHandler) Setup(_ sarama.ConsumerGroupSession) error   { return nil }
func (h *ConsumerGroupHandler) Cleanup(_ sarama.ConsumerGroupSession) error { return nil }
func (h *ConsumerGroupHandler) ConsumeClaim(session sarama.ConsumerGroupSession, claim sarama.ConsumerGroupClaim) error {
    for msg := range claim.Messages() {
        fmt.Printf("Message: %s = %s\n", msg.Key, msg.Value)
        session.MarkMessage(msg, "")
    }
    return nil
}
```

## Examples

```go
package main

import (
    "fmt"
    "log"
    "time"

    "github.com/IBM/sarama"
)

func main() {
    config := sarama.NewConfig()
    config.Producer.Return.Successes = true

    producer, err := sarama.NewSyncProducer([]string{"localhost:9092"}, config)
    if err != nil {
        log.Fatal(err)
    }
    defer producer.Close()

    msg := &sarama.ProducerMessage{
        Topic: "test-topic",
        Key:   sarama.StringEncoder("key1"),
        Value: sarama.StringEncoder("hello kafka"),
    }

    partition, offset, err := producer.SendMessage(msg)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Message sent to partition %d at offset %d\n", partition, offset)
}
```

## Related Errors

- [net-dial]({{< relref "/languages/go/net-dial" >}}) — TCP connection to broker fails
- [grpc-unavailable]({{< relref "/languages/go/grpc-unavailable" >}}) — if using gRPC-based Kafka protocol
- [tls-handshake]({{< relref "/languages/go/tls-handshake-error" >}}) — TLS negotiation with broker fails
