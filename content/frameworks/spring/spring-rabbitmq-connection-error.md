---
title: "[Solution] spring RabbitMQ Connection Error"
description: "RabbitMQ not connecting."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

RabbitMQ not connecting.

## Common Causes

Wrong host/port.

## How to Fix

Check connection.

## Example

```java
@Bean
public ConnectionFactory cf() {
    CachingConnectionFactory f = new CachingConnectionFactory("localhost");
    return f;
}
```
