---
title: "[Solution] Vitess Tablet Transaction Retry Error"
description: "Fix Vitess transaction retry errors when transient failures cause automatic retry loops"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Transaction Retry Error

Transaction retry errors occur when vtgate automatically retries failed transactions, causing duplicate writes or retry storms.

## Common Causes

- Transient network error causing retry
- Primary failover during transaction
- Retry budget exhausted
- Non-idempotent operation being retried

## How to Fix

Check retry settings:

```bash
curl http://localhost:15200/debug/vars | jq '.QueryRetryCount'
```

Disable automatic retry:

```bash
vtgate -retry_count 0
```

Implement idempotent operations in application:

```sql
INSERT INTO orders (id, customer_id, total) VALUES (UUID(), 123, 99.99)
ON DUPLICATE KEY UPDATE total = VALUES(total);
```

## Examples

```bash
vtgate -retry_count 2 -transaction_mode=single
```
