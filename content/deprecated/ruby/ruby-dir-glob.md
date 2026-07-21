---
title: "[Solution] Deprecated Function Migration: Dir.glob with closing to Dir.each_child"
description: "Migrate from deprecated Dir patterns to modern directory iteration in Ruby."
deprecated_function: "Dir.open / Dir.glob"
replacement_function: "Dir.children / Dir.each_child"
languages: ["ruby"]
deprecated_since: "Ruby 2.5+"
---

# [Solution] Deprecated Function Migration: Dir.glob with closing to Dir.each_child

The `Dir.open / Dir.glob` has been deprecated in favor of `Dir.children / Dir.each_child`.

## Migration Guide

Dir.children and Dir.each_child provide safer directory iteration without manual close.

## Before (Deprecated)

```ruby
dir = Dir.open("/path")
while entry = dir.read
    puts entry if entry != "." && entry != ".."
end
dir.close
```

## After (Modern)

```ruby
Dir.children("/path").each do |entry|
    puts entry
end

# Or with full paths
Dir.each_child("/path") do |entry|
    puts File.join("/path", entry)
end
```

## Key Differences

- Dir.children returns entries excluding . and ..
- Dir.each_child iterates without . and ..
- No manual open/close needed
- Uses block form for automatic cleanup
