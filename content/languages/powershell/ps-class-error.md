---
title: "[Solution] Class Definition Error"
description: "Class definition errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Class Definition Error

Class definition errors.

### Common Causes
Missing braces; wrong inheritance

### How to Fix
```powershell
class MyClass {
  [string]$Name
  MyClass([string]$n) { $this.Name = $n }
}
```

### Examples
```powershell
$c = [MyClass]::new("Test")
$c.Name
```
