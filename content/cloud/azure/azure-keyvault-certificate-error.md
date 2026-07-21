---
title: "[Solution] Azure Key Vault Certificate Error"
description: "Resolve Azure Key Vault certificate creation, renewal, and retrieval failures."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Certificate errors prevent Key Vault from creating, renewing, or serving certificates for TLS and authentication scenarios.

## Common Causes

- Certificate issuance policy references a CA that is not connected to Key Vault
- Certificate request is pending administrator approval and has not been signed
- Key size or algorithm is not supported by the configured certificate policy
- Certificate has expired and auto-renewal was not configured

## How to Fix

### Create a self-signed certificate

```bash
az keyvault certificate get-default-policy \
  --output json > policy.json

az keyvault certificate create \
  --vault-name myKeyVault \
  --name myCert \
  --policy @policy.json
```

### List certificates and their status

```bash
az keyvault certificate list \
  --vault-name myKeyVault \
  --query "[].{Name:name,Enabled:attributes.enabled,Expiry:attributes.expires}"
```

### Set auto-renewal

```bash
az keyvault certificate set-attributes \
  --vault-name myKeyVault \
  --name myCert \
  --enabled true
```

### Download a certificate

```bash
az keyvault certificate download \
  --vault-name myKeyVault \
  --name myCert \
  --file ./myCert.pem
```

## Examples

- Certificate creation fails with `BadParameter` when the key size is too small
- Auto-renewal does not trigger because the certificate policy has no issuer configured
- Certificate download returns a PEM file without the private key due to export permissions

## Related Errors

- [Azure Key Vault Error]({{< relref "/cloud/azure/azure-key-vault-error" >}}) -- General Key Vault errors.
- [Azure Key Vault Access Denied]({{< relref "/cloud/azure/azure-keyvault-access-denied" >}}) -- Access issues.
