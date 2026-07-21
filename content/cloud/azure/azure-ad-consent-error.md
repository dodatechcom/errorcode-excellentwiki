---
title: "[Solution] Azure AD Consent Error"
description: "Fix Azure AD admin and user consent errors preventing application permission grants."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Consent errors occur when Azure AD blocks permission grants due to tenant-level consent policies. This prevents applications from accessing Microsoft Graph or other APIs.

## Common Causes

- Admin consent is required but has not been granted for high-privilege permissions
- User consent is disabled in the tenant and no admin has approved the app
- Consent request workflow is enabled but the request has not been approved
- Application requests permissions that do not exist in the API

## How to Fix

### Grant admin consent via CLI

```bash
az rest --method POST \
  --uri "https://login.microsoftonline.com/{tenantId}/adminconsent" \
  --body '{
    "clientId": "appId",
    "state": "12345",
    "redirect_uri": "https://myApp.azurewebsites.net"
  }'
```

### Check consent policies

```bash
az rest --method GET \
  --uri "https://graph.microsoft.com/v1.0/policies/authorizationPolicy"
```

### Enable user consent for specific apps

```bash
az rest --method PATCH \
  --uri "https://graph.microsoft.com/v1.0/policies/authorizationPolicy" \
  --body '{
    "defaultUserRolePermissions": {
      "permissionGrantPoliciesAssigned": ["UserConsentInitiated"]
    }
  }'
```

### List application permissions

```bash
az ad app show --id appId --query "requiredResourceAccess"
```

## Examples

- Users see `AADSTS65001: The user or administrator has not consented` error
- Admin consent redirect loop when the redirect URI is misconfigured
- Application permissions for Microsoft Graph require tenant-wide admin consent

## Related Errors

- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error" >}}) -- General Azure AD errors.
- [Azure AD Permission Denied]({{< relref "/cloud/azure/azure-ad-permission-denied" >}}) -- Permission issues.
