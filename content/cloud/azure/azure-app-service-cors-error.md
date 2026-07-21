---
title: "[Solution] Azure App Service CORS Error"
description: "Resolve Azure App Service CORS policy errors blocking cross-origin requests from browsers."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

CORS errors prevent frontend applications from accessing App Service APIs. This is a common issue when deploying single-page applications that call a separate backend.

## Common Causes

- Allowed origins list does not include the frontend URL
- Preflight OPTIONS request is not handled by the API
- CORS configuration is set at the platform level but overridden by code
- Wildcard `*` origin is used but credentials are also required

## How to Fix

### Configure CORS allowed origins

```bash
az webapp cors add \
  --name myApp \
  --resource-group myRG \
  --allowed-origins "https://myfrontend.azurewebsites.net"
```

### View current CORS configuration

```bash
az webapp cors show \
  --name myApp \
  --resource-group myRG
```

### Remove incorrect CORS entries

```bash
az webapp cors remove \
  --name myApp \
  --resource-group myRG \
  --allowed-origins "https://oldfrontend.azurewebsites.net"
```

### Handle OPTIONS preflight in code

```csharp
app.UseCors(builder => builder
    .WithOrigins("https://myfrontend.azurewebsites.net")
    .AllowAnyMethod()
    .AllowAnyHeader()
    .AllowCredentials());
```

## Examples

- Browser blocks XHR request with `No 'Access-Control-Allow-Origin' header` error
- Preflight OPTIONS request returns 405 Method Not Allowed
- CORS works for GET requests but fails for POST requests due to missing method allowance

## Related Errors

- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error" >}}) -- General App Service errors.
- [Azure API Management Error]({{< relref "/cloud/azure/azure-api-management-error" >}}) -- API Management CORS.
