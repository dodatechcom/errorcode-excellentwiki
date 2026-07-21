---
title: "[Solution] AWS Multipart upload"
description: "EntityTooLarge/SlowDown for S3 multipart upload."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Multipart upload` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Part less than 5 MiB or more than 5 GiB
- Upload ID expired or aborted
- Number of parts more than 10000

## How to Fix

### List parts

```bash
aws s3api list-parts --bucket my-bucket --key largefile.zip --upload-id ID
```

### Complete multipart

```bash
aws s3api complete-multipart-upload --bucket my-bucket --key largefile.zip
```

## Examples

- Example scenario: part less than 5 mib or more than 5 gib
- Example scenario: upload id expired or aborted
- Example scenario: number of parts more than 10000

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
