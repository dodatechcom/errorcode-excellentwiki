---
title: "Array bounds error"
description: "An array bounds error occurs when accessing an array element with an index outside its valid range."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An array bounds error (NSRangeException) occurs when you try to access an NSArray element using an index that is outside the valid range (less than 0 or greater than or equal to the array's count).

## Common Causes

- Off-by-one errors
- Using wrong index calculation
- Empty array access
- Incorrect loop bounds

## How to Fix

```objc
// WRONG: Accessing beyond bounds
NSArray *arr = @[@"a", @"b", @"c"];
NSString *s = arr[3];  // NSRangeException

// CORRECT: Check bounds first
NSArray *arr = @[@"a", @"b", @"c"];
if (arr.count > 3) {
    NSString *s = arr[3];
}
```

```objc
// WRONG: No bounds check
NSString *getElement(NSArray *arr, NSUInteger idx) {
    return arr[idx];  // may throw
}

// CORRECT: Safe access
NSString *getElement(NSArray *arr, NSUInteger idx) {
    if (idx < arr.count) {
        return arr[idx];
    }
    return nil;
}
```

## Examples

```objc
// Example 1: Off by one
NSArray *arr = @[@"a", @"b", @"c"];
NSString *s = arr[arr.count];  // NSRangeException

// Example 2: Negative index
NSArray *arr = @[@"a", @"b", @"c"];
NSString *s = arr[-1];  // NSRangeException

// Example 3: Empty array
NSArray *empty = @[];
NSString *s = empty[0];  // NSRangeException
```

## Related Errors

- [EXC_BAD_ACCESS](/languages/objective-c/exc-bad-access)
- [key not found](/languages/objective-c/key-not-found)
