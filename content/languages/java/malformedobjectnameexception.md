---
title: "[Solution] Java MalformedObjectNameException — JMX ObjectName Fix"
description: "Fix Java javax.management.MalformedObjectNameException by using valid ObjectName format, checking domain and property syntax, and using ObjectName.quote() for special values."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 8
---

# MalformedObjectNameException — JMX ObjectName Fix

A `MalformedObjectNameException` is thrown when a string cannot be parsed into a valid JMX `ObjectName`. This occurs when the ObjectName format is incorrect, contains invalid characters, or uses improper domain/property syntax.

## Description

The `javax.management.MalformedObjectNameException` extends `javax.management.JMException` and is thrown by `ObjectName` constructors and `ObjectName.getInstance()` when the provided string does not conform to the JMX ObjectName syntax. An ObjectName has the format `domain:property1=value1,property2=value2` where the domain and property values must follow specific rules.

Common message variants:

- `javax.management.MalformedObjectNameException: Invalid character '=' in value part of property`
- `javax.management.MalformedObjectNameException: Empty domain`
- `javax.management.MalformedObjectNameException: Invalid property list`

Class hierarchy:

```
java.lang.Object
  └── java.lang.Throwable
        └── java.lang.Exception
              └── javax.management.JMException
                    └── javax.management.MalformedObjectNameException
```

## Common Causes

```java
// Cause 1: Missing domain
ObjectName name = ObjectName.getInstance(":type=MyMBean");  // No domain

// Cause 2: Invalid property separator
ObjectName name = ObjectName.getInstance("com.example;type=MyMBean");  // ; instead of :

// Cause 3: Invalid characters in property value
ObjectName name = ObjectName.getInstance("com.example:type=My MBean");  // Space in value

// Cause 4: Unclosed property list
ObjectName name = ObjectName.getInstance("com.example:type=MyMBean");  // OK
ObjectName name = ObjectName.getInstance("com.example:type=MyMBean");  // OK
// But: ObjectName.getInstance("com.example:type=MyMBean");  // Missing quote on special char

// Cause 5: Constructing ObjectName from user input
String userInput = request.getParameter("name");
ObjectName name = ObjectName.getInstance(userInput);  // May contain invalid chars

// Cause 6: Colon in property value without quoting
ObjectName name = ObjectName.getInstance("com.example:type=url,host=http://example.com");
// Colon in value must be quoted
```

## Solutions

### Fix 1: Use valid ObjectName format

```java
// Wrong — missing domain or wrong separators
ObjectName name1 = ObjectName.getInstance(":type=MyMBean");
ObjectName name2 = ObjectName.getInstance("com.example;type=MyMBean");

// Correct — proper format
ObjectName name = ObjectName.getInstance("com.example:type=MyMBean");

// Or use constructor for clarity
ObjectName name = new ObjectName("com.example", "type", "MyMBean");
```

### Fix 2: Quote special characters in property values

```java
// Wrong — unquoted special characters
ObjectName name = ObjectName.getInstance(
    "com.example:type=Service,host=http://example.com:8080");

// Correct — use ObjectName.quote() for values with special chars
String domain = "com.example";
String type = "Service";
String host = ObjectName.quote("http://example.com:8080");
ObjectName name = ObjectName.getInstance(
    domain + ":type=" + type + ",host=" + host);

// Or use the key=value constructor
ObjectName name = new ObjectName(
    domain, "type", "Service");
// For multiple properties, use quoted values
```

### Fix 3: Use ObjectName constructors for type safety

```java
// Wrong — manual string construction is error-prone
String nameStr = "com.example:type=" + type + ",name=" + name;
ObjectName objName = ObjectName.getInstance(nameStr);

// Correct — use ObjectName constructors
ObjectName objName = new ObjectName("com.example", "type", type);

// For multiple properties
Hashtable<String, String> props = new Hashtable<>();
props.put("type", "Service");
props.put("name", "MyService");
ObjectName objName = new ObjectName("com.example", props);
```

### Fix 4: Validate ObjectName before using

```java
// Correct — validate ObjectName format
public ObjectName createObjectName(String domain, String key, String value) {
    try {
        // Quote values that might contain special characters
        String safeValue = ObjectName.quote(value);
        return new ObjectName(domain + ":" + key + "=" + safeValue);
    } catch (MalformedObjectNameException e) {
        throw new IllegalArgumentException(
            "Invalid ObjectName: domain=" + domain + ", " + key + "=" + value, e);
    }
}

// Usage
ObjectName name = createObjectName("com.example", "type", "My Service: v1.0");
```

### Fix 5: Handle user-provided ObjectName strings safely

```java
// Correct — parse and validate user input
public ObjectName parseObjectName(String input) throws MalformedObjectNameException {
    if (input == null || input.isBlank()) {
        throw new MalformedObjectNameException("ObjectName must not be null or empty");
    }

    // Check basic format
    if (!input.contains(":")) {
        throw new MalformedObjectNameException(
            "ObjectName must contain domain and properties separated by ':'");
    }

    // Use ObjectName for full validation
    return ObjectName.getInstance(input);
}

// Safe wrapper that handles the exception
public ObjectName safeParseObjectName(String input) {
    try {
        return parseObjectName(input);
    } catch (MalformedObjectNameException e) {
        System.err.println("Invalid ObjectName: " + e.getMessage());
        return null;
    }
}
```

## Prevention Checklist

- Always use `ObjectName.quote()` for property values containing special characters (`:`, `,`, `=`, `*`, `?`).
- Use `ObjectName` constructors (`new ObjectName(domain, key, value)`) instead of string concatenation.
- Validate ObjectName strings from external sources before using them.
- Escape domain and property values that may contain JMX special characters.
- Test ObjectName construction with edge cases (special chars, empty values, unicode).

## Related Errors

- [InstanceNotFoundException](../instancenotfoundexception) — ObjectName does not match registered MBean.
- [InstanceAlreadyExistsException](../instancealreadyexistsexception) — MBean already registered with that ObjectName.
- [InvalidAttributeValueException](../invalidattributevalueexception) — invalid value set on MBean attribute.
