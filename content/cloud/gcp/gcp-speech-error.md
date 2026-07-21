---
title: "[Solution] GCP Speech Error -- Speech-to-Text Text-to-Speech recognition synthesis errors"
description: "Fix GCP Speech API errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 140
---

Speech API errors occur when there are issues with audio recognition, text synthesis, or model configuration.

## Common Causes
- Audio format not supported by recognizer
- Sample rate mismatch between audio and API config
- Language model not available for locale
- Audio file exceeds maximum length
- Cloud Speech-to-Text API not enabled

## How to Fix

### 1. Enable Speech APIs
```bash
gcloud services enable speech.googleapis.com --project=PROJECT_ID
```

### 2. List supported languages
```bash
gcloud speech speech-to-text list \
  --filter="languageCodes:en-US"
```

### 3. Recognize audio file
```bash
gcloud speech speech-to-text recognize \
  --language-code=en-US \
  --audio-uri=gs://bucket/audio.wav \
  --model=latest_long
```

### 4. Synthesize text
```bash
gcloud text-to-speech synthesize \
  --input-text="Hello, welcome to GCP" \
  --output-file=output.mp3 \
  --voice=language-code=en-US,name=en-US-Wavenet-D
```

### 5. Long-running recognition
```bash
gcloud speech speech-to-text recognize \
  --language-code=en-US \
  --audio-uri=gs://bucket/long-audio.wav \
  --model=latest_long \
  --async
```

## Examples

### Transcribe with custom model
```bash
gcloud speech speech-to-text recognize \
  --language-code=en-US \
  --audio-uri=gs://bucket/medical-audio.wav \
  --model=medical_dictation \
  --enable-word-time-offsets
```

### Generate speech
```bash
gcloud text-to-speech synthesize \
  --input-text="Error detected in service" \
  --output-file=notification.mp3 \
  --voice=language-code=en-US,name=en-US-Standard-C \
  --audio-encoding=MP3
```

## Related Errors
- [GCP Translation Error](/cloud/gcp/gcp-translation-error/)
- [GCP Natural Language Error](/cloud/gcp/gcp-natural-language-error/)
- [GCP Video Intelligence Error](/cloud/gcp/gcp-video-intelligence-error/)