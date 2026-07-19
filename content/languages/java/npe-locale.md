---
title: "[Solution] Java NullPointerException"
description: "Locale and Resource Bundle Null Lookup"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# looking up locale resources where key or bundle is missing

A `looking` is thrown when properties props = new properties();.

## Common Causes

```java
Properties props = new Properties();
props.load(new FileInputStream("app.properties"));
String v = props.getProperty("missing.key");  // null
v.toUpperCase();  // NPE
```

## Solutions

```java
// Fix: containsKey check
if (bundle.containsKey("welcome")) { bundle.getString("welcome"); }

// Fix: getOptional (Java 9+)
bundle.getOptional("welcome").ifPresent(m -> process(m));

// Fix: Properties with defaults
String v = props.getProperty("key", "default");

// Fix: null-safe helper
public static String getResource(String k, ResourceBundle b, String d) {
    try { return b.getString(k); }
    catch (MissingResourceException e) { return d; }
}
```

## Prevention Checklist

- Use containsKey/getOptional before accessing.
- Provide default values for lookups.
- Validate MessageFormat patterns before formatting.

## Related Errors

[NullPointerException](nullpointerexception), [MissingResourceException](missingresourceexception)
