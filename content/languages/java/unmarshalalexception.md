---
title: "[Solution] Java UnmarshalException — XML Unmarshalling Fix"
description: "Fix javax.xml.bind.UnmarshalException by validating XML against schema, checking @XmlElement annotations, and handling nil elements properly."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnmarshalException — XML Unmarshalling Fix

A `UnmarshalException` is thrown when unmarshalling XML content into a Java object fails. This occurs when the XML structure does not match the expected Java class model, contains unexpected elements, or violates validation constraints.

## Description

UnmarshalException extends JAXBException and signals a failure during the XML-to-Java conversion phase. It wraps more specific errors about what went wrong during unmarshalling, such as unexpected elements, type mismatches, or missing required fields.

Common message variants include:

- `UnmarshalException: unexpected element (uri:"...", local:"...")`
- `UnmarshalException: Unable to create contextual instance of type ...`
- `UnmarshalException: null or empty value for ...`
- `UnmarshalException: Property ... is read-only`

## Common Causes

```java
// Cause 1: XML contains elements not mapped in the Java class
// XML: <user><name>John</name><extra>data</extra></user>
// Java class has no field for "extra" element

// Cause 2: Missing @XmlElement annotation on a required field
public class User {
    private String name; // No @XmlElement — JAXB may not map it correctly
}

// Cause 3: nil element without proper annotation
// XML: <user><name xsi:nil="true"/></user>
// @XmlElement with required=true causes failure on nil
```

## Solutions

### Fix 1: Validate XML against the expected schema

```java
import javax.xml.bind.*;
import javax.xml.transform.stream.StreamSource;
import java.io.StringReader;

String xml = "<user><name>John</name></user>";
JAXBContext context = JAXBContext.newInstance(User.class);
Unmarshaller unmarshaller = context.createUnmarshaller();

// Enable schema validation to catch mismatches early
SchemaFactory sf = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
Schema schema = sf.newSchema(new File("user.xsd"));
unmarshaller.setSchema(schema);

try {
    User user = (User) unmarshaller.unmarshal(new StreamSource(new StringReader(xml)));
} catch (UnmarshalException e) {
    System.err.println("XML does not match expected structure: " + e.getMessage());
}
```

### Fix 2: Add proper @XmlElement annotations

```java
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAccessType;

@XmlRootElement(name = "user")
@XmlAccessorType(XmlAccessType.FIELD)
public class User {
    @XmlElement(name = "name", required = true)
    private String name;

    @XmlElement(name = "email", required = false)
    private String email;
}
```

### Fix 3: Handle nil elements correctly

```java
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlElementWrapper;

public class User {
    @XmlElement(name = "phone", required = false, nillable = true)
    private String phone;

    @XmlElementWrapper(name = "addresses")
    @XmlElement(name = "address", nillable = true)
    private List<String> addresses;
}
```

### Fix 4: Use an Unmarshaller.Listener to catch errors

```java
JAXBContext context = JAXBContext.newInstance(User.class);
Unmarshaller unmarshaller = context.createUnmarshaller();

unmarshaller.setListener(new Unmarshaller.Listener() {
    @Override
    public void beforeUnmarshal(Object target, Object parent) {
        // Validate before unmarshalling
    }

    @Override
    public void afterUnmarshal(Object target, Object parent) {
        // Post-process after unmarshalling
        if (target instanceof User) {
            User user = (User) target;
            if (user.getName() == null) {
                throw new UnmarshalException("Name cannot be null");
            }
        }
    }
});
```

## Prevention Checklist

- Always validate XML against an XSD schema before unmarshalling.
- Use `@XmlElement(required = true)` for mandatory fields.
- Mark optional fields with `required = false` and `nillable = true` if needed.
- Test unmarshalling with well-formed and malformed XML samples.
- Use `@XmlTransient` to ignore unexpected XML elements.

## Related Errors

- [JAXBException](../jaxbexception) — General JAXB binding error.
- [MarshalException](../marshallexception) — Java to XML conversion failure.
- [SAXParseException](../saxparseexception) — XML parsing failure.
