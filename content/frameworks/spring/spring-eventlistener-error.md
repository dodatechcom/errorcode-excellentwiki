---
title: "[Solution] Spring EventListener Error"
description: "Event not being handled."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Event not being handled.

## Common Causes

Listener not registered.

## How to Fix

Add @EventListener.

## Example

```java
@Component
public class Handler {
    @EventListener
    public void handle(UserCreatedEvent e) { /* process */ }
}
```
