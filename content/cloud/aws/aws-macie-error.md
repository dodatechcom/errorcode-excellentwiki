---
title: "[Solution] AWS Macie Error — classification/discovery failures"
description: "Fix AWS Macie errors. Resolve Macie classification job, finding, and S3 bucket discovery issues."
error-types: ["api-error"]
severities: ["error"]
weight: 119
---

An AWS Macie error occurs when classification jobs fail to run, findings are not generated, or S3 bucket discovery encounters permission issues. Macie discovers and protects sensitive data in S3 but requires proper S3 access.

## Common Causes

- Macie not enabled in the account/region
- S3 bucket lacks required Macie access permissions
- Classification job targeting non-existent buckets
- Finding publication destination not configured
- Custom data identifiers have invalid regex patterns

## How to Fix

### Enable Macie

```bash
aws macie2 enable-macie \
  --finding-publishing-destination S3Destination=Destination=S3_BUCKET_ARN
```

### List Classification Jobs

```bash
aws macie2 list-classification-jobs \
  --query 'items[*].{ID:jobId,Name:name,Status:status.code}'
```

### Get Findings

```bash
aws macie2 list-findings \
  --finding-criteria '{"severity":{"gte":7}}' \
  --max-results 10
```

### Create Custom Data Identifier

```bash
aws macie2 create-custom-data-identifier \
  --name my-custom-regex \
  --regex "[0-9]{3}-[0-9]{2}-[0-9]{4}"
```

### Update S3 Bucket Classification

```bash
aws macie2 create-classification-job \
  --name my-s3-scan \
  --s3-job-definition '{"bucketDefinitions":[{"accountId":"123456789012","buckets":["my-bucket"]}]}' \
  --schedule-frequency DAILY
```

## Examples

```bash
# Example 1: Macie not enabled
# BadRequestException: Macie is not enabled
# Fix: run enable-macie command

# Example 2: S3 access denied
# AccessDeniedException: Cannot access S3 bucket
# Fix: add macie:GetBucket to bucket policy
```

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 access errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS GuardDuty Error]({{< relref "/cloud/aws/aws-guardduty-error" >}}) — GuardDuty threat detection errors
