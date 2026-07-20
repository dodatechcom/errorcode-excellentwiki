---
title: "[Solution] Java InvalidNameException — JNDI Name Format Invalid"
description: "Fix Java InvalidNameException by checking name format, using proper naming conventions, validating names before operations, and following provider-specific rules."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 1504
---

# InvalidNameException — JNDI Name Format Invalid

A `javax.naming.InvalidNameException` is thrown when a name is not valid for the specific naming or directory service being used.

## Description

`InvalidNameException` is a subclass of `NamingException` that indicates the name provided does not conform to the syntax rules of the naming system. Different JNDI providers (LDAP, RMI, COS, DNS) have different naming conventions and characters that are allowed or reserved.

**Message variants:**
- `javax.naming.InvalidNameException`
- `Invalid name`
- `Name contains invalid characters`
- `Malformed name`

## Common Causes

```java
// Cause 1: Using invalid characters for LDAP DN
Context ctx = new InitialContext();
ctx.bind("cn=John#Doe,dc=example,dc=com", obj); // InvalidNameException (# is special)

// Cause 2: Using forward slash in RMI binding name
Context ctx = new InitialContext();
ctx.bind("service/config", obj); // May be invalid depending on provider

// Cause 3: Empty name components
Context ctx = new InitialContext();
ctx.bind("ou=,dc=example,dc=com", obj); // Empty RDN value

// Cause 4: Unescaped special characters in LDAP names
Context ctx = new InitialContext();
ctx.bind("cn=John,Doe,dc=example,dc=com", obj); // Comma not escaped

// Cause 5: Name too long for the naming system
String longName = "cn=" + "a".repeat(10000) + ",dc=example,dc=com";
ctx.bind(longName, obj); // InvalidNameException
```

## Solutions

### Fix 1: Escape Special Characters in LDAP Names

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.directory.DirContext;
import javax.naming.directory.InitialDirContext;
import javax.naming.directory.Attribute;
import javax.naming.directory.Attributes;
import javax.naming.directory.BasicAttributes;

// Properly escape special characters in LDAP names
public static String escapeLdapName(String name) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < name.length(); i++) {
        char c = name.charAt(i);
        switch (c) {
            case '\\': sb.append("\\5c"); break;
            case ',':  sb.append("\\2c"); break;
            case '+':  sb.append("\\2b"); break;
            case '"':  sb.append("\\22"); break;
            case '<':  sb.append("\\3c"); break;
            case '>':  sb.append("\\3e"); break;
            case ';':  sb.append("\\3b"); break;
            default:   sb.append(c);
        }
    }
    return sb.toString();
}

// Usage
String safeRdn = escapeLdapName("John,Doe");
String fullDn = "cn=" + safeRdn + ",dc=example,dc=com";
```

### Fix 2: Validate Names Before JNDI Operations

```java
import javax.naming.Name;
import javax.naming.InvalidNameException;

public static boolean isValidLdapName(String name) {
    if (name == null || name.isEmpty()) return false;
    // LDAP names should not start or end with whitespace
    if (name.startsWith(" ") || name.endsWith(" ")) return false;
    // Check for unescaped special characters at component boundaries
    String[] rdnParts = name.split("(?<!\\\\),");
    for (String part : rdnParts) {
        String trimmed = part.trim();
        if (trimmed.isEmpty()) return false;
        int eqIndex = trimmed.indexOf('=');
        if (eqIndex <= 0 || eqIndex == trimmed.length() - 1) return false;
    }
    return true;
}

// Usage
String name = "cn=John Doe,dc=example,dc=com";
if (isValidLdapName(name)) {
    ctx.bind(name, obj);
} else {
    System.err.println("Invalid LDAP name: " + name);
}
```

### Fix 3: Use CompositeName or Name Parser for Complex Names

```java
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.InvalidNameException;
import javax.naming.CompositeName;

Context ctx = new InitialContext();

// Use CompositeName for names with multiple components
String complexName = "ou=sales+cn=John Doe";
CompositeName compositeName = new CompositeName();
compositeName.add(complexName);

try {
    Object obj = ctx.lookup(compositeName);
} catch (InvalidNameException e) {
    System.err.println("Invalid name format: " + e.getMessage());
}
```

### Fix 4: Use DirContext for Attribute-Based Operations

```java
import javax.naming.directory.DirContext;
import javax.naming.directory.InitialDirContext;
import javax.naming.directory.Attribute;
import javax.naming.directory.Attributes;
import javax.naming.directory.BasicAttribute;
import javax.naming.directory.BasicAttributes;

Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY,
        "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389");

DirContext ctx = new InitialDirContext(env);

// Use attributes for creation instead of encoding everything in the name
Attributes attrs = new BasicAttributes();
Attribute oc = new BasicAttribute("objectClass");
oc.add("inetOrgPerson");
attrs.put(oc);
attrs.put(new BasicAttribute("cn", "John Doe"));
attrs.put(new BasicAttribute("sn", "Doe"));

ctx.createSubcontext("cn=John\\20Doe,ou=users,dc=example,dc=com", attrs);
```

## Prevention Checklist

- Always escape special characters in LDAP distinguished names
- Validate name syntax before performing JNDI operations
- Use the naming system's parser (`NameParser`) to construct names
- Use attribute-based operations via `DirContext` instead of encoding data in names
- Consult provider documentation for allowed characters and naming rules
- Test name validation against the target naming service schema

## Related Errors

- [NamingException](/languages/java/namingexception) — Base JNDI exception
- [MalformedURLException](/languages/java/malformedurlexception-jndi) — JNDI URL is malformed
- [NameNotFoundException](/languages/java/namenotfoundexception-jndi) — Name not found in context
- [ContextNotEmptyException](/languages/java/contextnotemptyexception) — Cannot destroy non-empty context
