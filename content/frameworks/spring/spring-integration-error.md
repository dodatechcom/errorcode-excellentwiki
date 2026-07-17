---
title: "MessageHandlingException - Spring Integration"
description: "Spring Integration throws MessageHandlingException when a message handler fails to process a message"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a Spring Integration message handler throws an exception while processing a message. It wraps the original exception in a `MessageHandlingException`.

## Common Causes

- Handler throws a RuntimeException during processing
- Message payload type does not match expected type
- Channel is not connected to a consumer
- Message transformation fails
- Handler bean is not properly configured

## How to Fix

1. Add error handling to integration flows:

```java
@Bean
public IntegrationFlow orderFlow() {
    return IntegrationFlow.from("orderChannel")
        .handle(message -> {
            try {
                processOrder(message.getPayload());
            } catch (Exception e) {
                throw new MessageHandlingException(message, "Order processing failed", e);
            }
        })
        .get();
}
```

2. Configure error channel and error handler:

```java
@Bean
public IntegrationFlow errorFlow() {
    return IntegrationFlow.from("errorChannel")
        .handle(message -> {
            log.error("Integration error: {}", message.getPayload());
        })
        .get();
}
```

3. Use `@ServiceActivator` with error handling:

```java
@ServiceActivator(inputChannel = "orders", outputChannel = "processed")
public Order processOrder(Order order) {
    // Process and return
    return processedOrder;
}
```

## Examples

```java
// Type mismatch in payload
@Transformer(inputChannel = "raw", outputChannel = "processed")
public ProcessedOrder transform(String raw) {
    return objectMapper.readValue(raw, ProcessedOrder.class);
}
// MessageHandlingException: Failed to convert message payload
```

## Related Errors

- [Batch error]({{< relref "/frameworks/spring/spring-batch-error" >}})
- [AMQP error]({{< relref "/frameworks/spring/spring-amqp-error" >}})
