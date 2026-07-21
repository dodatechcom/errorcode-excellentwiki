---
title: "Room Embedded Type Error"
description: "Fix Room @Embedded type annotation errors for complex data structures"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room cannot store or retrieve data from embedded object fields

## Common Causes

- @Embedded class not properly annotated
- Nested embedded objects not supported
- Column name conflict with embedded fields
- TypeConverter not handling nested objects

## Fixes

- Use @Embedded on data class for composed types
- Flatten deeply nested objects into table
- Use columnPrefix to avoid name conflicts
- Create separate tables for complex relationships

## Code Example

```kotlin
data class Address(
    val street: String,
    val city: String,
    val zip: String
)

@Entity
data class User(
    @PrimaryKey val id: Long,
    val name: String,
    @Embedded(prefix = "addr_") val address: Address
)
// Creates columns: addr_street, addr_city, addr_zip
```

# @Embedded flattens object fields into table
# Use columnPrefix to avoid name conflicts
# Max nesting depth: keep it simple
