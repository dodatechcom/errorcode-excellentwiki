---
title: "[Solution] Java URISyntaxException — URI Parsing Fix"
description: "Fix Java URISyntaxException by validating URI format, encoding special characters, using URI.create() for validation, and checking for illegal characters."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# URISyntaxException — URI Parsing Fix

A `URISyntaxException` is thrown when a string cannot be parsed as a URI. This occurs when the string contains characters that are illegal in URIs, has a malformed structure, or violates the URI syntax rules defined in RFC 2396.

## Description

The `java.net.URISyntaxException` extends `Exception` (checked exception) and is thrown by `URI` constructors when the input string does not conform to URI syntax. Unlike `MalformedURLException` which extends `IOException`, `URISyntaxException` is thrown during parsing, not during network operations.

Common message variants:

- `java.net.URISyntaxException: Illegal character in path at index [N]`
- `java.net.URISyntaxException: Expected scheme name at index [N]`
- `java.net.URISyntaxException: Unterminated authority`
- `java.net.URISyntaxException: Illegal character in query at index [N]`

Class hierarchy:

```
java.lang.Object
  └── java.lang.Throwable
        └── java.lang.Exception
              └── java.net.URISyntaxException
```

## Common Causes

```java
// Cause 1: Illegal characters in URI path
URI uri = new URI("http://example.com/path with spaces/file");  // URISyntaxException

// Cause 2: Missing scheme (protocol)
URI uri = new URI("example.com/api");  // URISyntaxException: Expected scheme name

// Cause 3: Unencoded special characters in query string
URI uri = new URI("http://example.com/search?q=hello world&lang=java");  // Space is illegal

// Cause 4: Invalid characters in host
URI uri = new URI("http://exam ple.com/api");  // URISyntaxException: Illegal character

// Cause 5: Unclosed brackets or quotes
URI uri = new URI("http://example.com/path[unclosed");  // URISyntaxException
```

## Solutions

### Fix 1: Use URI.create() for quick validation

```java
// Wrong — URISyntaxException must be caught or declared
try {
    URI uri = new URI("http://example.com/api");
} catch (URISyntaxException e) {
    e.printStackTrace();
}

// Correct — URI.create() throws IllegalArgumentException (unchecked)
try {
    URI uri = URI.create("http://example.com/api");
    URL url = uri.toURL();
} catch (IllegalArgumentException e) {
    System.err.println("Invalid URI: " + e.getMessage());
}

// Note: URI.create() is convenient but wraps the exception in IllegalArgumentException
```

### Fix 2: Encode special characters before creating URI

```java
// Wrong — spaces and special characters are illegal
URI uri = new URI("http://example.com/search?q=hello world");

// Correct — encode special characters
String query = URLEncoder.encode("hello world", StandardCharsets.UTF_8);
URI uri = new URI("http", null, "example.com", -1, "/search", "q=" + query, null);

// Or encode the entire path
String path = URLEncoder.encode("/path with spaces/file", StandardCharsets.UTF_8);
URI uri = new URI("http", null, "example.com", -1, path, null, null);
```

### Fix 3: Use multi-argument URI constructor for proper encoding

```java
// The multi-argument constructor handles encoding automatically
URI uri = new URI(
    "http",           // scheme
    null,             // userInfo
    "example.com",    // host
    -1,               // port (-1 = default)
    "/api/search",    // path
    "q=hello&lang=java",  // query
    null              // fragment
);
URL url = uri.toURL();
```

### Fix 4: Validate and sanitize user-provided URIs

```java
public URI sanitizeUri(String input) throws URISyntaxException {
    if (input == null || input.isBlank()) {
        throw new URISyntaxException(input, "URI must not be null or empty");
    }

    // Trim whitespace
    input = input.trim();

    // Add scheme if missing
    if (!input.contains("://")) {
        input = "https://" + input;
    }

    // Replace illegal characters
    input = input.replaceAll("[\\s<>#{}|\\\\^`\\[\\]]", "");

    return new URI(input);
}

// Usage
try {
    URI uri = sanitizeUri(userInput);
    URL url = uri.toURL();
} catch (URISyntaxException e) {
    System.err.println("Invalid URI: " + e.getMessage());
}
```

### Fix 5: Parse URI components separately for complex URIs

```java
// Parse complex URIs by building components step by step
public URI buildUri(String host, String path, Map<String, String> params) throws URISyntaxException {
    StringBuilder queryBuilder = new StringBuilder();
    for (Map.Entry<String, String> entry : params.entrySet()) {
        if (queryBuilder.length() > 0) {
            queryBuilder.append("&");
        }
        queryBuilder.append(URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8));
        queryBuilder.append("=");
        queryBuilder.append(URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8));
    }

    return new URI("https", null, host, -1, path, queryBuilder.toString(), null);
}
```

## Prevention Checklist

- Always encode special characters (spaces, `#`, `?`, `&`, etc.) in URI components.
- Use the multi-argument `URI` constructor to handle encoding automatically.
- Validate user-provided URIs before parsing with `URI.create()` or `new URI()`.
- Use `URLEncoder.encode()` for query parameters and path segments.
- Test URIs with edge cases including special characters, internationalized domain names, and long paths.

## Related Errors

- [MalformedURLException](../malformedurlexception) — URL string is malformed.
- [UnknownHostException](../unknownhostexception) — hostname cannot be resolved.
- [IllegalArgumentException](../illegalargumentexception) — null or empty URI string.
- [UnsupportedEncodingException](../unsupportedoperationexception) — unsupported character encoding.
