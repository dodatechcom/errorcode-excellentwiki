---
title: "[Solution] Azure ARM Template Error"
description: "Fix Azure Resource Manager template deployment failures and validation issues."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

ARM template errors prevent infrastructure deployments from succeeding. These can be syntax errors, missing resource providers, or policy violations.

## Common Causes

- Template JSON is malformed or contains trailing commas
- Required resource provider is not registered in the subscription
- Resource names conflict with existing resources
- Azure Policy blocks the deployment due to compliance rules

## How to Fix

### Validate the ARM template

```bash
az deployment group validate \
  --resource-group myRG \
  --template-file template.json \
  --parameters parameters.json
```

### Register resource providers

```bash
az provider register --namespace Microsoft.Compute
az provider register --namespace Microsoft.Network
az provider register --namespace Microsoft.Storage
```

### Deploy with debug output

```bash
az deployment group create \
  --resource-group myRG \
  --template-file template.json \
  --parameters parameters.json \
  --verbose
```

### Check policy compliance

```bash
az policy state list \
  --resource-group myRG \
  --query "[?complianceState=='NonCompliant'].{Policy:policyDefinitionName,Resource:resourceId}"
```

## Examples

- Deployment fails with `InvalidDeploymentLocation` because the resource group is in a different region
- ARM template returns `MissingRegistrationForLocation` because the provider is not registered
- Policy blocks VM creation without the required tags `CostCenter` and `Environment`

## Related Errors

- [Azure ARM Error]({{< relref "/cloud/azure/azure-arm-error" >}}) -- General ARM errors.
- [Azure Policy Error]({{< relref "/cloud/azure/azure-policy-error" >}}) -- Policy issues.
