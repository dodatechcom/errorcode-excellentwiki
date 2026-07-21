---
title: "Objective-C NSJSONSerialization Error"
description: "Fix Objective-C NSJSONSerialization errors when parsing malformed JSON or serializing non-JSON-compatible objects."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- JSON data is not valid UTF-8
- Trying to serialize NSArray or NSDictionary containing non-property objects
- JSON has trailing commas (invalid JSON)
- Top-level object is not NSArray or NSDictionary
- NSNull values not handled in deserialized dictionaries

## How to Fix

```objc
// WRONG: Non-serializable object in dictionary
NSDictionary *dict = @{
    @"data": self,  // cannot serialize custom object
    @"name": @"test"
};
NSData *json = [NSJSONSerialization dataWithJSONObject:dict
    options:0 error:nil]; // error!

// CORRECT: Convert custom objects to property lists
NSDictionary *dict = @{
    @"name": self.name,
    @"age": @(self.age)
};
NSData *json = [NSJSONSerialization dataWithJSONObject:dict
    options:0 error:nil];
```

```objc
// WRONG: Not handling NSNull in parsed JSON
NSDictionary *json = [NSJSONSerialization JSONObjectWithData:data
    options:0 error:nil];
NSString *value = json[@"key"]; // could be NSNull!

// CORRECT: Check for NSNull
id raw = json[@"key"];
NSString *value = (raw && raw != [NSNull null]) ? raw : nil;
```

## Examples

```objc
// Example 1: Parse JSON
NSError *error = nil;
NSDictionary *dict = [NSJSONSerialization JSONObjectWithData:jsonData
    options:NSJSONReadingMutableContainers error:&error];
if (!dict) {
    NSLog(@"Parse error: %@", error);
}

// Example 2: Serialize JSON
NSArray *array = @[@"hello", @42, @YES, @[@"nested"]];
NSData *data = [NSJSONSerialization dataWithJSONObject:array
    options:NSJSONWritingPrettyPrinted error:nil];
NSString *jsonStr = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];

// Example 3: Pretty print
NSDictionary *config = @{@"host": @"localhost", @"port": @8080};
NSData *pretty = [NSJSONSerialization dataWithJSONObject:config
    options:NSJSONWritingPrettyPrinted error:nil];
NSLog(@"%@", [[NSString alloc] initWithData:pretty encoding:NSUTF8StringEncoding]);
```

## Related Errors

- [JSON error](objc-nsjsonserialization) -- JSON parsing issues
- [NSCoding error](objc-nscoding-error) -- serialization problems
