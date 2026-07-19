---
title: "[Solution] IntelliJ IDEA Spring Boot configuration error"
description: "Fix IntelliJ IDEA Spring Boot configuration and integration errors. Resolve annotation processing, auto-configuration, and runtime issues."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "spring-boot", "spring", "java-framework", "annotation-processing"]
severity: "error"
---

# Spring Boot configuration error

## Error Message

```
Spring Boot configuration error
Cannot resolve @Autowired reference
No qualifying bean of type 'ServiceClass' available
Consider defining a bean of type 'ServiceClass' in your configuration.

Error creating bean with name 'application': Unsatisfied dependency
```

## Common Causes

- Component scan package path is incorrect or incomplete
- Spring Boot annotation processing is disabled in IDE
- Application properties or YAML configuration has invalid values
- Missing Spring Boot DevTools or starter dependency
- Bean definition conflict or circular dependency

## Solutions

### Solution 1: Enable Annotation Processing

Ensure annotation processing is enabled for Spring Boot. Navigate to **File → Settings → Build → Compiler → Annotation Processors**.

```
File → Settings → Build → Compiler → Annotation Processors
# Check 'Enable annotation processing'
# Check 'Obtain processors from project classpath'
# Apply and restart IDE

# For Maven projects, also verify in pom.xml:
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <annotationProcessorPaths>
            <path>
                <groupId>org.projectlombok</groupId>
                <artifactId>lombok</artifactId>
                <version>1.18.30</version>
            </path>
        </annotationProcessorPaths>
    </configuration>
</plugin>
```

### Solution 2: Rebuild Project with Spring Profiles

Rebuild the project and ensure the correct Spring profile is activated.

```bash
# From IDE:
Build → Rebuild Project

# Or from command line with specific profile:
./mvnw clean package -Dspring-boot.run.profiles=dev

# Or for Gradle:
./gradlew clean build -Dspring.profiles.active=dev

# Set active profile in IDE:
# Run → Edit Configurations → Active Profiles: dev
```

### Solution 3: Verify Application Properties

Check your application.properties or application.yml for syntax errors and missing required properties.

```properties
# application.properties — verify these essential settings:
spring.application.name=my-app
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.username=root
spring.datasource.password=password

# Validate YAML syntax:
# Use online YAML validator or IDE's built-in YAML support
# Check for indentation errors — YAML is indentation-sensitive
```

### Solution 4: Run Spring Boot with Debug Output

Enable debug logging to identify the root cause of Spring Boot startup errors.

```properties
# application.properties:
logging.level.root=INFO
logging.level.org.springframework=DEBUG
logging.level.org.springframework.boot.autoconfigure=DEBUG

# Or run with --debug flag:
./mvnw spring-boot:run -Dspring-boot.run.arguments=--debug
```

## Prevention Tips

- Install the 'Spring Boot' plugin from JetBrains Marketplace for enhanced support
- Use Ctrl+Space in @Value annotations to auto-complete property keys
- Enable 'Spring' facets in Project Structure for better navigation
- Use the Actuator endpoint /actuator/env to verify runtime configuration

## Related Errors

- [Maven Integration Error]({{< relref "/tools/intellij/maven-integration-error" >}})
- [Compilation Failed]({{< relref "/tools/intellij/compilation-error" >}})
- [Run Configuration Error]({{< relref "/tools/intellij/run-configuration-error" >}})
