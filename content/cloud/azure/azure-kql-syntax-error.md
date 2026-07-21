---
title: "[Solution] AZURE KQL Syntax Error"
description: "KQLSyntaxError for Log Analytics Query."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `KQL Syntax Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Syntax error in KQL
- Table not found
- Time range filter wrong

## How to Fix

### Run query

```bash
az monitor log-analytics query -w myWorkspace --analytics-query "Heartbeat | count"
```

## Examples

- Example scenario: syntax error in kql
- Example scenario: table not found
- Example scenario: time range filter wrong

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
