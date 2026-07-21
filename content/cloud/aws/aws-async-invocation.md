---
title: "[Solution] AWS Async invocation"
description: "AsyncInvocationError events dropped."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Async invocation` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Queue full or throttled
- Payload more than 256KB

## How to Fix

### Check invoke config

```bash
aws lambda get-function-event-invoke-config --function my-function
```

## Examples

- Example scenario: queue full or throttled
- Example scenario: payload more than 256kb

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
