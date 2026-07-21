---
title: "[Solution] Deprecated Function Migration: Object#taint to sanitization"
description: "Migrate from deprecated Object#taint to input sanitization."
deprecated_function: "obj.taint"
replacement_function: "sanitize(obj)"
languages: ["ruby"]
deprecated_since: "Ruby 2.7+"
---

# [Solution] Deprecated Function Migration: Object#taint to sanitization

The `obj.taint` has been deprecated in favor of `sanitize(obj)`.

## Migration Guide

Taint checking was removed.

## Before (Deprecated)

```ruby
str.taint
```

## After (Modern)

```ruby
sanitized = CGI.escapeHTML(str)
```

## Key Differences

- Use explicit sanitization
