---
title: "[Solution] YugabyteDB Clock Error — How to Fix"
description: "Fix YugabyteDB clock errors by resolving hybrid logical clock issues, fixing clock skew problems, and handling clock synchronization failures"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Clock Error

YugabyteDB clock errors occur when hybrid logical clocks (HLC) are not synchronized across nodes. Clock skew can cause consistency issues in distributed transactions.

## Why It Happens

- Clock skew between nodes exceeds threshold
- NTP is not configured or not working
- Node clock jumps forward or backward
- Clock offset exceeds max_clock_skew_usec
- VM migration causes clock disruption
- Leap second causes clock anomaly

## Common Error Messages

```
WARNING: clock skew detected
```

```
ERROR: HLC timestamp exceeds max allowed
```

```
ERROR: clock skew between nodes too large
```

```
WARNING: clock skew offset: 500ms
```

## How to Fix It

### 1. Check Clock Synchronization

```bash
# Check time on all nodes
for node in yb-master-1 yb-master-2 yb-tserver-1 yb-tserver-2; do
  echo "$node: $(ssh $node date)"
done

# Check NTP status
chronyc tracking
ntpq -p
```

### 2. Configure NTP

```bash
# Install chrony
sudo apt install chrony

# Configure /etc/chrony/chrony.conf
# server time1.google.com iburst
# server time2.google.com iburst

# Start chrony
sudo systemctl enable chrony
sudo systemctl start chrony

# Verify synchronization
chronyc sources
```

### 3. Configure Clock Skew Settings

```bash
# In tserver.gflags and master.gflags:
--max_clock_skew_usec=5000000  # 5 seconds default

# Reduce if NTP is reliable:
--max_clock_skew_usec=1000000  # 1 second
```

### 4. Monitor Clock Health

```bash
# Check clock offset across cluster
for node in yb-master-1 yb-master-2 yb-tserver-1; do
  echo "$node offset:"
  ssh $node "chronyc tracking | grep 'System time'"
done
```

## Common Scenarios

- **Clock skew warnings**: Ensure NTP is running and synchronized on all nodes.
- **Transaction ordering issues**: Reduce max_clock_skew_usec setting.
- **VM clock drift**: Configure NTP to resync quickly after migration.

## Prevent It

- Run chrony on all YugabyteDB nodes
- Monitor clock skew with alerts
- Avoid VM migrations during critical operations

## Related Pages

- [YugabyteDB Transaction Error](/tools/yugabyte/yugabyte-transaction-error)
- [YugabyteDB Node Error](/tools/yugabyte/yugabyte-node-error)
- [YugabyteDB Config Error](/tools/yugabyte/yugabyte-gflag-error)
