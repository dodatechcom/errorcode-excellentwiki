---
title: "[Solution] AWS S3 Multipart Upload Error"
description: "EntityTooLarge/SlowDown when using S3 Multipart Upload."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Multipart Upload Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Part size is below minimum (5 MiB) or above maximum (5 GiB)
- Number of parts exceeds limit of 10,000
- Upload ID has expired or been aborted
- Concurrent upload rate exceeds S3 limits
- Source file changed during multipart upload

## How to Fix

### List parts

```bash
aws s3api list-parts --bucket my-bucket --key largefile.zip --upload-id EXAMPLE_UPLOAD_ID
```

### Complete multipart upload

```bash
aws s3api complete-multipart-upload --bucket my-bucket --key largefile.zip --upload-id EXAMPLE_UPLOAD_ID --multipart-upload file://parts.json
```

### Abort incomplete upload

```bash
aws s3api abort-multipart-upload --bucket my-bucket --key largefile.zip --upload-id EXAMPLE_UPLOAD_ID
```

## Examples

- Example scenario: part size is below minimum (5 mib) or above maximum (5 gib)
- Example scenario: number of parts exceeds limit of 10,000
- Example scenario: upload id has expired or been aborted
- Example scenario: concurrent upload rate exceeds s3 limits

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
