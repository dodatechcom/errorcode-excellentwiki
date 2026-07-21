---
title: "WebView Bridge Error"
description: "Fix Android WebView bridge communication between JavaScript and native code"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Communication between WebView JavaScript and Android native code fails

## Common Causes

- WebViewClient not intercepting page navigation
- ShouldOverrideUrlLoading not returning true for custom schemes
- PostMessage not received by native code
- Callback from native to JavaScript not executing

## Fixes

- Override shouldOverrideUrlLoading for custom URL schemes
- Return true to prevent default navigation
- Use evaluateJavascript() for native-to-web calls
- Use channel API for bidirectional communication

## Code Example

```kotlin
// Intercept custom URL scheme
webView.webViewClient = object : WebViewClient() {
    override fun shouldOverrideUrlLoading(view: WebView, request: WebResourceRequest): Boolean {
        if (request.url.scheme == "myapp") {
            handleDeepLink(request.url)
            return true  // Prevent navigation
        }
        return false
    }
}

// Native to JavaScript:
webView.evaluateJavascript("javascriptFunction('data')") { result ->
    Log.d("WebView", "JS returned: $result")
}
```

# shouldOverrideUrlLoading: intercept navigation
# evaluateJavascript: call JS from native
# addJavascriptInterface: call native from JS
