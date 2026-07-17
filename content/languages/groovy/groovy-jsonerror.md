---
title: "JsonSlurper error in Groovy"
description: "Fix JsonSlurper errors when Groovy fails to parse malformed or invalid JSON content."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["json", "JsonSlurper", "parse", "malformed", "groovy"]
weight: 5
---

## What This Error Means

Groovy's `JsonSlurper` parses JSON strings and files into maps and lists. Parse errors occur when the JSON is malformed, has trailing commas, or contains invalid syntax.

## Common Causes

- Trailing commas in JSON (not valid JSON)
- Single quotes instead of double quotes
- Unquoted keys
- Comments in JSON (not valid)

## How to Fix

```groovy
// WRONG: Trailing comma
def json = '{"name": "Alice", "age": 30,}'

// CORRECT: No trailing comma
def json = '{"name": "Alice", "age": 30}'
```

```groovy
// WRONG: Single quotes for keys
def json = "{'name': 'Alice'}"

// CORRECT: Double quotes
def json = '{"name": "Alice"}'
```

## Examples

```groovy
def jsonStr = '{"name": "Alice", "scores": [95, 87, 92]}'
def parsed = new JsonSlurper().parseText(jsonStr)
println parsed.name       // Alice
println parsed.scores[0]  // 95
```

## Related Errors

- [XmlSlurper Error](/languages/groovy/xmlparseerror) - XML parsing issues
