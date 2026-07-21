---
title: "Objective-C NSData Base64 Encoding Error"
description: "Fix Objective-C NSData base64 encoding errors when converting between NSData and base64 strings incorrectly."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Using deprecated base64 methods (before iOS 7)
- Not handling padding characters correctly
- Encoding data with embedded null bytes
- Mixing base64 encoding options (with/without line breaks)
- Decoding invalid base64 strings without error handling

## How to Fix

```objc
// WRONG: Deprecated method
NSString *encoded = [data base64EncodedStringWithOptions:0]; // wrong on old iOS

// CORRECT: Use proper API
NSString *encoded = [data base64EncodedStringWithOptions:0]; // iOS 7+

// Decoding
NSData *decoded = [[NSData alloc] initWithBase64EncodedString:encoded
    options:0];
```

```objc
// WRONG: Not handling nil input
NSString *base64 = nil;
NSData *data = [[NSData alloc] initWithBase64EncodedString:base64
    options:NSDataBase64DecodingIgnoreUnknownCharacters];
// data is nil

// CORRECT: Check input first
if (base64.length > 0) {
    NSData *data = [[NSData alloc] initWithBase64EncodedString:base64
        options:0];
}
```

## Examples

```objc
// Example 1: Encode data to base64
NSData *data = [@"Hello World" dataUsingEncoding:NSUTF8StringEncoding];
NSString *base64 = [data base64EncodedStringWithOptions:0];
NSLog(@"Encoded: %@", base64); // "SGVsbG8gV29ybGQ="

// Example 2: Decode base64 to data
NSString *base64 = @"SGVsbG8gV29ybGQ=";
NSData *data = [[NSData alloc] initWithBase64EncodedString:base64 options:0];
NSString *decoded = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
NSLog(@"Decoded: %@", decoded); // "Hello World"

// Example 3: URL-safe base64
NSString *urlSafe = [base64 stringByReplacingOccurrencesOfString:@"+" withString:@"-"];
urlSafe = [urlSafe stringByReplacingOccurrencesOfString:@"/" withString:@"_"];
```

## Related Errors

- [NSData error](objc-nsdata-error) -- data operation problems
- [NSCoding error](objc-nscoding-error) -- serialization issues
