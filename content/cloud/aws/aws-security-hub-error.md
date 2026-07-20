---
title: "[Solution] AWS Security Hub Error — integration/finding/std failures"
description: "Fix AWS Security Hub errors. Resolve Security Hub integration, finding aggregation, and standard issues."
error-types: ["api-error"]
severities: ["error"]
weight: 120
---

An AWS Security Hub error occurs when findings fail to aggregate, integrations stop working, or security standards controls report errors. Security Hub centralizes security findings from multiple AWS services.

## Common Causes

- Security Hub not enabled in aggregation region
- Cross-account aggregation permissions missing
- Integration source (GuardDuty, Inspector, Macie) not enabled
- Finding import format does not match ASFF schema
- Custom actions not configured for findings

## How to Fix

### Enable Security Hub

```bash
aws securityhub enable-security-hub \
  --regions us-east-1 us-west-2
```

### Check Integration Status

```bash
aws securityhub describe-integrations \
  --integration-ids default-all
```

### List Findings

```bash
aws securityhub get-findings \
  --max-items 10 \
  --filters '{"SeverityLabel":[{"Value":"HIGH","Comparison":"EQUALS"}]}'
```

### Create Custom Action

```bash
aws securityhub create-action-target \
  --name "Send to SNS" \
  --description "Send high severity findings to SNS"
```

### Enable Standards Subscription

```bash
aws securityhub batch-enable-standards \
  --standards-subscription-requests '[{"StandardsArn":"arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.4.0"}]'
```

## Examples

```bash
# Example 1: Aggregation region mismatch
# InvalidInputException: Aggregation region not enabled
# Fix: enable Security Hub in the aggregation region first

# Example 2: Finding format error
# InvalidFindingException: Finding does not conform to ASFF
# Fix: ensure finding matches AWS Security Finding Format
```

## Related Errors

- [AWS GuardDuty Error]({{< relref "/cloud/aws/aws-guardduty-error" >}}) — GuardDuty findings errors
- [AWS Config Error]({{< relref "/cloud/aws/aws-config-error" >}}) — Config recorder errors
- [AWS CloudTrail Error]({{< relref "/cloud/aws/aws-cloudtrail-error" >}}) — CloudTrail logging errors
