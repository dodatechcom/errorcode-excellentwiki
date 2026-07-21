---
title: "[Solution] RabbitMQ Peer Verification Error"
description: "Fix RabbitMQ peer verification error. Resolve TLS peer certificate verification issues."
tools: ["rabbitmq"]
error-types: ["tool-error"]
severities: ["error"]
---

# RabbitMQ Peer Verification Error

TLS peer certificate verification fails. The client or server rejects the peer certificate.

## Common Causes

- Peer certificate is invalid
- Certificate CN does not match hostname
- CA certificate is not trusted

## How to Fix

### Solution 1

```bash
openssl s_client -connect localhost:5671 -showcerts
```

## Related Pages

- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})
- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})
- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})
