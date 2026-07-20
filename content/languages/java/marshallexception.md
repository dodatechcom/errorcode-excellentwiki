---
title: "[Solution] Java MarshalException — XML Marshalling Fix"
description: "Fix javax.xml.bind.MarshalException by validating object graph, checking for circular references, and ensuring all fields are marshallable."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# MarshalException — XML Marshalling Fix

A `MarshalException` is thrown when marshalling a Java object to XML fails. This occurs when the object graph contains non-marshallable types, circular references, or when the Java-to-XML mapping is broken.

## Description

MarshalException extends JAXBException and signals a failure during the Java-to-XML conversion phase. It wraps errors such as inability to serialize a type, circular object references, or missing XML mappings.

Common message variants include:

- `MarshalException: ... has no @XmlRootElement annotation`
- `MarshalException: Class ... has two properties of the same name`
- `MarshalException: Circular reference to ... detected`
- `MarshalException: Unable to marshal type ...`

## Common Causes

```java
// Cause 1: Circular reference in object graph
public class Order {
    private Customer customer;
}
public class Customer {
    private List<Order> orders; // Each order holds customer, customer holds orders
}

// Cause 2: Non-marshallable type without XmlAdapter
public class User {
    private BigDecimal balance; // Custom type needs adapter
}

// Cause 3: Duplicate XML element names from different Java properties
public class Product {
    @XmlElement(name = "id")
    private String productId;
    @XmlElement(name = "id") // Duplicate — marshal fails
    private String orderId;
}
```

## Solutions

### Fix 1: Break circular references with @XmlTransient

```java
public class Order {
    private Customer customer;

    public Customer getCustomer() {
        return customer;
    }
}

public class Customer {
    private List<Order> orders;

    @XmlTransient // Prevents circular reference during marshalling
    public List<Order> getOrders() {
        return orders;
    }
}
```

### Fix 2: Provide XmlAdapter for custom types

```java
import javax.xml.bind.annotation.adapters.XmlAdapter;

public class BigDecimalAdapter extends XmlAdapter<String, BigDecimal> {
    @Override
    public BigDecimal unmarshal(String v) {
        return new BigDecimal(v);
    }

    @Override
    public String marshal(BigDecimal v) {
        return v.toPlainString();
    }
}

// Usage
@XmlJavaTypeAdapter(BigDecimalAdapter.class)
public BigDecimal getBalance() {
    return balance;
}
```

### Fix 3: Use @XmlIDREF to handle object references

```java
public class Order {
    @XmlIDREF
    private Customer customer; // Marshals as a reference, not full object
}

public class Customer {
    @XmlID
    private String id;
    private String name;
}
```

### Fix 4: Enable Marshaller properties for debugging

```java
JAXBContext context = JAXBContext.newInstance(Order.class);
Marshaller marshaller = context.createMarshaller();
marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

// Enable debugging output
marshaller.setProperty("com.sun.xml.bind.namespacePrefixMapper",
    new NamespacePrefixMapper() {
        @Override
        public String getPreferredPrefix(String namespaceUri, String suggestion, boolean requirePrefix) {
            return suggestion;
        }
    });

marshaller.marshal(order, System.out);
```

## Prevention Checklist

- Always break circular references with `@XmlTransient` or `@XmlIDREF`.
- Implement `XmlAdapter` for any custom types JAXB cannot handle.
- Ensure unique `@XmlElement(name = ...)` values across all properties in a class.
- Test marshalling complex object graphs early.
- Use `@XmlInverseReference` if bidirectional mapping is needed.

## Related Errors

- [JAXBException](../jaxbexception) — General JAXB binding error.
- [UnmarshalException](../unmarshalalexception) — XML to Java conversion failure.
- [StackOverflowError](../stackoverflowerror) — Infinite recursion in object graph.
