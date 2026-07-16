---
title: "[Solution] JavaScript Deprecated Features — MDN Migration Guide"
description: "JavaScript deprecated feature migration guides. Replace escape, substr, and execCommand with modern JS APIs. Copy-paste fixes."
deprecated: ["javascript"]
---

Browser vendors and the TC39 standards committee regularly deprecate APIs that are superseded by better, more secure, or more consistent alternatives. Each entry below covers the deprecated function, why it was removed, and the modern replacement you can copy immediately.

## Deprecated Features

| Deprecated | Description | Replacement |
|------------|-------------|-------------|
| [escape() / unescape()](/deprecated/javascript/escape-unescape/) | Deprecated encoding functions — unsafe and inconsistent behavior | Use `encodeURIComponent()` / `decodeURIComponent()` for URI components |
| [document.execCommand()](/deprecated/javascript/exec-command/) | Deprecated for modifying document content — no longer maintained | Use the modern Clipboard API (`navigator.clipboard.writeText()`) |
| [String.substr()](/deprecated/javascript/substr-to-slice/) | Deprecated string extraction — unclear semantics with negative indices | Use `slice()` or `substring()` for string extraction |

## Quick Check

```javascript
// Run ESLint with the deprecated API rules enabled
npx eslint --rule '{"no-restricted-globals": "error"}' src/
```
