---
title: "[Solution] ScyllaDB Node Not Joining Cluster"
description: "How to fix ScyllaDB node not joining cluster errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Seeds list misconfigured
- Listen address wrong
- RPC address not set
- Cluster name mismatch

## How to Fix

Check seeds configuration:

```yaml
seeds: "node1, node2"
listen_address: <local-ip>
rpc_address: 0.0.0.0
```

Bootstrap node:

```bash
nodetool status  # Check if node is in UN state
```

## Examples

```bash
nodetool status
cat /etc/scylla/scylla.yaml | grep -E '(seeds|listen_address|rpc_address)'
```
