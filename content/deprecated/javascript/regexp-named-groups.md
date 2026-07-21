---
title: "[Solution] Deprecated Function Migration: unnamed regex groups to named capture groups"
description: "Migrate from complex unnamed regex groups to named capture groups and lookbehind assertions."
deprecated_function: "Unnamed regex groups"
replacement_function: "Named groups (?<name>)"
languages: ["javascript"]
deprecated_since: "ES2018"
---

# [Solution] Deprecated Function Migration: unnamed regex groups to named capture groups

The `Unnamed regex groups` has been deprecated in favor of `Named groups (?<name>)`.

## Migration Guide

Named capture groups make complex regex patterns more readable and maintainable.

## Before (Deprecated)

```javascript
const match = /(\d{4})-(\d{2})-(\d{2})/.exec("2024-01-15");
const year = match[1];
const month = match[2];
const day = match[3];
```

## After (Modern)

```javascript
const match = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/.exec("2024-01-15");
const { year, month, day } = match.groups;

// Lookbehind
const prices = "$100 €200";
const dollarPrices = prices.match(/(?<=\$)\d+/g);
```

## Key Differences

- (?<name>...) names a capture group
- match.groups gives named captures
- (?<=pattern) is positive lookbehind
