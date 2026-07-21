---
title: "[Solution] Deprecated Function Migration: IO.read to File.read"
description: "Migrate from deprecated IO.read to File.read."
deprecated_function: "IO.read(path)"
replacement_function: "File.read(path)"
languages: ["ruby"]
deprecated_since: "Ruby 1.0+"
---

# [Solution] Deprecated Function Migration: IO.read to File.read

The `IO.read(path)` has been deprecated in favor of `File.read(path)`.

## Migration Guide

File.read is more specific.

## Before (Deprecated)

```ruby
content = IO.read('file.txt')
```

## After (Modern)

```ruby
content = File.read('file.txt')
```

## Key Differences

- File.read is more specific
