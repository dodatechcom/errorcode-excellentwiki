---
title: "[Solution] Java Quarkus startup error — application fails to start"
description: "Fix Java Quarkus startup error by checking configuration, verifying beans, and handling CDI issues. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 118
---

# Quarkus startup error — application fails to start

A Quarkus startup error occurs when the application fails to initialize during the build or runtime phase. Quarkus performs build-time processing, and many errors are caught before the application starts. This covers CDI issues, configuration errors, and build-time failures.

## Description

Quarkus uses ArC (CDI implementation) and build-time augmentation. Errors occur when beans cannot be created, configuration is invalid, or required extensions are missing. Common message variants include:

- `javax.enterprise.inject.spi.DefinitionException: Normal scope requires a default constructor`
- `io.quarkus.runtime.ApplicationLifecycleException: Failed to start`
- `javax.enterprise.inject.UnsatisfiedResolutionException`
- `SRGREQ00004: Required class not found`
- `Build step X threw an exception`
- `Configuration property 'X' not defined`

## Common Causes

```java
// Cause 1: CDI bean with unsatisfied dependency
@ApplicationScoped
public class OrderService {
    @Inject PaymentProcessor processor;  // No bean implementing PaymentProcessor
}

// Cause 2: Missing default constructor for scope
@RequestScoped
public class RequestContext {
    // No default constructor — CDI requires one for normal scopes
    public RequestContext(String param) {  // Only parameterized constructor
    }
}

// Cause 3: Missing Quarkus extension
// Trying to use JPA without quarkus-hibernate-orm-panache

// Cause 4: Configuration property not set
@ConfigProperty(name = "app.api.key")
String apiKey;  // app.api.key not in application.properties

// Cause 5: Native compilation issue
// Reflection not registered for native image
```

## Solutions

### Fix 1: Ensure all CDI dependencies are satisfied

```java
@ApplicationScoped
public class OrderService {

    private final PaymentProcessor processor;

    @Inject
    public OrderService(PaymentProcessor processor) {
        this.processor = processor;
    }
}

// Implement the dependency
@ApplicationScoped
public class StripePaymentProcessor implements PaymentProcessor {
    @Override
    public void process(double amount) {
        // Stripe implementation
    }
}

// For optional dependencies
@ApplicationScoped
public class NotificationService {
    @Inject
    @Optional
    EmailService emailService;  // Won't fail if no bean exists
}
```

### Fix 2: Add default constructor for CDI scopes

```java
@RequestScoped
public class RequestContext {
    private String userId;
    private String traceId;

    // Required: default constructor for CDI
    public RequestContext() {}

    public RequestContext(String userId, String traceId) {
        this.userId = userId;
        this.traceId = traceId;
    }
}

// Or use @Dependent scope (no default constructor required)
@Dependent
public class TransientService {
    public TransientService(String config) {
        this.config = config;
    }
}
```

### Fix 3: Add required Quarkus extensions

```xml
<!-- pom.xml -->
<dependencies>
    <!-- Web -->
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-resteasy-reactive</artifactId>
    </dependency>

    <!-- JPA -->
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-hibernate-orm-panache</artifactId>
    </dependency>

    <!-- JDBC -->
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-jdbc-postgresql</artifactId>
    </dependency>

    <!-- Config -->
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-config-yaml</artifactId>
    </dependency>
</dependencies>
```

### Fix 4: Set required configuration properties

```properties
# application.properties

# DataSource
quarkus.datasource.db-kind=postgresql
quarkus.datasource.jdbc.url=jdbc:postgresql://localhost:5432/mydb
quarkus.datasource.username=quarkus
quarkus.datasource.password=quarkus

# JPA
quarkus.hibernate-orm.database.generation=drop-and-create

# Application config
app.api.key=${APP_API_KEY:default-dev-key}

# HTTP
quarkus.http.port=8080
```

### Fix 5: Register reflection for native compilation

```java
@RegisterForReflection
public class UserDto {
    public String name;
    public String email;
}

// Or use @RegisterForReflection(targets = {User.class, Order.class})
@RegisterForReflection(targets = {User.class, Order.class, Product.class})
public class ReflectionConfig {}

// For REST responses, Quarkus auto-registers most framework classes
```

### Fix 6: Debug startup failures

```bash
# Run in dev mode to see detailed errors
./mvnw quarkus:dev

# Enable verbose logging
quarkus.log.level=DEBUG
quarkus.log.category."io.quarkus".level=DEBUG
quarkus.log.category."org.hibernate".level=DEBUG

# Check build-time errors
./mvnw clean package -Dquarkus.log.category."io.quarkus.builder".level=TRACE
```

## Prevention Checklist

- Use `./mvnw quarkus:dev` during development for live reload and detailed errors
- Ensure all `@Inject` dependencies have at least one CDI bean implementation
- Add default constructors for `@RequestScoped` and `@SessionScoped` beans
- Add all required Quarkus extensions to `pom.xml` before using their features
- Set all required `application.properties` values — use `@ConfigProperty(defaultValue = "...")` for optional ones
- Test native compilation with `./mvnw package -Pnative` to catch reflection issues early

## Related Errors

- [UnsatisfiedResolutionException](/languages/java/spring-nosuchbean/)
- [BeanCreationException](/languages/java/spring-bean-creation-failed/)
- [IllegalArgumentException from config](/languages/java/spring-boot-properties/)
