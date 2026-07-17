---
title: "[Solution] Hibernate Type Mapping Error Fix"
description: "Fix Hibernate type mapping errors. Resolve entity attribute type mismatches, custom type converters, and database column type conflicts."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["hibernate", "jpa", "type", "mapping", "entity"]
weight: 5
---

# Hibernate Type Mapping Error Fix

A Hibernate type mapping error occurs when the Java entity attribute type cannot be mapped to the corresponding database column type, causing persistence failures or incorrect data.

## What This Error Means

Common messages:

- `MappingException: No type discriminator value found for [entity]`
- `HibernateException: Wrong column type encountered`
- `SchemaValidationException: Wrong column type found`

Hibernate expects a specific database column type for a Java field but encounters a different type. This can happen with enums, JSON columns, date types, or custom converters.

## Common Causes

```java
// Cause 1: Enum stored as integer in DB but Hibernate expects string
@Entity
public class Task {
    @Enumerated(EnumType.STRING)  // Missing — defaults to ordinal
    private Status status;  // DB column is VARCHAR
}

// Cause 2: Date type mismatch
@Entity
public class Event {
    private LocalDateTime createdAt;  // DB column is TIMESTAMP WITH TIME ZONE
}

// Cause 3: JSON column mapped as String
@Entity
public class Config {
    private Map<String, Object> settings;  // DB column is JSONB
}
```

## How to Fix

### Fix 1: Specify enum mapping explicitly

```java
@Entity
public class Task {
    @Enumerated(EnumType.STRING)
    @Column(columnDefinition = "VARCHAR(20)")
    private Status status;
}
```

### Fix 2: Use @Convert for custom type conversion

```java
@Converter(autoApply = true)
public class JsonConverter implements AttributeConverter<Map<String, Object>, String> {
    private final ObjectMapper mapper = new ObjectMapper();

    @Override
    public String convertToDatabaseColumn(Map<String, Object> attribute) {
        try {
            return mapper.writeValueAsString(attribute);
        } catch (Exception e) {
            throw new IllegalArgumentException("Error converting to JSON");
        }
    }

    @Override
    public Map<String, Object> convertToEntityAttribute(String dbData) {
        try {
            return mapper.readValue(dbData, new TypeReference<>() {});
        } catch (Exception e) {
            throw new IllegalArgumentException("Error parsing JSON");
        }
    }
}

@Entity
public class Config {
    @Convert(converter = JsonConverter.class)
    private Map<String, Object> settings;
}
```

### Fix 3: Use @Column with explicit columnDefinition

```java
@Entity
public class Event {
    @Column(columnDefinition = "TIMESTAMP WITH TIME ZONE")
    private ZonedDateTime createdAt;

    @Column(columnDefinition = "JSONB")
    private String metadata;
}
```

### Fix 4: Use Hibernate @TypeDef for custom types

```java
@TypeDef(name = "jsonb", typeClass = JsonBinaryType.class)
@Entity
public class Config {
    @Type(JsonBinaryType.class)
    @Column(columnDefinition = "jsonb")
    private Map<String, Object> settings;
}
```

### Fix 5: Align Hibernate dialect with database version

```yaml
# application.properties
spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQL15Dialect
```

## Related Errors

- {{< relref "hibernate-mapping" >}} — Hibernate mapping configuration error.
- {{< relref "jpa-entity" >}} — JPA entity definition error.
