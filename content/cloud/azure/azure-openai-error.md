---
title: "[Solution] Azure OpenAI Error — deployment, quota, and content filter failures"
description: "Fix Azure OpenAI error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 138
---

OpenAI errors occur when model deployments hit quota limits, content filters reject requests, or API key authentication fails for inference calls.

## Common Causes
- TPM (tokens per minute) quota exhausted for deployment model
- Content filter blocking prompts or completions containing flagged content
- API version mismatch between client SDK and Azure OpenAI endpoint
- Deployment name incorrect or model not yet provisioned
- Regional capacity limits preventing new deployment creation

## How to Fix
### List OpenAI deployments
```bash
az cognitiveservices account deployment list \
  --resource-group myResourceGroup \
  --account-name myOpenAIResource \
  --query "[].{name:name, model:{model:model, format:format}, scaleType:scaleType}"
```

### Create new deployment
```bash
az cognitiveservices account deployment create \
  --resource-group myResourceGroup \
  --account-name myOpenAIResource \
  --deployment-name myGPT4Deployment \
  --model-name gpt-4 \
  --model-version "2023-12-01" \
  --model-format OpenAI \
  --sku-name "Standard" \
  --sku-capacity 10
```

### Check quota usage
```bash
az cognitiveservices account usage list \
  --resource-group myResourceGroup \
  --account-name myOpenAIResource \
  --query "[].{name:name.value, currentValue:currentValue, limit:limit}"
```

### Update content filter settings
```bash
az cognitiveservices account update \
  --resource-group myResourceGroup \
  --name myOpenAIResource \
  --set "properties.networkAcls.defaultAction=Allow"
```

## Examples
### List available models
```bash
az cognitiveservices account list-models \
  --resource-group myResourceGroup \
  --account-name myOpenAIResource
```

### Test endpoint connectivity
```bash
az rest --method post \
  --uri "https://myopenai.openai.azure.com/openai/deployments/myGPT4Deployment/chat/completions?api-version=2024-02-01" \
  --headers "api-key=myApiKey" \
  --body '{"messages":[{"role":"user","content":"Hello"}]}'
```

## Related Errors
- {{< relref "/cloud/azure/azure-cognitive-services-error" >}}
- {{< relref "/cloud/azure/azure-key-vault-error" >}}
- {{< relref "/cloud/azure/azure-monitor-error" >}}
