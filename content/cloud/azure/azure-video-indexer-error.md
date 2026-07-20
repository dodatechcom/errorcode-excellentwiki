---
title: "[Solution] Azure Video Indexer Error — upload, index, and insight extraction failures"
description: "Fix Azure Video Indexer error. Actionable solutions with Azure CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 145
---

Video Indexer errors appear as video upload failures, indexing job timeouts, or insight extraction returning incomplete metadata.

## Common Causes
- Video file size exceeding account storage quota
- Indexing API token expired requiring new access token
- Video format not supported by Video Indexer encoding pipeline
- Connected Azure Media Services resource in different region
- Insight processing exceeding maximum allowed video duration

## How to Fix
### Check account status
```bash
az account show --query "id"
```

### Get Video Indexer access token
```bash
az account get-access-token --query "accessToken" -o tsv
```

### Upload video for indexing
```bash
curl -X PUT "https://api.videoindexer.ai/accounts/{accountId}/videos/{videoId}/index" \
  -H "Authorization: Bearer myAccessToken" \
  -H "Content-Type: multipart/form-data" \
  -F "video=@myvideo.mp4"
```

### List indexed videos
```bash
curl -X GET "https://api.videoindexer.ai/accounts/{accountId}/videos" \
  -H "Authorization: Bearer myAccessToken"
```

## Examples
### Get video insights
```bash
curl -X GET "https://api.videoindexer.ai/accounts/{accountId}/videos/{videoId}/index?language=English" \
  -H "Authorization: Bearer myAccessToken"
```

### Delete video
```bash
curl -X DELETE "https://api.videoindexer.ai/accounts/{accountId}/videos/{videoId}" \
  -H "Authorization: Bearer myAccessToken"
```

## Related Errors
- {{< relref "/cloud/azure/azure-media-services-error" >}}
- {{< relref "/cloud/azure/azure-storage-error" >}}
- {{< relref "/cloud/azure/azure-speech-error" >}}
