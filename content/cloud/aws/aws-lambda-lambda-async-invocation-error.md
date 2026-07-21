---
title: "[Solution] AWS Lambda Async Invocation Error"
description: "AsyncInvocationError when events are dropped."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Async Invocation Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Async event queue is full or throttled
- Function concurrency limit blocks new events
- Event payload exceeds the async payload limit (256KB)
- No DLQ configured and retries exhausted
- Too many async events accumulating

## How to Fix

### Check event invoke config

```bash
aws lambda get-function-event-invoke-config --function-name my-function
```

## Examples

- Example scenario: async event queue is full or throttled
- Example scenario: function concurrency limit blocks new events
- Example scenario: event payload exceeds the async payload limit (256kb)
- Example scenario: no dlq configured and retries exhausted

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
