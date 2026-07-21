---
title: "[Solution] Flutter TabController Error"
description: "TabController not working."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

TabController not working.

## Common Causes

Not initialized.

## How to Fix

Initialize.

## Example

```dart
late TabController tc;
@override
void initState() { tc = TabController(length: 3, vsync: this); }
```
