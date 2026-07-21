---
title: "[Solution] Spring Data Auditing Error"
description: "Fix Spring Data auditing errors when @CreatedDate or @LastModifiedDate fields are not automatically populated."
frameworks: ["spring"]
error-types: ["database-error"]
severities: ["error"]
---

Auditing errors occur when `@CreatedDate`, `@LastModifiedDate`, or `@CreatedBy` fields are not automatically set by Spring Data JPA.

## Common Causes

- `@EnableJpaAuditing` not configured
- Entity does not implement `Persistable` or extend `AbstractAuditable`
- `@CreatedDate` field not of correct type
- Auditor aware not configured for `@CreatedBy`
- Entity saved with `em.merge()` instead of `save()`

## How to Fix

### Enable JPA Auditing

```java
@Configuration
@EnableJpaAuditing
public class AuditingConfig {
    @Bean
    public AuditorAware<String> auditorProvider() {
        return () -> Optional.ofNullable(SecurityContextHolder.getContext())
            .map(SecurityContext::getAuthentication)
            .map(Authentication::getName);
    }
}
```

### Add Audit Annotations to Entity

```java
@Entity
@EntityListeners(AuditingEntityListener.class)
public class Article {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;

    @CreatedDate
    private LocalDateTime createdAt;

    @LastModifiedDate
    private LocalDateTime updatedAt;

    @CreatedBy
    private String createdBy;

    @LastModifiedBy
    private String lastModifiedBy;
}
```

### Use BaseEntity

```java
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
public abstract class BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @CreatedDate
    private LocalDateTime createdAt;

    @LastModifiedDate
    private LocalDateTime updatedAt;
}

@Entity
public class User extends BaseEntity {
    private String name;
}
```

## Examples

```java
// Bug -- missing @EnableJpaAuditing
// @CreatedDate fields stay null

// Fix -- add configuration
@Configuration
@EnableJpaAuditing
public class AuditingConfig {}
```

```java
// Bug -- wrong field type
@CreatedDate
private Date createdAt;  // Should be LocalDateTime

// Fix -- correct type
@CreatedDate
private LocalDateTime createdAt;
```
