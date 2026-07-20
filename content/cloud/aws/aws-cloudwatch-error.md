---
title: "[Solution] AWS CloudWatch Error — metric/alarm/log-group failures"
description: "Fix AWS CloudWatch errors. Resolve metric, alarm, and log group configuration issues."
error-types: ["api-error"]
severities: ["error"]
weight: 127
---

An AWS CloudWatch error occurs when metrics fail to publish, alarms remain in INSUFFICIENT_DATA state, or log groups cannot be created. CloudWatch provides monitoring and observability for AWS resources.

## Common Causes

- Metric namespace or dimension name invalid
- Alarm threshold never reached or data points insufficient
- Log group already exists or retention period invalid
- IAM role lacks PutMetricData permissions
- Cross-account metric access not configured

## How to Fix

### List Alarms

```bash
aws cloudwatch describe-alarms \
  --query 'MetricAlarms[*].{Name:AlarmName,State:StateValue,Action:AlarmActions}'
```

### Put Metric Data

```bash
aws cloudwatch put-metric-data \
  --namespace MyApp \
  --metric-name RequestCount \
  --value 100 \
  --unit Count
```

### Create Log Group

```bash
aws logs create-log-group \
  --log-group-name /aws/myapp/errors \
  --retention-in-days 30
```

### Check Metric Statistics

```bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-xxx \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2025-01-01T01:00:00Z \
  --period 300 \
  --statistics Average
```

### Enable Metrics for Namespace

```bash
aws cloudwatch put-metric-alarm \
  --alarm-name HighCPU \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --evaluation-periods 2 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold
```

## Examples

```bash
# Example 1: Invalid metric name
# InvalidParameterValue: Metric name invalid
# Fix: check metric name and namespace spelling

# Example 2: Alarm stuck in INSUFFICIENT_DATA
# State: INSUFFICIENT_DATA
# Fix: ensure metric has data points and evaluation periods are met
```

## Related Errors

- [AWS CloudWatch Logs Error]({{< relref "/cloud/aws/aws-cloudwatch-logs-error" >}}) — CloudWatch Logs errors
- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
