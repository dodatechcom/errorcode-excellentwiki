---
title: "[Solution] Java TransformerException — XSLT Transformation Fix"
description: "Fix Java TransformerException by validating XSLT stylesheet, checking input XML, and verifying transformer configuration."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# TransformerException — XSLT Transformation Fix

A `TransformerException` is thrown when an error occurs during XSLT transformation. This is part of the `javax.xml.transform` package and signals problems with the stylesheet, input XML, or transformer configuration.

## Description

The exception wraps the underlying cause of the transformation failure, which could be a stylesheet parsing error, invalid XML input, or configuration issue. The `TransformerException` contains a `Location` object that provides details about where the error occurred.

## Common Causes

```java
// Cause 1: Invalid XSLT stylesheet
TransformerFactory factory = TransformerFactory.newInstance();
Transformer transformer = factory.newTransformer(
    new StreamSource(new StringReader("<xsl:stylesheet>invalid</xsl:stylesheet>"))
); // TransformerException — malformed XSLT

// Cause 2: Null source or result
Transformer transformer = TransformerFactory.newInstance().newTransformer();
transformer.transform(null, null); // TransformerException — null source

// Cause 3: Missing required XSLT parameters
Transformer transformer = TransformerFactory.newInstance().newTransformer();
transformer.setParameter("outputDir", null);
// May cause issues during transformation

// Cause 4: Input XML does not match stylesheet expectations
String xml = "<root><data>value</data></root>";
String xsl = "<xsl:stylesheet><xsl:template match=\"missing\"><xsl:value-of select=\".\"/></xsl:template></xsl:stylesheet>";
// TransformerException — no matching template

// Cause 5: Output encoding not supported
Transformer transformer = TransformerFactory.newInstance().newTransformer();
transformer.setOutputProperty(OutputKeys.ENCODING, "INVALID-ENCODING");
// TransformerException — unsupported encoding
```

## Solutions

### Fix 1: Validate XSLT Stylesheet

```java
TransformerFactory factory = TransformerFactory.newInstance();
try {
    Source xslSource = new StreamSource(new File("style.xsl"));
    Transformer transformer = factory.newTransformer(xslSource);
} catch (TransformerException e) {
    System.err.println("Invalid XSLT: " + e.getMessage());
    System.err.println("Location: " + e.getLocationAsString());
}
```

### Fix 2: Check Input XML

```java
TransformerFactory factory = TransformerFactory.newInstance();
Transformer transformer = factory.newTransformer(new StreamSource(new File("style.xsl")));

Source xmlSource = new StreamSource(new File("input.xml"));
Result result = new StreamResult(new File("output.xml"));

try {
    transformer.transform(xmlSource, result);
} catch (TransformerException e) {
    System.err.println("Transformation failed: " + e.getMessage());
    if (e.getCause() != null) {
        System.err.println("Caused by: " + e.getCause().getMessage());
    }
}
```

### Fix 3: Verify Transformer Configuration

```java
TransformerFactory factory = TransformerFactory.newInstance();
Transformer transformer = factory.newTransformer();

// Set output properties before transformation
transformer.setOutputProperty(OutputKeys.INDENT, "yes");
transformer.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
transformer.setOutputProperty(OutputKeys.METHOD, "xml");

// Set parameters
transformer.setParameter("param1", "value1");

transformer.transform(xmlSource, result);
```

### Fix 4: Use ErrorListener for Detailed Diagnostics

```java
TransformerFactory factory = TransformerFactory.newInstance();
Transformer transformer = factory.newTransformer(new StreamSource(new File("style.xsl")));

transformer.setErrorListener(new ErrorListener() {
    @Override
    public void warning(TransformerException e) {
        System.err.println("Warning: " + e.getMessage());
    }

    @Override
    public void error(TransformerException e) {
        System.err.println("Error: " + e.getMessage());
        System.err.println("Location: " + e.getLocationAsString());
    }

    @Override
    public void fatalError(TransformerException e) {
        System.err.println("Fatal: " + e.getMessage());
    }
});
```

### Fix 5: Use URIResolver for External Resources

```java
TransformerFactory factory = TransformerFactory.newInstance();
Transformer transformer = factory.newTransformer(new StreamSource(new File("style.xsl")));

transformer.setURIResolver((href, base) -> {
    // Resolve relative paths
    Path resolvedPath = Paths.get(base).resolveSibling(href).normalize();
    if (Files.exists(resolvedPath)) {
        return new StreamSource(resolvedPath.toFile());
    }
    throw new TransformerException("Resource not found: " + href);
});
```

## Prevention Checklist

- Validate XSLT stylesheets before using them in transformation
- Check that input XML matches the expected structure for the stylesheet
- Set all transformer output properties before calling `transform()`
- Use `ErrorListener` for detailed error reporting in production
- Implement `URIResolver` for external resource resolution
- Test transformations with representative XML data

## Related Errors

- [SAXException]({{< relref "/languages/java/saxparseexception-detailed" >}}) — SAX parsing error
- [ParserConfigurationException]({{< relref "/languages/java/parserconfigurationexception" >}}) — parser configuration error
- [XMLStreamException]({{< relref "/languages/java/xmlstreamexception" >}}) — StAX parsing error
