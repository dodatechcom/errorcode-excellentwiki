---
title: "[Solution] Spring Error Attributes Error"
description: "Fix Spring error attributes errors when custom error information is not properly exposed in error responses."
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
---

Error attributes errors occur when the default error response does not include enough information or custom error attributes are not registered.

## Common Causes

- `ErrorController` not customized
- Default error attributes not extended
- Stack trace exposed in production
- Error path not configured correctly
- `server.error.include-message` not enabled

## How to Fix

### Customize Error Attributes

```java
@Component
public class CustomErrorAttributes extends DefaultErrorAttributes {
    @Override
    public Map<String, Object> getErrorAttributes(WebRequest webRequest, ErrorAttributeOptions options) {
        Map<String, Object> errorAttributes = super.getErrorAttributes(webRequest, options);
        errorAttributes.put("timestamp", LocalDateTime.now());
        errorAttributes.put("customMessage", "Something went wrong");
        return errorAttributes;
    }
}
```

### Configure Error Exposure

```yaml
# application.yml
server:
  error:
    include-message: always
    include-binding-errors: always
    include-stacktrace: never  # Never expose in production
    include-exception: true
```

### Custom Error Controller

```java
@Controller
public class CustomErrorController implements ErrorController {
    @RequestMapping("/error")
    @ResponseBody
    public ResponseEntity<Map<String, Object>> handleError(HttpServletRequest request) {
        Integer statusCode = (Integer) request.getAttribute(RequestDispatcher.ERROR_STATUS_CODE);
        String message = (String) request.getAttribute(RequestDispatcher.ERROR_MESSAGE);

        Map<String, Object> body = new HashMap<>();
        body.put("status", statusCode);
        body.put("message", message != null ? message : "Unknown error");
        body.put("timestamp", LocalDateTime.now());

        return ResponseEntity.status(statusCode != null ? statusCode : 500).body(body);
    }
}
```

## Examples

```yaml
# Bug -- no error details exposed
server:
  error:
    include-message: never
    include-stacktrace: never

# Fix -- enable error details (development only)
server:
  error:
    include-message: always
    include-stacktrace: on_param
```
