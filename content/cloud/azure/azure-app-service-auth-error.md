---
title: "[Solution] Azure App Service Authentication Error"
description: "Fix Azure App Service Easy Auth failures for built-in identity provider authentication."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Authentication errors in App Service Easy Auth prevent users from logging in via Azure AD, Google, Facebook, or other configured identity providers.

## Common Causes

- Authentication provider configuration is missing or has invalid client secret
- Redirect URI does not match the configured callback URL
- Token validation fails because the issuer URL is incorrect
- Easy Auth extension is disabled or has not been deployed to the slot

## How to Fix

### Enable App Service authentication

```bash
az webapp auth update \
  --name myApp \
  --resource-group myRG \
  --enabled true \
  --action LoginWithAzureActiveDirectory
```

### Configure Azure AD provider

```bash
az webapp auth update \
  --name myApp \
  --resource-group myRG \
  --aad-allowed-token-audiences "https://myapp.azurewebsites.net" \
  --aad-client-id "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" \
  --aad-client-secret "mySecret" \
  --token-store enabled
```

### Check authentication status

```bash
az webapp auth show \
  --name myApp \
  --resource-group myRG
```

### Test the authentication endpoint

```bash
curl -I https://myApp.azurewebsites.net/.auth/me
```

## Examples

- Login redirects to Azure AD but callback returns `AuthenticationFailed` with invalid state
- Easy Auth works in the default slot but not in the staging slot
- API calls return 401 Unauthorized even after successful browser login

## Related Errors

- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error" >}}) -- General App Service errors.
- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error" >}}) -- Azure AD issues.
