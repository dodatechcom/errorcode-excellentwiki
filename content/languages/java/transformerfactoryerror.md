---
title: "[Solution] Java TransformerFactoryConfigurationError — XSLT Stylesheet Compilation Failure"
description: "Fix Java TransformerFactoryConfigurationError by validating XSLT stylesheets, checking classpath for XSLT processor, and correcting TransformerFactory setup."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 44
---

# TransformerFactoryConfigurationError — XSLT Stylesheet Compilation Failure

A `TransformerFactoryConfigurationError` is thrown when `javax.xml.transform.TransformerFactory` encounters an error during XSLT stylesheet compilation or factory configuration. Unlike `TransformerConfigurationException` (a recoverable exception), this `Error` subclass indicates an unrecoverable problem — such as a missing XSLT processor, an invalid stylesheet, or a broken factory configuration. It is the XSLT counterpart to `SchemaFactoryConfigurationError`.

## Description

Java's XSLT processing relies on `TransformerFactory` to compile stylesheets into `Transformer` objects. When the factory cannot be configured — for example, if the JAXP XSLT processor is missing from the classpath, the stylesheet references unsupported extensions, or the stylesheet itself is structurally invalid — a `TransformerFactoryConfigurationError` is thrown.

Common message variants:

- `TransformerFactoryConfigurationError: Could not compile stylesheet` — syntax or structural error in XSLT.
- `TransformerFactoryConfigurationError: No TransformerFactory implementation found` — classpath issue.
- `TransformerFactoryConfigurationError: Failed to create TransformerFactory` — factory instantiation failure.
- `TransformerFactoryConfigurationError: Invalid stylesheet URI` — referenced stylesheet resource not found.

## Common Causes

```java
// Cause 1: Missing XSLT processor on classpath
TransformerFactory factory = TransformerFactory.newInstance();
// TransformerFactoryConfigurationError: no JAXP processor available

// Cause 2: Invalid XSLT stylesheet syntax
TransformerFactory factory = TransformerFactory.newInstance();
Source xslt = new StreamSource(new File("broken.xslt"));
Transformer transformer = factory.newTransformer(xslt);
// Error if XSLT has syntax errors or unsupported elements

// Cause 3: Trying to load a non-XSLT file as a stylesheet
Source xslt = new StreamSource(new File("data.xml"));  // not an XSLT file
Transformer transformer = factory.newTransformer(xslt);  // configuration error

// Cause 4: Factory attribute set to invalid value
TransformerFactory factory = TransformerFactory.newInstance();
factory.setAttribute("http://javax.xml.XMLConstants/property/accessExternalDTD",
    "invalid-value");  // TransformerFactoryConfigurationError

// Cause 5: Stylesheet references non-existent imported/included files
// stylesheet.xslt has: <xsl:import href="missing-module.xslt"/>
// The imported file does not exist — error during compilation
```

## Solutions

### Fix 1: Ensure XSLT processor is on the classpath

```xml
<!-- Maven: Add Saxon as the XSLT processor -->
<dependency>
    <groupId>net.sf.saxon</groupId>
    <artifactId>Saxon-HE</artifactId>
    <version>12.4</version>
</dependency>

<!-- Or use Xalan -->
<dependency>
    <groupId>xalan</groupId>
    <artifactId>xalan</artifactId>
    <version>2.7.3</version>
</dependency>
```

```bash
# Verify which XSLT processor is being used
java -Djavax.xml.transform.TransformerFactory= \
    net.sf.saxon.TransformerFactoryImpl -jar myapp.jar

# Check classpath for JAXP providers
java -verbose:class -jar myapp.jar 2>&1 | grep -i "transform\|xslt\|saxon\|xalan"
```

### Fix 2: Validate XSLT stylesheet before compiling

