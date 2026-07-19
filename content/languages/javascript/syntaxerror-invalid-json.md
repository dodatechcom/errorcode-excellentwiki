---
title: "[Solution] SyntaxError JSON.parse — Unexpected Token Fix"
description: "Fix SyntaxError in JSON.parse when input is not valid JSON. Validate JSON and handle parse errors."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# SyntaxError in JSON.parse

```javascript
// These all fail
JSON.parse(undefined);
JSON.parse('');
JSON.parse('{ name: "test" }');  // unquoted key
JSON.parse("{'name': 'test'}");  // single quotes
JSON.parse("{name: \"test\"}"); // no quotes on key
JSON.parse(null);
```

## Safe Parsing

```javascript
function safeParse(json) {
  try {
    return JSON.parse(json);
  } catch (e) {
    console.error('Invalid JSON:', e.message);
    return null;
  }
}
```
