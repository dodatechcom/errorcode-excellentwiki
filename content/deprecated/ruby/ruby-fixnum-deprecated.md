---
title: "[Solution] Deprecated Function Migration: Fixnum to Integer"
description: "Migrate from deprecated Fixnum to Integer."
deprecated_function: "Fixnum"
replacement_function: "Integer"
languages: ["ruby"]
deprecated_since: "Ruby 2.4+"
---

# [Solution] Deprecated Function Migration: Fixnum to Integer

The `Fixnum` has been deprecated in favor of `Integer`.

## Migration Guide

Fixnum and Bignum were unified.

## Before (Deprecated)

```ruby
x = 42.is_a?(Fixnum)
```

## After (Modern)

```ruby
x = 42.is_a?(Integer)
```

## Key Differences

- Fixnum was unified with Integer
