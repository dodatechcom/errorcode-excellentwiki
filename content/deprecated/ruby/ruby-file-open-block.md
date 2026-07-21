---
title: "[Solution] Deprecated Function Migration: File.open without block to with block"
description: "Migrate from deprecated File.open without block to using blocks for automatic file closure."
deprecated_function: "f = File.open(); f.close"
replacement_function: "File.open do |f| end"
languages: ["ruby"]
deprecated_since: "Ruby 1.8+"
---

# [Solution] Deprecated Function Migration: File.open without block to with block

The `f = File.open(); f.close` has been deprecated in favor of `File.open do |f| end`.

## Migration Guide

File.open without a block requires manual close. The block form auto-closes the file.

## Before (Deprecated)

```ruby
f = File.open("data.txt", "r")
data = f.read
f.close
```

## After (Modern)

```ruby
File.open("data.txt", "r") do |f|
    data = f.read
end

# Simpler
data = File.read("data.txt")
File.write("output.txt", "Hello")
```

## Key Differences

- Block form auto-closes the file
- File.read/write for simple operations
- No need for manual close with blocks
