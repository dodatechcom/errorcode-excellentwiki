---
title: "[Solution] Azure Speech Error — speech-to-text, text-to-speech, and transcription failures"
description: "Fix Azure Speech error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 142
---

Speech Service errors involve STT/TTS API failures, transcription job timeouts, or audio format compatibility issues that block speech processing.

## Common Causes
- Audio file format not supported (requires PCM/WAV for STT)
- Speech SDK subscription key region mismatch with endpoint
- Real-time transcription connection timeout exceeding limit
- Custom speech model not deployed to target region
- Audio stream bitrate exceeding maximum allowed rate

## How to Fix
### Check Speech resource status
```bash
az cognitiveservices account show \
  --resource-group myResourceGroup \
  --name mySpeechService \
  --query "provisioningState"
```

### List speech resources
```bash
az cognitiveservices account list \
  --resource-group myResourceGroup \
  --query "[?kind=='SpeechServices'].{name:name, location:location}"
```

### Create Speech resource
```bash
az cognitiveservices account create \
  --resource-group myResourceGroup \
  --name mySpeechService \
  --kind "SpeechServices" \
  --sku S1 \
  --location eastus
```

### Regenerate speech key
```bash
az cognitiveservices account keys regenerate \
  --resource-group myResourceGroup \
  --name mySpeechService \
  --key-kind Key1
```

## Examples
### Test speech endpoint
```bash
curl -X POST "https://eastus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1" \
  -H "Ocp-Apim-Subscription-Key: myApiKey" \
  -H "Content-Type: audio/wav; codecs=audio/pcm; samplerate=16000" \
  --data-binary @audio.wav
```

### List custom speech models
```bash
az cognitiveservices account show \
  --resource-group myResourceGroup \
  --name mySpeechService \
  --query "properties.customSubDomainName"
```

## Related Errors
- {{< relref "/cloud/azure/azure-cognitive-services-error" >}}
- {{< relref "/cloud/azure/azure-language-service-error" >}}
- {{< relref "/cloud/azure/azure-video-indexer-error" >}}
