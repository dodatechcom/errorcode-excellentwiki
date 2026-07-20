---
title: "[Solution] Azure Form Recognizer Error — model, analysis, and layout extraction failures"
description: "Fix Azure Form Recognizer error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 144
---

Form Recognizer errors involve document analysis failures, custom model training issues, or OCR extraction returning incomplete results.

## Common Causes
- Document file size exceeding 50MB limit for analysis
- Supported file format not PDF, JPEG, PNG, TIFF, or BMP
- Custom model training data insufficient for accurate extraction
- Layout API failing on low-resolution scanned documents
- Prebuilt model not compatible with document language

## How to Fix
### Check Form Recognizer resource
```bash
az cognitiveservices account show \
  --resource-group myResourceGroup \
  --name myFormRecognizer \
  --query "provisioningState"
```

### List custom models
```bash
az rest --method get \
  --uri "https://eastus.api.cognitive.microsoft.com/formrecognizer/v2.1/custom/models" \
  --headers "Ocp-Apim-Subscription-Key: myApiKey"
```

### Create Form Recognizer resource
```bash
az cognitiveservices account create \
  --resource-group myResourceGroup \
  --name myFormRecognizer \
  --kind "FormRecognizer" \
  --sku S0 \
  --location eastus
```

### Train custom model
```bash
curl -X POST "https://eastus.api.cognitive.microsoft.com/formrecognizer/v2.1/custom/models" \
  -H "Ocp-Apim-Subscription-Key: myApiKey" \
  -H "Content-Type: application/json" \
  -d '{"source":"https://myaccount.blob.core.windows.net/training-data"}'
```

## Examples
### Analyze receipt with prebuilt model
```bash
curl -X POST "https://eastus.api.cognitive.microsoft.com/formrecognizer/v2.1/prebuilt/receipt/analyze" \
  -H "Ocp-Apim-Subscription-Key: myApiKey" \
  -H "Content-Type: application/json" \
  -d '{"source":"https://example.com/receipt.jpg"}'
```

### Get analysis result
```bash
curl -X GET "https://eastus.api.cognitive.microsoft.com/formrecognizer/v2.1/custom/models/{modelId}/analyze" \
  -H "Ocp-Apim-Subscription-Key: myApiKey"
```

## Related Errors
- {{< relref "/cloud/azure/azure-computer-vision-error" >}}
- {{< relref "/cloud/azure/azure-cognitive-services-error" >}}
- {{< relref "/cloud/azure/azure-storage-error" >}}
