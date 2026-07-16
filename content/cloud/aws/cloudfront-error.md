---
title: "AWS CloudFront Error: The Request Could Not Be Satisfied (403)"
description: "CloudFront: The request could not be satisfied (403) — Fix CloudFront access denied errors."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "cloudfront", "cdn", "403", "forbidden", "origin", "distribution"]
weight: 5
---

The CloudFront `403 Forbidden` error with message "The request could not be satisfied" occurs when CloudFront rejects a request due to origin access restrictions, origin misconfiguration, or WAF/signed URL requirements.

## Common Causes

- Origin (S3 bucket or ALB) denies access to CloudFront's IP addresses
- Origin Access Control (OAC) or Origin Access Identity (OAI) not configured
- CloudFront distribution is associated with a WAF web ACL that blocks the request
- Signed cookies or signed URLs are required but not provided
- The origin bucket policy does not allow the CloudFront distribution

## How to Fix

Check the distribution configuration:

```bash
aws cloudfront get-distribution \
  --id E1234567890ABC \
  --query 'Distribution.{Origins:DistributionConfig.Origins.Items,OAC:DistributionConfig.Origins.Items[0].OriginAccessControlId}'
```

Grant CloudFront access to the S3 origin:

```bash
aws s3api put-bucket-policy \
  --bucket my-origin-bucket \
  --policy '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "cloudfront.amazonaws.com"
        },
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::my-origin-bucket/*",
        "Condition": {
          "StringEquals": {
            "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/E1234567890ABC"
          }
        }
      }
    ]
  }'
```

Create an Origin Access Control:

```bash
aws cloudfront create-origin-access-control \
  --origin-access-control-config '{
    "Name": "my-oac",
    "OriginAccessControlOriginType": "s3",
    "SigningBehavior": "always",
    "SigningProtocol": "sigv4"
  }'
```

## Examples

- Static website in S3 blocks CloudFront because the bucket is not public and no OAI/OAC is configured
- CloudFront returns 403 for all paths because WAF blocks requests without a specific header
- Signed URL has expired and CloudFront rejects the request

## Related Errors

- [AWS S3 AccessDenied]({{< relref "/cloud/aws/s3-access-denied2" >}}) — S3 bucket access denied.
- [AWS AccessDenied]({{< relref "/cloud/aws/access-denied" >}}) — IAM permission denied.
- [Azure NSG Error]({{< relref "/cloud/azure/nsg-error" >}}) — network security group issues.
