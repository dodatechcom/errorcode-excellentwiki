---
title: "[Solution] Spring WebSocket Handler Error"
description: "Fix Spring WebSocket handler errors when WebSocket connections fail or message handlers throw exceptions."
frameworks: ["spring"]
error-types: ["connection-error"]
severities: ["error"]
---

WebSocket handler errors occur when the WebSocket handler does not properly manage connections, sessions, or message processing.

## Common Causes

- Handler not registered with WebSocket handler registry
- Session management not implemented
- Binary message handling not configured
- Exception not caught in handler
- Handler does not close connection properly

## How to Fix

### Register WebSocket Handler

```java
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(chatHandler(), "/ws/chat")
            .setAllowedOrigins("*");
    }

    @Bean
    public ChatWebSocketHandler chatHandler() {
        return new ChatWebSocketHandler();
    }
}
```

### Implement WebSocket Handler

```java
@Component
public class ChatWebSocketHandler extends TextWebSocketHandler {
    private final Map<String, WebSocketSession> sessions = new ConcurrentHashMap<>();

    @Override
    public void afterConnectionEstablished(WebSocketSession session) {
        sessions.put(session.getId(), session);
        log.info("Connected: {}", session.getId());
    }

    @Override
    protected void handleTextMessage(WebSocketSession session, TextMessage message) {
        for (WebSocketSession s : sessions.values()) {
            try {
                s.sendMessage(message);
            } catch (IOException e) {
                log.error("Failed to send message", e);
            }
        }
    }

    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) {
        sessions.remove(session.getId());
        log.info("Disconnected: {}", session.getId());
    }

    @Override
    public void handleTransportError(WebSocketSession session, Throwable exception) {
        log.error("Transport error: {}", session.getId(), exception);
        sessions.remove(session.getId());
    }
}
```

### Handle Binary Messages

```java
@Override
protected void handleBinaryMessage(WebSocketSession session, BinaryMessage message) {
    byte[] payload = message.getPayload().array();
    // Process binary data
}
```

## Examples

```java
// Bug -- no error handling in handler
@Override
protected void handleTextMessage(WebSocketSession session, TextMessage message) {
    session.sendMessage(new TextMessage("Echo: " + message.getPayload()));
    // IOException not caught
}

// Fix -- add error handling
@Override
protected void handleTextMessage(WebSocketSession session, TextMessage message) {
    try {
        session.sendMessage(new TextMessage("Echo: " + message.getPayload()));
    } catch (IOException e) {
        log.error("Failed to send message", e);
    }
}
```
