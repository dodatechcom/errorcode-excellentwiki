---
title: "[Solution] Azure DevOps Build Agent Error"
description: "Fix Azure DevOps build agent failures that block CI/CD pipeline execution."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Build agent errors prevent Azure DevOps pipelines from running on hosted or self-hosted agents. This blocks code compilation, testing, and artifact creation.

## Common Causes

- Self-hosted agent has lost connection to the Azure DevOps server
- Agent pool has no available agents to pick up the job
- Agent version is outdated and incompatible with the pipeline tasks
- Agent machine lacks required build tools or SDKs

## How to Fix

### Check agent pool status

```bash
az devops agent list \
  --agent-pool "myPool" \
  --project myProject \
  --query "[].{Name:name,Status:status,Enabled:enabled}"
```

### Reconfigure the build agent

```bash
./config.sh --unattended --url https://dev.azure.com/myOrg --token PAT_TOKEN --pool myPool
```

### Check agent capabilities

```bash
az devops agent get \
  --agent-pool "myPool" \
  --agent-id 1 \
  --query "userCapabilities"
```

### Install build tools on the agent

```bash
sudo apt-get update && sudo apt-get install -y dotnet-sdk-8.0 nodejs npm
```

## Examples

- Build job fails with `No agents found in pool` because all agents are busy
- Agent disconnects with ` Lost connection to the server` due to network issues
- Pipeline task fails because the agent does not have Docker installed

## Related Errors

- [Azure DevOps Error]({{< relref "/cloud/azure/azure-devops-error" >}}) -- General DevOps errors.
- [Azure Build Definition]({{< relref "/cloud/azure/azure-build-definition" >}}) -- Build configuration.
