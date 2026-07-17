---
title: "[Solution] Azure Storage — authentication failed"
description: "Fix Azure Storage authentication failed. Resolve storage account access key and SAS token issues."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Azure Storage authentication failed error means the client cannot authenticate to the storage account using the provided credentials. The access key, SAS token, or Azure AD token is invalid or missing.

## What This Error Means

Azure Storage supports three authentication methods: storage account access keys, shared access signatures (SAS), and Azure AD (Entra ID) tokens. An authentication failure means none of the provided credentials are valid — the access key may be regenerated, the SAS token may be expired, or the Azure AD identity may lack the required role assignment. The error appears as `Server failed to authenticate the request` (HTTP 403) or `The specified access key is not valid`.

## Common Causes

- Storage account access key was rotated (old key no longer valid)
- SAS token has expired
- Azure AD token is for the wrong audience or expired
- Storage account name is misspelled in the connection string
- The identity lacks the `Storage Blob Data Reader` or equivalent role
- Account-level SAS does not include required permissions

## How to Fix

### Check Storage Account Access Keys

```bash
az storage account keys list \
  --account-name mystorageaccount \
  --resource-group my-rg
```

### Regenerate Access Keys

```bash
az storage account keys renew \
  --account-name mystorageaccount \
  --resource-group my-rg \
  --key key1
```

### Generate SAS Token

```bash
az storage container generate-sas \
  --account-name mystorageaccount \
  --container-name mycontainer \
  --permissions rwdl \
  --expiry 2025-12-31
```

### Test Connection

```bash
az storage blob list \
  --account-name mystorageaccount \
  --container-name mycontainer \
  --account-key <key>
```

### Assign Azure AD Role

```bash
az role assignment create \
  --assignee <principal-id> \
  --role "Storage Blob Data Contributor" \
  --scope "/subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.Storage/storageAccounts/<account>"
```

### Use DefaultAzureCredential

```python
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

credential = DefaultAzureCredential()
client = BlobServiceClient(
    account_url="https://mystorageaccount.blob.core.windows.net",
    credential=credential
)
```

### Verify Connection String

```bash
# Check connection string format
# DefaultEndpointsProtocol=https;AccountName=mystorageaccount;AccountKey=xxx;EndpointSuffix=core.windows.net
```

## Related Errors

- [Azure Key Vault Error]({{< relref "/cloud/azure/azure-key-vault-error-v2" >}}) — ForbiddenByPolicy
- [Azure AD Error]({{< relref "/cloud/azure/azure-ad-error-v2" >}}) — redirect URI mismatch
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error-v2" >}}) — S3 access denied
