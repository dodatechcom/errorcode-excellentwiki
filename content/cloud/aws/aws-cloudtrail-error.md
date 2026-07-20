---
title: "[Solution] AWS CloudTrail Error — trail/log-file/delivery failures"
description: "Fix AWS CloudTrail errors. Resolve trail, log file, and S3 delivery issues."
error-types: ["api-error"]
severities: ["error"]
weight: 129
---

An AWS CloudTrail error occurs when trails fail to deliver logs, S3 bucket access is denied, or log file integrity validation fails. CloudTrail records API activity for auditing and compliance.

## Common Causes

- S3 bucket policy does not allow CloudTrail writes
- Log file validation not enabled
- Trail is in a different region than events
- CloudWatch Logs log group not accessible
- Multi-region trail conflicts with single-region trail

## How to Fix

### List Trails

```bash
aws cloudtrail describe-trails \
  --query 'trailList[*].{Name:Name,ARN:TrailARN,S3Bucket:S3BucketName,Logging:IsLogging}'
```

### Check Trail Status

```bash
aws cloudtrail get-trail-status \
  --name arn:aws:cloudtrail:us-east-1:123456789012:trail/my-trail
```

### Create Trail

```bash
aws cloudtrail create-trail \
  --name my-trail \
  --s3-bucket-name my-cloudtrail-bucket \
  --is-multi-region-trail \
  --enable-log-file-validation
```

### Start Logging

```bash
aws cloudtrail start-logging \
  --name arn:aws:cloudtrail:us-east-1:123456789012:trail/my-trail
```

### Lookup Events

```bash
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=EventName,AttributeValue=RunInstances \
  --max-results 10
```

## Examples

```bash
# Example 1: S3 access denied
# S3BucketDoesNotExistException: Bucket does not exist
# Fix: create S3 bucket and add CloudTrail bucket policy

# Example 2: Log delivery failing
# Status: STOPPED, Error: AccessDenied
# Fix: update S3 bucket policy to allow CloudTrail service principal
```

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 bucket errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS Config Error]({{< relref "/cloud/aws/aws-config-error" >}}) — Config recorder errors
