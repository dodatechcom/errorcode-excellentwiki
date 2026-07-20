---
title: "[Solution] AWS Personal Health Dashboard Error — event notification failures"
description: "Fix AWS Health Dashboard errors. Resolve Personal Health event, notification, and API issues."
error-types: ["api-error"]
severities: ["error"]
weight: 132
---

An AWS Personal Health Dashboard error occurs when health events are not visible, notifications fail to deliver, or the Health API returns permission errors. Personal Health Dashboard provides proactive guidance on AWS service health.

## Common Causes

- Health API permissions not granted to IAM user
- CloudWatch Events rule for Health not configured
- Event ARN format incorrect for API calls
- Organization level health events not visible to member accounts
- Event filter not matching current events

## How to Fix

### List Health Events

```bash
aws health describe-events \
  --query 'events[*].{ARN:ARN,Service:service,Type:type,StatusCode:statusCode}'
```

### Get Event Details

```bash
aws health describe-event-details \
  --event-arns arn:aws:health:us-east-1::event/ECS/MAINTENANCE/xxx
```

### Check Event Affected Entities

```bash
aws health describe-affected-entities \
  --event-arn arn:aws:health:us-east-1::event/ECS/MAINTENANCE/xxx
```

### Create CloudWatch Events Rule

```bash
aws events put-rule \
  --name health-events-rule \
  --event-pattern '{"source":["aws.health"],"detail-type":["AWS Health Event"]}'
```

### List Health Services

```bash
aws health describe-health-services-status
```

## Examples

```bash
# Example 1: Access denied
# AccessDeniedException: Health API access denied
# Fix: add health:* permissions to IAM policy

# Example 2: No events found
# NoHealthEventsFoundException: No events in timeframe
# Fix: expand search timeframe or check correct region
```

## Related Errors

- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) — CloudWatch event errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS SNS Error]({{< relref "/cloud/aws/aws-sns-error" >}}) — SNS notification errors
