---
title: "[Solution] Objective-C Bridging Error"
description: "Fix Objective-C and Swift bridging errors including type conversion issues"
languages: ["objective-c", "swift"]
error-types: ["runtime-error"]
severities: ["medium"]
weight: 5
---

## What This Error Means
Bridging errors occur when converting between Objective-C and Swift types, often due to incorrect type annotations or missing nullability information.

## Common Causes
- Missing nullability annotations in ObjC headers
- Incorrect nullable/nonnull annotations
- Bridging between NSString and String incorrectly
- Optionality mismatches
- Missing NS_SWIFT_NAME annotations

## How to Fix
```objectivec
// Add nullability annotations to ObjC headers
- (nullable NSString *)fetchDataWithError:(NSError *_Nullable *_Nullable)error;

// Use NS_ASSUME_NONNULL_BEGIN/END
NS_ASSUME_NONNULL_BEGIN
@interface MyClass : NSObject
- (NSString *)requiredMethod;
- (nullable NSString *)optionalMethod;
@end
NS_ASSUME_NONNULL_END

// Use NS_REFINED_FOR_SWIFT for better Swift naming
- (NSString *)dataDescription NS_REFINED_FOR_SWIFT;
```