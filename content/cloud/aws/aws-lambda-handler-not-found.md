---
title: "[Solution] AWS Lambda Handler Not Found"
description: "HandlerNotFoundException when Lambda cannot find the handler."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Handler Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Handler name does not match code
- Module path is incorrect
- Function file name does not match module path
- Deployment package missing handler file

## How to Fix

### Check handler config

```bash
aws lambda get-function-configuration --function-name my-function --query Handler
```
### Update handler

```bash
aws lambda update-function-configuration --function-name my-function --handler src/index.handler
```
### Test handler

```bash
aws lambda invoke --function-name my-function --payload '{"key":"value"}' response.json
```

## Examples

- Handler set to index.handler but file is named lambda_function.py
- Handler path is handler.main but function is lambda_handler

## Related Errors

- [Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General Lambda errors
- [Function Not Found]({{< relref "/cloud/aws/aws-lambda-function-not-found" >}}) -- Function not found
