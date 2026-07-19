---
title: "[Solution] NotFoundError — Element Not Found in DOM Fix"
description: "Fix NotFoundError when trying to remove or replace a DOM node that is not attached to the document."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# NotFoundError — DOM Node Not Found

```javascript
const el = document.createElement('div');

// Trying to remove a node not in the DOM
el.remove(); // NotFoundError

// Fix — check if connected
if (el.parentNode) {
  el.remove();
}

// Or use optional chaining
el.parentNode?.removeChild(el);
```
