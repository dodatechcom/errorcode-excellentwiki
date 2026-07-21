---
title: "[Solution] React Native FlatList keyExtractor Error"
description: "Key warning."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Key warning.

## Common Causes

Wrong extractor.

## How to Fix

Return unique key.

## Example

```javascript
<FlatList data={d} keyExtractor={i => i.id.toString()} />
```
