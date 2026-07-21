---
title: "Objective-C NSString Encoding Conversion Error"
description: "Fix Objective-C NSString encoding errors when converting between string encodings with invalid byte sequences."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Using wrong NSStringEncoding constant for the data
- Data contains bytes invalid for the target encoding
- lossyConversion flag silently drops characters
- BOM (byte order mark) present but not accounted for
- Mixing ASCII and multi-byte encodings in same data

## How to Fix

```objc
// WRONG: Assuming UTF-8 without checking
NSData *data = ...;
NSString *str = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
if (str == nil) {
    // data is not valid UTF-8
}

// CORRECT: Try multiple encodings
NSString *str = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
if (!str) {
    str = [[NSString alloc] initWithData:data encoding:NSISOLatin1StringEncoding];
}
```

```objc
// WRONG: Lossy conversion drops characters
NSString *original = @"Héllo Wörld 日本語";
NSData *data = [original dataUsingEncoding:NSASCIIStringEncoding
                      allowLossyConversion:YES];
// Characters are lost

// CORRECT: Use UTF-8 for full Unicode
NSData *data = [original dataUsingEncoding:NSUTF8StringEncoding];
NSString *restored = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
```

## Examples

```objc
// Example 1: UTF-8 conversion
NSString *str = @"Hello こんにちは";
NSData *data = [str dataUsingEncoding:NSUTF8StringEncoding];
NSString *back = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];

// Example 2: Handle encoding errors
NSData *rawData = ...;
NSError *error = nil;
NSString *str = [[NSString alloc] initWithData:rawData
                                       encoding:NSUTF8StringEncoding];
if (!str) {
    NSDictionary *opts = @{NSCharacterConversionFallbackKey: @YES};
    str = [[NSString alloc] initWithData:rawData
                                encoding:NSISOLatin1StringEncoding];
}

// Example 3: Detect encoding
NSStringEncoding detected = [NSString stringEncodingForData:rawData
                                          encodingOptions:@{}
                                            convertedString:nil
                                        usedLossyConversion:nil];
```

## Related Errors

- [Unicode error](objc-nsstring-error) -- string encoding issues
- [NSString error](objc-nsstring-format-error) -- string formatting problems
