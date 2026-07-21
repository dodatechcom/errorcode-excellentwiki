---
title: "[Solution] Deprecated Function Migration: Fixnum/Bignum to Integer"
description: "Migrate from deprecated Fixnum and Bignum classes to unified Integer in Ruby."
deprecated_function: "Fixnum / Bignum"
replacement_function: "Integer"
languages: ["ruby"]
deprecated_since: "Ruby 2.4+"
---

# [Solution] Deprecated Function Migration: Fixnum/Bignum to Integer

The `Fixnum / Bignum` has been deprecated in favor of `Integer`.

## Migration Guide

In Ruby 2.4, Fixnum and Bignum were unified into Integer.

## Before (Deprecated)

```ruby
x = 42
puts x.class  # Fixnum (Ruby < 2.4)

big = 2**100
puts big.class  # Bignum
```

## After (Modern)

```ruby
x = 42
puts x.class  # Integer

big = 2**100
puts big.class  # Integer

puts x.is_a?(Integer)  # true
```

## Key Differences

- Fixnum and Bignum are now aliases for Integer
- Integer handles arbitrary precision automatically
- Replace Fixnum/Bignum with Integer
