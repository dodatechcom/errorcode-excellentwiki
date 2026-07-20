---
title: "[Solution] Java cannot find symbol: package-info — Fix package-info.java"
description: "Fix Java compiler error 'cannot find symbol: package-info' by verifying the file exists, checking package declaration, and ensuring correct directory structure. Copy-paste solutions."
languages: ["java"]
severities: ["error"]
error_types: ["compile"]
weight: 455
---

# Java Compiler Error: cannot find symbol: package-info

This compile-time error occurs when the Java compiler (or annotation processor) cannot locate a `package-info.java` file. The `package-info.java` file provides package-level documentation and annotations. If it's missing or incorrectly structured, tools and annotations that depend on it will fail.

## Error Message

```
error: cannot find symbol: package-info
  symbol:   class package-info
```

Other variants:

```
error: package-info.java does not exist
warning: no description for @since
error: cannot find symbol: package-info.java
```

## Common Causes

### Cause 1: package-info.java File Does Not Exist

```java
// Annotation processor or Javadoc tool expects:
// src/main/java/com/example/package-info.java
// But the file is missing
```

### Cause 2: Wrong Package Declaration in package-info.java

```java
// package-info.java is in: src/main/java/com/example/package-info.java
// But it has wrong package declaration:
package com.example.sub; // ERROR: wrong package — doesn't match directory
```

### Cause 3: Wrong Directory Structure

```
src/
  main/
    java/
      com/
        example/
          MyClass.java          # package com.example
          package-info.java     # file exists here — OK
```

But if the file is misplaced:

```
src/
  main/
    java/
      com/
        MyClass.java            # package com.example
        package-info.java       # WRONG: should be in com/example/
```

### Cause 4: Annotation Processing Cannot Find It

```java
// package-info.java
package com.example;

@Generated("my-tool")
// Missing the package declaration — just has Javadoc but no package line
```

### Cause 5: Build Tool Not Including It

```xml
<!-- Maven may exclude package-info.java by default in some configurations -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <excludes>
            <exclude>**/package-info.java</exclude> <!-- This would cause the error -->
        </excludes>
    </configuration>
</plugin>
```

## Solutions

### Fix 1: Create the package-info.java File

```java
// src/main/java/com/example/package-info.java

/**
 * Common utilities for the example package.
 */
package com.example;
```

### Fix 2: Verify Package Declaration Matches Directory

```java
// File: src/main/java/com/example/utils/package-info.java
// Must have: package com.example.utils;

/**
 * Utility classes for the example project.
 */
package com.example.utils;
```

### Fix 3: Fix Directory Structure

```
src/
  main/
    java/
      com/
        example/
          utils/
            MyClass.java
            package-info.java    # Must be in same package directory
```

### Fix 4: Ensure File Has Correct Minimal Content

```java
// package-info.java
package com.example;

/**
 * Package-level documentation goes here.
 */
```

### Fix 5: Remove Build Tool Exclusions

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <!-- Remove excludes that filter package-info.java -->
        <excludes>
            <!-- Do NOT exclude **/package-info.java -->
        </excludes>
    </configuration>
</plugin>
```

## Prevention Checklist

- Always include a `package` declaration in `package-info.java` that matches the directory
- Place `package-info.java` in the same directory as the package's classes
- Keep the package declaration as the first statement (after comments)
- Use Javadoc tools to verify package-level documentation generates correctly
- Check build tool configurations for exclusions that might filter `package-info.java`
- Use IDE package-info generation (IntelliJ: right-click package > New > package-info)

## Related Errors

- [cannot find symbol (cannot-find-symbol)](/languages/java/cannot-find-symbol)
- [package does not exist](/languages/java/cannot-find-symbol)
- [symbol not found in annotation processing](/languages/java/annotationformaterror)
