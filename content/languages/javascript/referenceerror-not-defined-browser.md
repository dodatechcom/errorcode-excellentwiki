---
title: "[Solution] ReferenceError Not Defined — Browser Global Variable Fix"
description: "Fix ReferenceError in browser when accessing undefined global variables. Check for missing script tags and variable declarations."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ReferenceError in Browser

```javascript
// Variable not in global scope
console.log(myVar); // ReferenceError

// Missing script tag (library not loaded)
console.log(React); // ReferenceError if React not loaded

// Fix: check loading order
<script src="react.js"></script>
<script src="app.js"></script>
```
