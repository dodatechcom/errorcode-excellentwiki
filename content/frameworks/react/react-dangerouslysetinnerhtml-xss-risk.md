---
title: "[Solution] React dangerouslySetInnerHTML XSS Risk"
description: "Security warning with dangerouslySetInnerHTML."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Security warning with dangerouslySetInnerHTML.

## Common Causes

Rendering unsanitized HTML.

## How to Fix

Sanitize content.

## Example

```javascript
import DOMPurify from 'dompurify';
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(h) }} />
```
