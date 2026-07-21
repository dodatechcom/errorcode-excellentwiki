---
title: "[Solution] Objective-C URLSession Error"
description: "NSURLSession errors."
languages: ["objective-c"]
error-types: ["language-error"]
severities: ["error"]
---

# Objective-C URLSession Error

NSURLSession errors.

### Common Causes
Wrong delegate; missing completion

### How to Fix
```objc
NSURLSessionDataTask *task = [[NSURLSession sharedSession]
    dataTaskWithURL:[NSURL URLWithString:@"https://example.com"]
    completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
        if (error) {
            NSLog(@"Error: %@", error);
            return;
        }
        // process data
    }];
[task resume];
```

### Examples
```objc
- (void)URLSession:(NSURLSession *)session
    task:(NSURLSessionTask *)task
    didCompleteWithError:(NSError *)error {
    if (error) NSLog(@"Task failed: %@", error);
}
```
