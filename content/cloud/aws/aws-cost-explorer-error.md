---
title: "[Solution] AWS Cost Explorer Error — data/forecast/report failures"
description: "Fix AWS Cost Explorer errors. Resolve data retrieval, forecast, and report issues."
error-types: ["api-error"]
severities: ["error"]
weight: 160
---

An AWS Cost Explorer error occurs when cost data is not available, forecasts fail, or reports encounter date range issues. Cost Explorer provides cost visibility but requires correct date ranges and permissions.

## Common Causes

- Data not available for requested time period
- IAM user lacks ce:GetCostAndUsage permissions
- Forecast requires historical data (30+ days)
- Group-by dimensions exceed API limits
- Cost allocation tags not activated

## How to Fix

### Get Cost and Usage

```bash
aws ce get-cost-and-usage \
  --time-period Start=2025-01-01,End=2025-01-31 \
  --granularity MONTHLY \
  --metrics "BlendedCost" \
  --group-by Type=DIMENSION,Key=SERVICE
```

### Get Cost Forecast

```bash
aws ce get-cost-forecast \
  --time-period Start=2025-02-01,End=2025-02-28 \
  --metric BLENDED_COST \
  --granularity MONTHLY \
  --prediction-interval-level 80
```

### List Cost Allocation Tags

```bash
aws ce list-cost-allocation-tags \
  --status Active \
  --query 'CostAllocationTags[*].{Key:TagKey,Status:Status}'
```

### Activate Cost Allocation Tags

```bash
aws ce update-cost-allocation-tags-status \
  --cost-allocation-tags-status '[{"TagKey":"Environment","Status":"Active"}]'
```

### Get Reservation Coverage

```bash
aws ce get-reservation-coverage \
  --time-period Start=2025-01-01,End=2025-01-31 \
  --group-by Type=DIMENSION,Key=SERVICE
```

## Examples

```bash
# Example 1: Data not available
# DataUnavailableException: Data not available for period
# Fix: ensure time period is within available data range

# Example 2: Forecast failed
# DataNotAvailableException: Insufficient data for forecast
# Fix: provide at least 30 days of historical data
```

## Related Errors

- [AWS Budgets Error]({{< relref "/cloud/aws/aws-budgets-error" >}}) — Budgets errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 report errors
