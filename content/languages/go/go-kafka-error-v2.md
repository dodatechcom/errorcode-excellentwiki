---
title: "[Solution] kafka-go: No Brokers Available Fix"
description: "Fix kafka-go no brokers available errors. Handle connection failures, SASL authentication, and topic configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["kafka", "kafka-go", "broker", "message-queue", "streaming"]
weight: 5
---

# kafka-go: No Brokers Available

This error occurs when the kafka-go library cannot connect to any Kafka broker. It covers standalone, SASL-authenticated, and cluster topologies.

## What This Error Means

Common error messages:

- `no brokers available`
- `dial tcp 127.0.0.1:9092: connect: connection refused`
- `kafka: client has run out of available brokers to talk to`
- `connection refused: kafka server not reachable`

The kafka-go library tries to connect to at least one broker in the configured list. If none are reachable, it returns the "no brokers available" error.

## Common Causes

```go
// Cause 1: Kafka not running
r := kafka.NewReader(kafka.ReaderConfig{
    Brokers: []string{"localhost:9092"},
    Topic:   "my-topic",
})

// Cause 2: Wrong broker address
Brokers: []string{"kafka:9092"}, // actual is on 9093

// Cause 3: SASL authentication required but not configured
// Broker requires SASL, client connects without auth

// Cause 4: Broker list empty
Brokers: []string{},

// Cause 5: Network/firewall blocking port 9092
```

## How to Fix

### Fix 1: Configure reader with timeout and retry

```go
r := kafka.NewReader(kafka.ReaderConfig{
    Brokers:        []string{"localhost:9092"},
    Topic:          "my-topic",
    GroupID:        "my-group",
    MinBytes:       1,
    MaxBytes:       10e6,
    DialTimeout:    10 * time.Second,
    ReadTimeout:    10 * time.Second,
    WriteTimeout:   10 * time.Second,
    MaxAttempts:    3,
})

ctx := context.Background()
msg, err := r.ReadMessage(ctx)
if err != nil {
    log.Printf("Failed to read message: %v", err)
}
```

### Fix 2: Use writer with multiple brokers

```go
w := &kafka.Writer{
    Addr:         kafka.TCP("kafka1:9092", "kafka2:9092", "kafka3:9092"),
    Topic:        "my-topic",
    BatchTimeout: 10 * time.Millisecond,
    BatchSize:    100,
    Balancer:     &kafka.LeastBytes{},
    RequiredAcks: kafka.RequireAll,
}

err := w.WriteMessages(ctx, kafka.Message{
    Key:   []byte("key"),
    Value: []byte("value"),
})
```

### Fix 3: Configure SASL authentication

```go
w := &kafka.Writer{
    Addr: kafka.TCP("kafka:9093"),
    Transport: &kafka.Transport{
        SASL: kafka.SASLMechanism{
            Mechanism: kafka.SASLTypeScramSHA256,
            Username:  "user",
            Password:  "pass",
        },
        TLS: &tls.Config{},
    },
}
```

### Fix 4: Verify brokers on startup

```go
func checkBrokers(brokers []string, timeout time.Duration) error {
    for _, broker := range brokers {
        conn, err := net.DialTimeout("tcp", broker, timeout)
        if err != nil {
            log.Printf("Broker %s unreachable: %v", broker, err)
            continue
        }
        conn.Close()
        return nil
    }
    return fmt.Errorf("no brokers available from: %v", brokers)
}

if err := checkBrokers([]string{"kafka1:9092", "kafka2:9092"}, 5*time.Second); err != nil {
    log.Fatal(err)
}
```

### Fix 5: Use kafka-go admin for topic creation

```go
conn, err := kafka.Dial("tcp", "kafka:9092")
if err != nil {
    log.Fatal(err)
}
defer conn.Close()

err = conn.CreateTopics(kafka.TopicConfig{
    Topic:             "my-topic",
    NumPartitions:     3,
    ReplicationFactor: 1,
})
if err != nil {
    log.Printf("Topic creation failed: %v", err)
}
```

## Examples

```
no brokers available
```

```go
// Fix: create reader with backoff retry
func createReader(brokers []string, topic string) *kafka.Reader {
    return kafka.NewReader(kafka.ReaderConfig{
        Brokers:     brokers,
        Topic:       topic,
        GroupID:     "my-group",
        DialTimeout: 10 * time.Second,
        MaxAttempts: 5,
    })
}
```

## Related Errors

- [go-nats-error]({{< relref "/languages/go/go-nats-error" >}}) — NATS connection error
- [go-redis-error-v2]({{< relref "/languages/go/go-redis-error-v2" >}}) — Redis connection error
- [go-postgres-error-v2]({{< relref "/languages/go/go-postgres-error-v2" >}}) — PostgreSQL connection error
