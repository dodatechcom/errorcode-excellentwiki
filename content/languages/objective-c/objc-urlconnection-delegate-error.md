---
title: "Objective-C NSURLConnection Delegate Error"
description: "Fix Objective-C NSURLConnection delegate errors when connection delegates are not properly implemented."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- NSURLConnection deprecated, use NSURLSession
- Required delegate methods not implemented
- Connection released before delegate callback
- Not handling authentication challenges in delegate
- Forgetting to call completion block in didReceiveResponse

## How to Fix

```objc
// WRONG: Using deprecated NSURLConnection
NSURLConnection *conn = [[NSURLConnection alloc]
    initWithRequest:request delegate:self];
// Deprecated since iOS 9

// CORRECT: Use NSURLSession
NSURLSessionDataTask *task = [[NSURLSession sharedSession]
    dataTaskWithRequest:request
    completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
        // handle response
    }];
[task resume];
```

```enrl
// WRONG: Missing required delegate
- (void)connection:(NSURLConnection *)connection
    didReceiveResponse:(NSURLResponse *)response {
    // forgot to initialize receivedData
}

// CORRECT: Initialize data in response
- (void)connection:(NSURLConnection *)connection
    didReceiveResponse:(NSURLResponse *)response {
    self.receivedData = [[NSMutableData alloc] init];
}
```

## Examples

```objc
// Example 1: NSURLSession delegate
- (void)startDownload {
    NSURLSessionConfiguration *config = [NSURLSessionConfiguration defaultSessionConfiguration];
    self.session = [NSURLSession sessionWithConfiguration:config
        delegate:self delegateQueue:nil];
    NSURLSessionDataTask *task = [self.session dataTaskWithRequest:self.request];
    [task resume];
}

- (void)URLSession:(NSURLSession *)session
    dataTask:(NSURLSessionDataTask *)task
    didReceiveData:(NSData *)data {
    [self.receivedData appendData:data];
}

- (void)URLSession:(NSURLSession *)session
    task:(NSURLSessionTask *)task
    didCompleteWithError:(NSError *)error {
    if (!error) {
        [self processData:self.receivedData];
    }
}

// Example 2: Download task
NSURLSessionDownloadTask *downloadTask = [self.session
    downloadTaskWithRequest:request];
[downloadTask resume];
```

## Related Errors

- [URLSession error](objc-nsurlsession-error) -- session issues
- [URL connection error](objc-nsurlconnection-error) -- connection problems
