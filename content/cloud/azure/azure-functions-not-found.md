---
title: "[Solution] AZURE Function App Not Found"
description: "ResourceNotFound when the specified Function App does not exist."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Function App Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Function app name is incorrect
- Function app was deleted
- Function app in different subscription
- Function app is stopped

## How to Fix

### Check function app

```bash
az functionapp show --name myFuncApp --resource-group myRG --query "{Name:name,State:state}" --output table
```
### List function apps

```bash
az functionapp list --resource-group myRG --query "[].{Name:name,State:state,Runtime:runtime}" --output table
```
### Create function app

```bash
az functionapp create --name myFuncApp --resource-group myRG --storage-account mystorage --consumption-plan eastus --runtime dotnet --functions-version 4
```

## Examples

- Function app not found in resource group
- Function app is in Stopped state

## Related Errors

- [Azure Functions Error]({{< relref "/cloud/azure/azure-functions-error" >}}) -- General Functions errors
- [Runtime Error]({{< relref "/cloud/azure/azure-functions-runtime-error" >}}) -- Runtime
