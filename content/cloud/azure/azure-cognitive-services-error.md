---
title: "[Solution] Azure Cognitive Services Error — key, region, and quota failures"
description: "Fix Azure Cognitive Services error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 140
---

Cognitive Services errors involve API key failures, regional deployment issues, or quota exhaustion that prevent AI model inference calls.

## Common Causes
- API key revoked or rotated without updating client applications
- Service deployed in region with insufficient GPU/CPU capacity
- Free tier transaction limit exceeded per month
- Multi-service vs single-service resource mismatch in endpoint calls
- Private endpoint DNS not resolving Cognitive Services domain

## How to Fix
### Check Cognitive Services account status
```bash
az cognitiveservices account show \
  --resource-group myResourceGroup \
  --name myCogService \
  --query "provisioningState"
```

### Regenerate API keys
```bash
az cognitiveservices account keys regenerate \
  --resource-group myResourceGroup \
  --name myCogService \
  --key-kind Key1
```

### List quota usage
```bash
az cognitiveservices account usage list \
  --resource-group myResourceGroup \
  --account-name myCogService
```

### Update network rules
```bash
az cognitiveservices account update \
  --resource-group myResourceGroup \
  --name myCogService \
  --set "properties.networkAcls.defaultAction=Allow"
```

## Examples
### Create Cognitive Services account
```bash
az cognitiveservices account create \
  --resource-group myResourceGroup \
  --name myCogService \
  --kind "CognitiveServices" \
  --sku S1 \
  --location eastus \
  --api-properties '{"StatisticsEnabled":false}'
```

### List available SKUs
```bash
az cognitiveservices account list-skus \
  --resource-group myResourceGroup \
  --name myCogService
```

## Related Errors
- {{< relref "/cloud/azure/azure-openai-error" >}}
- {{< relref "/cloud/azure/azure-computer-vision-error" >}}
- {{< relref "/cloud/azure/azure-speech-error" >}}
