---
title: "[Solution] Spring WebSocket Error"
description: "Fix Spring WebSocket errors when STOMP or SockJS connections fail or messages are not delivered."
frameworks: ["spring"]
error-types: ["connection-error"]
severities: ["error"]
---

WebSocket errors in Spring occur when STOMP message broker configuration is incorrect, connections are rejected, or message routing fails.

## Common Causes

- STOMP broker not configured
- Message broker URL incorrect
- Client connects with wrong protocol
- CORS not configured for WebSocket origin
- Message destination does not match any @MessageMapping

## How to Fix

### Configure WebSocket with STOMP

```java
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic", "/queue");
        config.setApplicationDestinationPrefixes("/app");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws")
            .setAllowedOrigins("*")
            .withSockJS();
    }
}
```

### Handle WebSocket Messages

```java
@Controller
public class ChatController {
    @MessageMapping("/chat.send")
    @SendTo("/topic/messages")
    public ChatMessage sendMessage(ChatMessage message) {
        return message;
    }

    @MessageMapping("/chat.join")
    @SendTo("/topic/chatroom")
    public ChatMessage join(ChatMessage message) {
        message.setType(MessageType.JOIN);
        return message;
    }
}
```

### Handle WebSocket Errors

```java
@Component
public class WebSocketErrorHandler implements WebSocketHandler {
    @Override
    public void afterConnectionEstablished(WebSocketSession session) {
        log.info("Connected: {}", session.getId());
    }

    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) {
        log.info("Disconnected: {} - {}", session.getId(), status);
    }

    @Override
    public void handleTransportError(WebSocketSession session, Throwable exception) {
        log.error("Transport error: {}", session.getId(), exception);
    }
}
```

## Examples

```java
// Bug -- missing destination prefix
@MessageMapping("send")  // Should be "/app/send"
public void handleMessage(String message) {
    // Never reached
}

// Fix -- add prefix
@MessageMapping("/send")
public void handleMessage(String message) {
    messagingTemplate.convertAndSend("/topic/receive", message);
}
```
