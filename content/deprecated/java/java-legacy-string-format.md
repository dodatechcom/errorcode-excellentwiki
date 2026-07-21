---
title: "[Solution] Deprecated Function Migration: String.format to text blocks"
description: "Migrate from verbose String.format to text blocks."
deprecated_function: "String.format with %s"
replacement_function: "Text blocks or string concatenation"
languages: ["java"]
deprecated_since: "Java 15+"
---

# [Solution] Deprecated Function Migration: String.format to text blocks

The `String.format with %s` has been deprecated in favor of `Text blocks or string concatenation`.

## Migration Guide

Text blocks are more readable.

## Before (Deprecated)

```java
String html = String.format("<html>\\n  <body>\\n    <p>%s</p>\\n  </body>\\n</html>", text);
```

## After (Modern)

```java
String html = textBlocksExample;
```

## Key Differences

- Text blocks for multi-line strings
