---
title: "AWS S3 AccessDenied"
description: "AccessDenied — Fix Amazon S3 access denied errors for bucket and object operations."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

The `AccessDenied` error in S3 occurs when an API call to read, write, or list objects in an S3 bucket is rejected due to missing or insufficient permissions. This is distinct from the generic IAM AccessDenied as it specifically involves S3 resource policies.

## Common Causes

- IAM user/role lacks the required S3 action permission
- Bucket policy explicitly denies the request
- S3 Object Ownership (bucket owner enforced) prevents cross-account writes
- ACLs are disabled and bucket policy does not grant access
- The request is not signed with valid credentials

## How to Fix

Check the bucket policy:

```bash
aws s3api get-bucket-policy --bucket my-bucket --output json
```

Attach an IAM policy granting S3 access:

```bash
aws iam put-user-policy \
  --user-name deploy-user \
  --policy-name S3DeployAccess \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
        "Resource": "arn:aws:s3:::my-bucket/*"
      },
      {
        "Effect": "Allow",
        "Action": "s3:ListBucket",
        "Resource": "arn:aws:s3:::my-bucket"
      }
    ]
  }'
```

Test access:

```bash
aws s3 ls s3://my-bucket/
aws s3 cp test.txt s3://my-bucket/test.txt
```

## Examples

- Uploading to an S3 bucket created by a different account without cross-account policy
- Lambda function cannot read from S3 because the execution role lacks `s3:GetObject`
- Bucket owner enforced ACLs block writes from external accounts

## Related Errors

- [AWS AccessDenied]({{< relref "/cloud/aws/access-denied" >}}) — generic AWS access denied.
- [AWS IAM Error]({{< relref "/cloud/aws/iam-error" >}}) — IAM authorization failures.
- [GCP Storage Error]({{< relref "/cloud/gcp/storage-error2" >}}) — GCP Cloud Storage equivalent.
