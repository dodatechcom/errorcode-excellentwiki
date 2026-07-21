---
title: "[Solution] Azure Cosmos DB SDK Error"
description: "Fix Azure Cosmos DB SDK compatibility and configuration errors in application code."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

SDK errors occur when the Cosmos DB client library is misconfigured or incompatible with the database API version. This causes connection failures and query errors.

## Common Causes

- SDK version is outdated and does not support newer API features
- Connection string format is incorrect or contains invalid characters
- Direct mode configuration requires firewall rules that are not in place
- Gateway mode is used but the endpoint URL is incorrect

## How to Fix

### Verify SDK version

```bash
dotnet list package --include-outdated | grep Cosmos
```

### Update SDK to latest version

```bash
dotnet add package Microsoft.Azure.Cosmos --version 3.42.0
```

### Configure connection in code

```csharp
var client = new CosmosClient(
    accountEndpoint: "https://myCosmosDB.documents.azure.com:443/",
    authKeyOrResourceToken: "myPrimaryKey",
    new CosmosClientOptions
    {
        ConnectionMode = ConnectionMode.Gateway,
        MaxRetryAttemptsOnRateLimitedRequests = 9,
        MaxRetryWaitTimeOnRateLimitedRequests = TimeSpan.FromSeconds(30)
    });
```

### Validate connection string

```bash
az cosmosdb keys list \
  --name myCosmosDB \
  --resource-group myRG \
  --query primaryMasterKey
```

## Examples

- SDK throws `ArgumentException` when connection string is missing the AccountEndpoint
- Direct mode connection fails with `SocketException` because the VM is not in the allowed subnet
- Gateway mode works but direct mode fails with TLS handshake errors

## Related Errors

- [Azure Cosmos DB Error]({{< relref "/cloud/azure/azure-cosmos-error" >}}) -- General Cosmos DB errors.
- [Azure Cosmos Throttling]({{< relref "/cloud/azure/azure-cosmos-throttling" >}}) -- Throttling issues.
