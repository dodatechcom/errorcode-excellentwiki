---
title: "Azure Authentication Failed"
description: "AuthenticationFailed - Authentication failed, check your credentials"
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `AuthenticationFailed` error occurs when Azure cannot validate the credentials provided in a request. This typically involves invalid, expired, or misconfigured authentication tokens.

## Common Causes

- Expired access token or refresh token
- Incorrect client ID, client secret, or tenant ID
- Missing or wrong audience/scope in the token
- Conditional Access policies blocking the sign-in

## How to Fix

Re-authenticate using the Azure CLI:

```bash
az login --service-principal \
  --username <client-id> \
  --password <client-secret> \
  --tenant <tenant-id>
```

Verify the current account:

```bash
az account show
```

## Examples

- Using a service principal whose client secret has expired
- Calling the Azure Resource Manager API with a token issued for a different tenant
- Missing the required scope (e.g., `https://management.azure.com/.default`) in a client credentials flow

## Related Errors

- [Azure Resource Not Found]({{< relref "/cloud/azure/resource-not-found" >}})
- [AWS S3 Access Denied]({{< relref "/cloud/aws/s3-access-denied" >}})
- [GCP Permission Denied]({{< relref "/cloud/gcp/permission-denied" >}})
