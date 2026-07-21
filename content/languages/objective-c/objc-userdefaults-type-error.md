---
title: "Objective-C NSUserDefaults Type Mismatch Error"
description: "Fix Objective-C NSUserDefaults type mismatch errors when reading or writing values with incorrect types."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Storing NSNumber but reading as NSString
- Storing custom object that does not support NSCoding
- Key name typo returns nil or default value
- Overwriting array with dictionary for same key
- Not calling synchronize after critical writes

## How to Fix

```objc
// WRONG: Assuming type without checking
NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
NSString *value = [defaults objectForKey:@"count"]; // could be NSNumber!

// CORRECT: Use typed accessors
NSInteger count = [defaults integerForKey:@"count"];
NSString *name = [defaults stringForKey:@"name"];
NSArray *items = [defaults arrayForKey:@"items"];
```

```enrl
// WRONG: Storing custom object
MyModel *model = [[MyModel alloc] init];
[defaults setObject:model forKey:@"model"]; // crashes!

// CORRECT: Archive custom object
NSData *data = [NSKeyedArchiver archivedDataWithRootObject:model
    requiringSecureCoding:YES error:nil];
[defaults setObject:data forKey:@"model"];
```

## Examples

```objc
// Example 1: Basic defaults operations
NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
[defaults setInteger:42 forKey:@"score"];
[defaults setBool:YES forKey:@"soundEnabled"];
[defaults setObject:@"dark" forKey:@"theme"];
[defaults synchronize];

// Example 2: Read with defaults
NSString *theme = [defaults stringForKey:@"theme"] ?: @"light";
BOOL sound = [defaults boolForKey:@"soundEnabled"];

// Example 3: Register defaults
[defaults registerDefaults:@{
    @"theme": @"light",
    @"fontSize": @14,
    @"showWelcome": @YES
}];
```

## Related Errors

- [NSCoding error](objc-nscoding-error) -- serialization issues
- [Plist error](objc-plist-error) -- property list problems
