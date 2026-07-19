---
title: "[Solution] NotFoundError — Media Device Not Found Fix"
description: "Fix NotFoundError when camera or microphone is not available. Check device enumeration and permissions."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# NotFoundError — Media Device Not Found

```javascript
try {
  const stream = await navigator.mediaDevices.getUserMedia({
    video: true,
    audio: true
  });
} catch (err) {
  if (err.name === 'NotFoundError') {
    console.error('No camera/microphone found');
  } else if (err.name === 'NotAllowedError') {
    console.error('Permission denied');
  }
}
```

## Enumerate Devices

```javascript
const devices = await navigator.mediaDevices.enumerateDevices();
cameras = devices.filter(d => d.kind === 'videoinput');
```
