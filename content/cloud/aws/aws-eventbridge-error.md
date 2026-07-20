---
title: "[Solution] AWS EventBridge Error — rule/bus/target/schedule failures"
description: "Fix AWS EventBridge errors. Resolve rules, event buses, targets, and schedule issues."
error-types: ["api-error"]
severities: ["error"]
weight: 148
---

An AWS EventBridge error occurs when rules fail to trigger, event buses cannot deliver, or scheduled rules misfire. EventBridge provides serverless event bus but requires correct rule and target configuration.

## Common Causes

- Rule pattern does not match incoming events
- Target Lambda function ARN is incorrect
- Event bus does not exist or is not accessible
- Input transformer format invalid
- Scheduler cron expression syntax error

## How to Fix

### List Rules

```bash
aws events list-rules \
  --query 'Rules[*].{Name:Name,State:State,Schedule:ScheduleExpression}'
```

### Describe Rule

```bash
aws events describe-rule \
  --name my-rule
```

### Put Rule

```bash
aws events put-rule \
  --name my-schedule-rule \
  --schedule-expression "rate(5 minutes)" \
  --state ENABLED
```

### Add Target

```bash
aws events put-targets \
  --rule my-rule \
  --targets '[{"Id":"1","Arn":"arn:aws:lambda:us-east-1:123456789012:function:my-function"}]'
```

### List Event Buses

```bash
aws events list-event-buses \
  --query 'EventBuses[*].{Name:Name,ARN:Arn}'
```

## Examples

```bash
# Example 1: Rule pattern mismatch
# No events matched the event pattern
# Fix: verify pattern matches event source and detail-type

# Example 2: Target not found
# TargetNotFoundException: Lambda function not found
# Fix: verify Lambda function ARN and ensure it exists
```

## Related Errors

- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS SNS Error]({{< relref "/cloud/aws/aws-sns-error" >}}) — SNS notification errors
