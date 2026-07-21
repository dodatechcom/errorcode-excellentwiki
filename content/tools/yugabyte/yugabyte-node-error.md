---
title: "[Solution] YugabyteDB Node Error — How to Fix"
description: "Fix YugabyteDB node errors by resolving node failures, fixing tablet server connectivity issues, and handling cluster node management"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Node Error

YugabyteDB node errors occur when master or tablet server nodes fail, become unreachable, or cannot join the cluster due to configuration or network issues.

## Why It Happens

- Node process crashed or was terminated
- Network partition isolates the node from the cluster
- Disk failure makes the node unable to serve data
- Master quorum is lost (fewer than half of masters running)
- Node cannot register with the master due to hostname resolution
- Firewall rules block inter-node communication

## Common Error Messages

```
ERROR: tablet server is not responding
```

```
ERROR: master server is not available
```

```
ERROR: node is not a leader for any tablets
```

```
FATAL: cannot connect to master
```

## How to Fix It

### 1. Check Node Status

```bash
# Check master status
yb-admin -master_addresses yugabyte:7100 list_masters

# Check tserver status
yb-admin -master_addresses yugabyte:7100 list_tablet_servers

# Check cluster health
yb-admin -master_addresses yugabyte:7100 get_cluster_config
```

### 2. Restart Failed Nodes

```bash
# Check service status
sudo systemctl status yugabyte-master
sudo systemctl status yugabyte-tserver

# Restart master
sudo systemctl restart yugabyte-master

# Restart tserver
sudo systemctl restart yugabyte-tserver

# Check logs for errors
tail -100 /opt/yugabyte/logs/yugabyte-master.ERROR
```

### 3. Add New Node to Cluster

```bash
# Start a new tserver
/opt/yugabyte/bin/yb-tserver \
  --fs_data_dirs=/data/yugabyte \
  --tserver_master_addrs=master1:7100,master2:7100,master3:7100 \
  --rpc_bind_addresses=newnode:9100 &

# Verify the node joined
yb-admin -master_addresses yugabyte:7100 list_tablet_servers
```

### 4. Remove Dead Node

```bash
# Decommission a dead tserver
yb-admin -master_addresses yugabyte:7100 \
  remove_tablet_server <tserver_id>

# Force remove if node is permanently gone
yb-admin -master_addresses yugabyte:7100 \
  heartbeat_tablet_server <tserver_id> force=true
```

## Common Scenarios

- **Node crashes and does not restart**: Check logs and fix the underlying issue before restarting.
- **Cannot add new node**: Ensure the node can reach all master addresses.
- **Master quorum lost**: Restart at least 2 of 3 masters to restore quorum.

## Prevent It

- Run at least 3 master nodes for HA
- Monitor node health with alerts
- Keep sufficient spare capacity for node failures

## Related Pages

- [YugabyteDB Master Error](/tools/yugabyte/yugabyte-master-error)
- [YugabyteDB TServer Error](/tools/yugabyte/yugabyte-tserver-error)
- [YugabyteDB Raft Error](/tools/yugabyte/yugabyte-raft-error)
