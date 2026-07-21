---
title: "[Solution] Azure Media Services Error"
description: "Fix Azure Media Services encoding, streaming, and content protection failures."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Media Services errors occur during video encoding, live streaming, or content protection. This affects media delivery workflows and DRM-protected content.

## Common Causes

- Encoding preset is not compatible with the input video format
- Streaming endpoint is not started and cannot serve content
- Content key policy references a deleted Key Vault key
- Live event has exceeded the maximum input bitrate

## How to Fix

### Check encoding job status

```bash
az rest --method GET \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Media/mediaservices/myAccount/transforms/myTransform/jobs?api-version=2022-08-01"
```

### Start streaming endpoint

```bash
az rest --method POST \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Media/mediaservices/myAccount/streamingEndpoints/myEndpoint/start?api-version=2022-08-01"
```

### List content key policies

```bash
az rest --method GET \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Media/mediaservices/myAccount/contentKeyPolicies?api-version=2022-08-01"
```

### Create encoding transform

```bash
az rest --method PUT \
  --uri "https://management.azure.com/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Media/mediaservices/myAccount/transforms/myTransform?api-version=2022-08-01" \
  --body '{"properties":{"presets":[{"@odata.type":"#Media.Encoding.StreamingPreset.H264AdaptiveBitrateMP4Set720p"}]}}'
```

## Examples

- Encoding job fails with `InvalidInputCodec` because the input uses AV1 and the preset only supports H.264
- Streaming endpoint returns 404 because it was stopped after a billing cost optimization
- DRM playback fails because the content key policy references a Key Vault key that was rotated

## Related Errors

- [Azure Media Services Error]({{< relref "/cloud/azure/azure-media-services-error" >}}) -- General Media Services errors.
- [Azure Key Vault Error]({{< relref "/cloud/azure/azure-key-vault-error" >}}) -- Key Vault issues.
