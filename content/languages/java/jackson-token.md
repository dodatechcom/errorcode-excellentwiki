---
title: "[Solution] JsonProcessingException Unexpected Character — Jackson Token Fix"
description: "Fix JsonProcessingException when Jackson encounters unexpected characters during parsing. Handle malformed JSON input."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jackson", "json", "parsing", "unexpected-character", "token"]
weight: 5
---

# JsonProcessingException Unexpected Character — Jackson Token Fix

A `JsonProcessingException` with "Unexpected character" is thrown when Jackson encounters a character that is not valid at that position in the JSON stream. This usually indicates malformed JSON input.

## What This Error Means

Common messages:

- `Unexpected character 'x' (code 120): expected a valid value`
- `Unexpected end-of-input within/between Object entries`

## Common Causes

```java
// Cause 1: Trailing comma
// JSON: {"name": "John", "age": 30,}

// Cause 2: Single quotes instead of double
// JSON: {'name': 'John'}  // Single quotes not valid in JSON

// Cause 3: Comments in JSON
// JSON: {"name": "John" /* comment */}

// Cause 4: Incomplete JSON
// JSON: {"name": "John"  // Missing closing brace
```

## How to Fix

### Fix 1: Validate JSON input

```java
try {
    ObjectMapper mapper = new ObjectMapper();
    User user = mapper.readValue(jsonString, User.class);
} catch (JsonProcessingException e) {
    log.error("Invalid JSON: {}", e.getOriginalMessage());
}
```

### Fix 2: Use lenient parser

```java
ObjectMapper mapper = new ObjectMapper();
mapper.configure(JsonParser.Feature.ALLOW_COMMENTS, true);
mapper.configure(JsonParser.Feature.ALLOW_SINGLE_QUOTES, true);
mapper.configure(JsonParser.Feature.ALLOW_TRAILING_COMMA, true);
```

### Fix 3: Pre-process JSON

```java
String cleanJson = jsonString
    .replaceAll("//.*$", "")
    .replaceAll("/\\*.*?\\*/", "")
    .replaceAll(",\\s*([}\\]])", "$1");
```

## Related Errors

- {{< relref "jackson-deserialization" >}} — MismatchedInputException
- {{< relref "jackson-unknown" >}} — UnrecognizedPropertyException
- {{< relref "jackson-incomplete" >}} — IncompleteReadWithSourceException
