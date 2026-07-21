---
title: "Objective-C NSURLSession Task Cancel Error"
description: "Fix Objective-C NSURLSession task errors when cancelling tasks or handling cancellation in completion handlers."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Completion handler called with NSURLErrorCancelled after cancel
- Not checking for cancellation error before processing result
- Cancelling task after session is invalidated
- Multiple cancel calls on same task
- Not handling partial data on cancellation

## How to Fix

```objc
// WRONG: Not checking for cancellation
- (void)URLSession:(NSURLSession *)session
    task:(NSURLSessionTask *)task
    didCompleteWithError:(NSError *)error {
    if (error) {
        // treats cancellation same as real error
        [self showError:error];
    }
}

// CORRECT: Distinguish cancellation from real errors
- (void)URLSession:(NSURLSession *)session
    task:(NSURLSessionTask *)task
    didCompleteWithError:(NSError *)error {
    if ([error.domain isEqualToString:NSURLErrorDomain] &&
        error.code == NSURLErrorCancelled) {
        NSLog(@"Task was cancelled");
        return;
    }
    if (error) {
        [self showError:error];
    }
}
```

## Examples

```objc
// Example 1: Cancel a task
NSURLSessionDataTask *task = [session dataTaskWithRequest:request
    completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
        if ([error.domain isEqualToString:NSURLErrorDomain] &&
            error.code == NSURLErrorCancelled) {
            return; // silently handle cancellation
        }
        // process data
    }];
[task cancel];

// Example 2: Cancel all tasks
[session getTasksWithCompletionHandler:^(NSArray *dataTasks,
    NSArray *uploadTasks, NSArray *downloadTasks) {
    for (NSURLSessionTask *task in dataTasks) {
        [task cancel];
    }
}];

// Example 3: Save partial data on cancel
- (void)URLSession:(NSURLSession *)session
    task:(NSURLSessionTask *)task
    didCompleteWithError:(NSError *)error {
    if (error.code == NSURLErrorCancelled && self.partialData.length > 0) {
        [self savePartialData:self.partialData];
    }
}
```

## Related Errors

- [URLSession error](objc-nsurlsession-error) -- session-related issues
- [NSURLError](objc-nsurlerror) -- URL operation errors
