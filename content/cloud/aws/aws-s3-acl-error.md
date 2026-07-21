---
title: "[Solution] AWS S3 ACL error"
description: "AccessControlListError for ACL configuration."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 ACL error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Invalid grantee email or URI
- Exceeds 100 ACL grants
- Bucket policy conflicts

## How to Fix

### Set ACL

```bash
aws s3api put-object-acl --bucket my-bucket --key file.txt --acl bucket-owner-full-control
```

## Examples

- Example scenario: invalid grantee email or uri
- Example scenario: exceeds 100 acl grants
- Example scenario: bucket policy conflicts

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General s3 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
