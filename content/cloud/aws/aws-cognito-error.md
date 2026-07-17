---
title: "[Solution] AWS Cognito Authentication Error"
description: "Fix AWS Cognito authentication errors. Resolve Cognito user pool issues."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "cognito", "authentication", "user-pool", "login"]
weight: 5
---

An AWS Cognito authentication error occurs when users cannot authenticate through Cognito User Pools. This can be caused by credential, configuration, or policy issues.

## Common Causes

- Incorrect username or password
- User account is in CONFIRMED state (requires confirmation)
- MFA challenge not completed
- App client secret is misconfigured
- Token has expired or is invalid

## How to Fix

### Check User Status

```bash
aws cognito-idp admin-get-user \
  --user-pool-id us-east-1_xxxxx \
  --username myuser
```

### Initiate Auth

```bash
aws cognito-idp initiate-auth \
  --auth-flow USER_PASSWORD_AUTH \
  --client-id xxxxx \
  --auth-parameters USERNAME=myuser,PASSWORD=mypass
```

### Reset Password

```bash
aws cognito-idp admin-set-user-password \
  --user-pool-id us-east-1_xxxxx \
  --username myuser \
  --password NewPass123! \
  --permanent
```

### Confirm User

```bash
aws cognito-idp admin-confirm-sign-up \
  --user-pool-id us-east-1_xxxxx \
  --username myuser
```

## Examples

```bash
# Example 1: NotAuthorizedException
# Incorrect username or password
# Fix: verify credentials or reset password

# Example 2: UserNotConfirmedException
# User account not confirmed
# Fix: admin-confirm-sign-up
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission denied
- [AWS API Gateway Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) — API Gateway error
