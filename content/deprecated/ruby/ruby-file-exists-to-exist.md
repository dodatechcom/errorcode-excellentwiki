---
title: "[Solution] Deprecated Function Migration: File.exists? to File.exist?"
description: "Migrate from deprecated File.exists? to File.exist? in Ruby."
deprecated_function: "File.exists?"
replacement_function: "File.exist?"
languages: ["ruby"]
deprecated_since: "Ruby 2.1+ / removed Ruby 3.2"
---

# [Solution] Deprecated Function Migration: File.exists? to File.exist?

The `File.exists?` has been deprecated in favor of `File.exist?`.

## Migration Guide

File.exists? was deprecated in Ruby 2.1 and removed in Ruby 3.2. Use File.exist? instead.

## Before (Deprecated)

```ruby
if File.exists?("config.yml")
    puts "Config found"
end
```

## After (Modern)

```ruby
if File.exist?("config.yml")
    puts "Config found"
end
```

## Key Differences

- Replace exists? with exist? (remove the s)
- Applies to both File and Dir
- Removed in Ruby 3.2
