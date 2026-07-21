---
title: "[Solution] AWS Lambda Runtime Not Supported"
description: "InvalidParameterValueException when the specified runtime is not supported."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Runtime Not Supported` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Runtime identifier is deprecated or removed
- Runtime version does not exist
- Runtime not available in target region
- Custom runtime without bootstrap

## How to Fix

### List available runtimes

```bash
aws lambda get-account-settings --query AccountLimit
```
### Update runtime

```bash
aws lambda update-function-configuration --function-name my-function --runtime python3.12
```
### Use provided runtime

```bash
aws lambda update-function-configuration --function-name my-function --runtime provided.al2023
```

## Examples

- Using python2.7 which was deprecated
- Using dotnetcore3.1 which is no longer supported

## Related Errors

- [Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General Lambda errors
- [Handler Not Found]({{< relref "/cloud/aws/aws-lambda-handler-not-found" >}}) -- Handler issues
