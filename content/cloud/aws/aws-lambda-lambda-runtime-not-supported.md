---
title: "[Solution] AWS Lambda Runtime Not Supported"
description: "RuntimeNotSupportedException when the Lambda runtime is deprecated."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Runtime Not Supported` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Runtime reached end of support date
- AWS ended standard support for the runtime
- Security patches no longer applied
- Node.js/Python/Java/PHP version is deprecated
- Runtime SDK compatibility issues

## How to Fix

### Check current runtime

```bash
aws lambda get-function-configuration --function-name my-function --query Runtime
```

### Update to newer runtime

```bash
aws lambda update-function-configuration --function=my-function --runtime=nodejs20.x
```

## Examples

- Example scenario: runtime reached end of support date
- Example scenario: aws ended standard support for the runtime
- Example scenario: security patches no longer applied
- Example scenario: node.js/python/java/php version is deprecated

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
