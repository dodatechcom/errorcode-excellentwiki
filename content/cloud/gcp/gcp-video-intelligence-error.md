---
title: "[Solution] GCP Video Intelligence Error -- annotation shot label errors"
description: "Fix GCP Video Intelligence errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 146
---

Video Intelligence errors occur when there are issues with video annotation, shot detection, or label recognition.

## Common Causes
- Video file exceeds maximum duration limit
- Video format not supported by annotation
- Feature not available for video type
- Invalid video URI or format
- Video Intelligence API not enabled

## How to Fix

### 1. Enable Video Intelligence API
```bash
gcloud services enable videointelligence.googleapis.com --project=PROJECT_ID
```

### 2. Annotate video
```bash
curl -X POST \
  "https://videointelligence.googleapis.com/v1/projects/PROJECT:AnnotateVideo" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"inputUri":"gs://bucket/video.mp4","features":["LABEL_DETECTION"]}'
```

### 3. Check annotation results
```bash
curl -X GET \
  "https://videointelligence.googleapis.com/v1/operations/OPERATION_ID" \
  -H "Authorization: Bearer TOKEN"
```

### 4. List supported features
```bash
curl -s "https://videointelligence.googleapis.com/v1/projects/PROJECT/config" \
  -H "Authorization: Bearer TOKEN"
```

### 5. Annotate specific segments
```bash
curl -X POST \
  "https://videointelligence.googleapis.com/v1/projects/PROJECT:AnnotateVideo" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"inputUri":"gs://bucket/video.mp4","features":["SHOT_CHANGE_DETECTION"],"videoContext":{"segment":{"startTimeOffset":"0s","endTimeOffset":"60s"}}}'
```

## Examples

### Detect labels with confidence
```bash
curl -X POST \
  "https://videointelligence.googleapis.com/v1/projects/PROJECT:AnnotateVideo" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"inputUri":"gs://bucket/video.mp4","features":["LABEL_DETECTION","LABEL_TRACKING"]}'
```

### Extract shots for video editing
```bash
curl -X POST \
  "https://videointelligence.googleapis.com/v1/projects/PROJECT:AnnotateVideo" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"inputUri":"gs://bucket/video.mp4","features":["SHOT_CHANGE_DETECTION"]}'
```

## Related Errors
- [GCP Speech Error](/cloud/gcp/gcp-speech-error/)
- [GCP Vision Error](/cloud/gcp/gcp-vision-error/)
- [GCP Media Translation Error](/cloud/gcp/gcp-media-translation-error/)