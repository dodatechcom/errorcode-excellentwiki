---
title: "[Solution] Objective-C NSURLConnection Connection Failed"
description: "Fix Objective-C NSURLConnection connection failed error. Handle network errors, timeouts, and authentication."
languages: ["objective-c"]
error-types: ["network-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

NSURLConnection connection failed errors occur when the legacy NSURLConnection class cannot establish or complete a network request. This includes timeout, DNS failure, and SSL errors.

## Why It Happens

- Server is unreachable or DNS resolution fails: The hostname cannot be resolved.
- Connection timeout exceeded: The server takes too long to respond.
- SSL certificate validation failure: The server certificate is invalid.
- Network interface not available: The device has no network connection.
- Server returned non-200 status code: The server responded with an error.

## How to Fix It

Implement delegate with proper error handling:

```objectivec
- (void)connection:(NSURLConnection *)connection 
    didFailWithError:(NSError *)error {
    NSLog(@"Connection failed: %@", error.localizedDescription);
    NSLog(@"Error domain: %@", error.domain);
    NSLog(@"Error code: %ld", (long)error.code);
}
```

Handle HTTP response codes:

```objectivec
- (void)connection:(NSURLConnection *)connection 
    didReceiveResponse:(NSURLResponse *)response {
    NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)response;
    if (httpResponse.statusCode != 200) {
        NSLog(@"HTTP Error: %ld", (long)httpResponse.statusCode);
    }
}
```

Set appropriate timeouts:

```objectivec
NSMutableURLRequest *request = [NSMutableURLRequest 
    requestWithURL:url 
    cachePolicy:NSURLRequestReloadIgnoringLocalCacheData
    timeoutInterval:30.0];
```

Handle SSL challenges:

```objectivec
- (void)connection:(NSURLConnection *)connection 
    willSendRequestForAuthenticationChallenge:
    (NSURLAuthenticationChallenge *)challenge {
    if ([challenge.protectionSpace.authenticationMethod 
         isEqualToString:NSURLAuthenticationMethodServerTrust]) {
        [challenge.sender useCredential:
            [NSURLCredential credentialForTrust:
                challenge.protectionSpace.serverTrust] 
            forAuthenticationChallenge:challenge];
    }
}
```

Use synchronous requests for simple operations:

```objectivec
// WARNING: Only use on background thread
NSURLResponse *response = nil;
NSError *error = nil;
NSData *data = [NSURLConnection sendSynchronousRequest:request 
    returningResponse:&response 
    error:&error];
```

Handle redirect responses:

```objectivec
- (NSURLRequest *)connection:(NSURLConnection *)connection 
    willSendRequest:(NSURLRequest *)request 
    redirectResponse:(NSURLResponse *)response {
    NSLog(@"Redirecting to: %@", request.URL);
    return request;
}
```

Handle different connection states:

```objectivec
- (void)connectionDidFinishLoading:(NSURLConnection *)connection {
    NSLog(@"Connection completed successfully");
    NSLog(@"Received %lu bytes", (unsigned long)self.receivedData.length);
}
```

Use appropriate cache policies:

```objectivec
request.cachePolicy = NSURLRequestReturnCacheDataElseLoad;
request.timeoutInterval = 60.0;
```

Handle cookie storage:

```objectivec
[NSURLCache setSharedURLCache:[[NSURLCache alloc] 
    initWithMemoryCapacity:1024 * 1024 
    diskCapacity:1024 * 1024 * 10 
    diskPath:@"com.company.cache"]];
```

## Common Mistakes

- Not handling all delegate methods. Each delegate method serves a specific purpose.
- Using synchronous requests on main thread. This blocks the UI and causes watchdog kills.
- Ignoring HTTP status codes. Always check the status code before processing data.
- Not cancelling connections in dealloc. Unclosed connections leak memory.
- Not implementing didReceiveData for incremental data processing. Loading all data at once can cause memory issues.
- Forgetting to call [connection start] after creation. The connection does not start automatically.
- Not implementing willSendRequestForAuthenticationChallenge for SSL handling.
- Not handling connection redirects properly. Implement willSendRequest:redirectResponse:.

## Related Pages

- [objc-nsurlsession-error]({{< relref "/languages/objective-c/objc-nsurlsession-error" >}}) - URLSession errors
- [objc-network-error]({{< relref "/languages/objective-c/objc-network-error" >}}) - network errors
- [objc-thread-error]({{< relref "/languages/objective-c/objc-thread-error" >}}) - threading issues
- [objc-file-error]({{< relref "/languages/objective-c/objc-file-error" >}}) - file errors
