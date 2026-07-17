---
title: "[Solution] AWS CloudFront Distribution Error"
description: "Fix AWS CloudFront distribution errors. Resolve CloudFront configuration issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

A CloudFront distribution error occurs when CloudFront cannot serve content or is misconfigured. This can cause 4xx/5xx errors for end users.

## Common Causes

- Origin server is not accessible from CloudFront
- SSL certificate not attached to the distribution
- Origin access identity not configured for S3
- Cache behavior rules blocking requests
- Distribution is disabled

## How to Fix

### Check Distribution Status

```bash
aws cloudfront get-distribution --id EXXXXX
```

### Check Distribution Configuration

```bash
aws cloudfront get-distribution-config --id EXXXXX
```

### Test Origin Access

```bash
curl -H "Host: mybucket.s3.amazonaws.com" https://mybucket.s3.amazonaws.com/
```

### Create Invalidation

```bash
aws cloudfront create-invalidation \
  --distribution-id EXXXXX \
  --paths "/*"
```

### Check Origin Health

```bash
aws cloudfront get-origin-health --distribution-id EXXXXX
```

## Examples

```bash
# Example 1: Origin not accessible
# 502 Bad Gateway
# Fix: verify origin server is running and accessible

# Example 2: SSL certificate not found
# 403 Forbidden
# Fix: attach ACM certificate to distribution
```

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 access denied
- [AWS API Gateway Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) — API Gateway error
