---
title: "[Solution] Objective-C NSDate Error"
description: "NSDate formatting errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C NSDate Error

NSDate formatting errors.

### Common Causes
Wrong format string; timezone

### How to Fix
```objc
NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
[formatter setDateFormat:@"yyyy-MM-dd HH:mm:ss"];
NSString *dateStr = [formatter stringFromDate:[NSDate date]];
```

### Examples
```objc
NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
formatter.dateFormat = @"yyyy-MM-dd";
formatter.timeZone = [NSTimeZone timeZoneWithAbbreviation:@"UTC"];
```
