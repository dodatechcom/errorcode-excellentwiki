---
title: "[Solution] GCP Schema (Pub/Sub)"
description: "PubSubSchemaError for schemas."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Schema (Pub/Sub)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Schema name taken
- Schema definition invalid (Avro/Protobuf)
- Schema revision not found

## How to Fix

### Create schema

```bash
gcloud pubsub schemas create mySchema --type=AVRO --definition=schema.avsc
```

## Examples

- Example scenario: schema name taken
- Example scenario: schema definition invalid (avro/protobuf)
- Example scenario: schema revision not found

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
