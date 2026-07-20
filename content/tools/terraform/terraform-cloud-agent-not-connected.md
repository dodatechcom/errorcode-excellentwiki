---
title: "[Solution] Terraform Cloud Agent Not Connected"
description: "Fix Terraform Cloud agent not connected errors when the remote agent is offline."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Agent not connected errors occur when TFC agent pool is unreachable:

```
Error: Agent pool not connected

The agent pool "my-pool" has no connected agents. Runs will
be queued until an agent becomes available.
```

## Common Causes

- Agent process stopped on the machine.
- Network connectivity issue.
- Agent token expired.

## How to Fix

**Check agent status:**

```bash
# On the agent machine
ps aux | grep terraform-agent
```

**Restart the agent:**

```bash
# Using systemd
sudo systemctl restart terraform-agent

# Or run directly
terraform-agent run --token $AGENT_TOKEN
```

**Verify agent is registered:**

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/agent-pools/pool-id/agents | jq '.data[].attributes'
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/agent-pools/pool-id/agents   | jq '.data[] | {id: .id, status: .attributes.status, last_ping: .attributes.last-ping-at}'
```
