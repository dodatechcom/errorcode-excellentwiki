---
title: "[Solution] AWS S3 Replication Error"
description: "ReplicationError when S3 Cross-Region/Same-Region Replication fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Replication Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Source or destination bucket in different region
- KMS key for destination not accessible
- Replication IAM role permissions insufficient
- Object versioning not enabled on source or destination
- Replication Time Control SLA not met

## How to Fix

### Check replication config

```bash
aws s3api get-bucket-replication --bucket my-bucket
```

## Examples

- Example scenario: source or destination bucket in different region
- Example scenario: kms key for destination not accessible
- Example scenario: replication iam role permissions insufficient
- Example scenario: object versioning not enabled on source or destination

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
