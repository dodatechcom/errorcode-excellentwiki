---
title: "[Solution] Azure API Management Backend Error"
description: "Fix Azure API Management backend connection and response errors for proxied APIs."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Backend errors in API Management occur when the gateway cannot reach or get a valid response from the backend service. This returns 502 or 504 errors to API consumers.

## Common Causes

- Backend URL is incorrect or the service has been moved
- Backend service is down or returning error responses
- TLS certificate on the backend is expired or not trusted
- Backend timeout is shorter than the API Management gateway timeout

## How to Fix

### Check backend connectivity

```bash
az apim api backend show \
  --resource-group myRG \
  --service-name myAPIM \
  --backend-id myBackend \
  --query "url"
```

### Test backend health

```bash
curl -I https://myBackend.azurewebsites.net/health
```

### Update backend URL

```bash
az apim api backend update \
  --resource-group myRG \
  --service-name myAPIM \
  --backend-id myBackend \
  --protocol http \
  --url "https://new-backend.azurewebsites.net"
```

### Configure backend timeout

```xml
<policies>
    <outbound>
        <set-backend-service base-url="https://myBackend.azurewebsites.net" />
        <timeout seconds="30" />
    </outbound>
</policies>
```

## Examples

- API returns 502 Bad Gateway because the backend returns HTML instead of JSON
- Backend connection times out after 60 seconds but APIM gateway timeout is 30 seconds
- Backend returns 403 because the API Management managed identity is not authorized

## Related Errors

- [Azure API Management Error]({{< relref "/cloud/azure/azure-api-management-error" >}}) -- General APIM errors.
- [Azure Connection Failed]({{< relref "/cloud/azure/azure-connection-failed" >}}) -- Connection issues.
