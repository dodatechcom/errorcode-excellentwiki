---
title: "[Solution] Canvas Tainted SecurityError — Cross-Origin Image Fix"
description: "Fix SecurityError: Tainted canvases may not be exported when drawing cross-origin images to canvas."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Canvas Tainted SecurityError

Drawing a cross-origin image to canvas 'taints' it, preventing data export.

## Fix

Set CORS on the image element:

```javascript
const img = new Image();
img.crossOrigin = 'anonymous';
img.src = 'https://example.com/image.jpg';

img.onload = () => {
  ctx.drawImage(img, 0, 0);
  // Now toDataURL() works
  const dataUrl = canvas.toDataURL();
};
```

The server must send `Access-Control-Allow-Origin` header.
