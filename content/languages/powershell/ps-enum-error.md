---
title: "[Solution] Enum Definition Error"
description: "Enum definition errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Enum Definition Error

Enum definition errors.

### Common Causes
Wrong values; duplicate names

### How to Fix
```powershell
enum Color { Red; Green; Blue }
```

### Examples
```powershell
enum Status {
  Active = 1
  Inactive = 2
}
```
