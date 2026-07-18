---
title: "[Solution] YugabyteDB Upgrade Error — How to Fix"
description: "Fix YugabyteDB upgrade errors by resolving rolling upgrade failures, fixing version compatibility issues, and handling cluster upgrade procedures"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Upgrade Error

YugabyteDB upgrade errors occur when performing rolling upgrades or major version upgrades. Upgrades require careful sequencing to maintain availability.

## Why It Happens

- Upgrade is not performed in correct order (Masters before TServers)
- Version mismatch between Masters and TServers
- Upgrade fails on one node causing cluster instability
- New version has incompatible GFlags
- Upgrade process is interrupted
- Pre-upgrade checks fail

## Common Error Messages

```
ERROR: version mismatch between Master and TServer
```

```
ERROR: upgrade failed on node
```

```
ERROR: incompatible GFlag configuration
```

```
ERROR: pre-upgrade check failed
```

## How to Fix It

### 1. Check Current Version

```bash
# Check TServer version
/home/yugabyte/tserver/bin/yb-serverversion.sh

# Check Master version
/home/yugabyte/master/bin/yb-serverversion.sh

# Check cluster status
/home/yugabyte/master/bin/yb-admin list_masters
/home/yugabyte/tserver/bin/yb-admin list_tablet_servers
```

### 2. Perform Rolling Upgrade

```bash
# Step 1: Upgrade Masters first (one at a time)
for master in yb-master-1 yb-master-2 yb-master-3; do
  ssh $master "sudo systemctl stop yugabyte-master"
  ssh $master "sudo yum install yugabyte-master-<version>"
  ssh $master "sudo systemctl start yugabyte-master"
  sleep 60  # Wait for Master to join quorum
done

# Step 2: Upgrade TServers (one at a time)
for tserver in yb-tserver-1 yb-tserver-2 yb-tserver-3; do
  ssh $tserver "sudo systemctl stop yugabyte-tserver"
  ssh $tserver "sudo yum install yugabyte-tserver-<version>"
  ssh $tserver "sudo systemctl start yugabyte-tserver"
  sleep 60  # Wait for tablets to rebalance
done
```

### 3. Fix Upgrade Failures

```bash
# If upgrade fails on a node, rollback to previous version
ssh $node "sudo systemctl stop yugabyte-tserver"
ssh $node "sudo yum install yugabyte-tserver-<previous_version>"
ssh $node "sudo systemctl start yugabyte-tserver"

# Check if cluster recovers
/home/yugabyte/tserver/bin/yb-admin list_tablet_servers
```

### 4. Validate After Upgrade

```bash
# Check all nodes are on new version
for node in yb-master-1 yb-master-2 yb-tserver-1 yb-tserver-2; do
  echo "$node: $(ssh $node /home/yugabyte/tserver/bin/yb-serverversion.sh)"
done

# Verify cluster health
curl http://yb-master-1:7000/cluster-config | jq '.tablet_servers[].version'
```

## Common Scenarios

- **Master upgrade fails**: Ensure quorum is maintained and retry.
- **TServer upgrade causes tablet relocation**: Wait for rebalancing to complete.
- **Version mismatch after partial upgrade**: Complete the upgrade on remaining nodes.

## Prevent It

- Always upgrade Masters before TServers
- Test upgrades on staging environment
- Keep backup of data directory before upgrade

## Related Pages

- [YugabyteDB Config Error](/tools/yugabyte/yugabyte-gflag-error)
- [YugabyteDB TServer Error](/tools/yugabyte/yugabyte-tserver-error)
- [YugabyteDB Master Error](/tools/yugabyte/yugabyte-master-error)
