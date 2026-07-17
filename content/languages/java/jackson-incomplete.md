---
title: "[Solution] IncompleteReadWithSourceException — Jackson Fix"
description: "Fix IncompleteReadWithSourceException when Jackson encounters incomplete JSON input. Ensure complete JSON before parsing."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jackson", "json", "incomplete-read", "truncated", "parsing"]
weight: 5
---

# IncompleteReadWithSourceException — Jackson Fix

An `IncompleteReadWithSourceException` is thrown when Jackson encounters an incomplete JSON stream. This typically happens when the input stream is truncated or closed before the full JSON is read.

## What This Error Means

Common message:

- `Unexpected end-of-input: expected closing quote`

## Common Causes

```java
// Cause 1: Truncated response body
InputStream is = response.getBody();
User user = objectMapper.readValue(is, User.class);
// Response body incomplete

// Cause 2: Stream closed before full read
try (InputStream is = new FileInputStream("file.json")) {
    User user = objectMapper.readValue(is, User.class);
}
// File was being written while reading
```

## How to Fix

### Fix 1: Ensure complete input

```java
String jsonString = getFullResponseFromServer();
User user = objectMapper.readValue(jsonString, User.class);
```

### Fix 2: Add input validation

```java
try {
    User user = objectMapper.readValue(inputStream, User.class);
} catch (IncompleteReadWithSourceException e) {
    log.error("Incomplete JSON input: {}", e.getMessage());
    throw new DataParsingException("Received incomplete data from server");
}
```

### Fix 3: Use buffered reading

```java
String responseBody = new String(inputStream.readAllBytes(), StandardCharsets.UTF_8);
User user = objectMapper.readValue(responseBody, User.class);
```

## Related Errors

- {{< relref "jackson-token" >}} — JsonProcessingException: Unexpected character
- {{< relref "jackson-deserialization" >}} — MismatchedInputException
