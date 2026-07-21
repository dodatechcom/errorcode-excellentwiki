---
title: "[Solution] ScyllaDB Alternator (DynamoDB API) Error"
description: "How to fix ScyllaDB Alternator DynamoDB-compatible API errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Alternator port not configured
- Wrong API endpoint
- DynamoDB API version mismatch
- Missing IAM permissions

## How to Fix

Enable Alternator:

```yaml
alternator_port: 8000
alternator_write_isolation: only_rmw_uses_lwt
```

## Examples

```bash
aws dynamodb list-tables --endpoint-url http://scylla:8000 --region none
```
