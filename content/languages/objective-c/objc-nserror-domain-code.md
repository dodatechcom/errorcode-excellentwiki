---
title: "Objective-C NSError Domain Code Error"
description: "Fix Objective-C NSError errors when creating or handling errors with incorrect domain and code combinations."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Using wrong error domain string constant
- Error code does not match the domain's defined codes
- Not checking NSError pointer after operation
- Creating NSError with nil userInfo dictionary when needed
- Comparing error domains with == instead of isEqualToString

## How to Fix

```objc
// WRONG: Wrong domain constant
NSError *error = nil;
[NSJSONSerialization JSONObjectWithData:data options:0 error:&error];
if (error.code == NSURLErrorTimedOut) { // wrong domain!
    // NSJSONSerialization uses NSCocoaErrorDomain, not NSURLErrorDomain
}

// CORRECT: Check both domain and code
if ([error.domain isEqualToString:NSCocoaErrorDomain] &&
    error.code == NSJSONSerializationReadingNotAllowed) {
    // handle JSON error
}
```

```objc
// WRONG: Not checking error at all
NSURL *url = [NSURL URLWithString:@"invalid url"];
NSData *data = [NSData dataWithContentsOfURL:url]; // nil, no error check

// CORRECT: Use error parameter
NSError *error = nil;
NSData *data = [NSData dataWithContentsOfURL:url options:0 error:&error];
if (!data) {
    NSLog(@"Failed: %@", error.localizedDescription);
}
```

## Examples

```objc
// Example 1: Create custom error
NSError *error = [NSError errorWithDomain:@"com.myapp"
                                     code:1001
                                 userInfo:@{
    NSLocalizedDescriptionKey: @"Invalid configuration",
    NSLocalizedRecoverySuggestionErrorKey: @"Check settings"
}];

// Example 2: Check specific error
if ([error.domain isEqualToString:NSURLErrorDomain]) {
    switch (error.code) {
        case NSURLErrorTimedOut: break;
        case NSURLErrorNotConnectedToInternet: break;
    }
}

// Example 3: Nil-coalescing with error
NSString *desc = error.localizedDescription ?: @"Unknown error";
```

## Related Errors

- [NSError error](objc-nserror-error) -- NSError handling issues
- [NSURLError](objc-nsurlerror) -- URL-related errors
