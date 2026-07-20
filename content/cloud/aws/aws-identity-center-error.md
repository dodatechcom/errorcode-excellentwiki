---
title: "[Solution] AWS IAM Identity Center Error — user/group sync failures"
description: "Fix AWS IAM Identity Center errors. Resolve user, group, and directory sync issues."
error-types: ["api-error"]
severities: ["error"]
weight: 126
---

An AWS IAM Identity Center error occurs when users cannot authenticate, groups fail to sync with external directories, or SCIM provisioning encounters issues. IAM Identity Center (formerly AWS SSO) centralizes identity management.

## Common Causes

- External IdP SCIM endpoint misconfigured
- Directory synchronization job failed
- User attributes do not match IdP schema
- MFA policy blocking user authentication
- Session expiration causing re-authentication loops

## How to Fix

### List Users

```bash
aws identitystore list-users \
  --identity-store-id d-xxx
```

### List Groups

```bash
aws identitystore list-groups \
  --identity-store-id d-xxx
```

### Check Group Memberships

```bash
aws identitystore list-group-memberships \
  --group-id g-xxx
```

### Create User

```bash
aws identitystore create-user \
  --identity-store-id d-xxx \
  --user-name jdoe \
  --name GivenName=John,FamilyName=Doe \
  --emails Value=jdoe@company.com,Type=work
```

### Provision User via SCIM

```bash
aws sso-admin provision-identity-source \
  --instance-arn arn:aws:sso:::instance/ssoins-xxx
```

## Examples

```bash
# Example 1: SCIM sync failed
# ThrottlingException: Too many requests
# Fix: wait and retry, or check SCIM endpoint configuration

# Example 2: User not found
# ResourceNotFoundException: User not found
# Fix: verify user exists in external directory and sync completed
```

## Related Errors

- [AWS SSO Error]({{< relref "/cloud/aws/aws-sso-error" >}}) — SSO portal errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS Organizations Error]({{< relref "/cloud/aws/aws-organizations-error" >}}) — Organizations errors
