---
title: "[Solution] Java IllegalDataException — XML Data Fix"
description: "Fix org.xml.sax.IllegalDataException by validating XML input, escaping special characters, and checking encoding."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# IllegalDataException — XML Data Fix

An `IllegalDataException` is thrown when XML data is not legal according to the XML specification. This is part of the `org.xml.sax` package and occurs during SAX parsing when the parser encounters invalid data.

## Description

The exception is part of SAX (Simple API for XML) and signals that the XML data being processed contains illegal characters, improper encoding, or data that violates XML well-formedness rules. The message typically includes details about the specific data violation.

## Common Causes

```java
// Cause 1: Illegal characters in XML content
String xml = "<root>Hello\u0000World</root>"; // null character is illegal

// Cause 2: Invalid XML encoding declaration
String xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<root>caf\u00e9</root>";
// If file is actually encoded in ISO-8859-1 but declared as UTF-8

// Cause 3: Unescaped special characters
String xml = "<root>price < 100 & quantity > 5</root>"; // & and < must be escaped

// Cause 4: Binary data in XML content
byte[] data = new byte[]{0x00, 0x01, 0x02};
String xml = "<root>" + new String(data) + "</root>"; // illegal XML characters

// Cause 5: CDATA section with illegal sequence
String xml = "<root><![CDATA[data ]] > more]]></root>"; // ]]> ends CDATA prematurely
```

## Solutions

### Fix 1: Validate XML Input Before Parsing

```java
import javax.xml.XMLConstants;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;

SchemaFactory factory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
Schema schema = factory.newSchema(new StreamSource("schema.xsd"));
Validator validator = schema.newValidator();
validator.validate(new StreamSource(new StringReader(xml)));
```

### Fix 2: Escape Special Characters

```java
public class XMLEscaper {
    public static String escape(String input) {
        return input
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\"", "&quot;")
            .replace("'", "&apos;");
    }
}
```

### Fix 3: Check and Normalize Encoding

```java
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

// Ensure consistent encoding
byte[] bytes = xmlString.getBytes(StandardCharsets.UTF_8);
String normalized = new String(bytes, StandardCharsets.UTF_8);

// Verify encoding matches declaration
if (!Charset.isSupported("UTF-8")) {
    throw new IllegalDataException("UTF-8 encoding not supported");
}
```

### Fix 4: Strip Illegal XML Characters

```java
public class XMLSanitizer {
    public static String stripIllegalChars(String input) {
        return input.replaceAll("[\\x00-\\x08\\x0B\\x0C\\x0E-\\x1F]", "");
    }
}
```

### Fix 5: Use Proper XML Builder

```java
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
factory.setValidating(true);
DocumentBuilder builder = factory.newDocumentBuilder();
Document doc = builder.newDocument();
Element root = doc.createElement("root");
root.setTextContent("safe content"); // properly escaped
```

## Prevention Checklist

- Always validate XML input before parsing
- Use XML escape sequences for special characters (`&`, `<`, `>`, `"`, `'`)
- Ensure file encoding matches the XML declaration
- Strip or replace illegal XML characters (control characters below 0x20)
- Use XML builder APIs instead of string concatenation
- Test XML parsers with edge-case inputs

## Related Errors

- [SAXException]({{< relref "/languages/java/saxparseexception-detailed" >}}) — general SAX parsing error
- [ParserConfigurationException]({{< relref "/languages/java/parserconfigurationexception" >}}) — parser not properly configured
- [TransformerException]({{< relref "/languages/java/transformerexception" >}}) — XSLT transformation error
