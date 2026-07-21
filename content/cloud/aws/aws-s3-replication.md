---
title: "[Solution] AWS S3 replication"
description: "ReplicationError for S3 replication."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 replication` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Source or dest in different regions
- KMS dest inaccessible
- Versioning not enabled

## How to Fix

### Check replication

```bash
aws s3api get-bucket-replication --bucket my-bucket
```

## Examples

- Example scenario: source or dest in different regions
- Example scenario: kms dest inaccessible
- Example scenario: versioning not enabled

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General s3 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
