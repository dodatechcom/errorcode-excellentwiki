---
title: "[Solution] ScyllaDB Alternator API Error — How to Fix"
description: "Fix ScyllaDB Alternator API errors when DynamoDB-compatible requests fail with unexpected responses"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Alternator API Error

Alternator API errors occur when DynamoDB-compatible applications fail to interact with ScyllaDB through the Alternator interface, typically due to unsupported features or configuration mismatches.

## Why It Happens

- DynamoDB feature is not yet supported by Alternator
- Alternator is not enabled in ScyllaDB configuration
- Request payload contains unsupported DynamoDB expressions
- Alternator port conflicts with native CQL port
- Authorization settings block Alternator requests

## Common Error Messages

```
com.amazonaws.dynamodb.v20120810#InternalServerError
```

```
error: Alternator is not enabled on this node
```

```
ValidationException: ConditionalCheckFailed
```

## How to Fix It

### 1. Enable Alternator

```yaml
# In scylla.yaml
alternator_port: 8000
alternator_enforce_authorization: true
alternator_write_isolation: 'only_rmw_uses_read_modify_write'
```

```bash
sudo systemctl restart scylla-server
```

### 2. Check Alternator Compatibility

```bash
curl -XPOST 'http://localhost:8000' \
  -H 'Content-Type: application/x-amz-json-1.0' \
  -H 'X-Amz-Target: DynamoDB_20120810.ListTables' \
  -d '{}'
```

### 3. Create Table via Alternator

```bash
curl -XPOST 'http://localhost:8000' \
  -H 'Content-Type: application/x-amz-json-1.0' \
  -H 'X-Amz-Target: DynamoDB_20120810.CreateTable' \
  -d '{
    "TableName": "users",
    "KeySchema": [{"AttributeName": "id", "KeyType": "HASH"}],
    "AttributeDefinitions": [{"AttributeName": "id", "AttributeType": "S"}],
    "BillingMode": "PAY_PER_REQUEST"
  }'
```

### 4. Fix Write Isolation Setting

```yaml
# In scylla.yaml
alternator_write_isolation: 'always_use_read_modify_write'
```

## Examples

```
$ curl -s http://localhost:8000 -H 'X-Amz-Target: DynamoDB_20120810.ListTables' -d '{}'
{"TableNames": ["users", "sessions"]}
```

## Prevent It

- Test Alternator compatibility with your DynamoDB client library
- Monitor Alternator-specific metrics in Scylla Monitoring
- Review Alternator documentation for unsupported features

## Related Pages

- [ScyllaDB Auth Error](/tools/scylladb/scylladb-auth-error)
- [ScyllaDB CQL Error](/tools/scylladb/scylladb-cql-error)
- [ScyllaDB Connection Error](/tools/scylladb/scylladb-connection-error)
