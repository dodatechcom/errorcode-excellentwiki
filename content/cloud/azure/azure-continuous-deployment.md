---
title: "[Solution] AZURE Continuous Deployment"
description: "ContinuousDeploymentError for CI/CD."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Continuous Deployment` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Repo not connected
- Build script not found
- Branch does not match

## How to Fix

### Setup CI/CD

```bash
az webapp deployment source config -g myRG -n myApp --repo-url https://github.com/user/repo
```

## Examples

- Example scenario: repo not connected
- Example scenario: build script not found
- Example scenario: branch does not match

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
