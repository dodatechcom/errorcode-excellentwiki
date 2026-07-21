---
title: "[Solution] Deprecated Function Migration: File.readlines to File.foreach"
description: "Migrate from deprecated eager File.readlines to lazy file reading."
deprecated_function: "File.readlines(file)"
replacement_function: "File.foreach(file)"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: File.readlines to File.foreach

The `File.readlines(file)` has been deprecated in favor of `File.foreach(file)`.

## Migration Guide

Lazy reading is memory-efficient

File.readlines reads entire file into memory.

## Before (Deprecated)

```ruby
lines = File.readlines('data.txt')
lines.each { |line| process(line) }
```

## After (Modern)

```ruby
File.foreach('data.txt') do |line|
  process(line)
end
```

## Key Differences

- File.foreach reads line by line
- Memory-efficient for large files
