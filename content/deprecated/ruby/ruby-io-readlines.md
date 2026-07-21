---
title: "[Solution] Deprecated Function Migration: IO.readlines to File.readlines"
description: "Migrate from deprecated IO.readlines to File.readlines."
deprecated_function: "IO.readlines(path)"
replacement_function: "File.readlines(path)"
languages: ["ruby"]
deprecated_since: "Ruby 1.0+"
---

# [Solution] Deprecated Function Migration: IO.readlines to File.readlines

The `IO.readlines(path)` has been deprecated in favor of `File.readlines(path)`.

## Migration Guide

File.readlines is more specific.

## Before (Deprecated)

```ruby
lines = IO.readlines('file.txt')
```

## After (Modern)

```ruby
lines = File.readlines('file.txt')
```

## Key Differences

- File.readlines is more specific
