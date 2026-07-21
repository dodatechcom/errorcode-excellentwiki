---
title: "[Solution] Azure Web App SSL Error"
description: "Fix Azure App Service TLS/SSL certificate errors preventing secure HTTPS connections."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

SSL errors in App Service prevent browsers and clients from establishing secure HTTPS connections. This causes certificate warnings and blocked requests.

## Common Causes

- Custom SSL certificate has expired and needs renewal
- Certificate is bound to the wrong hostname or slot
- TLS version is set to 1.0 or 1.1 which is deprecated
- Managed certificate was revoked or not renewed automatically

## How to Fix

### Check custom domain bindings

```bash
az webapp config ssl list \
  --resource-group myRG \
  --query "[].{Name:name,Thumbprint:thumbprint,Subject:subjectName}"
```

### Upload an updated certificate

```bash
az webapp config ssl upload \
  --name myApp \
  --resource-group myRG \
  --certificate-file ./mycert.pfx \
  --certificate-password "certPassword"
```

### Bind certificate to hostname

```bash
az webapp config ssl bind \
  --name myApp \
  --resource-group myRG \
  --certificate-thumbprint "thumbprint" \
  --hostname mydomain.com \
  --ssl-type SNI
```

### Set TLS version

```bash
az webapp config set \
  --name myApp \
  --resource-group myRG \
  --min-tls-version 1.2
```

## Examples

- Browser shows `NET::ERR_CERT_DATE_INVALID` because the App Service certificate expired
- SSL binding fails with `CertificateNotFound` because the certificate was uploaded to the wrong resource group
- Managed certificate was auto-renewed but the binding was not updated to the new thumbprint

## Related Errors

- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error" >}}) -- General App Service errors.
- [Azure Key Vault Certificate Error]({{< relref "/cloud/azure/azure-keyvault-certificate-error" >}}) -- Certificate issues.
