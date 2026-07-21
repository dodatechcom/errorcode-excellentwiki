---
title: "[Solution] flutter WebSocket Error Flutter"
description: "WebSocket not connecting."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

WebSocket not connecting.

## Common Causes

Wrong URL.

## How to Fix

Check URL.

## Example

```dart
final ws = WebSocketChannel.connect(Uri.parse('wss://example.com/ws'));
ws.stream.listen((data) => print(data));
```
