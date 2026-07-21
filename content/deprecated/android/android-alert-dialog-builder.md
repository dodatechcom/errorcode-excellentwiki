---
title: "[Solution] Deprecated Function Migration: AlertDialog.Builder to MaterialAlertDialogBuilder"
description: "Migrate from deprecated AlertDialog.Builder to MaterialAlertDialogBuilder."
deprecated_function: "AlertDialog.Builder(context)"
replacement_function: "MaterialAlertDialogBuilder(context)"
languages: ["android"]
deprecated_since: "Material Components"
---

# [Solution] Deprecated Function Migration: AlertDialog.Builder to MaterialAlertDialogBuilder

The `AlertDialog.Builder(context)` has been deprecated in favor of `MaterialAlertDialogBuilder(context)`.

## Migration Guide

MaterialAlertDialogBuilder follows Material Design.

## Before (Deprecated)

```android
AlertDialog.Builder(context)
    .setTitle("Title")
    .setMessage("Message")
    .show()
```

## After (Modern)

```android
MaterialAlertDialogBuilder(context)
    .setTitle("Title")
    .setMessage("Message")
    .show()
```

## Key Differences

- MaterialAlertDialogBuilder follows Material Design
