---
title: "[Solution] Eclipse Test runner error"
description: "Test error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "junit", "testng", "testing"]
severity: "error"
---

# Test runner error

## Error Message

```
Class not found: org.junit.runner.JUnitCore. JUnit tests require the JUnit library on the build path. Add JUnit to the project via Build Path > Add Libraries.
```

## Common Causes

- The JUnit or TestNG library has not been added to the project's build path.
- The test class does not follow the naming conventions expected by the test runner.
- A dependency required by the test (e.g., Spring TestContext) is missing from the classpath.

## Solutions

### Solution 1: Add JUnit Library to Build Path

Right-click the project in **Package Explorer** and go to **Build Path > Add Libraries > JUnit**. Select the JUnit 4 or JUnit 5 version as required. Eclipse will add the JUnit JAR files to the project classpath automatically.

```java
// JUnit 5 test class example
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    @Test
    void shouldAddTwoNumbers() {
        Calculator calc = new Calculator();
        assertEquals(4, calc.add(2, 2));
    }

    @Test
    void shouldDivideByZero() {
        Calculator calc = new Calculator();
        assertThrows(ArithmeticException.class, () -> calc.divide(1, 0));
    }
}
```

### Solution 2: Configure TestNG in Eclipse

Install the **TestNG for Eclipse** plugin from Eclipse Marketplace. Then right-click the test class, select **Run As > TestNG Test**. To configure TestNG, go to **Window > Preferences > TestNG** and set the XML suite file location.

```bash
<!-- testng.xml - TestNG suite configuration -->
<suite name="My Test Suite" verbose="1">
    <test name="All Tests">
        <classes>
            <class name="com.example.CalculatorTest"/>
            <class name="com.example.StringUtilTest"/>
        </classes>
    </test>
</suite>
```

## Prevention Tips

- Use **Run As > JUnit Test** (or **Run As > TestNG Test**) to run all tests in a class.
- Enable **coverage** with **Run As > JUnit Test with Coverage** to see code coverage reports.
- Use the **JUnit** view to see test results, failures, and execution times.

## Related Errors

- [debug-error]({{< relref "/tools/eclipse/debug-error" >}})
- [run-configuration-error]({{< relref "/tools/eclipse/run-configuration-error" >}})
- [build-path-error]({{< relref "/tools/eclipse/build-path-error" >}})
