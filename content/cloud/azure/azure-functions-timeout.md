---
title: "[Solution] Azure Functions Timeout Error"
description: "Fix Azure Functions execution timeout errors for long-running operations and async patterns."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Timeout errors occur when Azure Functions exceed the maximum execution time allowed for the hosting plan. This is common with synchronous long-running operations.

## Common Causes

- Function execution exceeds Consumption plan 5-minute default timeout
- Synchronous HTTP calls block the function thread without async patterns
- Database queries or API calls are too slow under load
- Durable Functions orchestrator has too many activities without fan-out/fan-in

## How to Fix

### Increase timeout in host.json

```json
{
  "version": "2.0",
  "functionTimeout": "00:10:00"
}
```

### Upgrade to Premium or Dedicated plan for longer timeouts

```bash
az functionapp plan create \
  --name myPlan \
  --resource-group myRG \
  --location eastus \
  --sku EP1
```

### Use async patterns for HTTP triggers

```csharp
public static async Task<IActionResult> Run(
    [HttpTrigger(AuthorizationLevel.Function, "post")] HttpRequest req)
{
    var result = await ProcessDataAsync(req);
    return new OkObjectResult(result);
}
```

### Enable Durable Functions for orchestration

```bash
az functionapp config appsettings set \
  --name myFuncApp \
  --resource-group myRG \
  --settings "AzureWebJobsStorage=DefaultEndpoints..."
```

## Examples

- HTTP trigger times out after 5 minutes with `FunctionTimeout` exception
- Queue-triggered function fails because processing takes longer than 5 minutes
- Durable Functions orchestrator times out with 50+ activity functions in sequence

## Related Errors

- [Azure Functions Error]({{< relref "/cloud/azure/azure-functions-error" >}}) -- General Functions errors.
- [Azure Functions Cold Start]({{< relref "/cloud/azure/azure-functions-cold-start" >}}) -- Cold start issues.
