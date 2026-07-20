---
title: "[Solution] GCP Translation API Error — language glossary adaptive errors"
description: "Fix GCP Translation API errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 139
---

Translation API errors occur when there are issues with language support, glossary management, or adaptive translation.

## Common Causes
- Source or target language code invalid
- Glossary file format incorrect
- Adaptive translation model not available
- Text length exceeds API limits
- Cloud Translation API not enabled

## How to Fix

### 1. Enable Translation API
```bash
gcloud services enable translate.googleapis.com --project=PROJECT_ID
```

### 2. List supported languages
```bash
gcloud translate languages list --target-language=en
```

### 3. Create glossary
```bash
gcloud translate glossaries create GLOSSARY_NAME \
  --location=global \
  --glossary-file=gs://bucket/glossary.csv \
  --source-language-code=en \
  --target-language-codes=es
```

### 4. Translate text
```bash
gcloud translate text \
  --source-language-code=en \
  --target-language-code=es \
  --format=text \
  "Hello world"
```

### 5. List glossaries
```bash
gcloud translate glossaries list --location=global
```

## Examples

### Translate with glossary
```bash
gcloud translate text \
  --source-language-code=en \
  --target-language-code=es \
  --glossary=projects/PROJECT/locations/global/glossaries/GLOSSARY \
  --format=text \
  "This is a technical term"
```

### Batch translate files
```bash
gcloud translate text \
  --source-language-code=en \
  --target-language-code=de \
  --input-file=gs://bucket/input.txt \
  --output-file=gs://bucket/output.txt
```

## Related Errors
- [GCP Document AI Error](/cloud/gcp/gcp-document-ai-error/)
- [GCP Natural Language Error](/cloud/gcp/gcp-natural-language-error/)
- [GCP Speech Error](/cloud/gcp/gcp-speech-error/)