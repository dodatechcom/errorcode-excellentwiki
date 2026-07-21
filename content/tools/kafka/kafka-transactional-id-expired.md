---
title: "[Solution] Kafka Transactional ID Expired Error"
description: "Fix Kafka transactional ID expired errors. Resolve producer transaction timeout and fencing issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Transactional ID Expired Error

Kafka transactional ID expired errors occur when a producer's transactional ID is fenced or expired because the transaction timeout elapsed without a commit or abort.

## Common Causes

- Transaction took longer than transaction.timeout.ms
- Producer was idle for too long without completing the transaction
- Another producer with the same transactional.id registered
- Transaction coordinator lost the transaction metadata

## How to Fix

1. Increase the transaction timeout:

```properties
transaction.timeout.ms=120000
transactional.id=my-producer-1
```

2. Ensure transactions are committed or aborted promptly:

```java
producer.beginTransaction();
try {
    producer.send(record).get();
    producer.commitTransaction();
} catch (Exception e) {
    producer.abortTransaction();
}
```

3. Use unique transactional IDs per producer instance:

```properties
transaction.id=producer-${HOSTNAME}-${PID}
```

4. Check transaction coordinator status:

```bash
kafka-transactions.sh --bootstrap-server localhost:9092 \
  --describe --transactional-id my-producer-1
```

## Examples

```bash
# List active transactions
kafka-transactions.sh --bootstrap-server localhost:9092 --list

# Check transaction coordinator
kafka-console-producer.sh --bootstrap-server localhost:9092 \
  --topic __transaction_state --property print.key=true
```
