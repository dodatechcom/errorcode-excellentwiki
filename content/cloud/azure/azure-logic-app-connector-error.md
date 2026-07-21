---
title: "[Solution] Azure Logic Apps Connector Error"
description: "Fix Azure Logic Apps connector authentication and configuration failures for external services."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Connector errors prevent Logic Apps from connecting to external services like Salesforce, SAP, or custom APIs. This breaks workflow automation that depends on those connections.

## Common Causes

- Connector OAuth token has expired and needs re-authentication
- Connection was created in a different region than the Logic App
- Custom connector endpoint is unreachable due to firewall restrictions
- Connector requires a premium plan but the Logic App is on Consumption

## How to Fix

### List connections in a Logic App

```bash
az rest --method GET \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Logic/workflows/myLogicApp/connections?api-version=2019-05-01"
```

### Update connection credentials

```bash
az rest --method PUT \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Logic/workflows/myLogicApp/connections/myConnection?api-version=2019-05-01" \
  --body '{"properties":{"parameterValues":{"token":"newAccessToken"}}}'
```

### Test custom connector

```bash
az rest --method POST \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Web/customApis/myConnector/testConnection?api-version=2022-09-01"
```

### Verify connector availability

```bash
az rest --method GET \
  --uri "https://management.azure.com/subscriptions/xxx/providers/Microsoft.Web/locations/eastus/managedApis?api-version=2022-09-01" \
  --query "value[?name=='slack']"
```

## Examples

- Salesforce connector fails with `TokenRefreshFailed` after the refresh token expires
- Custom connector returns `CertificateValidationFailed` due to an expired TLS certificate
- Logic App on Consumption plan cannot use premium connectors like SAP

## Related Errors

- [Azure Logic Apps Error]({{< relref "/cloud/azure/azure-logic-apps-error" >}}) -- General Logic Apps errors.
- [Azure API Management Error]({{< relref "/cloud/azure/azure-api-management-error" >}}) -- API Management errors.
