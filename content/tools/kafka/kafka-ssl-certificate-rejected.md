---
title: "[Solution] Kafka SSL Certificate Rejected Error"
description: "Fix Kafka SSL certificate rejected errors. Resolve client or broker TLS certificate trust failures."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka SSL Certificate Rejected Error

Kafka SSL certificate rejected errors occur when a broker or client refuses a TLS certificate because it is not signed by a trusted CA or has expired.

## Common Causes

- Client certificate not signed by the broker's trusted CA
- Certificate CN/SAN does not match the broker hostname
- Expired certificate still in use
- Truststore missing intermediate CA certificates

## How to Fix

1. Verify the broker certificate details:

```bash
openssl s_client -connect localhost:9093 -showcerts < /dev/null 2>/dev/null | \
  openssl x509 -noout -subject -issuer -dates
```

2. Ensure the client truststore contains the broker's CA:

```bash
keytool -list -keystore /etc/kafka/ssl/client.truststore.jks
```

3. Regenerate a self-signed certificate with correct SAN:

```bash
openssl req -new -x509 -keyout kafka.key -out kafka.crt -days 365 \
  -subj "/CN=broker.kafka.local" \
  -addext "subjectAltName=DNS:broker.kafka.local,IP:10.0.0.5"
```

4. Restart the broker after replacing certificates:

```bash
kafka-server-stop.sh
kafka-server-start.sh -daemon /etc/kafka/server.properties
```

## Examples

```bash
# Test SSL connection
openssl s_client -connect broker:9093 -CAfile ca.crt

# Check certificate expiration
openssl x509 -in kafka.crt -noout -dates
```
