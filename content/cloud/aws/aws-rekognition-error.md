---
title: "[Solution] AWS Rekognition Error — image/video/collection failures"
description: "Fix AWS Rekognition errors. Resolve image analysis, video processing, and collection issues."
error-types: ["api-error"]
severities: ["error"]
weight: 165
---

An AWS Rekognition error occurs when image analysis fails, video jobs timeout, or face collections encounter errors. Rekognition provides computer vision but requires correct S3 access and image formats.

## Common Causes

- Image file size exceeds 15 MB limit
- S3 bucket not accessible for video analysis
- Face collection does not exist
- IAM role lacks Rekognition permissions
- Video job exceeds maximum duration

## How to Fix

### Detect Labels

```bash
aws rekognition detect-labels \
  --image '{"S3Object":{"Bucket":"my-bucket","Name":"image.jpg"}}' \
  --max-labels 10
```

### Create Collection

```bash
aws rekognition create-collection \
  --collection-id my-faces
```

### Index Faces

```bash
aws rekognition index-faces \
  --collection-id my-faces \
  --image '{"S3Object":{"Bucket":"my-bucket","Name":"face.jpg"}}' \
  --external-image-id person-001
```

### Search Faces

```bash
aws rekognition search-faces \
  --collection-id my-faces \
  --face-id face-xxx
```

### Start Label Detection Job

```bash
aws rekognition start-label-detection \
  --video '{"S3Object":{"Bucket":"my-bucket","Name":"video.mp4"}}' \
  --min-confidence 80
```

## Examples

```bash
# Example 1: Image too large
# InvalidImageFormatException: Image size exceeds limit
# Fix: resize image to under 15 MB

# Example 2: Collection not found
# ResourceNotFoundException: Collection not found
# Fix: create collection with create-collection
```

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 image errors
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
