---
title: "[Solution] AWS Translate Error — text/language/terminology failures"
description: "Fix AWS Translate errors. Resolve text translation, language detection, and terminology issues."
error-types: ["api-error"]
severities: ["error"]
weight: 166
---

An AWS Translate error occurs when translation jobs fail, language detection errors, or custom terminology does not apply. Translate provides machine translation but requires correct input format and language codes.

## Common Causes

- Input text exceeds 50 KB per request
- Language pair not supported
- Custom terminology file not in CSV format
- IAM role lacks translate:* permissions
- Parallel translation job limit exceeded

## How to Fix

### Translate Text

```bash
aws translate translate-text \
  --text "Hello, how are you?" \
  --source-language-code en \
  --target-language-code es
```

### Detect Language

```bash
aws translate detect-dominant-language \
  --text "Bonjour, comment allez-vous?"
```

### List Terminology

```bash
aws translate list-terminologies
```

### Import Terminology

```bash
aws translate import-terminology \
  --name my-terms \
  --merge-strategy OVERWRITE \
  --terminology-data file://terms.csv \
  --data-format CSV
```

### Start Text Translation Job

```bash
aws translate start-text-translation-job \
  --job-name my-batch-translation \
  --source-language-code en \
  --target-language-codes es fr de \
  --input-data-config S3Uri=s3://my-bucket/input/ \
  --output-data-config S3Uri=s3://my-bucket/output/
```

## Examples

```bash
# Example 1: Unsupported language
# UnsupportedLanguagePairException: Language not supported
# Fix: use supported language code pair

# Example 2: Text too large
# TextSizeLimitExceededException: Text exceeds 50 KB
# Fix: split text into smaller chunks
```

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 data errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS Comprehend Error]({{< relref "/cloud/aws/aws-comprehend-error" >}}) — NLP analysis errors
