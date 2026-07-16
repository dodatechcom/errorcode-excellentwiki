---
title: "AWS Lambda Error: Unable to Import Module / Task Timed Out"
description: "Lambda error: Unable to import module / Task timed out — Fix AWS Lambda function errors."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "lambda", "serverless", "timeout", "import", "module", "cold-start"]
weight: 5
---

Lambda errors include `Unable to import module` (initialization failure) and `Task timed out after N seconds` (execution exceeded timeout). These are among the most common Lambda debugging scenarios.

## Common Causes

- `Unable to import module`: missing dependency in the deployment package or wrong handler path
- `Task timed out`: function exceeds the configured timeout (default 3 seconds)
- Wrong runtime specified (e.g., Python 3.8 handler on a Python 3.12 runtime)
- Missing environment variables or secrets required at import time

## How to Fix

For `Unable to import module`, check the handler configuration and package:

```bash
# Verify the handler exists in the deployment package
unzip -l function.zip | grep index.py

# Check Lambda function configuration
aws lambda get-function-configuration \
  --function-name my-function \
  --query 'Handler'
```

Install dependencies for the correct platform:

```bash
# Install Python dependencies for Lambda (Linux x86_64)
pip install -r requirements.txt -t ./package --platform manylinux2014_x86_64

# Install Node.js dependencies
npm install --production
```

For `Task timed out`, increase the timeout:

```bash
aws lambda update-function-configuration \
  --function-name my-function \
  --timeout 30
```

View CloudWatch logs:

```bash
aws logs tail /aws/lambda/my-function --follow
```

## Examples

- `Unable to import module 'handler'`: the file is named `lambda_function.py` but handler is set to `handler.handler`
- `Task timed out after 3.00 seconds`: Lambda is waiting for a database connection that never completes
- Cold start timeout: initializing ML models at import time takes longer than the timeout

## Related Errors

- [AWS AccessDenied]({{< relref "/cloud/aws/access-denied" >}}) — Lambda execution role lacks permissions.
- [AWS Throttling]({{< relref "/cloud/aws/throttling" >}}) — Lambda invocation throttled.
- [Azure App Service Error]({{< relref "/cloud/azure/app-service-error" >}}) — Azure equivalent.
