---
title: "[Solution] Java TransformerException — XSLT Transformation Fix"
description: "Fix Java TransformerException during XSLT transformation by validating XSLT stylesheet, checking input XML, and verifying transformer factory configuration."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 8
---

# TransformerException — XSLT Transformation Fix

A `TransformerException` is thrown when an XSLT transformation fails due to an invalid stylesheet, malformed input XML, misconfigured transformer factory, or errors during the transformation process itself. It wraps the underlying cause and includes location information.

## Description

The `javax.xml.transform.Transformer` API processes XML documents through XSLT stylesheets. When the stylesheet is invalid, the input XML is malformed, or the transformer encounters an error during processing, it throws `TransformerException`. The exception chain often contains a `SAXParseException` with precise line/column information.

Message variants:

- `javax.xml.transform.TransformerException: A network error occurred`
- `javax.xml.transform.TransformerException: com.sun.org.apache.xalan.internal.xsltc.TransletException`
- `org.xml.sax.SAXParseException: The reference to entity "x" ends with ';'`

## Common Causes

```java
// Cause 1: Invalid XSLT stylesheet
TransformerFactory factory = TransformerFactory.newInstance();
Source xslt = new StreamSource(new File("broken.xsl"));  // has syntax errors
Transformer transformer = factory.newTransformer(xslt);  // TransformerException

// Cause 2: Malformed input XML
Source xml = new StreamSource(new File("invalid.xml"));  // unclosed tags
transformer.transform(xml, result);  // TransformerException wrapping SAXParseException

// Cause 3: XSLT imports missing stylesheet
// stylesheet.xsl references <xsl:import href="common.xsl"/> but file is missing

// Cause 4: Security restrictions on external entities
// XSLT tries to access external file:// or http:// resources

// Cause 5: Output encoding not supported
 transformer.setOutputProperty(OutputKeys.ENCODING, "INVALID-ENCODING");
```

## Solutions

### Fix 1: Validate XSLT stylesheet before transformation

```java
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.Source;
import javax.xml.transform.stream.StreamSource;

public class XsltValidator {
    public static boolean validateStylesheet(String xsltPath) {
        try {
            TransformerFactory factory = TransformerFactory.newInstance();
            Source xslt = new StreamSource(new File(xsltPath));
            Transformer transformer = factory.newTransformer(xslt);
            System.out.println("Stylesheet is valid");
            return true;
        } catch (TransformerException e) {
            // Unwrap to find root cause
            Throwable cause = e;
            while (cause.getCause() != null) {
                cause = cause.getCause();
            }
            System.err.println("Stylesheet error: " + cause.getMessage());
            return false;
        }
    }
}
```

### Fix 2: Check input XML before transformation

```java
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.helpers.DefaultHandler;
import org.xml.sax.SAXParseException;

public static void validateInputXml(String xmlPath) {
    try {
        SAXParserFactory.newInstance().newSAXParser().parse(xmlPath, new DefaultHandler() {
            @Override
            public void error(SAXParseException e) {
                throw new RuntimeException(String.format(
                    "XML error at line %d, col %d: %s",
                    e.getLineNumber(), e.getColumnNumber(), e.getMessage()
                ), e);
            }
        });
    } catch (RuntimeException e) {
        throw new TransformerException("Input XML validation failed", e);
    } catch (Exception e) {
        throw new TransformerException("Cannot validate input XML", e);
    }
}
```

### Fix 3: Configure transformer factory with security restrictions

```java
TransformerFactory factory = TransformerFactory.newInstance();

// Disable external entity resolution
factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");
factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);

// Create transformer with safe configuration
Source xslt = new StreamSource(new File("template.xsl"));
Transformer transformer = factory.newTransformer(xslt);

// Set output properties explicitly
transformer.setOutputProperty(OutputKeys.INDENT, "yes");
transformer.setOutputProperty(OutputKeys.ENCODING, "UTF-8");

// Transform
Source xml = new StreamSource(new File("input.xml"));
StreamResult output = new StreamResult(new File("output.xml"));
transformer.transform(xml, output);
```

### Fix 4: Handle TransformerException with full cause chain

```java
try {
    TransformerFactory factory = TransformerFactory.newInstance();
    Transformer transformer = factory.newTransformer(new StreamSource("template.xsl"));
    transformer.transform(
        new StreamSource("input.xml"),
        new StreamResult(new File("output.xml"))
    );
} catch (TransformerException e) {
    // Print the full cause chain
    Throwable cause = e;
    while (cause != null) {
        System.err.println("Cause: " + cause.getClass().getSimpleName()
            + " — " + cause.getMessage());
        if (cause instanceof SAXParseException) {
            SAXParseException spe = (SAXParseException) cause;
            System.err.printf("  Line %d, Col %d in %s%n",
                spe.getLineNumber(), spe.getColumnNumber(), spe.getSystemId());
        }
        cause = cause.getCause();
    }
}
```

## Prevention Checklist

- Validate XSLT stylesheets independently before using them in production.
- Validate input XML before passing it to the transformer.
- Set `XMLConstants.FEATURE_SECURE_PROCESSING` and disable external access.
- Always handle `TransformerException` and unwrap the full cause chain.
- Use `setOutputProperty` to specify encoding explicitly.
- Test transformations with both valid and invalid inputs.

## Related Errors

- [SAXParseException](../saxparseexception) — XML syntax or schema errors
- [TransformerFactoryError](../transformerfactoryerror) — factory initialization failure
- [XMLStreamException](../xmlstreamexception) — StAX streaming parse errors
