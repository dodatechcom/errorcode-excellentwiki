---
title: "WebView SSL Error"
description: "Fix WebView SSL certificate errors and HTTPS loading issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
WebView fails to load HTTPS pages because of SSL certificate issues

## Common Causes

- onReceivedSslError not properly handled
- Self-signed certificate not accepted
- SSL error callback not implemented
- Should not call proceed() on SSL error in production

## Fixes

- Implement onReceivedSslError to show error page
- Do not call handler.proceed() in production
- Use network security config for custom certificates
- Handle certificate errors gracefully

## Code Example

```kotlin
 webView.webViewClient = object : WebViewClient() {
    override fun onReceivedSslError(
        view: WebView, handler: SslErrorHandler, error: SslError
    ) {
        // Show error dialog, NEVER call handler.proceed() in production!
        handler.cancel()
        showErrorPage("SSL certificate error")
    }
}
```

# NEVER call handler.proceed() in production
# Use network_security_config for trusted certificates
# Show user-friendly error page for SSL issues
