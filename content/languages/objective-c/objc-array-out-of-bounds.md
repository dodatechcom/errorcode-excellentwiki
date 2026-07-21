---
title: "Objective-C NSMutableArray Out Of Bounds Error"
description: "Fix Objective-C NSMutableArray out of bounds errors when accessing or inserting array elements beyond valid indices."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Accessing array index equal to or greater than count
- Inserting at index beyond array bounds
- Removing object at non-existent index
- Enumeration while modifying array causes mutation exception
- Using objectAtIndex on empty array

## How to Fix

```objc
// WRONG: Accessing out of bounds
NSMutableArray *arr = [@[@"a", @"b"] mutableCopy];
NSString *item = arr[5]; // NSException: index 5 beyond bounds

// CORRECT: Check count first
if (arr.count > 5) {
    NSString *item = arr[5];
}
```

```objc
// WRONG: Mutating during enumeration
NSMutableArray *arr = [NSMutableArray arrayWithObjects:@"a", @"b", @"c", nil];
for (NSString *item in arr) {
    if ([item isEqualToString:@"b"]) {
        [arr removeObject:item]; // mutation exception
    }
}

// CORRECT: Collect items to remove, then remove
NSMutableArray *toRemove = [NSMutableArray array];
for (NSString *item in arr) {
    if ([item isEqualToString:@"b"]) {
        [toRemove addObject:item];
    }
}
[arr removeObjectsInArray:toRemove];
```

## Examples

```objc
// Example 1: Safe access
NSArray *arr = @[@"first", @"second", @"third"];
id item = (arr.count > 10) ? arr[10] : nil;

// Example 2: Safe insert
NSMutableArray *arr = [NSMutableArray array];
NSUInteger idx = MIN(3, arr.count); // clamp to valid range
[arr insertObject:@"new" atIndex:idx];

// Example 3: Safe remove
NSMutableArray *arr = [@[@"a", @"b", @"c"] mutableCopy];
if (arr.count > 1) {
    [arr removeObjectAtIndex:1];
}
```

## Related Errors

- [Array bounds error](array-bounds) -- array index issues
- [Index out of bounds](objc-nsarray-error) -- NSArray access failures
