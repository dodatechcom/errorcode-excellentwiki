---
title: "[Solution] Java NullPointerException"
description: "Deserialization Null Fields"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# fields expected non-null are null after JSON or Java deserialization

A `fields` is thrown when user user = objectmapper.readvalue(json, user.class);.

## Common Causes

```java
User user = objectMapper.readValue(json, User.class);
user.email.length();  // NPE if email not in JSON
```

## Solutions

```java
// Fix: @JsonProperty defaults
@JsonProperty(defaultValue="") private String email;

// Fix: @JsonSetter with null handling
@JsonSetter("email")
public void setEmail(String e) { this.email = e != null ? e : ""; }

// Fix: Optional for deserialized fields
@JsonIgnore public Optional<String> getEmailOpt() { return Optional.ofNullable(email); }
```

## Prevention Checklist

- Null-check fields after deserialization.
- Use @JsonProperty(defaultValue=...) for optional fields.
- Write tests for deserialization with missing fields.

## Related Errors

[NullPointerException](nullpointerexception), [InvalidClassException](invalidclassexception)
