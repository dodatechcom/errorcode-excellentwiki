---
title: "[Solution] AWS Runtime Not Supported"
description: "RuntimeNotSupportedException deprecated runtime."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Runtime Not Supported` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Runtime reached end of support
- Security patches no longer applied
- Node/Python/Java version is deprecated

## How to Fix

### Check runtime

```bash
aws lambda get-function-config --function my-function --query Runtime
```

### Change runtime

```bash
aws lambda update-function-config --function my-function --runtime nodejs20.x
```

## Examples

- Example scenario: runtime reached end of support
- Example scenario: security patches no longer applied
- Example scenario: node/python/java version is deprecated

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
