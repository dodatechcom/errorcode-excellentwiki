---
title: "[Solution] Apache Kafka Controller Error"
description: "Fix Apache Kafka controller errors. Learn why this happens and how to resolve it quickly."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Apache Kafka Controller Error

Kafka controller errors occur when the cluster controller fails to manage metadata or elections.

## Why This Happens

- Controller not available
- Election failed
- Metadata sync error
- Controller overload

## Common Error Messages

- `controller_not_available_error`
- `controller_election_error`
- `controller_metadata_error`
- `controller_overload_error`

## How to Fix It

### Solution 1: Check controller status

View controller:

```bash
kafka-broker-api-versions.sh --bootstrap-server localhost:9092
```

### Solution 2: Fix controller issues

Check controller logs for errors.

### Solution 3: Monitor controller health

Track controller metrics.


## Common Scenarios

- **Controller not available:** Check controller process.
- **Election failed:** Verify ZooKeeper/KRaft connectivity.

## Prevent It

- Monitor controller health
- Set up alerts
- Plan capacity
