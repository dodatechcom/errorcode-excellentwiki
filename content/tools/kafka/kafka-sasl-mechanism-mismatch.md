---
title: "[Solution] Kafka SASL Mechanism Mismatch Error"
description: "Fix Kafka SASL mechanism mismatch errors. Resolve authentication failures from SASL protocol disagreements."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka SASL Mechanism Mismatch Error

Kafka SASL mechanism mismatch errors occur when the client and broker are configured with different SASL authentication mechanisms, causing the handshake to fail.

## Common Causes

- Client configured with SCRAM-SHA-256 while broker expects GSSAPI
- SASL mechanism changed on broker without updating clients
- Mixed mechanism configuration across multiple brokers
- JAAS configuration referencing the wrong mechanism

## How to Fix

1. Verify broker SASL configuration:

```properties
listeners=SASL_PLAINTEXT://0.0.0.0:9092
sasl.enabled.mechanisms=SCRAM-SHA-256
sasl.mechanism.inter.broker.protocol=SCRAM-SHA-256
```

2. Match client SASL mechanism to broker:

```properties
security.protocol=SASL_PLAINTEXT
sasl.mechanism=SCRAM-SHA-256
```

3. Create the SASL user if using SCRAM:

```bash
kafka-configs.sh --bootstrap-server localhost:9092 \
  --alter --add-config 'SCRAM-SHA-256=[password=secret]' \
  --entity-type users --entity-name appuser
```

4. Test the SASL connection:

```bash
kafka-broker-api-versions.sh --bootstrap-server localhost:9092 \
  --listener-security-protocol-map PLAINTEXT:PLAINTEXT,SASL_PLAINTEXT:SASL_PLAINTEXT
```

## Examples

```bash
# List configured SASL mechanisms
kafka-configs.sh --describe --bootstrap-server localhost:9092 \
  --entity-type brokers --entity-default
```
