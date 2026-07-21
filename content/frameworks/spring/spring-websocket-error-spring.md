---
title: "[Solution] Spring WebSocket Error Spring"
description: "WebSocket not connecting."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

WebSocket not connecting.

## Common Causes

Wrong config.

## How to Fix

Configure handler.

## Example

```java
@Configuration @EnableWebSocket
public class WSConfig implements WebSocketConfigurer {
    public void registerWebSocketHandlers(WebSocketHandlerRegistry r) {
        r.addHandler(myHandler(), "/ws");
    }
}
```
