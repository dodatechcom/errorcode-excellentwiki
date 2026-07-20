---
title: "[Solution] Java TypeMismatchException — Hibernate type conversion error"
description: "Fix Java TypeMismatchException by checking property types, verifying mappings, and handling type conversions. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 110
---

# TypeMismatchException — Hibernate type conversion error

A `TypeMismatchException` is thrown when Hibernate encounters a mismatch between the expected Java type and the actual value provided for an entity property or query parameter. This covers type incompatibilities in mappings, parameters, and result transformations.

## Description

Hibernate maps Java types to SQL types through the JPA type system. When a value cannot be converted to the expected type, a `TypeMismatchException` is thrown. Common message variants include:

- `Provided value of wrong type`
- `Type mismatch: expected X but got Y`
- `org.hibernate.TypeMismatchException: Expected type X, got Y`
- `Could not set parameter value: unable to coerce X to Y`

## Common Causes

```java
// Cause 1: Property type mismatch with database column
@Entity
public class Product {
    @Column(name = "price")
    private BigDecimal price;  // Database column is INTEGER
}

// Cause 2: Query parameter type mismatch
@Query("SELECT p FROM Product p WHERE p.price = :price")
List<Product> findByPrice(@Param("price") Double price);  // price is BigDecimal

// Cause 3: Enum mapping without @Enumerated
@Entity
public class Order {
    private Status status;  // Enum — database stores String
    // Missing @Enumerated(EnumType.STRING)
}

// Cause 4: Custom type converter missing
@Entity
public class Event {
    @Column
    private LocalDateTime eventTime;  // No @Convert annotation for custom mapping
}

// Cause 5: Incorrect @Column definition
@Entity
public class User {
    @Column(columnDefinition = "INT")
    private Long id;  // Mismatch: Long doesn't map cleanly to INT in some dialects
}
```

## Solutions

### Fix 1: Match Java types to database column types

```java
@Entity
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private BigDecimal price;  // DECIMAL in database — matches BigDecimal

    @Column(nullable = false)
    private String name;  // VARCHAR — matches String

    @Column(nullable = false)
    private Integer quantity;  // INT — matches Integer
}
```

### Fix 2: Use correct parameter types in queries

```java
@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {

    // WRONG — Double parameter for BigDecimal field
    // @Query("SELECT p FROM Product p WHERE p.price = :price")
    // List<Product> findByPrice(@Param("price") Double price);

    // CORRECT — BigDecimal parameter for BigDecimal field
    @Query("SELECT p FROM Product p WHERE p.price = :price")
    List<Product> findByPrice(@Param("price") BigDecimal price);

    // CORRECT — string parameter for String field
    @Query("SELECT p FROM Product p WHERE p.name LIKE %:name%")
    List<Product> findByNameContaining(@Param("name") String name);
}
```

### Fix 3: Map enums properly

```java
@Entity
public class Order {
    @Id
    @GeneratedValue
    private Long id;

    // Store as String in database
    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private Status status;

    // Store as ordinal (integer) — fragile if enum order changes
    @Enumerated(EnumType.ORDINAL)
    private Priority priority;

    public enum Status { PENDING, CONFIRMED, SHIPPED, DELIVERED }
    public enum Priority { LOW, MEDIUM, HIGH }
}
```

### Fix 4: Use @Convert for custom type mapping

```java
@Converter
public class LocalDateTimeConverter implements AttributeConverter<LocalDateTime, Timestamp> {

    @Override
    public Timestamp convertToDatabaseColumn(LocalDateTime attribute) {
        return attribute == null ? null : Timestamp.valueOf(attribute);
    }

    @Override
    public LocalDateTime convertToEntityAttribute(Timestamp dbData) {
        return dbData == null ? null : dbData.toLocalDateTime();
    }
}

@Entity
public class Event {
    @Convert(converter = LocalDateTimeConverter.class)
    private LocalDateTime eventTime;
}
```

### Fix 5: Use @Column and @Type for precise control

```java
// Hibernate-specific @Type for fine-grained control
@Entity
public class Document {
    @Id
    @GeneratedValue
    private Long id;

    @Type(org.hibernate.type.TextType.class)
    @Column(columnDefinition = "TEXT")
    private String content;

    @Column(columnDefinition = "DECIMAL(10,2)")
    private BigDecimal score;
}

// Or use JPA @Column with explicit length and precision
@Entity
public class Measurement {
    @Column(precision = 10, scale = 2)
    private BigDecimal value;

    @Column(length = 255, nullable = false)
    private String label;
}
```

## Prevention Checklist

- Match Java field types to appropriate SQL types (`BigDecimal` for monetary values, `LocalDateTime` for timestamps)
- Use `@Enumerated(EnumType.STRING)` for enum fields — avoid `ORDINAL` unless stable
- Implement `AttributeConverter` for custom type mappings
- Set `@Column(precision, scale)` for numeric fields and `@Column(length)` for strings
- Verify query parameter types match entity field types
- Use `@TypeDef` or `@Type` for complex Hibernate-specific type mappings

## Related Errors

- [Hibernate QueryException](/languages/java/hibernate-query-exception/)
- [Hibernate MappingException](/languages/java/hibernate-mapping/)
- [Hibernate ConstraintViolationException](/languages/java/hibernate-constraint-violation/)
