---
title: "[Solution] spring RabbitMQ Listener Error"
description: "Listener not receiving."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Listener not receiving.

## Common Causes

Wrong queue.

## How to Fix

Check queue name.

## Example

```java
@RabbitListener(queues = "my-queue")
public void receive(String msg) { /* handle */ }
```
