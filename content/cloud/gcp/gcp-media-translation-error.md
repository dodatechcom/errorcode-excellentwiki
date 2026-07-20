---
title: "[Solution] GCP Media Translation Error — audio stream language errors"
description: "Fix GCP Media Translation errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 145
---

Media Translation errors occur when there are issues with audio streaming, language detection, or translation requests.

## Common Causes
- Audio encoding format not supported
- Streaming session timeout exceeded
- Target language not available for audio
- Audio sample rate mismatch
- Media Translation API not enabled

## How to Fix

### 1. Enable Media Translation API
```bash
gcloud services enable medi translation.googleapis.com --project=PROJECT_ID
```

### 2. Check supported languages
```bash
curl -s "https://mediatranslation.googleapis.com/v1/projects/PROJECT/config" \
  -H "Authorization: Bearer $(gcloud auth print-access-token)"
```

### 3. Start streaming translation
```bash
curl -X POST \
  "https://mediatranslation.googleapis.com/v1/projects/PROJECT/speech:StreamingTranslateSpeech" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d @streaming-request.json
```

### 4. List translation configurations
```bash
gcloud services list --enabled --filter="name:medi translation"
```

### 5. Check API quota
```bash
gcloud services quota describe medi translation.googleapis.com \
  --consumer=projects/PROJECT_ID
```

## Examples

### Configure streaming parameters
```bash
cat > streaming-config.json <<EOF
{
  "audioConfig": {
    "audioEncoding": "LINEAR16",
    "sampleRateHertz": 16000
  },
  "targetLanguageCode": "es"
}
EOF
```

### Test non-streaming translation
```bash
curl -X POST \
  "https://mediatranslation.googleapis.com/v1/projects/PROJECT:TranslateSpeech" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"config":{"audioConfig":{"audioEncoding":"LINEAR16","sampleRateHertz":16000},"targetLanguageCode":"es"},"audio":{"uri":"gs://bucket/audio.wav"}}'
```

## Related Errors
- [GCP Translation Error](/cloud/gcp/gcp-translation-error/)
- [GCP Speech Error](/cloud/gcp/gcp-speech-error/)
- [GCP Video Intelligence Error](/cloud/gcp/gcp-video-intelligence-error/)