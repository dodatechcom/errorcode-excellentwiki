---
title: "[Solution] Hashtable Error"
description: "Hashtable creation and access errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Hashtable Error

Hashtable creation and access errors.

### Common Causes
Wrong syntax; key not found; null

### How to Fix
```powershell
$ht = @{"key1" = "value1"; "key2" = "value2"}
$ht["key1"]
```

### Examples
```powershell
$ht = [ordered]@{
  Name = "Test"
  Value = 42
}
```
