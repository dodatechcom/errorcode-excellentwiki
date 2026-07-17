---
title: "[Solution] Groovy JsonSlurper Parse Error"
description: "Fix Groovy JsonSlurper parse errors when parsing malformed JSON. Handle encoding, validation, and type issues."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["json", "parse", "jsonslurper", "malformed", "groovy"]
weight: 5
---

## What This Error Means

A JSON parse error in Groovy's JsonSlurper occurs when the JSON document is malformed, has invalid syntax, or contains characters that aren't valid JSON.

## Common Causes

- Trailing commas in JSON
- Single quotes instead of double quotes
- Unquoted keys
- Comments in JSON (not allowed)
- Invalid escape sequences

## How to Fix

```groovy
// WRONG: Trailing comma
def json = '{"name": "Alice", "age": 30,}'  // Invalid
def slurper = new JsonSlurper()
def data = slurper.parseText(json)  // Error

// CORRECT: Remove trailing comma
def json = '{"name": "Alice", "age": 30}'
def data = new JsonSlurper().parseText(json)
```

```groovy
// WRONG: Single quotes
def json = '{'name': 'Alice'}'  // Invalid JSON

// CORRECT: Use double quotes
def json = '{"name": "Alice"}'
def data = new JsonSlurper().parseText(json)
```

```groovy
// WRONG: Comments in JSON
def json = '''
{
    // This is a comment
    "name": "Alice"
}
'''

// CORRECT: Remove comments
def json = '{"name": "Alice"}'
def data = new JsonSlurper().parseText(json)
```

## Examples

```groovy
// Example 1: Safe JSON parsing
def safeParseJson(String json) {
    try {
        def slurper = new JsonSlurper()
        return slurper.parseText(json)
    } catch (Exception e) {
        println "JSON parse error: ${e.message}"
        return null
    }
}

// Example 2: JsonSlurper with options
def slurper = new JsonSlurper().setType(JsonParserType.INDEX_OVERLAY)
def data = slurper.parseText('{"key": "value"}')

// Example 3: JSON with escaped characters
def json = '{"path": "C:\\\\Users\\\\test"}'
def data = new JsonSlurper().parseText(json)
println data.path  // C:\\Users\\test
```

## Related Errors

- [groovy-xmlparseerror]({{< relref "/languages/groovy/groovy-xmlparseerror" >}}) — XML parse error
- [groovy-casterror]({{< relref "/languages/groovy/groovy-casterror" >}}) — cast error
- [groovy-missingproperty]({{< relref "/languages/groovy/groovy-missingproperty" >}}) — missing property
