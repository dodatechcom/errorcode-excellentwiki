---
title: "[Solution] Flutter StreamBuilder Error"
description: "StreamBuilder not updating."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

StreamBuilder not updating.

## Common Causes

Wrong stream.

## How to Fix

Provide correct stream.

## Example

```dart
StreamBuilder(
  stream: myStream,
  builder: (context, snapshot) => Text(snapshot.data ?? ''),
)
```
