---
title: "[Solution] Java SAXParseException — XML Syntax and Schema Fix"
description: "Fix Java SAXParseException with line/column info by checking XML syntax, validating against schema, and using error handler for detailed reporting."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 8
---

# SAXParseException — XML Syntax and Schema Fix

A `SAXParseException` is thrown during XML parsing when the parser encounters a syntax error, malformed structure, or schema validation failure. It extends `SAXException` and includes precise line and column numbers for pinpointing the error location.

## Description

The SAX (Simple API for XML) parser reports errors through an `ErrorHandler`. When it encounters invalid XML, it wraps the error in a `SAXParseException` that contains the system ID (file path/URL), line number, and column number. This makes it one of the most informative XML exceptions.

Message variants:

- `org.xml.sax.SAXParseException; lineNumber: 5; columnNumber: 12; The element type "br" must be terminated by the matched end-tag "</br>".`
- `org.xml.sax.SAXParseException; lineNumber: 1; columnNumber: 1; Content is not allowed in prolog.`
- `org.xml.sax.SAXParseException: cvc-complex-type.2.4.a: Invalid content was found starting with element 'name'.`

## Common Causes

```java
// Cause 1: Unclosed XML tag
// <user><name>John</user>  → missing </name>

// Cause 2: Malformed XML entity
// <description>Tom & Jerry</description>  → & should be &amp;

// Cause 3: Wrong encoding declaration
// <?xml version="1.0" encoding="UTF-8"?> but file contains non-UTF-8 characters

// Cause 4: Schema validation failure
// <age>not-a-number</age> when schema defines <xs:element name="age" type="xs:int"/>

// Cause 5: Duplicate attribute in XML tag
// <user id="1" id="2">  → duplicate attribute
```

## Solutions

### Fix 1: Check XML syntax using an error handler

```java
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.helpers.DefaultHandler;
import org.xml.sax.SAXParseException;
import org.xml.sax.SAXException;

public class XmlValidator {
    public static void validate(String filePath) {
        try {
            SAXParserFactory factory = SAXParserFactory.newInstance();
            factory.setValidating(false);
            SAXParser parser = factory.newSAXParser();

            parser.parse(filePath, new DefaultHandler() {
                @Override
                public void error(SAXParseException e) {
                    System.err.printf("ERROR at line %d, col %d: %s%n",
                        e.getLineNumber(), e.getColumnNumber(), e.getMessage());
                }

                @Override
                public void fatalError(SAXParseException e) {
                    System.err.printf("FATAL at line %d, col %d: %s%n",
                        e.getLineNumber(), e.getColumnNumber(), e.getMessage());
                }

                @Override
                public void warning(SAXParseException e) {
                    System.err.printf("WARNING at line %d: %s%n",
                        e.getLineNumber(), e.getMessage());
                }
            });

            System.out.println("XML is well-formed");
        } catch (Exception e) {
            System.err.println("Parse error: " + e.getMessage());
        }
    }
}
```

### Fix 2: Validate against XML Schema (XSD)

```java
import javax.xml.XMLConstants;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;
import java.io.File;

public class XsdValidator {
    public static void validate(String xmlPath, String xsdPath) throws Exception {
        SchemaFactory factory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
        Schema schema = schemaFactory.newSchema(new File(xsdPath));
        Validator validator = schema.newValidator();

        validator.setErrorHandler(new DefaultHandler() {
            @Override
            public void error(SAXParseException e) {
                System.err.printf("Validation error at line %d: %s%n",
                    e.getLineNumber(), e.getMessage());
            }
        });

        validator.validate(new StreamSource(new File(xmlPath)));
    }
}
```

### Fix 3: Use SAXParser with full error reporting

```java
SAXParserFactory factory = SAXParserFactory.newInstance();
factory.setNamespaceAware(true);

// Enable schema validation
factory.setValidating(true);
factory.setProperty(
    "http://java.sun.com/xml/jaxp/properties/schemaLanguage",
    "http://www.w3.org/2001/XMLSchema"
);

SAXParser parser = factory.newSAXParser();
parser.setProperty("http://apache.org/xml/features/disallow-doctype-decl", true);

parser.parse("input.xml", new DefaultHandler() {
    @Override
    public void error(SAXParseException e) {
        throw new RuntimeException(String.format(
            "XML Error at line %d col %d in %s: %s",
            e.getLineNumber(),
            e.getColumnNumber(),
            e.getSystemId(),
            e.getMessage()
        ), e);
    }
});
```

### Fix 4: Pre-validate XML content before parsing

```java
public static String findXmlIssue(String xmlContent) {
    try {
        SAXParserFactory.newInstance().newSAXParser()
            .parse(new InputSource(new StringReader(xmlContent)), new DefaultHandler());
        return null;  // no issues
    } catch (SAXParseException e) {
        return String.format("Line %d, Col %d: %s",
            e.getLineNumber(), e.getColumnNumber(), e.getMessage());
    } catch (Exception e) {
        return e.getMessage();
    }
}
```

## Prevention Checklist

- Always register an `ErrorHandler` on the SAX parser to get line/column details.
- Validate XML against XSD schema in addition to well-formedness checks.
- Use `setNamespaceAware(true)` for namespace-aware parsing.
- Pre-validate XML strings before parsing in production code.
- Use `setFeature` to disable external entities and DTDs for security.
- Test XML parsing with intentionally malformed input to verify error handling.

## Related Errors

- [SAXException](../saxparseexception) — parent SAX parsing exception
- [TransformerException](../transformerexception) — XSLT transformation errors
- [XMLStreamException](../xmlstreamexception) — StAX parsing errors
- [XPathException](../xpathexception) — XPath evaluation errors
