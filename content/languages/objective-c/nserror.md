---
title: "NSError domain error"
description: "An NSError occurs when an operation fails and provides detailed error information through domains and codes."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nserror", "domain", "error", "objc"]
weight: 5
---

## What This Error Means

An `NSError` is an object that represents an error condition, including the domain (error category), code, and user info. Methods use `NSError **` parameters to report errors back to callers.

## Common Causes

- Network operations failing
- File I/O errors
- Invalid user input
- System resource unavailability

## How to Fix

```objc
// WRONG: Not checking NSError
NSError *error;
NSString *content = [NSString stringWithContentsOfFile:@"file.txt"
                      encoding:NSUTF8StringEncoding
                         error:&error];
// content may be nil, error not checked

// CORRECT: Always check error
NSError *error;
NSString *content = [NSString stringWithContentsOfFile:@"file.txt"
                      encoding:NSUTF8StringEncoding
                         error:&error];
if (error) {
    NSLog(@"Error: %@", error.localizedDescription);
    return;
}
```

```objc
// WRONG: Ignoring error in network request
NSURLSessionDataTask *task = [session dataTaskWithURL:url
    completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
    // error not checked
}];

// CORRECT: Check error in completion handler
NSURLSessionDataTask *task = [session dataTaskWithURL:url
    completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
    if (error) {
        NSLog(@"Network error: %@", error.localizedDescription);
        return;
    }
    // process data
}];
```

## Examples

```objc
// Example 1: File not found
NSError *error;
NSString *content = [NSString stringWithContentsOfFile:@"missing.txt"
                      encoding:NSUTF8StringEncoding
                         error:&error];
// Error domain: NSCocoaErrorDomain, code: 260

// Example 2: Network error
NSURLSessionDataTask *task = [session dataTaskWithURL:url
    completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
    // error.domain = NSURLErrorDomain
}];

// Example 3: JSON parse error
NSError *error;
NSDictionary *json = [NSJSONSerialization JSONObjectWithData:data
                      options:0
                        error:&error];
// error if data is not valid JSON
```

## Related Errors

- [unrecognized selector sent to instance](/languages/objective-c/unrecognized-selector)
- [EXC_BAD_ACCESS](/languages/objective-c/exc-bad-access)
