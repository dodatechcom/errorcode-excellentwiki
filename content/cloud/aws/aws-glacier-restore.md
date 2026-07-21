---
title: "[Solution] AWS Glacier Restore"
description: "RestoreObjectError Glacier restore fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Glacier Restore` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Object not in Glacier class
- Expedited capacity not available
- Tier mismatch

## How to Fix

### Initiate restore

```bash
aws s3api restore-object --bucket my-bucket --key archived.zip --restore Days=3
```

## Examples

- Example scenario: object not in glacier class
- Example scenario: expedited capacity not available
- Example scenario: tier mismatch

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General s3 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
