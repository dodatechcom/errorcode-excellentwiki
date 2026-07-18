---
title: "[Solution] Groovy JsonSlurper Parse Error"
description: "Fix Groovy JsonSlurper parse errors. Handle malformed JSON, encoding issues, and parsing configuration."
languages: ["groovy"]
error-types: ["parse-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `JsonSlurper` parse error occurs when Groovy cannot parse a JSON string due to syntax errors, encoding problems, or unexpected data formats. The JSON does not conform to the JSON specification.

## Why It Happens

- Malformed JSON with trailing commas: The JSON has commas after the last element in arrays or objects.
- Single quotes used instead of double quotes: JSON requires double quotes for strings.
- Unescaped special characters in strings: Characters like quotes and backslashes must be escaped.
- Unicode encoding issues in JSON content: The JSON contains non-ASCII characters with wrong encoding.
- JSON content is actually HTML or plain text: The input is not valid JSON at all.

## How to Fix It

Validate JSON before parsing:

```groovy
import groovy.json.JsonSlurper
import groovy.json.JsonException

def jsonText = '{"name": "Alice", "age": 30}'

try {
    def slurper = new JsonSlurper()
    def result = slurper.parseText(jsonText)
    println result.name
} catch (JsonException e) {
    println "Invalid JSON: ${e.message}"
}
```

Fix common JSON formatting issues:

```groovy
// WRONG: Single quotes
def badJson = "{'name': 'Alice'}"

// CORRECT: Double quotes
def goodJson = '{"name": "Alice"}'

// Or use JsonSlurper with lenient mode
def slurper = new groovy.json.JsonSlurper()
slurper.setAllowSingleQuotes(true)
def result = slurper.parseText(badJson)
```

Handle encoding issues:

```groovy
def bytes = "data".getBytes("UTF-8")
def jsonText = new String(bytes, "UTF-8")
def result = new JsonSlurper().parseText(jsonText)
```

Use type-safe parsing with null checks:

```groovy
def slurper = new JsonSlurper()
def result = slurper.parseText(jsonText)
if (result instanceof Map) {
    def name = result.name ?: "Unknown"
    def age = result.age ?: 0
    def items = result.items ?: []
}
```

Use different slurper modes for different use cases:

```groovy
// For large files
def parser = new groovy.json.JsonSlurper().setType(groovy.json.JsonSlurperType.INDEX_OVERLAY)

// For lenient parsing
def parser = new groovy.json.JsonSlurper()
parser.setAllowSingleQuotes(true)
parser.setAllowUnquotedObjectKeys(true)
```

## Common Mistakes

- Not trimming whitespace before parsing. Leading/trailing whitespace can cause issues.
- Forgetting to handle nested null values. Use the Elvis operator for defaults.
- Using wrong JsonSlurper mode for large files. INDEX_OVERLAY is more memory-efficient.
- Not handling BOM markers in UTF-8 files. Strip BOM before parsing.
- Not closing the slurper when done. While not strictly required, it is good practice.

## Related Pages

- [groovy-xml-parse-error]({{< relref "/languages/groovy/groovy-xmlparseerror-v2" >}}) - XML parse error
- [groovy-io-error]({{< relref "/languages/groovy/groovy-io-error" >}}) - I/O exception
- [groovy-null-pointer-v2]({{< relref "/languages/groovy/groovy-nullpointererror-v2" >}}) - null pointer
- [groovy-missing-property-v2]({{< relref "/languages/groovy/groovy-missingproperty-v2" >}}) - missing property
