---
title: "[Solution] Java MalformedURLException — Invalid URL Format Fix"
description: "Fix Java MalformedURLException by validating URL format, using URI class for parsing, checking protocol and scheme, and encoding special characters."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# MalformedURLException — Invalid URL Format Fix

A `MalformedURLException` is thrown when a URL string is malformed and cannot be parsed. This typically occurs when the URL is missing a protocol, contains invalid characters, or has an unsupported scheme.

## Description

The `java.net.MalformedURLException` extends `IOException` and is thrown by `URL` constructors and `URL.openConnection()` when the URL string does not conform to RFC 2396. Common issues include missing protocol, invalid characters, and incorrect URL structure.

Common message variants:

- `java.net.MalformedURLException: no protocol: [URL]`
- `java.net.MalformedURLException: Unknown protocol: [protocol]`
- `java.net.MalformedURLException: For input string: "[value]"`
- `java.net.MalformedURLException: Invalid URL character`

Class hierarchy:

```
java.lang.Object
  └── java.lang.Throwable
        └── java.lang.Exception
              └── java.io.IOException
                    └── java.net.MalformedURLException
```

## Common Causes

```java
// Cause 1: Missing protocol
URL url = new URL("example.com/api");  // MalformedURLException: no protocol

// Cause 2: Unsupported protocol
URL url = new URL("ftp://example.com/file");  // May work, but custom protocols fail

// Cause 3: Invalid characters in URL
URL url = new URL("http://example.com/path with spaces/file");  // MalformedURLException

// Cause 4: Missing port number when expected
URL url = new URL("http://localhost:abc/api");  // MalformedURLException: For input string: "abc"

// Cause 5: URL constructed from user input without validation
String userInput = request.getParameter("url");
URL url = new URL(userInput);  // May throw MalformedURLException if invalid
```

## Solutions

### Fix 1: Validate URL format before creating URL object

```java
// Wrong — no validation
String urlString = userInput;
URL url = new URL(urlString);  // May throw MalformedURLException

// Correct — validate first
String urlString = userInput;
if (!urlString.matches("^https?://.*")) {
    throw new MalformedURLException("URL must start with http:// or https://");
}
URL url = new URL(urlString);
```

### Fix 2: Use URI class for better parsing and validation

```java
// Wrong — URL constructor may accept some invalid formats
URL url = new URL("http://example.com/path with spaces");

// Correct — URI provides stricter validation and encoding
try {
    URI uri = new URI("http", null, "example.com", -1, "/path with spaces", null, null);
    URL url = uri.toURL();  // Properly encoded URL
} catch (URISyntaxException e) {
    System.err.println("Invalid URI: " + e.getMessage());
}

// Or use URI.create() for validation
try {
    URI uri = URI.create("http://example.com/api");
    URL url = uri.toURL();
} catch (IllegalArgumentException e) {
    System.err.println("Invalid URL format: " + e.getMessage());
}
```

### Fix 3: Encode special characters in URL components

```java
// Wrong — special characters cause MalformedURLException
String query = "name=John Doe&city=New York";
URL url = new URL("http://example.com/search?" + query);  // Spaces are invalid

// Correct — encode query parameters
String encodedQuery = URLEncoder.encode("name=John Doe&city=New York", StandardCharsets.UTF_8);
URL url = new URL("http://example.com/search?" + encodedQuery);

// Or use URI with proper encoding
URI uri = new URI("http", null, "example.com", -1, "/search",
    "name=John Doe&city=New York", null);
URL url = uri.toURL();
```

### Fix 4: Handle user-provided URLs safely

```java
public URL parseUrl(String urlString) throws MalformedURLException {
    if (urlString == null || urlString.isBlank()) {
        throw new MalformedURLException("URL must not be null or empty");
    }

    // Trim whitespace
    urlString = urlString.trim();

    // Add protocol if missing
    if (!urlString.startsWith("http://") && !urlString.startsWith("https://")) {
        urlString = "https://" + urlString;
    }

    try {
        URI uri = new URI(urlString);
        return uri.toURL();
    } catch (URISyntaxException e) {
        throw new MalformedURLException("Invalid URL format: " + e.getMessage());
    }
}
```

### Fix 5: Validate URL components individually

```java
public boolean isValidUrl(String urlString) {
    try {
        URL url = new URL(urlString);
        // Additional validation
        String protocol = url.getProtocol();
        if (!"http".equals(protocol) && !"https".equals(protocol)) {
            return false;
        }
        String host = url.getHost();
        if (host == null || host.isEmpty()) {
            return false;
        }
        int port = url.getPort();
        if (port != -1 && (port < 1 || port > 65535)) {
            return false;
        }
        return true;
    } catch (MalformedURLException e) {
        return false;
    }
}
```

## Prevention Checklist

- Always validate URL strings before constructing `URL` objects.
- Use `URI` class for stricter parsing and proper encoding.
- Encode special characters using `URLEncoder.encode()`.
- Handle user-provided URLs with extra validation and sanitization.
- Prefer `https://` over `http://` for security.
- Test URLs with various edge cases (missing protocol, invalid ports, special characters).

## Related Errors

- [URISyntaxException](../ursisyntaxexception) — string cannot be parsed as URI.
- [UnknownHostException](../unknownhostexception) — hostname cannot be resolved.
- [ConnectException](../connectexception) — connection to URL host refused.
- [SocketException](../socketexception) — general socket error during URL connection.
