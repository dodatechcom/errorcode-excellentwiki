---
title: "[Solution] Deprecated Function Migration: open-uri to URI.open"
description: "Migrate from deprecated open to URI.open for URLs."
deprecated_function: "open(url)"
replacement_function: "URI.open(url)"
languages: ["ruby"]
deprecated_since: "Ruby 2.7+"
---

# [Solution] Deprecated Function Migration: open-uri to URI.open

The `open(url)` has been deprecated in favor of `URI.open(url)`.

## Migration Guide

URI.open is more explicit.

## Before (Deprecated)

```ruby
open(url) do |f|
    puts f.read
end
```

## After (Modern)

```ruby
URI.open(url) do |f|
    puts f.read
end
```

## Key Differences

- URI.open is more explicit
