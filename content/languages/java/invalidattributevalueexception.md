---
title: "[Solution] Java InvalidAttributeValueException — MBean Attribute Fix"
description: "Fix Java javax.management.InvalidAttributeValueException by validating attribute values, checking allowed ranges, and implementing proper setters in MBean implementations."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 8
---

# InvalidAttributeValueException — MBean Attribute Fix

An `InvalidAttributeValueException` is thrown when an invalid value is set for an MBean attribute through JMX. This occurs when the MBean implementation rejects a value during `setAttribute()` or during the `setXxx()` method of an MBean interface.

## Description

The `javax.management.InvalidAttributeValueException` extends `javax.management.JMException` and is thrown when a value assigned to an MBean attribute is not acceptable. The MBean's setter method performs validation and rejects the value by throwing this exception. This is commonly seen when JMX clients (like JConsole or remote monitors) attempt to modify MBean attributes with out-of-range or invalid values.

Common message variants:

- `javax.management.InvalidAttributeValueException: Value not in range [min, max]`
- `javax.management.InvalidAttributeValueException: Invalid value for attribute [name]`
- `javax.management.InvalidAttributeValueException: Null value not allowed`

Class hierarchy:

```
java.lang.Object
  └── java.lang.Throwable
        └── java.lang.Exception
              └── javax.management.JMException
                    └── javax.management.InvalidAttributeValueException
```

## Common Causes

```java
// Cause 1: Setting numeric value outside allowed range
// MBean setter validates range
public void setPoolSize(int size) throws InvalidAttributeValueException {
    if (size < 1 || size > 100) {
        throw new InvalidAttributeValueException("Pool size must be between 1 and 100");
    }
    this.poolSize = size;
}
// JMX client: mbs.setAttribute(name, new Attribute("PoolSize", 0));

// Cause 2: Setting null value when not allowed
public void setName(String name) throws InvalidAttributeValueException {
    if (name == null || name.isBlank()) {
        throw new InvalidAttributeValueException("Name must not be null or blank");
    }
    this.name = name;
}
// JMX client: mbs.setAttribute(name, new Attribute("Name", null));

// Cause 3: Setting enum-like string to invalid value
public void setLogLevel(String level) throws InvalidAttributeValueException {
    if (!Set.of("DEBUG", "INFO", "WARN", "ERROR").contains(level)) {
        throw new InvalidAttributeValueException("Invalid log level: " + level);
    }
    this.logLevel = level;
}

// Cause 4: Setting attribute with wrong type
// MBean expects Integer but receives String
mbs.setAttribute(name, new Attribute("Port", "8080"));  // Wrong type

// Cause 5: Complex validation failure
public void setSchedule(String cron) throws InvalidAttributeValueException {
    if (!CronExpression.isValid(cron)) {
        throw new InvalidAttributeValueException("Invalid cron expression: " + cron);
    }
    this.schedule = cron;
}
```

## Solutions

### Fix 1: Validate attribute values before setting

```java
// Wrong — no validation
mbs.setAttribute(name, new Attribute("PoolSize", userProvidedValue));

// Correct — validate before setting
int value = Integer.parseInt(userProvidedValue);
if (value < 1 || value > 100) {
    throw new IllegalArgumentException("Pool size must be between 1 and 100");
}
mbs.setAttribute(name, new Attribute("PoolSize", value));
```

### Fix 2: Implement validation in MBean setter

```java
// Correct — MBean implementation validates in setter
public class ConfigMBeanImpl implements ConfigMBean {
    private int poolSize = 10;

    @Override
    public int getPoolSize() {
        return poolSize;
    }

    @Override
    public void setPoolSize(int size) throws InvalidAttributeValueException {
        if (size < 1 || size > 100) {
            throw new InvalidAttributeValueException(
                "Pool size must be between 1 and 100, got: " + size);
        }
        this.poolSize = size;
    }
}
```

### Fix 3: Handle the exception and report clear error

```java
// Correct — catch and provide actionable feedback
try {
    mbs.setAttribute(name, new Attribute("PoolSize", value));
} catch (InvalidAttributeValueException e) {
    System.err.println("Invalid value for attribute: " + e.getMessage());
    // Return current valid value or prompt user for correction
} catch (AttributeNotFoundException e) {
    System.err.println("Attribute not found: " + e.getMessage());
} catch (MBeanException e) {
    System.err.println("MBean error: " + e.getMessage());
}
```

### Fix 4: Check MBean attribute metadata before setting

```java
// Correct — inspect MBeanInfo for allowed values
MBeanInfo info = mbs.getMBeanInfo(name);
MBeanAttributeInfo[] attrs = info.getAttributes();

for (MBeanAttributeInfo attr : attrs) {
    if ("PoolSize".equals(attr.getName())) {
        System.out.println("Type: " + attr.getType());
        System.out.println("Readable: " + attr.isReadable());
        System.out.println("Writable: " + attr.isWritable());
    }
}
```

### Fix 5: Use descriptors for allowed values

```java
// Correct — MBean with Descriptor for value constraints
public class ConfigMBeanImpl implements ConfigMBean {
    private int poolSize = 10;

    @Override
    public int getPoolSize() {
        return poolSize;
    }

    @Override
    public void setPoolSize(int size) throws InvalidAttributeValueException {
        if (size < 1 || size > 100) {
            throw new InvalidAttributeValueException(
                "PoolSize must be 1-100");
        }
        this.poolSize = size;
    }

    public MBeanInfo getMBeanInfo() {
        Descriptor desc = new DescriptorSupport();
        desc.setField("maxPoolSize", "100");
        desc.setField("minPoolSize", "1");
        // ... build MBeanInfo with descriptor
    }
}
```

## Prevention Checklist

- Always validate attribute values in MBean setter methods.
- Define clear min/max ranges for numeric attributes.
- Reject null and empty values explicitly when they are not allowed.
- Use `InvalidAttributeValueException` in setters to provide clear rejection messages.
- Test MBean attributes with boundary values (min, max, null, wrong type).
- Document valid attribute ranges in MBean descriptions and descriptors.

## Related Errors

- [IllegalArgumentException](../illegalargumentexception) — general invalid argument.
- [MBeanException](../mbeanexception) — wraps exceptions thrown by MBean methods.
- [AttributeNotFoundException](../instancenotfoundexception) — attribute does not exist.
