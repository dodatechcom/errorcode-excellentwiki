---
title: "[Solution] AWS License Manager Error — configuration/usage failures"
description: "Fix AWS License Manager errors. Resolve license configuration, usage tracking, and grant issues."
error-types: ["api-error"]
severities: ["error"]
weight: 161
---

An AWS License Manager error occurs when license configurations fail, usage tracking encounters errors, or grants are not properly managed. License Manager tracks software licenses across AWS and on-premises.

## Common Causes

- License configuration limit exceeded
- Entitlement count does not match license terms
- Cross-account license grant not accepted
- AMI-based license does not match instance region
- License consumption exceeds allocated count

## How to Fix

### List License Configurations

```bash
aws license-manager list-license-configurations \
  --query 'LicenseConfigurations[*].{ID:LicenseConfigurationArn,Name:Name,Status:Status}'
```

### Create License Configuration

```bash
aws license-manager create-license-configuration \
  --name my-license-config \
  --description "My software license" \
  --license-counting-type VCPU \
  --license-count 100
```

### Get License Usage

```bash
aws license-manager list-usage-for-license-configuration \
  --license-configuration-arn arn:aws:license-manager:us-east-1:123456789012:license-configuration:xxx
```

### Create Grant

```bash
aws license-manager create-grant \
  --client-token unique-token-123 \
  --license-arn arn:aws:license-manager::123456789012:license:xxx \
  --grantee-principal-arn arn:aws:iam::098765432109:root \
  --home-region us-east-1
```

### Accept Grant

```bash
aws license-manager accept-grant \
  --grant-arn arn:aws:license-manager:us-east-1:123456789012:grant:xxx
```

## Examples

```bash
# Example 1: License count exceeded
# LicenseLimitExceededException: No available licenses
# Fix: increase license count or release unused licenses

# Example 2: Grant not found
# ResourceNotFoundException: Grant not found
# Fix: verify grant ARN and status
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS Organizations Error]({{< relref "/cloud/aws/aws-organizations-error" >}}) — Organizations errors
- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
