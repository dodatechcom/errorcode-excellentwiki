---
title: "[Solution] Azure AD Token Expired Error"
description: "Fix Azure AD token expiration errors causing authentication failures in applications."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Token expiration errors occur when Azure AD access or refresh tokens have passed their validity period. This causes applications to fail when calling protected APIs.

## Common Causes

- Access token lifetime is set too short for the application use case
- Refresh token was revoked due to security policy or password change
- Token cache was cleared and the application must re-authenticate
- Application uses long-lived tokens that exceed the maximum allowed lifetime

## How to Fix

### Configure token lifetime policy

```bash
az rest --method POST \
  --uri "https://graph.microsoft.com/v1.0/policies/tokenLifetimePolicies" \
  --body '{
    "definition": [
      "{\"TokenLifetimePolicy\":{\"Version\":1,\"AccessTokenLifetime\":\"01:00:00\",\"MaxInactiveTime\":\"14.00:00:00\"}}"
    ],
    "displayName": "CustomTokenPolicy",
    "type": "TokenLifetimePolicy"
  }'
```

### Apply policy to application

```bash
az rest --method POST \
  --uri "https://graph.microsoft.com/v1.0/applications/{objectId}/addTokenLifetimePolicy" \
  --body '{"id": "policyId"}'
```

### Acquire a new token using MSAL

```csharp
var app = PublicClientApplicationBuilder
    .Create(clientId)
    .WithAuthority(AzureCloudInstance.AzurePublic, tenantId)
    .WithRedirectUri("http://localhost")
    .Build();

var accounts = await app.GetAccountsAsync();
var result = await app.AcquireTokenSilent(scopes, accounts.FirstOrDefault())
    .WithForceRefresh(true)
    .ExecuteAsync();
```

## Examples

- API calls return `401 Unauthorized` with `token_expired` error in the response
- Refresh token fails with `invalid_grant` because the user changed their password
- Silent token acquisition throws `MsalUiRequiredException` requiring interactive login

## Related Errors

- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error" >}}) -- General Azure AD errors.
- [Azure App Service Auth]({{< relref "/cloud/azure/azure-app-service-auth-error" >}}) -- App Service auth.
