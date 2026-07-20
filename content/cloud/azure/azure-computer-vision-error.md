---
title: "[Solution] Azure Computer Vision Error — image, analysis, and OCR failures"
description: "Fix Azure Computer Vision error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 141
---

Computer Vision errors appear as image analysis failures, OCR processing timeouts, or quota exhaustion during batch image operations.

## Common Causes
- Image file size exceeding 20MB limit for analysis API
- OCR request rate exceeding per-second transaction limit
- Image URL inaccessible from Cognitive Services regional endpoint
- Analyze Image feature not enabled on resource
- Custom Vision export not compatible with Computer Vision API

## How to Fix
### Check Computer Vision resource
```bash
az cognitiveservices account show \
  --resource-group myResourceGroup \
  --name myVisionService \
  --query "kind"
```

### List available features
```bash
az cognitiveservices account show \
  --resource-group myResourceGroup \
  --name myVisionService \
  --query "properties.capabilities"
```

### Test endpoint with curl
```bash
curl -X POST "https://eastus.api.cognitive.microsoft.com/vision/v3.2/analyze" \
  -H "Ocp-Apim-Subscription-Key: myApiKey" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com/image.jpg"}'
```

### Create Computer Vision resource
```bash
az cognitiveservices account create \
  --resource-group myResourceGroup \
  --name myVisionService \
  --kind "ComputerVision" \
  --sku S1 \
  --location eastus
```

## Examples
### Analyze image from URL
```bash
curl -X POST "https://eastus.api.cognitive.microsoft.com/vision/v3.2/analyze?visualFeatures=Categories,Tags" \
  -H "Ocp-Apim-Subscription-Key: myApiKey" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com/photo.jpg"}'
```

### List cognitive services accounts
```bash
az cognitiveservices account list \
  --resource-group myResourceGroup \
  --query "[].{name:name, kind:kind, location:location}"
```

## Related Errors
- {{< relref "/cloud/azure/azure-cognitive-services-error" >}}
- {{< relref "/cloud/azure/azure-form-recognizer-error" >}}
- {{< relref "/cloud/azure/azure-language-service-error" >}}
