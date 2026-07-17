---
title: "[Solution] Azure ARM Template Deployment Error"
description: "Fix Azure ARM template deployment errors. Resolve ARM template issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An ARM template deployment error occurs when Azure Resource Manager cannot deploy the template. This can be caused by syntax errors, permission issues, or resource conflicts.

## Common Causes

- Template JSON syntax errors
- Missing or invalid parameter values
- Resource provider not registered
- Resource already exists and no update strategy defined
- Insufficient permissions for deployment

## How to Fix

### Validate Template

```bash
az deployment group validate --resource-group myRG --template-file template.json \
  --parameters parameters.json
```

### Check Deployment History

```bash
az deployment group list --resource-group myRG --query '[].{Name:name, Status:properties.provisioningState}'
```

### Check Deployment Errors

```bash
az deployment group show --resource-group myRG --name myDeployment \
  --query 'properties.error'
```

### What-If Deployment

```bash
az deployment group what-if --resource-group myRG --template-file template.json \
  --parameters parameters.json
```

### Register Provider

```bash
az provider register --namespace Microsoft.Compute
```

## Examples

```bash
# Example 1: Validation failed
# Template validation failed: invalid expression
# Fix: fix JSON syntax in template

# Example 2: Resource already exists
# Resource already exists and actionType is not set to 'match'
# Fix: set appropriate actionType or use existing resource
```

## Related Errors

- [Azure Bicep Error]({{< relref "/cloud/azure/azure-bicep-error" >}}) — Bicep deployment error
- [AWS CloudFormation Error]({{< relref "/cloud/aws/aws-cloudformation-error" >}}) — CloudFormation error
