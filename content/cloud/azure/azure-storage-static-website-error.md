---
title: "[Solution] Azure Storage Static Website Error"
description: "Fix Azure Storage static website hosting errors including 404 responses and CORS failures."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Static website errors occur when Azure Blob Storage cannot serve static content properly. This causes 404 errors, incorrect content types, or CORS policy violations.

## Common Causes

- Static website hosting is not enabled on the storage account
- `$web` container does not exist or is empty
- CORS policy blocks requests from the frontend domain
- Index document and error document paths are misconfigured

## How to Fix

### Enable static website hosting

```bash
az storage blob service-properties update \
  --account-name mystorageaccount \
  --resource-group myRG \
  --static-website \
  --index-document index.html \
  --404-document 404.html
```

### Upload files to the $web container

```bash
az storage blob upload-batch \
  --account-name mystorageaccount \
  --destination '$web' \
  --source ./dist \
  --overwrite
```

### Configure CORS policy

```bash
az storage cors add \
  --account-name mystorageaccount \
  --services blob \
  --origins "https://myfrontend.azurewebsites.net" \
  --methods GET HEAD OPTIONS \
  --allowed-headers "*" \
  --max-age 3600
```

### Verify the website endpoint

```bash
curl -I https://mystorageaccount.z13.web.core.windows.net/
```

## Examples

- Website returns 404 because the `$web` container has not been populated
- CORS error in browser console when the frontend at azurewebsites.net tries to fetch from blob storage
- Static website serves HTML but CSS and JS files return wrong content type

## Related Errors

- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error" >}}) -- General storage errors.
- [Azure CDN Error]({{< relref "/cloud/azure/azure-cdn-error" >}}) -- CDN errors.
