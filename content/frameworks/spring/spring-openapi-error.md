---
title: "[Solution] Spring OpenAPI Error"
description: "Fix Spring OpenAPI errors when Swagger UI fails to load or API documentation is incorrectly generated."
frameworks: ["spring"]
error-types: ["documentation-error"]
severities: ["error"]
---

OpenAPI errors occur when the Swagger UI does not load, API documentation is incomplete, or the OpenAPI specification is malformed.

## Common Causes

- SpringDoc or Swagger dependency not in classpath
- OpenAPI configuration not properly defined
- API models not annotated correctly
- CORS blocks Swagger UI access
- Version mismatch between SpringDoc and Spring Boot

## How to Fix

### Add SpringDoc Dependency

```xml
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.3.0</version>
</dependency>
```

### Configure OpenAPI

```java
@Configuration
public class OpenApiConfig {
    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
            .info(new Info()
                .title("My API")
                .version("1.0.0")
                .description("API documentation")
            );
    }
}
```

### Annotate Controllers

```java
@RestController
@RequestMapping("/api/users")
@Tag(name = "Users", description = "User management endpoints")
public class UserController {
    @GetMapping("/{id}")
    @Operation(summary = "Get user by ID", description = "Returns a single user")
    @ApiResponse(responseCode = "200", description = "User found")
    @ApiResponse(responseCode = "404", description = "User not found")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        return ResponseEntity.ok(userService.getUser(id));
    }
}
```

### Access Swagger UI

```
http://localhost:8080/swagger-ui.html
http://localhost:8080/swagger-ui/index.html
http://localhost:8080/v3/api-docs
```

## Examples

```java
// Bug -- missing annotations
@RestController
public class UserController {
    @GetMapping("/users/{id}")
    public User getUser(@PathVariable Long id) {
        return userService.getUser(id);
    }
}

// Fix -- add OpenAPI annotations
@RestController
@Tag(name = "Users")
public class UserController {
    @GetMapping("/users/{id}")
    @Operation(summary = "Get user")
    public User getUser(@PathVariable Long id) {
        return userService.getUser(id);
    }
}
```
