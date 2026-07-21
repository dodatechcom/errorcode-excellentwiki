---
title: "[Solution] AWS Upload part failed"
description: "UploadPartCopyError for upload part."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Upload part failed` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Part too small
- Network interruption
- Upload ID invalid

## How to Fix

### Check part sizes

```bash
aws s3api list-parts --bucket my-bucket --key bigfile.iso
```

## Examples

- Example scenario: part too small
- Example scenario: network interruption
- Example scenario: upload id invalid

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
