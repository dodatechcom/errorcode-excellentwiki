---
title: "[Solution] Azure AD Multi-Factor Authentication Error"
description: "Fix Azure AD MFA failures that block user authentication and service principal sign-ins."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

MFA errors prevent users or service principals from completing authentication when multi-factor verification fails or is not configured.

## Common Causes

- User has not registered MFA methods and the policy requires it
- MFA registration is pending approval in the combined registration workflow
- Phone call or SMS verification fails due to carrier issues
- Conditional access policy requires MFA but the device is not registered

## How to Fix

### Check MFA registration status

```bash
az rest --method GET \
  --uri "https://graph.microsoft.com/v1.0/users/{userId}/authentication/methods"
```

### Reset MFA for a user

```bash
az rest --method POST \
  --uri "https://graph.microsoft.com/v1.0/users/{userId}/authentication/resetMethods"
```

### Configure per-user MFA

```bash
az rest --method PATCH \
  --uri "https://graph.microsoft.com/v1.0/users/{userId}" \
  --body '{
    "authentication": {
      "methodsRegistrationRequired": true
    }
  }'
```

### Create conditional access policy for MFA

```bash
az rest --method POST \
  --uri "https://graph.microsoft.com/v1.0/identity/conditionalAccess/policies" \
  --body '{
    "displayName": "Require MFA for All Users",
    "state": "enabled",
    "conditions": {
      "users": {"includeUsers": ["All"]},
      "applications": {"includeApplications": ["All"]}
    },
    "grantControls": {
      "operator": "OR",
      "builtInControls": ["mfa"]
    }
  }'
```

## Examples

- User receives `AADSTS50076: MFA required` but has not registered any MFA methods
- Service principal authentication fails because the policy requires MFA but SPs cannot do MFA
- Authenticator push notification is never received due to network connectivity issues

## Related Errors

- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error" >}}) -- General Azure AD errors.
- [Azure Conditional Access]({{< relref "/cloud/azure/azure-conditional-access" >}}) -- Conditional access issues.
