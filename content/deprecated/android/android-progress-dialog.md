---
title: "[Solution] Deprecated Function Migration: ProgressDialog to ProgressBar in layout"
description: "Migrate from deprecated ProgressDialog to ProgressBar in layout."
deprecated_function: "ProgressDialog.show(context)"
replacement_function: "ProgressBar in XML layout"
languages: ["android"]
deprecated_since: "Android 8.0+"
---

# [Solution] Deprecated Function Migration: ProgressDialog to ProgressBar in layout

The `ProgressDialog.show(context)` has been deprecated in favor of `ProgressBar in XML layout`.

## Migration Guide

ProgressDialog was deprecated.

## Before (Deprecated)

```android
val dialog = ProgressDialog.show(context, "Loading", "Please wait...")
```

## After (Modern)

```android
<ProgressBar
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:visibility="gone" />
```

## Key Differences

- Use ProgressBar in layout
