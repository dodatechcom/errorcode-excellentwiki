---
title: "[Solution] InfluxDB Expired Token Error — How to Fix"
description: "Fix InfluxDB expired token errors by regenerating API tokens and updating token expiration policies"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Expired Token Error

InfluxDB returns an expired token error when an API token has passed its configured expiration date or has been revoked from the system.

## Why It Happens

- Token has exceeded its configured TTL
- Token was manually revoked by an admin
- Organization or bucket permissions changed after token creation
- Server clock drift causes premature token expiration
- Token was created with a short-lived session policy

## Common Error Messages

```
{"error":"token is expired"}
```

```
HTTP 401: Unauthorized — token expiration has passed
```

```
{"error":"unauthorized: expired token"}
```

```
Authorization failed: token no longer valid
```

## How to Fix It

### 1. Regenerate Token via CLI

```bash
influx auth create \
  --org myorg \
  --description "replacement-token" \
  --write-bucket mydb \
  --read-bucket mydb
```

### 2. Regenerate Token via API

```bash
curl -X POST 'http://localhost:8086/api/v2/authorizations' \
  -H 'Authorization: Token existing_mgmt_token' \
  -H 'Content-Type: application/json' \
  -d '{
    "orgID": "my-org-id",
    "description": "new-app-token",
    "permissions": [
      {"action": "read", "type": "buckets", "id": "my-bucket-id"},
      {"action": "write", "type": "buckets", "id": "my-bucket-id"}
    ]
  }'
```

### 3. List and Manage Existing Tokens

```bash
influx auth list --org myorg
influx auth delete --id <token-id>
```

### 4. Update Application Configuration

```bash
# Update the token in your application config
export INFLUX_TOKEN="new-generated-token"
```

## Examples

```
$ curl -H "Authorization: Token old_expired_token" http://localhost:8086/api/v2/query
{"error":"token is expired"}
```

After regeneration:

```
$ export INFLUX_TOKEN="new-token"
$ curl -H "Authorization: Token $INFLUX_TOKEN" http://localhost:8086/api/v2/query
# Query succeeds
```

## Prevent It

- Set longer TTLs for production tokens
- Monitor token expiration dates and rotate proactively
- Use separate read-only tokens for monitoring systems

## Related Pages

- [InfluxDB Auth Error](/tools/influxdb/influxdb-auth-error)
- [InfluxDB Token Error](/tools/influxdb/influxdb-token-error)
- [InfluxDB Permission Error](/tools/influxdb/influxdb-write-permission-error)
