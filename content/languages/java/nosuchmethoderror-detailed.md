---
title: "[Solution] Java NoSuchMethodError — Binary Incompatibility Fix"
description: "Fix Java NoSuchMethodError at runtime by doing clean build, resolving version conflicts, checking classpath order, and recompiling dependencies."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# NoSuchMethodError — Binary Incompatibility Fix

A `NoSuchMethodError` at runtime indicates binary incompatibility — the calling class was compiled against a version of the target class that had a method which no longer exists at runtime. This is different from `NoSuchMethodException` (which occurs during reflection).

## Description

This error occurs when the JVM performs method resolution at runtime and cannot find a method that was present when the calling code was compiled. The most common cause is having mixed versions of the same library on the classpath — one version compiled against, another version at runtime.

Message variants:

- `java.lang.NoSuchMethodError: com.google.common.collect.ImmutableList.of()Lcom/google/common/collect/ImmutableList;`
- `java.lang.NoSuchMethodError: 'void org.springframework.context.ConfigurableApplicationContext.refresh()'`
- `java.lang.NoSuchMethodError: com.example.Service.process(Ljava/lang/String;)V`

## Common Causes

```java
// Cause 1: Mixed library versions on classpath
// ProjectA compiled with Guava 30, runtime loads Guava 21
ImmutableList.of("a", "b", "c");  // NoSuchMethodError — method signature changed between versions

// Cause 2: Stale .class files from old compilation
// Service.process(String) was changed to process(String, int)
// Old .class file still references the one-arg version

// Cause 3: Classpath ordering — wrong JAR loaded first
// Two versions of library.jar on classpath
// JVM picks the first one, which has an older API

// Cause 4: Dependency pulled in an incompatible transitive version
// Your code uses Jackson 2.14
// Another dependency pulls Jackson 2.12 transitively
// Classpath resolution picks 2.12 — missing methods from 2.14

// Cause 5: Interface default method not visible due to classpath issue
// Java 8 interface with default method
// Runtime classpath has pre-8 version of the interface
```

## Solutions

### Fix 1: Clean and rebuild the entire project

```bash
# Delete all compiled output and rebuild
# Maven
mvn clean install

# Gradle
gradle clean build

# Manual cleanup
rm -rf target/classes build/classes
javac -d target/classes $(find src -name "*.java")
```

### Fix 2: Resolve version conflicts with dependency management

```bash
# Maven — check for version conflicts
mvn dependency:tree

# Look for duplicate libraries with different versions
# Example output:
# [INFO] +- com.google.guava:guava:jar:30.0-jre:compile
# [INFO] \- com.other:lib:jar:1.0:compile
#      \- com.google.guava:guava:jar:21.0:compile  ← conflict!

# Maven — force a single version
# pom.xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.guava</groupId>
            <artifactId>guava</artifactId>
            <version>31.1-jre</version>
        </dependency>
    </dependencies>
</dependencyManagement>

# Gradle — force resolution
configurations.all {
    resolutionStrategy {
        force 'com.google.guava:guava:31.1-jre'
    }
}
```

### Fix 3: Check classpath order and remove duplicates

```bash
# List all JARs on the classpath
echo $CLASSPATH | tr ':' '\n' | sort

# Check which version of a class is actually loaded
java -verbose:class -cp "libs/*:." Main 2>&1 | grep "com/google/common/collect/ImmutableList"

# Use classloader diagnostic flags
java -XX:+ShowCodeDetailsInExceptionMessages -cp "libs/*:." Main
```

### Fix 4: Use reflection for safe method invocation across versions

```java
public class VersionSafeInvoker {
    public static Object invoke(Object obj, String methodName, Class<?>[] paramTypes, Object... args) {
        try {
            Method method = obj.getClass().getMethod(methodName, paramTypes);
            return method.invoke(obj, args);
        } catch (NoSuchMethodException e) {
            System.err.println("Method " + methodName + " not available in this version");
            return null;
        } catch (InvocationTargetException e) {
            throw new RuntimeException(e.getCause());
        } catch (IllegalAccessException e) {
            throw new RuntimeException(e);
        }
    }
}
```

## Prevention Checklist

- Always run `mvn clean` or `gradle clean` before rebuilding.
- Use dependency management to lock library versions.
- Avoid mixing multiple versions of the same library on the classpath.
- Check `mvn dependency:tree` or `gradle dependencies` regularly for conflicts.
- Test with the actual runtime classpath, not just the compile classpath.
- Use `maven-shade-plugin` or `maven-assembly-plugin` to create fat JARs with resolved dependencies.

## Related Errors

- [NoSuchMethodException](../nosuchmethodexception) — method not found via reflection
- [NoSuchFieldError](../nosuchfielderror) — binary incompatibility for field access
- [IncompatibleClassChangeError](../incompatibleclasschangeerror) — class structure changed
- [NoClassDefFoundError](../noclassdeffounderror) — class missing at runtime
