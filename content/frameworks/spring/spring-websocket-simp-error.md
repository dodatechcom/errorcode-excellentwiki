---
title: "[Solution] Spring WebSocket SIMP Error"
description: "Fix Spring WebSocket SIMP messaging errors when Simple Messaging Protocol operations fail."
frameworks: ["spring"]
error-types: ["connection-error"]
severities: ["error"]
---

SIMP messaging errors occur when the Simple Message Protocol configuration is incorrect, causing message delivery failures.

## Common Causes

- SIMP message converter not configured
- Message size exceeds limits
- Broker does not support SIMP protocol
- Client subscribes to wrong destination
- Authentication not configured for broker

## How to Fix

### Configure SIMP Message Converter

```java
@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry registry) {
        registry.enableSimpleBroker("/topic", "/queue");
        registry.setApplicationDestinationPrefixes("/app");
        registry.setUserDestinationPrefix("/user");
    }

    @Override
    public void configureMessageConverters(List<MessageConverter> messageConverters) {
        messageConverters.add(new MappingJackson2MessageConverter());
    }
}
```

### Configure Authentication for Broker

```java
@Override
public void configureClientInboundChannel(ChannelRegistration registration) {
    registration.interceptors(new ChannelInterceptor() {
        @Override
        public Message<?> preSend(Message<?> message, Channel channel) {
            MessageHeaders headers = new MessageHeaders(message);
            if (headers.get(SimpMessagingTemplateAccessorHeadersAccessor.SESSION_ID) != null) {
                // Validate user authentication
            }
            return message;
        }
    });
}
```

## Examples

```java
// Bug -- no message converter
// JSON messages not deserialized

// Fix -- add converter
@Override
public void configureMessageConverters(List<MessageConverter> converters) {
    converters.add(new MappingJackson2MessageConverter());
}
```
