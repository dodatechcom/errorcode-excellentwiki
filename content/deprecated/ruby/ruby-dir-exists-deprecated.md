---
title: "[Solution] Deprecated Function Migration: Dir.exists? to Dir.exist?"
description: "Migrate from deprecated Dir.exists? to Dir.exist?."
deprecated_function: "Dir.exists?(path)"
replacement_function: "Dir.exist?(path)"
languages: ["ruby"]
deprecated_since: "Ruby 1.9.2+"
---

# [Solution] Deprecated Function Migration: Dir.exists? to Dir.exist?

The `Dir.exists?(path)` has been deprecated in favor of `Dir.exist?(path)`.

## Migration Guide

Dir.exist? is the correct form.

## Before (Deprecated)

```ruby
if Dir.exists?(path) { }
```

## After (Modern)

```ruby
if Dir.exist?(path) { }
```

## Key Differences

- Dir.exist? is the correct form
