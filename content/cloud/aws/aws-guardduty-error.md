---
title: "[Solution] AWS GuardDuty Error — finding/detector/malware scan failures"
description: "Fix AWS GuardDuty errors. Resolve GuardDuty finding, detector, and malware scan issues."
error-types: ["api-error"]
severities: ["error"]
weight: 117
---

An AWS GuardDuty error occurs when findings are not generated, detectors fail to initialize, or malware scans encounter permission issues. GuardDuty is a threat detection service that requires proper configuration to monitor effectively.

## Common Causes

- GuardDuty not enabled in the region
- Detector not associated with the account
- S3 protection not enabled for bucket findings
- Malware scan requires EBS snapshot permissions
- Publishing destination CloudWatch Logs not configured

## How to Fix

### Check Detector Status

```bash
aws guardduty list-detectors \
  --query 'DetectorIds'
```

### Get Detector Settings

```bash
aws guardduty get-detector \
  --detector-id xxx
```

### List Findings

```bash
aws guardduty list-findings \
  --detector-id xxx \
  --max-items 10
```

### Enable GuardDuty

```bash
aws guardduty create-detector \
  --enable \
  --publishing-destination S3Destination=BucketName=my-guardduty-bucket
```

### Create Malware Scan

```bash
aws guardduty create-malware-scan \
  --detector-id xxx \
  --resource-arn arn:aws:ec2:us-east-1:123456789012:instance/i-xxx
```

## Examples

```bash
# Example 1: Detector not found
# BadRequestException: Detector not found
# Fix: enable GuardDuty in the target region

# Example 2: Publishing destination failed
# InvalidInputException: S3 bucket not accessible
# Fix: verify bucket policy allows GuardDuty writes
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS CloudTrail Error]({{< relref "/cloud/aws/aws-cloudtrail-error" >}}) — CloudTrail logging errors
- [AWS Config Error]({{< relref "/cloud/aws/aws-config-error" >}}) — Config recorder errors
