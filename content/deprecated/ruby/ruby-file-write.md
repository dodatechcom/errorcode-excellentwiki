---
title: "[Solution] Deprecated Function Migration: File.open + write to File.write"
description: "Migrate from deprecated File.open + write to File.write."
deprecated_function: "File.open(path, 'w') { |f| f.write(data) }"
replacement_function: "File.write(path, data)"
languages: ["ruby"]
deprecated_since: "Ruby 1.9.3+"
---

# [Solution] Deprecated Function Migration: File.open + write to File.write

The `File.open(path, 'w') { |f| f.write(data) }` has been deprecated in favor of `File.write(path, data)`.

## Migration Guide

File.write is a one-liner.

## Before (Deprecated)

```ruby
File.open("output.txt", "w") do |f|
    f.write(data)
end
```

## After (Modern)

```ruby
File.write("output.txt", data)
```

## Key Differences

- File.write is a one-liner
