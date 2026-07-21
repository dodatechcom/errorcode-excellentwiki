---
title: "[Solution] react-native DateTimePicker Error"
description: "Date picker not working."
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

Date picker not working.

## Common Causes

Wrong platform.

## How to Fix

Check platform.

## Example

```javascript
import DateTimePicker from '@react-native-community/datetimepicker';
<DateTimePicker value={date} onChange={(e, d) => setDate(d)} />
```
