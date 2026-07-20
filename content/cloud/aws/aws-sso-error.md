---
title: "[Solution] AWS SSO Error — portal/permission-set/identity-source failures"
description: "Fix AWS SSO errors. Resolve SSO portal access, permission set, and identity source issues."
error-types: ["api-error"]
severities: ["error"]
weight: 124
---

An AWS SSO error occurs when users cannot access the portal, permission sets fail to assign, or identity source configuration breaks. AWS SSO (now IAM Identity Center) manages single sign-on across AWS accounts.

## Common Causes

- Identity source not configured or mismatched
- Permission set policy exceeds managed policy limits
- Portal URL or session expires
- MFA configuration blocks user login
- Directory sync not working with Active Directory

## How to Fix

### List Permission Sets

```bash
aws sso-admin list-permission-sets \
  --instance-arn arn:aws:sso:::instance/ssoins-xxx
```

### Check Assigned Accounts

```bash
aws sso-admin list-account-assignments \
  --instance-arn arn:aws:sso:::instance/ssoins-xxx \
  --account-id 123456789012
```

### Create Permission Set

```bash
aws sso-admin create-permission-set \
  --instance-arn arn:aws:sso:::instance/ssoins-xxx \
  --name AdminAccess \
  --managed-policies arn:aws:iam::aws:policy/AdministratorAccess
```

### Assign User to Account

```bash
aws sso-admin create-account-assignment \
  --instance-arn arn:aws:sso:::instance/ssoins-xxx \
  --target-id 123456789012 \
  --permission-set-arn arn:aws:sso:::instance/ssoins-xxx/permission-set/xxx \
  --principal-type USER \
  --principal-id user-xxx
```

### List Identity Sources

```bash
aws sso-admin list-identity-sources \
  --instance-arn arn:aws:sso:::instance/ssoins-xxx
```

## Examples

```bash
# Example 1: Permission set too large
# ValidationException: Managed policy size exceeds limit
# Fix: use inline policies or reduce managed policy count

# Example 2: Identity source not found
# ResourceNotFoundException: Identity source not found
# Fix: verify identity source is configured for this instance
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS Organizations Error]({{< relref "/cloud/aws/aws-organizations-error" >}}) — Organizations errors
- [AWS Identity Center Error]({{< relref "/cloud/aws/aws-identity-center-error" >}}) — Identity Center errors
