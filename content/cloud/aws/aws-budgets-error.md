---
title: "[Solution] AWS Budgets Error — threshold/notification/action failures"
description: "Fix AWS Budgets errors. Resolve budget threshold, notification, and budget action issues."
error-types: ["api-error"]
severities: ["error"]
weight: 159
---

An AWS Budgets error occurs when budgets fail to track costs, notifications do not send, or budget actions do not trigger. AWS Budgets provides cost and usage monitoring but requires correct threshold configuration.

## Common Causes

- Budget period not matching billing cycle
- SNS topic ARN for notifications incorrect
- Budget action IAM role lacks permissions
- Cost and Usage Report not enabled
- Budget limit set too low causing false alerts

## How to Fix

### List Budgets

```bash
aws budgets describe-budgets \
  --account-id 123456789012 \
  --query 'Budgets[*].{Name:BudgetName,BudgetLimit:BudgetLimit.Amount,Type:BudgetType}'
```

### Get Budget

```bash
aws budgets describe-budget \
  --account-id 123456789012 \
  --budget-name my-monthly-budget
```

### Create Budget

```bash
aws budgets create-budget \
  --account-id 123456789012 \
  --budget '{
    "BudgetName": "monthly-cost-budget",
    "BudgetLimit": {"Amount": "1000", "Unit": "USD"},
    "TimeUnit": "MONTHLY",
    "BudgetType": "COST"
  }'
```

### Create Notification

```bash
aws budgets create-notification \
  --account-id 123456789012 \
  --budget-name my-monthly-budget \
  --notification '{
    "NotificationType": "ACTUAL",
    "ComparisonOperator": "GREATER_THAN",
    "Threshold": 80,
    "ThresholdType": "PERCENTAGE"
  }'
```

### Describe Budget Action

```bash
aws budgets describe-budget-action \
  --account-id 123456789012 \
  --budget-name my-budget \
  --action-id action-xxx
```

## Examples

```bash
# Example 1: Notification not sent
# InternalErrorException: SNS topic not accessible
# Fix: verify SNS topic policy allows AWS Budgets

# Example 2: Budget not tracking
# NotFoundException: Budget not found
# Fix: verify budget name and account ID
```

## Related Errors

- [AWS SNS Error]({{< relref "/cloud/aws/aws-sns-error" >}}) — SNS notification errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS Cost Explorer Error]({{< relref "/cloud/aws/aws-cost-explorer-error" >}}) — Cost Explorer errors
