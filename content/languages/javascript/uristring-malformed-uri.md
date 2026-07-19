---
title: "[Solution] URIError Malformed URI — encodeURI / decodeURI Fix"
description: "Fix URIError: URI malformed when decoding invalid percent-encoded strings in JavaScript."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# URIError: Malformed URI

```javascript
decodeURIComponent('%E0%A4%A'); // URIError
decodeURI('%zz');               // URIError

// Fix — safe decoding
function safeDecode(str) {
  try {
    return decodeURIComponent(str);
  } catch (e) {
    return str; // return original if invalid
  }
}
```
