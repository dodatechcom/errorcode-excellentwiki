---
title: "[Solution] ScyllaDB Gossip Permission Error"
description: "How to fix ScyllaDB gossip permission errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Inter-node authentication failing
- Gossip credentials wrong
- Permission denied for gossip

## How to Fix

```yaml
authenticator: PasswordAuthenticator
authorizer: CassandraAuthorizer
```

## Examples

```bash
nodetool statusgossip
```
