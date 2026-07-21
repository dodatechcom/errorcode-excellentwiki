---
title: "WebView JavaScript Interface Error"
description: "Fix Android WebView JavaScript interface errors and security vulnerabilities"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
WebView JavaScript bridge does not work or poses security risk

## Common Causes

- @JavascriptInterface annotation missing
- JavaScript not enabled in WebView settings
- Interface object not added to WebView
- API 17+ requires @JavascriptInterface for security

## Fixes

- Add @JavascriptInterface to bridge methods
- Enable JavaScript with settings.javaScriptEnabled = true
- Add interface with addJavascriptInterface()
- Use @JavascriptInterface on all exposed methods

## Code Example

```kotlin
val webView = binding.webView
webView.settings.javaScriptEnabled = true

class WebAppInterface {
    @JavascriptInterface
    fun showToast(message: String) {
        Toast.makeText(context, message, Toast.LENGTH_SHORT).show()
    }
}

webView.addJavascriptInterface(WebAppInterface(), "Android")

// In JavaScript:
// Android.showToast("Hello from web!")
```

# Always use @JavascriptInterface (required API 17+)
# Never expose sensitive methods to JavaScript
# Validate all inputs from JavaScript
