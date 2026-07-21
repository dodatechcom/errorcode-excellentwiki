---
title: "[Solution] MongoDB Out of Order Oplog Error"
description: "Fix MongoDB out of order oplog error when replication encounters timestamps that violate ordering guarantees"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Out of Order Oplog Error

Replication fails because an oplog entry has a timestamp older than the last applied entry. This violates the oplog ordering guarantee that entries must be applied in strictly increasing timestamp order.

## Common Causes

- System clock moved backward on a replica set member
- Oplog entries were reordered due to network partitions
- Manual clock adjustment without restarting mongod
- VM host clock drift caused timestamp inconsistency
- Resynced member applied oplog entries out of order

## How to Fix

### Sync System Clock

```bash
# Check current time drift
ntpdate -q pool.ntp.org

# Sync clock
sudo systemctl stop mongod
sudo ntpdate -s pool.ntp.org
sudo systemctl start mongod
```

### Resync the Affected Member

```javascript
// On the affected secondary, resync from the primary
rs.syncFrom('primary-host:27017')

// Or do a full resync
// 1. Stop secondary
// 2. Remove data directory
// 3. Start mongod -- it will do an initial sync
```

### Monitor Clock Drift

```bash
# Check NTP status
timedatectl status

# Enable NTP sync
sudo timedatectl set-ntp true

# Monitor drift
watch -n 60 'chronyc tracking 2>/dev/null || ntpq -p'
```

### Set Proper Timezone

```bash
# Ensure all nodes use the same timezone
sudo timedatectl set-timezone UTC
```

## Examples

```
replSet: (Oplog) Operations not in order.
  Last op: (ts: 1715000000, 1) Current: (ts: 1714999999, 1)

replSet: Member's oplog is out of order with other members.
  Clock may have moved backward
```

## Related Errors

- [MongoDB Replication Lag]({{< relref "/tools/mongodb/mongodb-replication-lag" >}}) -- replication delay
- [MongoDB Replica Set Error]({{< relref "/tools/mongodb/mongodb-replica-set-error" >}}) -- replica set issues
- [MongoDB Election Timeout]({{< relref "/tools/mongodb/mongodb-election-timeout" >}}) -- election problems
