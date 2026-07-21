---
title: "[Solution] Deprecated Function Migration: String#gsub! to String#sub for single replacement"
description: "Migrate from deprecated gsub! for single replacement to sub."
deprecated_function: "str.gsub!(/pattern/, 'replacement')"
replacement_function: "str.sub(/pattern/, 'replacement')"
languages: ["ruby"]
deprecated_since: "Ruby 1.8+"
---

# [Solution] Deprecated Function Migration: String#gsub! to String#sub for single replacement

The `str.gsub!(/pattern/, 'replacement')` has been deprecated in favor of `str.sub(/pattern/, 'replacement')`.

## Migration Guide

sub replaces only first match.

## Before (Deprecated)

```ruby
str.gsub!(/old/, 'new')
```

## After (Modern)

```ruby
str.sub(/old/, 'new')
```

## Key Differences

- sub for single replacement
