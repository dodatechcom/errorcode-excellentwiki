---
title: "[Solution] URIError encodeURI/decodeURI — Special Character Encoding Fix"
description: "Fix URIError when encoding/decoding URIs with special characters. Use encodeURI vs encodeURIComponent correctly."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# URI Encoding/Decoding Errors

```javascript
// encodeURI — encodes everything except: A-Za-z0-9 ; , / ? : @ & = + $ - _ . ! ~ * ' ( )
encodeURI('https://example.com/path?query=hello world');
// → 'https://example.com/path?query=hello%20world'

// encodeURIComponent — encodes everything except: A-Za-z0-9 - _ . ! ~ * ' ( )
encodeURIComponent('hello world');
// → 'hello%20world'

// Wrong usage
decodeURIComponent('hello world'); // works (no-op)
decodeURIComponent('%zz');         // URIError
```
