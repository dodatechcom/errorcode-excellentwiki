---
title: "[Solution] Azure Language Service Error — sentiment, entity, and PII extraction failures"
description: "Fix Azure Language Service error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 143
---

Language Service errors appear as sentiment analysis failures, NER extraction returning empty results, or PII detection timeouts on large text batches.

## Common Causes
- Text input exceeding 5120 character limit for single request
- Language not supported by the requested analysis feature
- API key region mismatch between resource and endpoint
- Custom analyzer not trained or deployed to target resource
- Rate limiting during batch text analytics operations

## How to Fix
### Check Language Service resource
```bash
az cognitiveservices account show \
  --resource-group myResourceGroup \
  --name myLanguageService \
  --query "provisioningState"
```

### List supported languages
```bash
az rest --method get \
  --uri "https://eastus.api.cognitive.microsoft.com/text/analytics/v3.1/languages" \
  --headers "Ocp-Apim-Subscription-Key=myApiKey"
```

### Create Language Service resource
```bash
az cognitiveservices account create \
  --resource-group myResourceGroup \
  --name myLanguageService \
  --kind "TextAnalytics" \
  --sku S \
  --location eastus
```

### Update network rules
```bash
az cognitiveservices account update \
  --resource-group myResourceGroup \
  --name myLanguageService \
  --set "properties.networkAcls.defaultAction=Allow"
```

## Examples
### Analyze sentiment
```bash
curl -X POST "https://eastus.api.cognitive.microsoft.com/text/analytics/v3.1/sentiment" \
  -H "Ocp-Apim-Subscription-Key: myApiKey" \
  -H "Content-Type: application/json" \
  -d '{"documents":[{"id":"1","text":"I love this product!"}]}'
```

### Detect PII
```bash
curl -X POST "https://eastus.api.cognitive.microsoft.com/text/analytics/v3.1/entities/recognition/pii" \
  -H "Ocp-Apim-Subscription-Key: myApiKey" \
  -H "Content-Type: application/json" \
  -d '{"documents":[{"id":"1","text":"My SSN is 123-45-6789"}]}'
```

## Related Errors
- {{< relref "/cloud/azure/azure-cognitive-services-error" >}}
- {{< relref "/cloud/azure/azure-computer-vision-error" >}}
- {{< relref "/cloud/azure/azure-openai-error" >}}
