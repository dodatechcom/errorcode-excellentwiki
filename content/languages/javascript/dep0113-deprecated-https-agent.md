---
title: "[Solution] DEP0113 — Deprecation Warning: https.Agent options"
description: "Fix DEP0113 deprecation for deprecated HTTPS agent options. Update to current TLS options."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# DEP0113 — Deprecated https.Agent Options

## Fix

```javascript
// Deprecated options
new https.Agent({ secureProtocol: 'SSLv3_method' });

// Modern
new https.Agent({
  minVersion: 'TLSv1.2',
  maxVersion: 'TLSv1.3'
});
```
