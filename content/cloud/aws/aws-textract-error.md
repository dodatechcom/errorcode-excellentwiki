---
title: "[Solution] AWS Textract Error — document/analysis/quota failures"
description: "Fix AWS Textract errors. Resolve document analysis, extraction, and quota issues."
error-types: ["api-error"]
severities: ["error"]
weight: 169
---

An AWS Textract error occurs when document analysis fails, extraction encounters unsupported formats, or quota limits are exceeded. Textract extracts text and data from documents but requires correct input format and permissions.

## Common Causes

- Document file size exceeds 10 MB limit
- Document format not supported (only PDF, PNG, JPEG)
- S3 bucket not accessible for async operations
- IAM role lacks textract:* permissions
- Concurrent job limit exceeded

## How to Fix

### Analyze Document

```bash
aws textract analyze-document \
  --document '{"S3Object":{"Bucket":"my-bucket","Name":"document.pdf"}}' \
  --feature-types TABLES FORMS
```

### Start Document Analysis

```bash
aws textract start-document-analysis \
  --document-location '{"S3Object":{"Bucket":"my-bucket","Name":"document.pdf"}}' \
  --feature-types TABLES FORMS
```

### Get Analysis Results

```bash
aws textract get-document-analysis \
  --job-id job-xxx
```

### Detect Document Text

```bash
aws textract detect-document-text \
  --document '{"S3Object":{"Bucket":"my-bucket","Name":"scan.jpg"}}'
```

### Start Expense Analysis

```bash
aws textract start-expense-analysis \
  --document-location '{"S3Object":{"Bucket":"my-bucket","Name":"receipt.pdf"}}'
```

## Examples

```bash
# Example 1: Document too large
# InvalidParameterException: Document size exceeds limit
# Fix: compress document or split into smaller files

# Example 2: Unsupported format
# UnsupportedDocumentException: Document format not supported
# Convert to PDF or image format (PNG/JPEG)
```

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 document errors
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
