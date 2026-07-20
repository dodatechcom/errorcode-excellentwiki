---
title: "[Solution] Java FactoryConfigurationError — JAXP Parser Factory Error Fix"
description: "Fix javax.xml.parsers.FactoryConfigurationError by checking classpath for parser implementation, verifying factory class name, and handling missing provider."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 444
---

# FactoryConfigurationError — JAXP Parser Factory Error Fix

A `FactoryConfigurationError` is thrown when a parser factory (SAX, DOM, or Schema) cannot be instantiated due to configuration problems. This indicates that the JAXP implementation is missing or misconfigured.

## Description

`javax.xml.parsers.FactoryConfigurationError` extends `Error` (not `Exception`) and indicates a fatal configuration problem with the XML parser factory. It occurs when:

- The factory class specified in system properties or classpath cannot be found
- The factory class exists but cannot be instantiated
- The JAXP implementation jar is missing from the classpath

Common message variants:

- `FactoryConfigurationError: Provider org.apache.xerces.jaxp.SAXParserFactoryImpl not found`
- `FactoryConfigurationError: SAXParserFactory class not found`
- `FactoryConfigurationError: Cannot instantiate factory class`

## Common Causes

```java
// Cause 1: Missing JAXP implementation in classpath
SAXParserFactory factory = SAXParserFactory.newInstance();
// FactoryConfigurationError if no JAXP implementation is available

// Cause 2: Wrong factory class name in system property
System.setProperty("javax.xml.parsers.SAXParserFactory",
    "com.nonexistent.package.MySAXParserFactory");
SAXParserFactory factory = SAXParserFactory.newInstance();
// FactoryConfigurationError: class not found

// Cause 3: Conflicting JAXP versions in classpath
// Multiple XML parser implementations causing class loading issues
SAXParserFactory factory = SAXParserFactory.newInstance();
// FactoryConfigurationError: wrong version loaded

// Cause 4: Module system blocking XML parser access (Java 9+)
// Missing module declaration for XML parsing
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
// FactoryConfigurationError: module access denied

// Cause 5: Security manager preventing factory instantiation
System.setSecurityManager(new SecurityManager());
SAXParserFactory factory = SAXParserFactory.newInstance();
// FactoryConfigurationError: security exception during instantiation
```

## Solutions

### Fix 1: Ensure JAXP implementation is on the classpath

```xml
<!-- Maven: Add an XML parser implementation -->
<dependency>
    <groupId>org.apache.xerces</groupId>
    <artifactId>xercesImpl</artifactId>
    <version>2.12.2</version>
</dependency>

<!-- Or use the JDK built-in (Java 9+) -->
<!-- No additional dependency needed if using JDK's built-in XML -->
```

```java
// Verify the factory can be instantiated
try {
    SAXParserFactory factory = SAXParserFactory.newInstance();
    System.out.println("SAX parser factory: " + factory.getClass().getName());
} catch (FactoryConfigurationError e) {
    System.err.println("Cannot create SAX parser factory: " + e.getMessage());
    System.err.println("Add xercesImpl or another XML parser to classpath");
}
```

### Fix 2: Check and fix system property configuration

```java
// Check what factory class is being used
String saxFactoryClass = System.getProperty("javax.xml.parsers.SAXParserFactory");
String domFactoryClass = System.getProperty("javax.xml.parsers.DocumentBuilderFactory");
String transformerClass = System.getProperty("javax.xml.transform.TransformerFactory");

System.out.println("SAX factory: " + saxFactoryClass);
System.out.println("DOM factory: " + domFactoryClass);
System.out.println("Transformer factory: " + transformerClass);

// Fix: Set to known working implementations
System.setProperty("javax.xml.parsers.SAXParserFactory",
    "org.apache.xerces.jaxp.SAXParserFactoryImpl");
System.setProperty("javax.xml.parsers.DocumentBuilderFactory",
    "org.apache.xerces.jaxp.DocumentBuilderFactoryImpl");
```

### Fix 3: Use try-catch with fallback parsers

```java
public class ResilientXmlParser {
    public static SAXParser createSAXParser() throws SAXException, FactoryConfigurationError {
        SAXParserFactory factory = null;

        // Try default factory first
        try {
            factory = SAXParserFactory.newInstance();
            return factory.newSAXParser();
        } catch (FactoryConfigurationError e) {
            System.err.println("Default SAX factory failed: " + e.getMessage());
        }

        // Try Xerces explicitly
        try {
            factory = SAXParserFactory.newInstance(
                "org.apache.xerces.jaxp.SAXParserFactoryImpl", null);
            return factory.newSAXParser();
        } catch (FactoryConfigurationError e) {
            System.err.println("Xerces SAX factory failed: " + e.getMessage());
        }

        // Try JDK built-in
        try {
            factory = SAXParserFactory.newInstance(
                "com.sun.org.apache.xerces.internal.jaxp.SAXParserFactoryImpl", null);
            return factory.newSAXParser();
        } catch (FactoryConfigurationError e) {
            System.err.println("JDK SAX factory failed: " + e.getMessage());
        }

        throw new FactoryConfigurationError("No working SAX parser factory available");
    }
}
```

### Fix 4: Configure module access for Java 9+

```java
// In module-info.java, ensure XML module is accessible:
// requires java.xml;

// Or run with JVM flags:
// --add-opens java.xml/com.sun.org.apache.xerces.internal.jaxp=ALL-UNNAMED
```

```java
// Verify XML module is available
try {
    Class.forName("javax.xml.parsers.SAXParserFactory");
    System.out.println("XML module is available");
} catch (ClassNotFoundException e) {
    System.err.println("XML module not available — add java.xml module");
}
```

## Prevention Checklist

- Always include an XML parser implementation in the project dependencies.
- Don't set JAXP system properties unless you have a specific parser to use.
- Test XML parsing on all target deployment environments.
- For Java 9+, ensure `java.xml` module is accessible.
- Handle `FactoryConfigurationError` with informative error messages.

## Related Errors

- [XPathException](../xpathexception) — XPath-related errors.
- [SAXException](../saxexception) — SAX parsing errors.
- [ClassNotFoundException](../classnotfound-generic) — missing implementation class.
