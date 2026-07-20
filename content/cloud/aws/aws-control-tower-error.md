---
title: "[Solution] AWS Control Tower Error — landing zone/OU failures"
description: "Fix AWS Control Tower errors. Resolve landing zone, OU, and guardrail configuration issues."
error-types: ["api-error"]
severities: ["error"]
weight: 123
---

An AWS Control Tower error occurs when landing zone setup fails, OUs cannot be created, or guardrails encounter permission conflicts. Control Tower automates multi-account governance based on AWS best practices.

## Common Causes

- Landing zone drift from baseline configuration
- OU creation conflicts with existing organization structure
- Guardrail enrollment permissions missing
- Account factory provisioning fails
- SCP from Control Tower conflicts with custom policies

## How to Fix

### Check Landing Zone Status

```bash
aws controltower get-landing-zone \
  --landing-zone-identifier arn:aws:controltower:us-east-1::landingzone/xxx
```

### List Guardrails

```bash
aws controltower list-enabled-guardrails \
  --path ou-xxx
```

### List Account Factory Configurations

```bash
aws controltower list-account-factory-configurations
```

### Create Provisioned Product

```bash
aws servicecatalog provision-product \
  --product-id prod-xxx \
  --provisioning-artifact-id pa-xxx \
  --provisioned-product-name my-account \
  --provisioning-parameters Key=AccountName,Value=NewAccount
```

### Check Guardrail Compliance

```bash
aws controltower get-control-operation \
  --operation-id op-xxx
```

## Examples

```bash
# Example 1: Landing zone drift
# InvalidStateException: Landing zone is drifted
# Fix: update landing zone to baseline configuration

# Example 2: OU conflict
# ConflictException: OU already exists
# Fix: use existing OU or reorganize structure
```

## Related Errors

- [AWS Organizations Error]({{< relref "/cloud/aws/aws-organizations-error" >}}) — Organizations errors
- [AWS Service Catalog Error]({{< relref "/cloud/aws/aws-service-catalog-error" >}}) — Service Catalog errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
