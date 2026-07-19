---
title: "[Solution] WebRTC Not Supported — RTCPeerConnection Error Fix"
description: "Fix WebRTC errors when RTCPeerConnection is not available. Handle browser compatibility and permissions."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# WebRTC Not Supported

```javascript
if (!window.RTCPeerConnection) {
  console.error('WebRTC not supported in this browser');
  // Fallback to WebSockets or HTTP
}
```

## Common Errors

- `RTCPeerConnection is not defined` — browser doesn't support
- `Failed to execute 'createObjectURL'` — deprecated API
- `Permission denied` — camera/mic access denied
