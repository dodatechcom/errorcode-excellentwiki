---
title: "[Solution] AWS Lambda Timeout Error"
description: "Task timed out when Lambda duration exceeds timeout limit."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Timeout Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Function execution time exceeds defined timeout
- Cold start takes up significant time
- Infinite loops or blocking I/O in code
- External API calls are slow or hanging
- Large dataset processing takes too long

## How to Fix

### Check timeout setting

```bash
aws lambda get-function-configuration --function-name my-function --query Timeout
```

### Update timeout

```bash
aws lambda update-function-configuration --function-name my-function --timeout 30
```

## Examples

- Example scenario: function execution time exceeds defined timeout
- Example scenario: cold start takes up significant time
- Example scenario: infinite loops or blocking i/o in code
- Example scenario: external api calls are slow or hanging

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
