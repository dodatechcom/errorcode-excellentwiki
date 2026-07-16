---
title: "[Solution] Java ClassNotFoundException — Class Not Found Fix"
description: "Fix Java ClassNotFoundException when a class cannot be found at runtime. Check your classpath, JAR files, Maven dependencies, and class loaders."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["classnotfoundexception", "classpath", "dependency", "reflection"]
weight: 20
---

# ClassNotFoundException — Class Not Found Fix

A `ClassNotFoundException` is thrown when the JVM or a classloader attempts to load a class by its fully qualified name but cannot locate the corresponding `.class` file. This is a checked exception that typically appears at runtime when dependencies are missing, classpath is misconfigured, or reflection is used incorrectly.

## Description

Unlike `NoClassDefFoundError` (which means the class was present at compile time but missing at runtime), `ClassNotFoundException` means the class was never found at all. Common variants:

- `java.lang.ClassNotFoundException: com.example.MyClass`
- `java.lang.ClassNotFoundException: org.apache.commons.lang3.StringUtils`
- `java.lang.ClassNotFoundException: com.mysql.cj.jdbc.Driver`

## Common Causes

```java
// Cause 1: Missing JAR dependency on the classpath
Class.forName("com.mysql.cj.jdbc.Driver");

// Cause 2: Wrong fully qualified class name (typo)
Class.forName("com.example.Myclass");  // should be MyClass

// Cause 3: Package name does not match directory structure
// File is at /MyClass.java but package says com.example

// Cause 4: Class loaded by a different classloader
// A web app's classloader cannot see classes from the parent in certain configurations

// Cause 5: ProGuard / R8 stripped the class during minification
Class.forName("com.example.KeepThisClass");
```

## Solutions

### Fix 1: Verify the class is on the classpath

```bash
# List JARs on the classpath
echo $CLASSPATH

# Or for a running JVM, use:
jcmd <PID> VM.classpath

# Compile with explicit classpath if using javac directly
javac -cp "libs/*:." Main.java

# Run with classpath
java -cp "libs/*:." Main
```

### Fix 2: Check Maven / Gradle dependencies

```xml
<!-- Wrong — dependency scope is 'test', so it's not available at runtime -->
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.12.0</version>
    <scope>test</scope>
</dependency>

<!-- Correct — scope 'compile' (or omit scope) makes it available at runtime -->
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.12.0</version>
</dependency>
```

```groovy
// Gradle — wrong: only in testImplementation
testImplementation 'org.apache.commons:commons-lang3:3.12.0'

// Correct: available at runtime
implementation 'org.apache.commons:commons-lang3:3.12.0'
```

### Fix 3: Verify the fully qualified class name

```java
// Wrong — typo in package or class name
Class.forName("com.example.userProfile");  // should be com.example.UserProfile

// Correct — match the exact package and class name
Class.forName("com.example.UserProfile");

// Tip: use the IDE's "Copy Reference" to get the correct FQCN
```

### Fix 4: Handle reflection loading safely

```java
// Wrong — unhandled ClassNotFoundException
Class<?> clazz = Class.forName("com.example.ServiceImpl");
Object instance = clazz.getDeclaredConstructor().newInstance();

// Correct — catch and provide meaningful error handling
try {
    Class<?> clazz = Class.forName("com.example.ServiceImpl");
    Object instance = clazz.getDeclaredConstructor().newInstance();
} catch (ClassNotFoundException e) {
    System.err.println("Plugin not found: " + e.getMessage());
    System.err.println("Make sure the plugin JAR is in the plugins/ directory.");
} catch (ReflectiveOperationException e) {
    System.err.println("Failed to instantiate: " + e.getMessage());
}
```

### Fix 5: Check for fat JAR / shade plugin conflicts

```xml
<!-- Wrong — maven-shade-plugin may produce an empty or invalid JAR -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-shade-plugin</artifactId>
    <version>3.5.0</version>
    <configuration>
        <transformers>
            <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                <mainClass>com.example.Main</mainClass>
            </transformer>
        </transformers>
    </configuration>
</plugin>
```

```bash
# Inspect the contents of the fat JAR to verify the class exists
jar tf target/myapp.jar | grep MyClass

# Should output something like:
# com/example/MyClass.class
```

### Fix 6: Use ServiceLoader instead of raw Class.forName

```java
// Wrong — fragile, breaks if implementation JAR is missing
Class<?> impl = Class.forName("com.example.DefaultFormatter");

// Correct — use ServiceLoader for plugin-style loading
ServiceLoader<Formatter> loader = ServiceLoader.load(Formatter.class);
Formatter formatter = loader.findFirst()
    .orElseThrow(() -> new IllegalStateException("No Formatter implementation found"));
```

## Debugging Checklist

- Run `java -verbose:class -jar myapp.jar` to see every class the JVM loads.
- Verify the class exists inside the JAR: `jar tf myapp.jar | grep ClassName`.
- Check for classloader conflicts in application servers (Tomcat, WildFly).
- Ensure `module-info.java` (Java 9+ modules) exports the required package.

## Related Errors

- [NoClassDefFoundError](#) — class was present at compile time but missing at runtime.
- [NoSuchMethodError](#) — method exists in a different version than expected.
- [LinkageError](#) — class has unsatisfied dependencies or incompatible versions.
