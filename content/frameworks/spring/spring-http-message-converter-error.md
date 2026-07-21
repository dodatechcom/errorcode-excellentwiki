---
title: "[Solution] Spring HTTP Message Converter Error"
description: "Fix Spring HTTP message converter errors when request/response body conversion fails."
frameworks: ["spring"]
error-types": ["serialization-error"]
severities: ["error"]
---

HTTP message converter errors occur when Spring cannot convert request or response bodies between Java objects and HTTP content.

## Common Causes

- Content-Type header not supported by any converter
- Request body is malformed JSON
- Response object not serializable
- Missing `@RequestBody` or `@ResponseBody` annotation
- Custom media type not registered

## How to Fix

### Configure Message Converters

```java
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void configureMessageConverters(List<HttpMessageConverter<?>> converters) {
        converters.add(new MappingJackson2HttpMessageConverter());
        converters.add(new StringHttpMessageConverter());
    }
}
```

### Use Correct Annotations

```java
@RestController
public class ApiController {
    @PostMapping("/data")
    public ResponseEntity<DataResponse> createData(@RequestBody DataRequest request) {
        // @RequestBody deserializes JSON to DataRequest
        // @ResponseBody (implied by @RestController) serializes DataResponse to JSON
        DataResponse response = service.process(request);
        return ResponseEntity.ok(response);
    }
}
```

### Handle Conversion Errors

```java
@RestControllerAdvice
public class ConversionExceptionHandler {
    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<Map<String, String>> handleConversion(HttpMessageNotReadableException e) {
        return ResponseEntity.badRequest()
            .body(Map.of("error", "Invalid request body", "detail", e.getMessage()));
    }
}
```

### Register Custom Converter

```java
@Component
public class CustomCsvConverter implements HttpMessageConverter<CsvData> {
    @Override
    public boolean canRead(Class<?> clazz, MediaType mediaType) {
        return mediaType != null && mediaType.toString().equals("text/csv");
    }

    @Override
    public CsvData read(Class<? extends CsvData> clazz, HttpInputMessage inputMessage) {
        // Parse CSV
        return new CsvData();
    }

    @Override
    public void write(CsvData data, MediaType contentType, HttpOutputMessage outputMessage) {
        // Write CSV
    }
}
```

## Examples

```java
// Bug -- missing annotation
@PostMapping("/data")
public DataResponse createData(DataRequest request) {
    // request is null -- missing @RequestBody
}

// Fix -- add annotation
@PostMapping("/data")
public DataResponse createData(@RequestBody DataRequest request) {
    // request is properly deserialized
}
```
