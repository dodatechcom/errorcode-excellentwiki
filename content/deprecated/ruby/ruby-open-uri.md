---
title: "[Solution] Deprecated Function Migration: Kernel.open to URI.open"
description: "Migrate from deprecated Kernel.open to URI.open."
deprecated_function: "open(url)"
replacement_function: "URI.open(url)"
languages: ["ruby"]
deprecated_since: "Ruby 2.7+"
---

# [Solution] Deprecated Function Migration: Kernel.open to URI.open

The `open(url)` has been deprecated in favor of `URI.open(url)`.

## Migration Guide

Kernel.open is dangerous

Kernel.open can execute commands (dangerous).

## Before (Deprecated)

```ruby
require 'open-uri'
html = open('https://example.com')
```

## After (Modern)

```ruby
require 'open-uri'
html = URI.open('https://example.com')

# Better: use net/http
require 'net/http'
response = Net::HTTP.get(URI('https://example.com'))
```

## Key Differences

- URI.open is explicit
- net/http is more robust
