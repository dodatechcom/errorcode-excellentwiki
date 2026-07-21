---
title: "[Solution] Deprecated Function Migration: implicit encoding to explicit encoding"
description: "Migrate from deprecated implicit string encoding to explicit."
deprecated_function: "str.encode('UTF-8')"
replacement_function: "str.encode('UTF-8', invalid: :replace)"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: implicit encoding to explicit encoding

The `str.encode('UTF-8')` has been deprecated in favor of `str.encode('UTF-8', invalid: :replace)`.

## Migration Guide

Explicit encoding prevents errors

String encoding can cause errors.

## Before (Deprecated)

```ruby
str.encode('UTF-8')
```

## After (Modern)

```ruby
str.encode('UTF-8', 'ASCII', invalid: :replace, undef: :replace)
```

## Key Differences

- Explicit encoding prevents errors
- Handle invalid/undefined characters
