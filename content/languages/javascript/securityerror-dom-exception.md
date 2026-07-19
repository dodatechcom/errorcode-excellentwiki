---
title: "[Solution] SecurityError — Blocked a Frame with Origin Fix"
description: "Fix SecurityError when cross-origin frame access is blocked by Same-Origin Policy."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# SecurityError — Same-Origin Policy

```javascript
// Cross-origin frame access blocked
try {
  const frame = document.getElementById('myFrame');
  const data = frame.contentDocument; // SecurityError
} catch (err) {
  console.error('Cross-origin access blocked');
}
```

## Fix

Use `postMessage` for cross-origin communication:

```javascript
// Parent
window.frames[0].postMessage('hello', 'https://target-origin.com');

// Child iframe
window.addEventListener('message', (e) => {
  if (e.origin === 'https://parent-origin.com') {
    console.log(e.data);
  }
});
```
