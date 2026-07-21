---
title: "[Solution] ScyllaDB Snitch Configuration Error"
description: "How to fix ScyllaDB snitch configuration errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Snitch type wrong for deployment
- DC/rack names not matching topology
- GossipingPropertyFileSnitch config files missing

## How to Fix

Configure snitch:

```yaml
endpoint_snitch: GossipingPropertyFileSnitch
```

Create topology file:

```properties
dc=dc1
rack=rack1
```

## Examples

```bash
cat /etc/scylla/cassandra-rackdc.properties
nodetool status
```
