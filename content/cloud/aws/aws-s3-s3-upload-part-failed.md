---
title: "[Solution] AWS S3 Upload Part Failed"
description: "UploadPartCopyError/SlowDown when an upload part fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Upload Part Failed` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Part size too small (minimum 5 MB)
- Network interruption during upload
- Upload ID is invalid or closed
- Source file changed mid-upload
- Server-side encryption mismatch

## How to Fix

### Verify part sizes

```bash
aws s3api list-parts --bucket my-bucket --key bigfile.iso --upload-id UPLOAD_ID
```

### Re-upload part

```bash
aws s3api upload-part --bucket my-bucket --key bigfile.iso --part-number 3 --body part3.dat --upload-id UPLOAD_ID
```

### Check integrity

```bash
aws s3api head-object --bucket my-bucket --key bigfile.iso
```

## Examples

- Example scenario: part size too small (minimum 5 mb)
- Example scenario: network interruption during upload
- Example scenario: upload id is invalid or closed
- Example scenario: source file changed mid-upload

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
