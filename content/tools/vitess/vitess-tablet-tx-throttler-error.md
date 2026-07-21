---
title: "[Solution] Vitess Tablet Tx Throttler Error"
description: "Fix Vitess transaction throttler errors when replication lag triggers write throttling"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Tx Throttler Error

Transaction throttler errors occur when vtgate blocks writes because replication lag exceeds the configured threshold.

## Common Causes

- Replica falling behind due to heavy load
- Throttler lag threshold set too low
- Large bulk operation causing temporary lag
- Network latency between primary and replicas

## How to Fix

Check replication lag:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "SHOW REPLICA STATUS\G" | grep Seconds_Behind
```

Adjust throttler threshold:

```bash
vtgate -enable_tx_throttler -tx_throttler_threshold 100 -tx_throttler_config 'target_replication_lag=30,max_replication_lag=60'
```

Temporarily disable throttler:

```bash
vtgate -enable_tx_throttler=false
```

## Examples

```bash
vtctlclient ThrottleCheckSelf cell1-tablet-100
```
