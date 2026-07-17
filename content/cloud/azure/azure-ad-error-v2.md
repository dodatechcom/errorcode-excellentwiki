---
title: "[Solution] Azure AD — AADSTS50011 redirect URI mismatch"
description: "Fix Azure AD AADSTS50011 redirect URI mismatch. Resolve Entra ID redirect URI configuration issues."
cloud: ["azure"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["azure", "ad", "entra-id", "redirect", "uri", "mismatch", "aadsts50011"]
weight: 5
---

An Azure AD AADSTS50011 error means the redirect URI in the authentication request does not match any redirect URI registered in the application registration. Entra ID rejects the sign-in attempt.

## What This Error Means

During OAuth 2.0 or OpenID Connect flows, Azure AD (Entra ID) validates the `redirect_uri` parameter against the redirect URIs configured in the app registration. If the URI doesn't match exactly — including protocol, hostname, port, and path — Entra ID returns `AADSTS50011: The reply URL specified in the request does not match the reply URLs configured for the application`. This prevents the authorization code or token from being delivered to the correct endpoint.

## Common Causes

- Redirect URI in code/config does not match app registration
- Trailing slash mismatch (e.g., `/callback` vs `/callback/`)
- HTTP vs HTTPS mismatch
- Localhost port mismatch (e.g., `localhost:3000` vs `localhost:8080`)
- Redirect URI not added to the app registration at all
- Using a different tenant's app registration

## How to Fix

### Check App Registration Redirect URIs

```bash
az ad app show --id <app-id> --query 'web.redirectUris'
az ad app show --id <app-id> --query 'publicClient.redirectUris'
```

### Add Redirect URI

```bash
az webapp auth update --name my-app --resource-group my-rg \
  --redirect-uris "https://myapp.azurewebsites.net/auth/callback"
```

### Fix Redirect URI in Code

```python
# Ensure redirect URI matches exactly
REDIRECT_URI = "https://myapp.azurewebsites.net/auth/callback"
# Not: http://myapp.azurewebsites.net/auth/callback
# Not: https://myapp.azurewebsites.net/auth/callback/
```

### List All Registered Redirect URIs

```bash
az rest --method GET \
  --uri "https://graph.microsoft.com/v1.0/applications/<app-id>?" \
  --query 'web.redirectUris'
```

### Test Authentication Flow

```bash
curl -v "https://login.microsoftonline.com/<tenant>/oauth2/v2.0/authorize?\
client_id=<app-id>&\
redirect_uri=https://myapp.azurewebsites.net/auth/callback&\
response_type=code&\
scope=openid"
```

### Check Specific Error Code

```bash
# AADSTS50011: Reply address not found
# Fix: Add the redirect URI to the app registration

# AADSTS50011: Reply address mismatch
# Fix: Ensure exact match including protocol, host, port, path
```

## Related Errors

- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error-v2" >}}) — Azure AD authentication
- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error-v2" >}}) — 503 Service Unavailable
- [Azure Key Vault Error]({{< relref "/cloud/azure/azure-key-vault-error-v2" >}}) — ForbiddenByPolicy
