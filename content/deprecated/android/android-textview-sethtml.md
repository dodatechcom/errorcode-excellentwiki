---
title: "[Solution] Deprecated Function Migration: TextView.setHtml to Linkify or custom MovementMethod"
description: "Migrate from deprecated setHtml to Linkify."
deprecated_function: "textView.setText(Html.fromHtml(html))"
replacement_function: "Linkify.addLinks(textView, Linkify.WEB_URLS)"
languages: ["android"]
deprecated_since: "Android"
---

# [Solution] Deprecated Function Migration: TextView.setHtml to Linkify or custom MovementMethod

The `textView.setText(Html.fromHtml(html))` has been deprecated in favor of `Linkify.addLinks(textView, Linkify.WEB_URLS)`.

## Migration Guide

Linkify is more standard.

## Before (Deprecated)

```android
textView.setText(Html.fromHtml(html))
```

## After (Modern)

```android
Linkify.addLinks(textView, Linkify.WEB_URLS)
```

## Key Differences

- Linkify is more standard
