---
title: "[Solution] AWS Organizations Error — policy/account/member failures"
description: "Fix AWS Organizations errors. Resolve Organizations policy, account creation, and member issues."
error-types: ["api-error"]
severities: ["error"]
weight: 122
---

An AWS Organizations error occurs when account creation fails, SCPs block actions, or member account relationships break. Organizations manages multi-account AWS environments but strict policies can cause unexpected failures.

## Common Causes

- SCP blocks required actions for member accounts
- Account creation limit reached
- Member account is suspended
- Organization root cannot be modified
- Handshake invitation not accepted

## How to Fix

### List Accounts

```bash
aws organizations list-accounts \
  --query 'Accounts[*].{ID:Id,Email:Email,Status:Status}'
```

### Check Organization Policy

```bash
aws organizations list-policies-for-target \
  --target-id ou-xxx \
  --filter SERVICE_CONTROL_POLICY
```

### Create Account

```bash
aws organizations create-account \
  email=new-account@company.com \
  account-name="New Account"
```

### Attach SCP

```bash
aws organizations attach-policy \
  policy-id p-FullAWSAccess \
  target-id 123456789012
```

### Invite Account to Organization

```bash
aws organizations invite-account-to-organization \
  --account Id=098765432109,Type=ACCOUNT
```

## Examples

```bash
# Example 1: SCP blocking action
# AccessDenied: User is not authorized to perform this action
# Fix: detach or modify the SCP blocking the action

# Example 2: Account limit reached
# AccountLimitExceededException: Maximum accounts reached
# Fix: request quota increase from AWS Support
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS RAM Error]({{< relref "/cloud/aws/aws-ram-error" >}}) — RAM share errors
- [AWS Control Tower Error]({{< relref "/cloud/aws/aws-control-tower-error" >}}) — Control Tower errors
