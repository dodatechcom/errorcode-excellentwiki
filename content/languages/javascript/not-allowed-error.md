---
title: "[Solution] NotAllowedError — Permission Denied by User Agent Fix"
description: "Fix NotAllowedError when browser denies an action requiring user gesture or permission."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# NotAllowedError

Occurs when an action requires a user gesture but none is present.

## Common Cases

```javascript
// Auto-play blocked
const video = document.querySelector('video');
video.play(); // NotAllowedError: play() requires user gesture

// Fix — play on user interaction
document.addEventListener('click', () => {
  video.play(); // works on user gesture
}, { once: true });
```
