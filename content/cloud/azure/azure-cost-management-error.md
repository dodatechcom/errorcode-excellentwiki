---
title: "[Solution] Azure Cost Management Error — scope, budget, and export failures"
description: "Fix Azure Cost Management error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 155
---

Cost Management errors appear as export generation failures, budget alert misconfigurations, or scope access issues that prevent cost visibility.

## Common Causes
- Export scope not including all child subscriptions
- Budget threshold exceeding maximum allowed currency value
- Storage account access denied for scheduled exports
- Cost Management not enabled for EA billing scope
- Currency or date format not matching regional requirements

## How to Fix
### List cost management exports
```bash
az costmanagement export list \
  --scope /subscriptions/xxx \
  --query "[].{name:name, scheduleStatus:scheduleStatus}"
```

### Create budget
```bash
az consumption budget create \
  --amount 5000 \
  --category Cost \
  --resource-group-filter myRG \
  --start-date 2023-01-01T00:00:00Z \
  --end-date 2023-12-31T23:59:59Z \
  --name myBudget
```

### Create cost export
```bash
az costmanagement export create \
  --scope /subscriptions/xxx \
  --name myExport \
  --storage-account-id /subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Storage/storageAccounts/myStorage \
  --recurrence Daily \
  --recurrence-period from=2023-01-01 to=2023-12-31
```

### Query cost data
```bash
az costmanagement query \
  --scope /subscriptions/xxx \
  --type Usage \
  --timeframe MonthToDate \
  --query "Properties.Rows"
```

## Examples
### List budget alerts
```bash
az consumption budget list \
  --query "[].{name:name,currentSpend:{amount:currentSpend.amount,currency:currentSpend.currency}}"
```

### Check cost anomalies
```bash
az costmanagement query \
  --scope /subscriptions/xxx \
  --type Usage \
  --timeframe Last7Days
```

## Related Errors
- {{< relref "/cloud/azure/azure-subscription-error" >}}
- {{< relref "/cloud/azure/azure-monitor-error" >}}
- {{< relref "/cloud/azure/azure-advisor-error" >}}
