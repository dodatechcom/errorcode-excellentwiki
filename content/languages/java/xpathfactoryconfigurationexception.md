---
title: "[Solution] Java XPathFactoryConfigurationException — XPath Factory Config Fix"
description: "Fix javax.xml.xpath.XPathFactoryConfigurationException by checking classpath for XPath implementation, verifying factory class, and handling missing provider."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 447
---

# XPathFactoryConfigurationException — XPath Factory Config Fix

An `XPathFactoryConfigurationException` is thrown when an `XPathFactory` cannot be created due to configuration problems. This typically means the XPath implementation is missing from the classpath or incorrectly configured.

## Description

`javax.xml.xpath.XPathFactoryConfigurationException` extends `XPathException` and indicates that the `XPathFactory` could not be instantiated. The factory class specified in system properties may not exist, or the default factory discovery mechanism failed.

Common message variants:

- `XPathFactoryConfigurationException: Provider net.sf.saxon.xpath.XPathFactoryImpl not found`
- `XPathFactoryConfigurationException: XPathFactory class not found`
- `XPathFactoryConfigurationException: Could not instantiate XPathFactory`

## Common Causes

```java
// Cause 1: Missing XPath implementation in classpath
XPathFactory factory = XPathFactory.newInstance();
// XPathFactoryConfigurationException if no XPath provider available

// Cause 2: Wrong factory class name in system property
System.setProperty("javax.xml.xpath.XPathFactory",
    "com.nonexistent.XPathFactoryImpl");
XPathFactory factory = XPathFactory.newInstance();
// XPathFactoryConfigurationException: class not found

// Cause 3: Conflicting XPath implementations
// Both Saxon and JDK built-in on classpath causing class loading issues
XPathFactory factory = XPathFactory.newInstance();
// XPathFactoryConfigurationException: wrong class loaded

// Cause 4: Using XPath 2.0 features with XPath 1.0 factory
XPathFactory factory = XPathFactory.newInstance();
XPath xpath = factory.newXPath();
xpath.compile("//user[exists(@name)]");
// 'exists()' requires XPath 2.0 — Saxon factory needed

// Cause 5: Module system blocking access (Java 9+)
XPathFactory factory = XPathFactory.newInstance();
// XPathFactoryConfigurationException: module access denied
```

## Solutions

### Fix 1: Ensure XPath implementation is on the classpath

```xml
<!-- Maven: For XPath 1.0 (built-in with JDK) -->
<!-- No additional dependency needed — java.xml module included by default -->

<!-- Maven: For XPath 2.0+ (Saxon) -->
<dependency>
    <groupId>net.sf.saxon</groupId>
    <artifactId>Saxon-HE</artifactId>
    <version>12.4</version>
</dependency>
```

```java
// Verify XPath factory is available
try {
    XPathFactory factory = XPathFactory.newInstance();
    System.out.println("XPath factory: " + factory.getClass().getName());
} catch (XPathFactoryConfigurationException e) {
    System.err.println("Cannot create XPath factory: " + e.getMessage());
    System.err.println("Add Saxon or ensure java.xml module is available");
}
```

### Fix 2: Specify factory class explicitly

```java
// Use JDK built-in XPath 1.0
XPathFactory factory = XPathFactory.newInstance(
    XPathFactory.DEFAULT_OBJECT_MODEL_URI,    // "http://java.sun.com/jaxp/xpath/dom"
    "com.sun.org.apache.xpath.internal.jaxp.XPathFactoryImpl",
    null
);
XPath xpath = factory.newXPath();

// Use Saxon for XPath 2.0/3.0
XPathFactory saxonFactory = XPathFactory.newInstance(
    "http://www.w3.org/1999/XSL/Transform",
    "net.sf.saxon.xpath.XPathFactoryImpl",
    null
);
```

### Fix 3: Set correct system property for factory selection

```java
// For JDK built-in XPath 1.0
System.setProperty("javax.xml.xpath.XPathFactory:" + XPathFactory.DEFAULT_OBJECT_MODEL_URI,
    "com.sun.org.apache.xpath.internal.jaxp.XPathFactoryImpl");

// For Saxon XPath 2.0/3.0
System.setProperty("javax.xml.xpath.XPathFactory:" + XPathFactory.DEFAULT_OBJECT_MODEL_URI,
    "net.sf.saxon.xpath.XPathFactoryImpl");

// Create factory after setting property
XPathFactory factory = XPathFactory.newInstance();
```

### Fix 4: Handle missing factory with fallback strategy

```java
public class ResilientXPathFactory {
    public static XPath createXPath() throws XPathFactoryConfigurationException {
        // Try default factory
        try {
            return XPathFactory.newInstance().newXPath();
        } catch (XPathFactoryConfigurationException e) {
            System.err.println("Default XPath factory failed: " + e.getMessage());
        }

        // Try Saxon explicitly
        try {
            XPathFactory saxonFactory = XPathFactory.newInstance(
                XPathFactory.DEFAULT_OBJECT_MODEL_URI,
                "net.sf.saxon.xpath.XPathFactoryImpl",
                null);
            return saxonFactory.newXPath();
        } catch (XPathFactoryConfigurationException e) {
            System.err.println("Saxon XPath factory failed: " + e.getMessage());
        }

        // Try JDK internal
        try {
            XPathFactory jdkFactory = XPathFactory.newInstance(
                XPathFactory.DEFAULT_OBJECT_MODEL_URI,
                "com.sun.org.apache.xpath.internal.jaxp.XPathFactoryImpl",
                null);
            return jdkFactory.newXPath();
        } catch (XPathFactoryConfigurationException e) {
            System.err.println("JDK XPath factory failed: " + e.getMessage());
        }

        throw new XPathFactoryConfigurationException(
            "No XPath factory implementation available");
    }
}

// Usage
XPath xpath = ResilientXPathFactory.createXPath();
String result = xpath.evaluate("//user/name", document);
```

### Fix 5: Verify and configure factory at application startup

```java
public class XPathConfigChecker {
    public static void checkXPathSupport() {
        try {
            XPathFactory factory = XPathFactory.newInstance();
            XPath xpath = factory.newXPath();

            // Test basic XPath compilation
            xpath.compile("//root");
            System.out.println("XPath support: OK (" + factory.getClass().getName() + ")");

            // Check XPath version support
            try {
                xpath.compile("//root[exists(@attr)]");
                System.out.println("XPath 2.0: supported");
            } catch (XPathExpressionException e) {
                System.out.println("XPath 2.0: not supported (XPath 1.0 only)");
            }
        } catch (XPathFactoryConfigurationException e) {
            System.err.println("XPath NOT available: " + e.getMessage());
        } catch (XPathExpressionException e) {
            System.err.println("XPath compilation test failed: " + e.getMessage());
        }
    }
}

// Call at application startup
XPathConfigChecker.checkXPathSupport();
```

## Prevention Checklist

- Always include an XPath implementation in the project dependencies.
- Test XPath factory creation at application startup.
- Use explicit factory class names when multiple XPath implementations are available.
- For XPath 2.0+ features, use Saxon or another 2.0+ implementation.
- Handle `XPathFactoryConfigurationException` with informative error messages.

## Related Errors

- [XPathException](../xpathexception) — base class for XPath errors.
- [XPathExpressionException](../xpathexpressionexception) — invalid XPath syntax.
- [FactoryConfigurationError](../factoryconfigurationerror-jaxp) — JAXP parser factory error.
