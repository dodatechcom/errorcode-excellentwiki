---
title: "No mapping found for HTTP request"
description: "Spring MVC logs this warning when no controller handler method matches the incoming HTTP request URL."
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["spring-mvc", "routing", "request-mapping", "controllers"]
weight: 5
---

This error occurs when Spring MVC receives an HTTP request but cannot find a `@RequestMapping`, `@GetMapping`, `@PostMapping`, or similar annotation that matches the request URL and method. The server returns a 404 with this warning in the logs.

## Common Causes

- The URL in the browser or client does not match the `@RequestMapping` path exactly (missing leading slash, wrong case)
- The controller class is missing `@RestController` or `@Controller` annotation
- The HTTP method does not match (e.g. POST request to a `@GetMapping` endpoint)
- The request mapping is on a method but the class-level mapping prefix was changed or removed

## How to Fix

Verify your request mapping annotations match the URL you are calling:

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    @GetMapping("/{id}")
    public User getUser(@PathVariable Long id) {
        return userService.findById(id);
    }
}

// GET /api/users/1  → matches
// GET /api/user/1   → no mapping found (singular vs plural)
```

Enable debug logging to see all registered mappings on startup:

```properties
logging.level.org.springframework.web=DEBUG
```

## Example

```java
@RestController
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello, World!";
    }
}

// Request to GET /Hello → No mapping found (case-sensitive)
```

```text
WARNING: No mapping found for HTTP request URI [/Hello] in DispatcherServlet
```

## Related Errors

- [No qualifying bean of type 'X']({{< relref "/frameworks/spring/bean-not-found" >}})
