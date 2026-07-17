---
title: "[Solution] AWS SQS — InvalidSecurity token"
description: "Fix AWS SQS InvalidSecurity token. Resolve SQS authentication and token issues."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An SQS InvalidSecurity token error means the AWS credentials used to sign the SQS request are invalid, expired, or malformed. The SQS service rejects the request before processing.

## What This Error Means

AWS SQS uses SigV4 request signing to authenticate API calls. When the security token is invalid, the service returns `InvalidSecurity` before processing the request. This error is not SQS-specific — it comes from the AWS STS signing layer. The credentials may be expired, the session token may be malformed, or the IAM role assumption may have failed.

## Common Causes

- Expired temporary security credentials from STS
- Malformed or truncated session token
- Wrong AWS account credentials being used
- IAM role session token not refreshed before expiry
- Clock skew causing signature time validation failure
- Access key or secret key is incorrect

## How to Fix

### Verify Current Credentials

```bash
aws sts get-caller-identity
aws sts get-session-token
```

### Refresh Expired Credentials

```bash
# Assume a role
aws sts assume-role \
  --role-arn arn:aws:iam::123456789012:role/my-role \
  --role-session-name my-session

# Use returned credentials
export AWS_ACCESS_KEY_ID=xxx
export AWS_SECRET_ACCESS_KEY=xxx
export AWS_SESSION_TOKEN=xxx
```

### Test SQS Access

```bash
aws sqs list-queues
aws sqs get-queue-attributes --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue
```

### Check IAM Role Trust

```bash
aws iam get-role --role-name my-role \
  --query 'Role.AssumeRolePolicyDocument'
```

### Fix Clock Skew

```bash
# Check system time
date -u
chronyc tracking

# NTP sync
sudo chronyc makestep
```

### Use IAM Roles for EC2

```bash
# Ensure instance profile is attached
aws ec2 describe-instance-attribute \
  --instance-id i-xxx \
  --attribute iamInstanceProfile
```

### Debug with AWS CLI Debug

```bash
aws sqs send-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue \
  --message-body "test" \
  --debug 2>&1 | grep -i "token\|signing"
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error-v2" >}}) — IAM access denied
- [AWS SNS Error]({{< relref "/cloud/aws/aws-sns-error-v2" >}}) — topic not found
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error-v2" >}}) — Lambda runtime error
