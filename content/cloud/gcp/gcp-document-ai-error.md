---
title: "[Solution] GCP Document AI Error — processor human review validation errors"
description: "Fix GCP Document AI errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 138
---

Document AI errors occur when there are issues with processor configuration, document processing, or human review workflows.

## Common Causes
- Processor type doesn't match document format
- Document size exceeds processor limits
- Human review queue overflow
- Document AI API not enabled
- Invalid document encoding or format

## How to Fix

### 1. Enable Document AI API
```bash
gcloud services enable documentai.googleapis.com --project=PROJECT_ID
```

### 2. List processors
```bash
gcloud documentai processors list --location=REGION
```

### 3. Create processor
```bash
gcloud documentai processors create PROCESSOR_NAME \
  --location=REGION \
  --type=OCR_PROCESSOR \
  --display-name="OCR Processor"
```

### 4. Process document
```bash
gcloud documentai processors process PROCESSOR_ID \
  --location=REGION \
  --document=gs://bucket/document.pdf
```

### 5. Describe processor
```bash
gcloud documentai processors describe PROCESSOR_ID --location=REGION
```

## Examples

### Create form parser
```bash
gcloud documentai processors create form-parser \
  --location=us-central1 \
  --type=FORM_PARSER_PROCESSOR \
  --display-name="Invoice Parser"
```

### Process batch of documents
```bash
gcloud documentai processors batch-process PROCESSOR_ID \
  --location=us-central1 \
  --input-documents=gs://bucket/docs/* \
  --output-location=gs://bucket/output/
```

## Related Errors
- [GCP Cloud Storage Error](/cloud/gcp/gcp-storage-error/)
- [GCP Vision Error](/cloud/gcp/gcp-vision-error/)
- [GCP Natural Language Error](/cloud/gcp/gcp-natural-language-error/)