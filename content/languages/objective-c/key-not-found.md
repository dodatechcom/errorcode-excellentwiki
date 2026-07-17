---
title: "key not found"
description: "A key not found error occurs when accessing a dictionary with a key that doesn't exist."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `key not found` error occurs when you try to access a value in an NSDictionary using a key that doesn't exist in the dictionary. In Objective-C, accessing a missing key returns nil (rather than throwing an exception), but this can lead to unexpected nil behavior.

## Common Causes

- Typo in key name
- Key was never added to dictionary
- Wrong dictionary being accessed
- Case sensitivity in key names

## How to Fix

```objc
// WRONG: Accessing missing key directly
NSDictionary *dict = @{@"name": @"Alice"};
NSString *age = dict[@"age"];  // nil, may cause issues later

// CORRECT: Check if key exists
NSDictionary *dict = @{@"name": @"Alice"};
if (dict[@"age"]) {
    NSString *age = dict[@"age"];
} else {
    NSLog(@"Key 'age' not found");
}
```

```objc
// WRONG: Using objectForKey without check
NSDictionary *config = @{@"host": @"localhost"};
NSString *port = [config objectForKey:@"port"];  // nil

// CORRECT: Use objectForKeyedSubscript with default
NSString *port = config[@"port"] ?: @"8080";
```

## Examples

```objc
// Example 1: Missing key
NSDictionary *dict = @{@"a": @1, @"b": @2};
NSNumber *value = dict[@"c"];  // nil

// Example 2: Typo in key
NSDictionary *settings = @{@"debug": @YES};
if (settings[@"debg"]) {  // typo, always nil
    // never reached
}

// Example 3: Wrong case
NSDictionary *data = @{@"Name": @"Alice"};
NSString *name = data[@"name"];  // nil (case sensitive)
```

## Related Errors

- [unrecognized selector sent to instance](/languages/objective-c/unrecognized-selector)
- [message sent to nil](/languages/objective-c/nil-message)
