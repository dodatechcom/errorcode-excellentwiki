---
title: "[Solution] Spring WebSocket STOMP Error"
description: "Fix Spring WebSocket STOMP errors when STOMP frames fail to parse or message routing fails."
frameworks: ["spring"]
error-types: ["connection-error"]
severities: ["error"]
---

STOMP errors occur when STOMP frame parsing fails, subscriptions are incorrect, or message broker cannot route messages.

## Common Causes

- STOMP frame malformed
- Subscription destination does not match broker configuration
- Message size exceeds STOMP frame limit
- Broker not configured for STOMP
- Client disconnects during STOMP handshake

## How to Fix

### Configure STOMP Broker

```java
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry registry) {
        registry.enableSimpleBroker("/topic", "/queue")
            .setHeartbeatValue(new long[]{10000, 10000});
        registry.setApplicationDestinationPrefixes("/app");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws")
            .setAllowedOrigins("*")
            .withSockJS();
    }

    @Override
    public void configureWebSocketTransport(WebSocketTransportRegistration registry) {
        registry.setMessageSizeLimit(128 * 1024);
        registry.setSendBufferSizeLimit(512 * 1024);
        registry.setSendTimeLimit(20 * 1000);
    }
}
```

### Handle STOMP Errors

```java
@Controller
public class StompController {
    @MessageMapping("/send")
    @SendTo("/topic/messages")
    public Message sendMessage(Message message) {
        return message;
    }

    @MessageExceptionHandler
    @SendToUser("/queue/errors")
    public ErrorMessage handleException(Exception e) {
        return new ErrorMessage(e.getMessage());
    }
}
```

## Examples

```java
// Bug -- no heartbeat configured
registry.enableSimpleBroker("/topic");

// Fix -- add heartbeat
registry.enableSimpleBroker("/topic")
    .setHeartbeatValue(new long[]{10000, 10000});
```

Client should send heartbeats to detect disconnection:
```javascript
const socket = new SockJS('/ws');
const stompClient = Stomp.over(socket);
stompClient.heartbeat.outgoing = 10000;
stompClient.heartbeat.incoming = 10000;
```
