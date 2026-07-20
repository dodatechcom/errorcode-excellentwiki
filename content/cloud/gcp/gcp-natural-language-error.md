---
title: "[Solution] GCP Natural Language Error — entity sentiment classification errors"
description: "Fix GCP Natural Language API errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 142
---

Natural Language API errors occur when there are issues with entity extraction, sentiment analysis, or content classification.

## Common Causes
- Text content exceeds maximum size limit
- Language not supported for analysis type
- Content type mismatch with requested feature
- Insufficient quota for batch requests
- Natural Language API not enabled

## How to Fix

### 1. Enable Natural Language API
```bash
gcloud services enable language.googleapis.com --project=PROJECT_ID
```

### 2. Analyze sentiment
```bash
gcloud language analyze-sentiment \
  --content="This is great service" \
  --format=json
```

### 3. Extract entities
```bash
gcloud language analyze-entities \
  --content="Google Cloud Platform is great" \
  --format=json
```

### 4. Classify content
```bash
gcloud language analyze-classify \
  --content="Breaking news about technology" \
  --format=json
```

### 5. Analyze syntax
```bash
gcloud language analyze-syntax \
  --content="The quick brown fox jumps" \
  --format=json
```

## Examples

### Sentiment with document metadata
```bash
gcloud language analyze-sentiment \
  --type=html \
  --language=en \
  --content="<html><body>Product review text</body></html>" \
  --format=json
```

### Entity analysis with moderate bias
```bash
gcloud language analyze-entities \
  --content="Apple CEO Tim Cook announced new products" \
  --encoding-type=utf16 \
  --format=json
```

## Related Errors
- [GCP Translation Error](/cloud/gcp/gcp-translation-error/)
- [GCP Speech Error](/cloud/gcp/gcp-speech-error/)
- [GCP Vision Error](/cloud/gcp/gcp-vision-error/)