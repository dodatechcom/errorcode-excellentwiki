---
title: "[Solution] Deprecated Function Migration: verbose blocks to Symbol#to_proc"
description: "Migrate from verbose proc patterns to Symbol#to_proc."
deprecated_function: "lambda { |x| x.method }"
replacement_function: "&:method"
languages: ["ruby"]
deprecated_since: "Ruby 1.8.7+"
---

# [Solution] Deprecated Function Migration: verbose blocks to Symbol#to_proc

The `lambda { |x| x.method }` has been deprecated in favor of `&:method`.

## Migration Guide

Symbol#to_proc is concise

Symbol#to_proc converts a symbol to a proc.

## Before (Deprecated)

```ruby
items.map { |item| item.name }
items.select { |item| item.active? }
```

## After (Modern)

```ruby
items.map(&:name)
items.select(&:active?)
```

## Key Differences

- &:method converts symbol to proc
- Much more concise
