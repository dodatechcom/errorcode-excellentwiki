---
title: "[Solution] Java ParserConfigurationException — Parser Config Fix"
description: "Fix Java ParserConfigurationException by checking parser factory configuration, verifying features/properties, and ensuring correct classpath."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ParserConfigurationException — Parser Config Fix

A `ParserConfigurationException` is thrown when a parser is not properly configured or when a requested configuration cannot be satisfied. This is part of the `java.xml.parsers` package and occurs during SAX or DOM parser setup.

## Description

The exception occurs when the `DocumentBuilderFactory` or `SAXParserFactory` is configured with invalid features, properties, or settings. The message typically indicates which configuration option caused the failure.

## Common Causes

```java
// Cause 1: Setting unsupported feature
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
factory.setFeature("http://xml.org/sax/features/unsupported-feature", true);
DocumentBuilder builder = factory.newDocumentBuilder(); // ParserConfigurationException

// Cause 2: Setting invalid property
SAXParserFactory factory = SAXParserFactory.newInstance();
factory.setFeature("http://javax.xml.XMLConstants/feature/secure-processing", true);
// May throw if feature not supported by implementation

// Cause 3: Mixing incompatible configurations
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
factory.setValidating(true);
factory.setNamespaceAware(false); // conflicting with some validation features

// Cause 4: Missing parser implementation on classpath
// If no SAX parser is available, factory.newDocumentBuilder() fails

// Cause 5: Setting feature after creating parser
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
DocumentBuilder builder = factory.newDocumentBuilder();
factory.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);
// Configuration change after parser creation
```

## Solutions

### Fix 1: Verify Parser Factory Configuration

```java
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
try {
    // Set features before creating parser
    factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
    factory.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);
    DocumentBuilder builder = factory.newDocumentBuilder();
} catch (ParserConfigurationException e) {
    System.err.println("Parser config error: " + e.getMessage());
}
```

### Fix 2: Check Feature Support Before Setting

```java
SAXParserFactory factory = SAXParserFactory.newInstance();
String feature = "http://javax.xml.XMLConstants/feature/secure-processing";
try {
    factory.setFeature(feature, true);
} catch (SAXNotRecognizedException | SAXNotSupportedException e) {
    System.err.println("Feature not supported: " + feature);
}
```

### Fix 3: Ensure Correct Classpath

```java
// Verify parser implementation is available
try {
    Class.forName("com.sun.org.apache.xerces.internal.jaxp.DocumentBuilderFactoryImpl");
    System.out.println("Parser implementation found");
} catch (ClassNotFoundException e) {
    System.err.println("Parser implementation missing from classpath");
}
```

### Fix 4: Configure All Settings Before Creating Parser

```java
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();

// Configure all settings first
factory.setNamespaceAware(true);
factory.setValidating(false);
factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);

// Then create parser
DocumentBuilder builder = factory.newDocumentBuilder();
```

### Fix 5: Use Default Configuration as Fallback

```java
DocumentBuilderFactory factory;
try {
    factory = DocumentBuilderFactory.newInstance();
    factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
} catch (Exception e) {
    // Fall back to default configuration
    factory = DocumentBuilderFactory.newInstance();
}
DocumentBuilder builder = factory.newDocumentBuilder();
```

## Prevention Checklist

- Set all factory features and properties before calling `newDocumentBuilder()`
- Verify feature support using `SAXNotRecognizedException` / `SAXNotSupportedException` catches
- Ensure XML parser implementation (Xerces, JDK built-in) is on the classpath
- Use `XMLConstants.FEATURE_SECURE_PROCESSING` for security
- Test parser configuration in unit tests
- Document required XML parser version in project README

## Related Errors

- [SAXException]({{< relref "/languages/java/saxparseexception-detailed" >}}) — SAX parsing error
- [TransformerException]({{< relref "/languages/java/transformerexception" >}}) — XSLT transformation error
- [XMLStreamException]({{< relref "/languages/java/xmlstreamexception" >}}) — StAX parsing error
