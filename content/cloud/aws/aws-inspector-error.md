---
title: "[Solution] AWS Inspector Error — assessment/finding/agent failures"
description: "Fix AWS Inspector errors. Resolve Inspector assessment, finding, and agent issues."
error-types: ["api-error"]
severities: ["error"]
weight: 118
---

An AWS Inspector error occurs when assessments fail to run, findings are not generated, or the Inspector agent cannot be installed. Inspector provides vulnerability assessments for EC2 and ECR but requires proper permissions and configuration.

## Common Causes

- Inspector agent not installed on target instances
- IAM role lacks Inspector permissions
- Assessment target has no running instances
- ECR scan fails due to image not in registry
- Finding publication destination not configured

## How to Fix

### List Assessment Templates

```bash
aws inspector list-assessment-templates \
  --query 'assessmentTemplateArns'
```

### Get Findings

```bash
aws inspector list-findings \
  --assessment-template-arn arn:aws:inspector:us-east-1:123456789012:assessmenttemplate/xxx
```

### Create ECR Scan

```bash
aws inspector2 start-resource-scan \
  --resource-types ECR_CONTAINER_IMAGE \
  --scan-type FULL
```

### Get Findings by Severity

```bash
aws inspector2 list-findings \
  --filter-criteria '{"severity":[{"comparison":"EQUALS","value":"HIGH"}]}'
```

### Create Assessment Target

```bash
aws inspector create-assessment-target \
  --assessment-target-name my-target \
  --resource-group-arn arn:aws:inspector:us-east-1:123456789012:resourcegroup/xxx
```

## Examples

```bash
# Example 1: No instances in target
# InvalidInputException: No instances match filter criteria
# Fix: ensure target instances have Inspector agent running

# Example 2: ECR scan failed
# AccessDeniedException: Inspector cannot access ECR
# Fix: add ecr:GetAuthorizationToken to Inspector role
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS ECR Error]({{< relref "/cloud/aws/aws-ecr-error" >}}) — ECR repository errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
