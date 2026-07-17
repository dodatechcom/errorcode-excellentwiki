---
title: "[Solution] Swift WKWebView JavaScript Error Fix"
description: "Fix Swift WKWebView JavaScript errors. Learn why JavaScript execution fails and how to handle web view errors."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["wkwebview", "javascript", "webview", "swift"]
weight: 5
---

## What This Error Means

A WKWebView JavaScript error occurs when JavaScript execution fails in a WKWebView. This can happen due to JavaScript syntax errors, content security policy violations, or communication issues between Swift and JavaScript.

## Common Causes

- JavaScript syntax errors
- Content security policy blocking scripts
- Missing message handler
- Invalid JavaScript bridge calls

## How to Fix

```swift
// WRONG: Not handling JavaScript errors
webView.evaluateJavaScript("invalid code") { result, error in
    // Ignoring error
}

// CORRECT: Handle JavaScript errors
webView.evaluateJavaScript("document.title") { result, error in
    if let error = error {
        print("JavaScript error: \(error)")
    } else if let title = result as? String {
        print("Title: \(title)")
    }
}
```

```swift
// WRONG: Missing message handler
// JavaScript can't communicate with Swift

// CORRECT: Add message handler
class ViewController: UIViewController, WKScriptMessageHandler {
    func setupWebView() {
        let config = WKWebViewConfiguration()
        config.userContentController.add(self, name: "bridge")
        webView = WKWebView(frame: .zero, configuration: config)
    }

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        if message.name == "bridge" {
            print("Message from JS: \(message.body)")
        }
    }
}
```

## Examples

```swift
// Example 1: Evaluate JavaScript
webView.evaluateJavaScript("document.title") { result, error in
    guard error == nil else { return }
    if let title = result as? String {
        print("Page title: \(title)")
    }
}

// Example 2: JavaScript bridge
let script = WKUserScript(source: "window.webkit.messageHandlers.bridge.postMessage('Hello from JS')", injectionTime: .atDocumentEnd, forMainFrameOnly: true)
webView.configuration.userContentController.addUserScript(script)

// Example 3: Handle content errors
func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
    print("Navigation failed: \(error)")
}
```

## Related Errors

- [Turbo navigation error](turbo-error) — Turbo navigation error
- [Stimulus controller error](stimulus-error) — Stimulus error
- [UIKit lifecycle error](uikit-error) — UIKit error
