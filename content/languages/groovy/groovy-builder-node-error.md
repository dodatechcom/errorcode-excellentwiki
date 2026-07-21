---
title: "Groovy Builder Node Creation Error"
description: "Fix Groovy Builder node creation errors when building markup or object graphs with incorrect node specifications."
languages: ["groovy"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Builder node errors occur when a Builder (MarkupBuilder, ObjectGraphBuilder, etc.) cannot create the expected node due to missing factory methods, invalid attribute types, or incorrect nesting structure.

## Common Causes

- Node name does not match any registered factory or class
- Attributes provided as wrong type (String where Integer expected)
- Builder method name does not match XML tag or property name
- Self-closing tags used where child content is required
- Circular parent-child relationships in ObjectGraphBuilder

## How to Fix

```groovy
// WRONG: MarkupBuilder node with invalid nesting
def xml = new MarkupBuilder()
xml.person {
    name "Alice"    // name should be an attribute or child element
}
// produces: <person><name>Alice</name></person>

// CORRECT: Use attribute syntax
def xml = new MarkupBuilder()
xml.person(name: "Alice")  // <person name="Alice"/>
```

```groovy
// WRONG: ObjectGraphBuilder with missing factory
def builder = new ObjectGraphBuilder()
builder.person {
    address(street: "123 Main St")
}
// Error: no factory for 'address'

// CORRECT: Register class resolver
builder.classResolver = { String name ->
    Class.forName("com.example.${name.capitalize()}")
}
```

## Examples

```groovy
// Example 1: MarkupBuilder XML
def writer = new StringWriter()
def xml = new MarkupBuilder(writer)
xml.books {
    book(title: "Groovy in Action", author: "Dierk Koenig") {
        chapter("Getting Started")
        chapter("Closures")
    }
}
println writer.toString()

// Example 2: JsonBuilder
def json = new JsonBuilder()
json.person {
    name "Alice"
    age 30
    hobbies(["reading", "coding"])
}
println json.toPrettyString()

// Example 3: NodeBuilder
def nodeBuilder = new NodeBuilder()
def tree = nodeBuilder.root {
    child1("value1")
    child2("value2") {
        subChild("nested")
    }
}
```

## Related Errors

- [Builder error](groovy-builder-error) -- builder configuration issues
- [XML parse error](groovy-xml-parse-error) -- XML processing problems
