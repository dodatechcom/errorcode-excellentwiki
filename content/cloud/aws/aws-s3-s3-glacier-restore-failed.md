---
title: "[Solution] AWS S3 Glacier Restore Failed"
description: "RestoreObjectError when restoring from S3 Glacier/Deep Archive."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Glacier Restore Failed` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Object not stored in Glacier storage class
- Restore Request rate limit exceeded
- Expedited restore capacity not available
- Tier mismatch (Standard vs Bulk vs Expedited)
- Object deleted during restore process

## How to Fix

### Initiate restore

```bash
aws s3api restore-object --bucket my-bucket --key archived.zip --restore-request Days=3,GlacierJobParameters={Tier=Standard}
```

### Check restore status

```bash
aws s3api head-object --bucket my-bucket --key archived.zip
```

## Examples

- Example scenario: object not stored in glacier storage class
- Example scenario: restore request rate limit exceeded
- Example scenario: expedited restore capacity not available
- Example scenario: tier mismatch (standard vs bulk vs expedited)

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
