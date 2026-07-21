---
title: "Objective-C UIWebView JavaScript Bridge Error"
description: "Fix Objective-C UIWebView JavaScript bridge errors when calling native methods from JavaScript or vice versa."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- UIWebView deprecated, WKWebView should be used instead
- JavaScript bridge not registered before page loads
- StringByEvaluatingJavaScript returns nil on error
- Not running JavaScript on main thread
- Cross-origin JavaScript calls blocked

## How to Fix

```objc
// WRONG: Using deprecated UIWebView
UIWebView *webView = [[UIWebView alloc] initWithFrame:self.view.bounds];
[webView loadRequest:[NSURLRequest requestWithURL:url]];
// Deprecated since iOS 12

// CORRECT: Use WKWebView
WKWebView *webView = [[WKWebView alloc] initWithFrame:self.view.bounds];
[webView loadRequest:[NSURLRequest requestWithURL:url]];
```

```objc
// WRONG: JavaScript bridge not registered
WKWebViewConfiguration *config = [[WKWebViewConfiguration alloc] init];
WKWebView *webView = [[WKWebView alloc] initWithFrame:CGRectZero configuration:config];
[webView loadHTMLString:@"<script>webkit.messageHandlers.myHandler.postMessage('hello')</script>"
               baseURL:nil];
// myHandler not registered!

// CORRECT: Register message handler first
WKUserContentController *uc = [[WKUserContentController alloc] init];
[uc addScriptMessageHandler:self name:@"myHandler"];
config.userContentController = uc;
```

## Examples

```objc
// Example 1: WKWebView JavaScript bridge
[config.userContentController addScriptMessageHandler:self name:@"native"];

- (void)userContentController:(WKUserContentController *)userContentController
      didReceiveScriptMessage:(WKScriptMessage *)message {
    if ([message.name isEqualToString:@"native"]) {
        NSLog(@"From JS: %@", message.body);
    }
}

// Example 2: Call JavaScript from Objective-C
[webView evaluateJavaScript:@"document.title"]
    completionHandler:^(id result, NSError *error) {
        NSLog(@"Title: %@", result);
    }];

// Example 3: Inject JavaScript
NSString *js = @"document.body.style.backgroundColor = 'lightblue'";
[webView evaluateJavaScript:js completionHandler:nil];
```

## Related Errors

- [UIWebView error](objc-uikit-error) -- WebView issues
- [JavaScript error](objc-runtime-error) -- JS execution problems
