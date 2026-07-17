---
title: "AsyncStorage - data corruption error"
description: "React Native AsyncStorage fails to read or write data due to corruption, exceeding size limits, or serialization errors"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["asyncstorage", "storage", "corruption", "data", "persistence", "serialization"]
weight: 5
---

An AsyncStorage corruption error occurs when stored data cannot be read back correctly. This can happen due to invalid JSON serialization, storage reaching platform size limits, or interrupted write operations leaving partial data.

## Common Causes

- Storing invalid JSON or circular references
- AsyncStorage size exceeded (6MB on Android, varies on iOS)
- Concurrent writes causing data corruption
- Storing undefined values directly
- Platform-specific storage limits reached

## How to Fix

1. Wrap all storage operations with error handling:

```javascript
import AsyncStorage from '@react-native-async-storage/async-storage';

const safeSetItem = async (key, value) => {
  try {
    const jsonValue = JSON.stringify(value);
    await AsyncStorage.setItem(key, jsonValue);
  } catch (error) {
    console.error('Storage write error:', error);
  }
};

const safeGetItem = async (key) => {
  try {
    const jsonValue = await AsyncStorage.getItem(key);
    return jsonValue ? JSON.parse(jsonValue) : null;
  } catch (error) {
    console.error('Storage read error:', error);
    await AsyncStorage.removeItem(key);
    return null;
  }
};
```

2. Clear corrupted storage as a recovery step:

```javascript
const clearAndReset = async () => {
  await AsyncStorage.clear();
  await safeSetItem('@app_data', { initialized: true });
};
```

3. Add size checks before storing:

```javascript
const safeStore = async (key, value) => {
  const json = JSON.stringify(value);
  if (json.length > 5 * 1024 * 1024) {
    throw new Error('Data too large for AsyncStorage');
  }
  await AsyncStorage.setItem(key, json);
};
```

4. Use MMKV as a faster, more reliable alternative:

```bash
npm install react-native-mmkv
```

```javascript
import { MMKV } from 'react-native-mmkv';

const storage = new MMKV();
storage.set('user', JSON.stringify({ name: 'John' }));
const user = JSON.parse(storage.getString('user') ?? '{}');
```

## Examples

```javascript
// Storing undefined causes corruption
await AsyncStorage.setItem('user', undefined);
// Next read: SyntaxError: Unexpected token u in JSON at position 0

// Fix: always store valid JSON
await AsyncStorage.setItem('user', JSON.stringify(null));
```

## Related Errors

- [RedBox error]({{< relref "/frameworks/react-native/rn-redbox-error-v2" >}})
- [Navigation error]({{< relref "/frameworks/react-native/rn-navigation-error" >}})
