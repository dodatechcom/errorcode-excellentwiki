---
title: "[Solution] AWS Lambda ZIP Size Too Large"
description: "InvalidParameterValueException due to ZIP file exceeding 50MB."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda ZIP Size Too Large` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Direct zip upload limited to 50MB
- Code includes node_modules or build artifacts
- Large dependencies not using layers
- Container images preferred for code > 50MB
- Optimize bundle with Webpack/esbuild/Rollup

## How to Fix

### Check bundled size

```bash
ls -lh my-function.zip
```

### Upload via S3 for larger packages

```bash
aws s3 cp my-function.zip s3://my-deployment-bucket/
```

## Examples

- Example scenario: direct zip upload limited to 50mb
- Example scenario: code includes node_modules or build artifacts
- Example scenario: large dependencies not using layers
- Example scenario: container images preferred for code > 50mb

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
