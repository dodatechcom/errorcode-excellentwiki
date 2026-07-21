---
title: "[Solution] Deprecated Function Migration: String#scan to String#match with named captures"
description: "Migrate from deprecated String#scan to String#match for pattern matching."
deprecated_function: "str.scan(/pattern/)"
replacement_function: "str.match(/pattern/)"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: String#scan to String#match with named captures

The `str.scan(/pattern/)` has been deprecated in favor of `str.match(/pattern/)`.

## Migration Guide

match provides capture groups and named captures

scan returns all matches. match returns MatchData with captures.

## Before (Deprecated)

```ruby
str = "2024-01-15"
str.scan(/\d{4}/)  # ["2024"]
str.scan(/(\d{4})-(\d{2})-(\d{2})/)
  # [["2024", "01", "15"]]
```

## After (Modern)

```ruby
str = "2024-01-15"
match = str.match(/(\d{4})-(\d{2})-(\d{2})/)
if match
    year = match[1]
    month = match[2]
    day = match[3]
end

# Named captures
match = str.match(/(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/)
year = match[:year]
```

## Key Differences

- match returns MatchData
- Named captures with (?<name>)
- scan for all matches
- match for first match with captures
