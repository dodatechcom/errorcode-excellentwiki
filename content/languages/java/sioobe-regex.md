---
title: "[Solution] Java StringIndexOutOfBoundsException — requesting regex group index that doesn't exist in pattern"
description: "Fix Java StringIndexOutOfBoundsException when requesting regex group index that doesn't exist in pattern with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# StringIndexOutOfBoundsException — requesting regex group index that doesn't exist in pattern

A `StringIndexOutOfBoundsException` occurs when Pattern p = Pattern.compile("(\\w+)@(\\w+\\.\\w+)");
Matcher m = p.matcher("alice@example.com");
String domain = m.group(3);  // SIOOBE — only 2 groups.

## Common Causes

```java
Pattern p = Pattern.compile("(\\w+)@(\\w+\\.\\w+)");
Matcher m = p.matcher("alice@example.com");
String domain = m.group(3);  // SIOOBE — only 2 groups
```

## Solutions

```java
// Fix: check group count
if (m.find() && m.groupCount() >= 2) { String domain = m.group(2); }

// Fix: named groups
Pattern p = Pattern.compile("(?<user>\\w+)@(?<domain>\\w+\\.\\w+)");
Matcher m = p.matcher("alice@example.com");
if (m.find()) { String domain = m.group("domain"); }
```

## Prevention Checklist

- Verify groupCount() before accessing.
- Use named groups instead of numeric.
- Handle optional groups.

## Related Errors

IndexOutOfBoundsException, PatternSyntaxException
