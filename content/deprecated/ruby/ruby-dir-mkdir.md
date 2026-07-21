---
title: "[Solution] Deprecated Function Migration: Dir.mkdir to FileUtils.mkdir_p"
description: "Migrate from deprecated Dir.mkdir to FileUtils.mkdir_p."
deprecated_function: "Dir.mkdir(path)"
replacement_function: "FileUtils.mkdir_p(path)"
languages: ["ruby"]
deprecated_since: "Ruby 1.0+"
---

# [Solution] Deprecated Function Migration: Dir.mkdir to FileUtils.mkdir_p

The `Dir.mkdir(path)` has been deprecated in favor of `FileUtils.mkdir_p(path)`.

## Migration Guide

mkdir_p creates parent dirs.

## Before (Deprecated)

```ruby
Dir.mkdir('a/b/c')  # fails if parent missing
```

## After (Modern)

```ruby
FileUtils.mkdir_p('a/b/c')  # creates all parents
```

## Key Differences

- mkdir_p creates parent dirs
