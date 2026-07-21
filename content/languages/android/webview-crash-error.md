---
title: "WebView Crash Error"
description: "Fix WebView crash and out-of-memory errors in Android applications"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
WebView crashes with out-of-memory or unexpected exceptions

## Common Causes

- WebView memory leak from Activity reference
- Multiple WebViews sharing same process
- Large page with many images consuming memory
- WebView not properly destroyed on Activity exit

## Fixes

- Destroy WebView in onDestroy
- Use application context for WebView initialization
- Clear cache and history on destruction
- Set WebView to hardware accelerated

## Code Example

```kotlin
override fun onDestroy() {
    binding.webView.apply {
        stopLoading()
        clearHistory()
        clearCache(true)
        loadUrl("about:blank")
        removeAllViews()
        destroy()
    }
    super.onDestroy()
}

// For memory issues:
webView.settings.cacheMode = WebSettings.LOAD_NO_CACHE
webView.setLayerType(View.LAYER_TYPE_SOFTWARE, null)
```

# Always destroy WebView in onDestroy
# Clear cache to free memory
# Use application context if possible
