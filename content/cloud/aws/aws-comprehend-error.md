---
title: "[Solution] AWS Comprehend Error — classification/entity/sentiment failures"
description: "Fix AWS Comprehend errors. Resolve classification, entity, and sentiment analysis issues."
error-types: ["api-error"]
severities: ["error"]
weight: 164
---

An AWS Comprehend error occurs when text analysis jobs fail, custom classifiers encounter errors, or PII detection returns incorrect results. Comprehend provides NLP but requires correct input format and IAM permissions.

## Common Causes

- Input text exceeds maximum length (5120 bytes per request)
- Custom classifier training data insufficient
- IAM role lacks comprehend:* permissions
- S3 input/output path not accessible
- Language not supported for the API call

## How to Fix

### Detect Sentiment

```bash
aws comprehend detect-sentiment \
  --text "I love this product, it works great!" \
  --language-code en
```

### Start Classification Job

```bash
aws comprehend create-classifier \
  --classifier-name my-classifier \
  --language-code en \
  --input-data-config S3Uri=s3://my-bucket/training-data/ \
  --output-data-config S3Uri=s3://my-bucket/output/
```

### Detect Entities

```bash
aws comprehend detect-entities \
  --text "Amazon is based in Seattle, Washington." \
  --language-code en
```

### Detect PII Entities

```bash
aws comprehend detect-pii-entities \
  --text "My SSN is 123-45-6789." \
  --language-code en
```

### Describe Classification Job

```bash
aws comprehend describe-classification-job \
  --job-id job-xxx
```

## Examples

```bash
# Example 1: Text too long
# TextSizeLimitExceededException: Text exceeds limit
# Fix: split text into chunks of 5120 bytes or less

# Example 2: Unsupported language
# UnsupportedLanguageException: Language not supported
# Fix: use supported language code (en, es, fr, etc.)
```

## Related Errors

- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 data errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
