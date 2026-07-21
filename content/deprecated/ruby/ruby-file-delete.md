---
title: "[Solution] Deprecated Function Migration: File.delete to File.remove"
description: "Migrate from deprecated File.delete to File.remove."
deprecated_function: "File.delete(path)"
replacement_function: "FileUtils.rm(path)"
languages: ["ruby"]
deprecated_since: "Ruby 1.0+"
---

# [Solution] Deprecated Function Migration: File.delete to File.remove

The `File.delete(path)` has been deprecated in favor of `FileUtils.rm(path)`.

## Migration Guide

FileUtils.rm is more flexible.

## Before (Deprecated)

```ruby
File.delete('file.txt')
```

## After (Modern)

```ruby
FileUtils.rm('file.txt')
```

## Key Differences

- FileUtils.rm is more flexible
