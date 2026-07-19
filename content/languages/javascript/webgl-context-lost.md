---
title: "[Solution] WebGL Context Lost — GPU Reset Error Fix"
description: "Fix WebGL CONTEXT_LOST_event when GPU resets or context is lost. Implement context restoration handler."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# WebGL Context Lost

The browser or GPU driver lost the WebGL context.

```javascript
canvas.addEventListener('webglcontextlost', (e) => {
  e.preventDefault(); // allows context restoration
  console.log('Context lost');
});

canvas.addEventListener('webglcontextrestored', () => {
  console.log('Context restored — reinitialize resources');
  initWebGL();
});
```

## Prevention

- Don't hold too many GPU resources
- Handle context restoration gracefully
- Release resources when not in use
