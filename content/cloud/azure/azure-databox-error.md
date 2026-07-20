---
title: "[Solution] Azure Data Box Error — order, copy, unlock, and shipping failures"
description: "Fix Azure Data Box error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 166
---

Data Box errors involve order provisioning failures, copy job issues, or device unlock problems that delay offline data transfer operations.

## Common Causes
- Data Box order exceeding maximum storage capacity for device type
- Shipping address not matching billing address on subscription
- Device unlock password not matching or expired after delivery
- Copy job failing due to file system incompatibilities
- Network connectivity lost during online transfer operations

## How to Fix
### Check order status
```bash
az databox job show \
  --resource-group myResourceGroup \
  --name myDataBoxOrder \
  --query "properties.orderStatus"
```

### List available orders
```bash
az databox job list \
  --resource-group myResourceGroup \
  --query "[].{name:name,status:properties.orderStatus,location:location}"
```

### Create new order
```bash
az databox job create \
  --resource-group myResourceGroup \
  --name myDataBoxOrder \
  --location eastus \
  --type DataBox \
  --sku Standard \
  --transfer-type ImportToAzure \
  --contact-name "Admin" \
  --email "admin@contoso.com" \
  --phone "555-1234" \
  --address-line1 "123 Main St" \
  --city "Redmond" \
  --state "WA" \
  --postal-code "98052" \
  --country "US"
```

### Get device credentials
```bash
az databox job show \
  --resource-group myResourceGroup \
  --name myDataBoxOrder \
  --query "properties.devicePassword"
```

## Examples
### Check copy job status
```bash
az databox job show \
  --resource-group myResourceGroup \
  --name myDataBoxOrder \
  --query "properties.copyLogDetails"
```

### List shipments
```bash
az databox job show \
  --resource-group myResourceGroup \
  --name myDataBoxOrder \
  --query "properties.shipmentTrackingUrl"
```

## Related Errors
- {{< relref "/cloud/azure/azure-storage-error" >}}
- {{< relref "/cloud/azure/azure-migrate-error" >}}
- {{< relref "/cloud/azure/azure-backup-error" >}}
