---
title: "[Solution] AWS Config Error — recorder/rules/remediation failures"
description: "Fix AWS Config errors. Resolve Config recorder, rules, and remediation configuration issues."
error-types: ["api-error"]
severities: ["error"]
weight: 130
---

An AWS Config error occurs when the configuration recorder fails to start, rules evaluate incorrectly, or remediation actions do not trigger. Config tracks resource configuration changes for compliance.

## Common Causes

- Config recorder not started or no IAM role assigned
- S3 bucket for Config delivery not accessible
- Rule evaluation frequency too high causing throttling
- Remediation action target does not exist
- Config rule Lambda function not configured

## How to Fix

### Check Recorder Status

```bash
aws configservice describe-configuration-recorder-status \
  --query 'ConfigurationRecordersStatus[*].{Name:name,Recording:recording,LastStatus:lastStopDeliveryStatus}'
```

### Start Recorder

```bash
aws configservice start-configuration-recorder \
  --configuration-recorder-name default
```

### List Config Rules

```bash
aws configservice describe-config-rules \
  --query 'ConfigRules[*].{Name:ConfigRuleName,State:ComplianceType}'
```

### Create Config Rule

```bash
aws configservice put-config-rule \
  --config-rule '{
    "ConfigRuleName": "s3-bucket-public-read-prohibited",
    "Source": {
      "Owner": "AWS",
      "SourceIdentifier": "S3_BUCKET_PUBLIC_READ_PROHIBITED"
    }
  }'
```

### Get Compliance Details

```bash
aws configservice get-compliance-details-by-config-rule \
  --config-rule-name s3-bucket-public-read-prohibited
```

## Examples

```bash
# Example 1: Recorder not started
# NoAvailableConfigurationRecorderException
# Fix: create and start configuration recorder

# Example 2: S3 delivery bucket access denied
# InsufficientDeliveryPolicyException
# Fix: add Config service write permissions to S3 bucket
```

## Related Errors

- [AWS CloudTrail Error]({{< relref "/cloud/aws/aws-cloudtrail-error" >}}) — CloudTrail logging errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 bucket errors
