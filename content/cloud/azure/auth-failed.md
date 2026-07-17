---
title: "Azure AADSTS50126: Invalid Username or Password"
description: "AADSTS50126: Invalid username or password — Fix Azure AD authentication failures."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

The `AADSTS50126` error occurs when Azure Active Directory (Entra ID) rejects a login attempt because the username or password is incorrect. This is the most common authentication failure in Azure AD.

## Common Causes

- Incorrect username or password entered
- Account is locked after too many failed attempts
- Multi-factor authentication (MFA) is required but not completed
- The account is a guest user and conditional access blocks the sign-in
- Password was recently changed and the old password is cached

## How to Fix

Verify credentials using the Azure CLI:

```bash
az login --username <email> --password <password>
```

Check if the account is locked:

```bash
az ad user show --id <user-id> --query 'accountEnabled'
```

Reset the password:

```bash
az ad user reset-password --user-id <user-id> --password <new-password> --force-change-password-next-login
```

Check conditional access policies:

```bash
az rest --method GET --uri "https://graph.microsoft.com/v1.0/conditionalAccess/policies" \
  --query 'value[].{Name:displayName,State:state}'
```

## Examples

- User mistypes password after a password rotation policy forces a change
- Service principal secret expired and is no longer valid
- Guest user from another tenant attempts login but conditional access blocks external accounts

## Related Errors

- [Azure Quota Exceeded]({{< relref "/cloud/azure/quota-exceeded" >}}) — Azure subscription quota limits.
- [Azure KeyVault Error]({{< relref "/cloud/azure/keyvault-error" >}}) — KeyVault access denied.
- [AWS IAM Error]({{< relref "/cloud/aws/iam-error" >}}) — AWS equivalent.
