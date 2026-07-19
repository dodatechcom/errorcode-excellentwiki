---
title: "[Solution] Hibernate MappingException — Unknown Entity"
description: "Fix org.hibernate.MappingException Unknown entity. Resolve Hibernate entity mapping and registration errors."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# MappingException — Unknown Entity

A `MappingException` with message `Unknown entity: com.example.Entity` occurs when Hibernate cannot find the entity class mapping. The entity is not registered in the Hibernate configuration, is missing the `@Entity` annotation, or is in a package not scanned by the configuration.

## What This Error Means

Hibernate needs to know about every entity class to generate SQL and manage the persistence context. If an entity class is not discovered during configuration (via scanning, explicit registration, or mapping files), any attempt to use it in queries or persistence operations will fail with this error.

## Common Causes

```java
// Cause 1: Missing @Entity annotation
public class User {  // Missing @Entity!
    @Id
    private Long id;
    private String name;
}
entityManager.find(User.class, 1L);  // MappingException: Unknown entity

// Cause 2: Entity in package not scanned
// Entity is in com.example.model but scan packages is com.example.repository
@Entity
public class Product { ... }

// Cause 3: Entity not added to persistence.xml or configuration
// persistence.xml does not list the entity class
```

## How to Fix

### Fix 1: Ensure @Entity annotation is present

```java
import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity  // Required!
public class User {
    @Id
    private Long id;
    private String name;
}
```

### Fix 2: Configure package scanning in Spring Boot

```properties
# application.properties — Spring Boot scans @SpringBootApplication package and sub-packages
spring.jpa.packages-to-scan=com.example.entity

# Or in Java config
@Configuration
@EnableTransactionManagement
@EntityScan(basePackages = "com.example.entity")
public class JpaConfig {
    @Bean
    public LocalContainerEntityManagerFactoryBean entityManagerFactory() {
        LocalContainerEntityManagerFactoryBean em = new LocalContainerEntityManagerFactoryBean();
        em.setPackagesToScan("com.example.entity");
        em.setDataSource(dataSource());
        em.setJpaVendorAdapter(new HibernateJpaVendorAdapter());
        return em;
    }
}
```

### Fix 3: Register entity in persistence.xml

```xml
<persistence-unit name="myPU">
    <class>com.example.entity.User</class>
    <class>com.example.entity.Order</class>
    <class>com.example.entity.Product</class>
    <properties>
        <property name="hibernate.dialect" value="org.hibernate.dialect.PostgreSQLDialect"/>
    </properties>
</persistence-unit>
```

### Fix 4: Verify entity with metadata explorer

```java
@PersistenceUnit
private EntityManagerFactory emf;

@PostConstruct
public void validateEntities() {
    Metamodel metamodel = emf.getMetamodel();
    Set<EntityType<?>> entities = metamodel.getEntities();
    entities.forEach(entity -> {
        log.info("Registered entity: {} -> {}",
            entity.getName(), entity.getJavaType().getName());
    });
}
```

## Prevention Tips

- Always annotate entity classes with `@Entity`.
- Use `@EntityScan` or configure package scanning explicitly.
- Add a startup validation that checks all expected entities are registered.
- Use static metamodel generation to catch mapping issues at compile time.

## Related Errors

- {{< relref "hibernate-type-error" >}} — Type mapping errors
- {{< relref "hibernate-dialect" >}} — Dialect not found
- {{< relref "hibernate-query-syntax" >}} — HQL syntax errors