```java
import javax.xml.transform.*;
import javax.xml.transform.stream.*;
import java.io.*;

public class SafeXsltCompiler {
    public static Transformer compileStylesheet(File xsltFile) {
        if (!xsltFile.exists()) {
            throw new IllegalArgumentException(
                "Stylesheet not found: " + xsltFile);
        }

        TransformerFactory factory = TransformerFactory.newInstance();

        // Set security features to prevent XXE attacks
        try {
            factory.setAttribute(
                javax.xml.XMLConstants.ACCESS_EXTERNAL_DTD, "");
            factory.setAttribute(
                javax.xml.XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");
        } catch (IllegalArgumentException e) {
            // attribute not supported by this implementation
        }

        try {
            Source xsltSource = new StreamSource(xsltFile);
            return factory.newTransformer(xsltSource);
        } catch (TransformerConfigurationException e) {
            throw new TransformerFactoryConfigurationError(
                "Invalid stylesheet " + xsltFile.getName()
                + ": " + e.getMessage(), e);
        }
    }
}
```

### Fix 3: Set security properties to prevent XXE in stylesheets

```java
import javax.xml.transform.TransformerFactory;
import javax.xml.XMLConstants;

TransformerFactory factory = TransformerFactory.newInstance();

// Prevent external entity injection via XSLT
factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");
factory.setAttribute(XMLConstants.SUPPORT_DTD, false);

// Safe to compile now
Transformer transformer = factory.newTransformer(
    new StreamSource(new File("safe.xslt")));
```

### Fix 4: Use classpath resources for reliable stylesheet loading

```java
import javax.xml.transform.*;
import javax.xml.transform.stream.*;

public class ClasspathXsltLoader {
    public static Transformer loadFromClasspath(String resourcePath) {
        InputStream is = ClasspathXsltLoader.class
            .getResourceAsStream(resourcePath);

        if (is == null) {
            throw new IllegalArgumentException(
                "Stylesheet not found on classpath: " + resourcePath);
        }

        TransformerFactory factory = TransformerFactory.newInstance();

        try {
            return factory.newTransformer(new StreamSource(is));
        } catch (TransformerConfigurationException e) {
            throw new TransformerFactoryConfigurationError(
                "Cannot compile stylesheet from classpath resource "
                + resourcePath + ": " + e.getMessage(), e);
        }
    }
}

// Usage
Transformer transformer = ClasspathXsltLoader
    .loadFromClasspath("/xslt/transform.xslt");
```

### Fix 5: Cache compiled Transformers to avoid repeated compilation

```java
import java.util.concurrent.ConcurrentHashMap;
import java.io.File;
import javax.xml.transform.*;
import javax.xml.transform.stream.*;

public class TransformerCache {
    private static final ConcurrentHashMap<String, Transformer> cache =
        new ConcurrentHashMap<>();

    public static Transformer getTransformer(String xsltPath) {
        return cache.computeIfAbsent(xsltPath, path -> {
            TransformerFactory factory = TransformerFactory.newInstance();
            try {
                return factory.newTransformer(new StreamSource(new File(path)));
            } catch (TransformerConfigurationException e) {
                throw new TransformerFactoryConfigurationError(
                    "Failed to compile stylesheet: " + path, e);
            }
        });
    }
}
```

## Prevention Checklist

- Include a known XSLT processor (Saxon, Xalan) as an explicit dependency — don't rely on the JRE's built-in one.
- Validate XSLT files during build or at deployment, not at runtime.
- Set `ACCESS_EXTERNAL_DTD` and `ACCESS_EXTERNAL_STYLESHEET` to `""` to prevent XXE attacks.
- Cache compiled `Transformer` objects — stylesheet compilation is expensive.
- Test all stylesheets in integration tests before deploying to production.

## Related Errors

- [TransformerConfigurationException](../transformerconfigurationexception) — recoverable version of this error with structured error info.
- [SchemaFactoryConfigurationError](schemaconfigurationerror) — similar error for XML schema compilation.
- [SAXParseException](../saxparseexception) — XML parsing errors in the stylesheet file.
