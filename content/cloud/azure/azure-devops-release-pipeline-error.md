---
title: "[Solution] Azure DevOps Release Pipeline Error"
description: "Fix Azure DevOps release pipeline deployment failures for multi-stage CI/CD workflows."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Release pipeline errors prevent deployments from completing across staging, testing, and production stages. This blocks automated release processes.

## Common Causes

- Release stage approval has not been granted by the required approver
- Artifact variable does not contain the expected value
- Deployment target agent is not connected or cannot reach the pipeline
- Pre-deployment approval timeout has expired

## How to Fix

### Check release definition

```bash
az devops release list \
  --project myProject \
  --query "[].{ID:definitionId,Name:definitionName,Status:status}"
```

### View release logs

```bash
az devops release show \
  --project myProject \
  --release-id 1 \
  --query "environments[].deploySteps[].jobLogUrl"
```

### Create a release

```bash
az devops release create \
  --project myProject \
  --definition-id 1 \
  --description "Hotfix deployment"
```

### Approve a pending release

```bash
az devops release approve \
  --project myProject \
  --release-id 1 \
  --environment-id 1 \
  --status approved \
  --comment "Approved for production"
```

## Examples

- Release is stuck in "Pending Approval" because the designated approver is on leave
- Deployment fails with `AgentNotFound` because the self-hosted agent pool is offline
- Pre-deployment script fails because the variable group was deleted from the project

## Related Errors

- [Azure DevOps Error]({{< relref "/cloud/azure/azure-devops-error" >}}) -- General DevOps errors.
- [Azure Pipeline Failed]({{< relref "/cloud/azure/azure-pipeline-failed" >}}) -- Pipeline failures.
