---
title: "[Solution] Deprecated Function Migration: document.write to DOM manipulation"
description: "Migrate from deprecated document.write to DOM manipulation."
deprecated_function: "document.write(html)"
replacement_function: "element.innerHTML / DOM APIs"
languages: ["javascript"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: document.write to DOM manipulation

The `document.write(html)` has been deprecated in favor of `element.innerHTML / DOM APIs`.

## Migration Guide

document.write can cause issues.

## Before (Deprecated)

```javascript
document.write('<p>Hello</p>');
```

## After (Modern)

```javascript
const p = document.createElement('p');
p.textContent = 'Hello';
document.body.appendChild(p);
```

## Key Differences

- DOM APIs are safer
