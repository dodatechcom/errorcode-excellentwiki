---
title: "OkHttp Proxy Error"
description: "Fix OkHttp proxy configuration errors for corporate network environments"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
OkHttp requests fail when using proxy servers in corporate environments

## Common Causes

- Proxy host and port misconfigured
- Proxy authentication not provided
- SOCKS proxy vs HTTP proxy confusion
- Proxy bypass list incorrect

## Fixes

- Configure proxy with Proxy class
- Add Authenticator for proxy credentials
- Use correct proxy type: HTTP or SOCKS
- Set proxySelector for complex routing

## Code Example

```kotlin
val proxy = Proxy(Proxy.Type.HTTP, InetSocketAddress("proxy.company.com", 8080))

val client = OkHttpClient.Builder()
    .proxy(proxy)
    .proxyAuthenticator { route, response ->
        val credential = Credentials.basic("username", "password")
        response.request.newBuilder()
            .header("Proxy-Authorization", credential)
            .build()
    }
    .build()
```

# For system proxy:
val client = OkHttpClient.Builder()
    .proxy(ProxySelector.getDefault())
    .build()
