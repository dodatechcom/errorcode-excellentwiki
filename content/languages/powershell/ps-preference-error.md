---
title: "[Solution] Preference Variable Error"
description: "Preference variable errors."
languages: ["powershell"]
error-types: ["language-error"]
severities: ["error"]
---

# Preference Variable Error

Preference variable errors.

### Common Causes
Wrong value; scope issues

### How to Fix
```powershell
$WarningPreference = "Continue"
```

### Examples
```powershell
$ProgressPreference = "SilentlyContinue"
```
