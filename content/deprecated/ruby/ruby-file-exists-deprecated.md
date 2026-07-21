---
title: "[Solution] Deprecated Function Migration: File.exists? to File.exist?"
description: "Migrate from deprecated File.exists? to File.exist?."
deprecated_function: "File.exists?(path)"
replacement_function: "File.exist?(path)"
languages: ["ruby"]
deprecated_since: "Ruby 1.9.2+"
---

# [Solution] Deprecated Function Migration: File.exists? to File.exist?

The `File.exists?(path)` has been deprecated in favor of `File.exist?(path)`.

## Migration Guide

File.exist? is the correct form.

## Before (Deprecated)

```ruby
if File.exists?(path) { }
```

## After (Modern)

```ruby
if File.exist?(path) { }
```

## Key Differences

- File.exist? is the correct form
