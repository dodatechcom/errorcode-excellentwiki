---
title: "SessionCreationException - Spring Session"
description: "Spring Session throws SessionCreationException when it cannot create or persist an HTTP session"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Spring Session fails to create or save an HTTP session. It typically indicates issues with the session store or configuration.

## Common Causes

- Session store (Redis, JDBC) is unavailable
- Session cookie configuration is invalid
- Session serialization fails (e.g., non-serializable objects stored)
- Maximum session limit reached
- Session ID conflict or cookie domain mismatch

## How to Fix

1. Configure Spring Session with Redis:

```yaml
spring:
  session:
    store-type: redis
    timeout: 1800
    redis:
      namespace: spring:session
  redis:
    host: localhost
    port: 6379
```

2. Store only serializable objects in session:

```java
// Bad -- non-serializable object
session.setAttribute("user", new User()); // User not Serializable

// Good -- store only the ID
session.setAttribute("userId", user.getId());
```

3. Configure session cookie properly:

```java
@Bean
public CookieSerializer cookieSerializer() {
    DefaultCookieSerializer serializer = new DefaultCookieSerializer();
    serializer.setCookieName("SESSIONID");
    serializer.setCookiePath("/");
    serializer.setDomainName("example.com");
    serializer.setUseHttpOnlyCookie(true);
    return serializer;
}
```

## Examples

```java
// Redis session store is down
httpSession.setAttribute("cart", cartItems);
// SessionCreationException: Unable to create session -- Redis connection refused
```

## Related Errors

- [Session error (Spring)]({{< relref "/frameworks/spring/session-error" >}})
- [Cache error]({{< relref "/frameworks/spring/cache-error" >}})
