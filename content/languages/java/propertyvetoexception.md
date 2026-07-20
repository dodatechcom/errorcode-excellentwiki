---
title: "[Solution] Java PropertyVetoException — Property Change Vetoed"
description: "Fix Java PropertyVetoException by handling veto gracefully, checking veto reason, and implementing proper veto handling in property change listeners."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 22
---

# PropertyVetoException — Property Change Vetoed

A `PropertyVetoException` is thrown when a `VetoableChangeListener` vetoes a proposed property change. The listener rejects the new value and the property change is rolled back. This is a checked exception used to enforce validation constraints on bean properties.

## Description

Java Beans provides a veto mechanism through `VetoableChangeListener`. When a property change is proposed, all registered veto listeners are notified. If any listener throws `PropertyVetoException`, the change is reverted to the old value. This allows property constraints to be enforced.

Common message variants:

- `java.beans.PropertyVetoException: New value violates constraint`
- `java.beans.PropertyVetoException: Value not allowed`
- `java.beans.PropertyVetoException: Property change rejected`
- `java.beans.PropertyVetoException: Invalid value for property`

## Common Causes

```java
// Cause 1: Age must be non-negative
public class Person {
    private int age;

    public void setAge(int age) throws PropertyVetoException {
        if (age < 0) {
            throw new PropertyVetoException("Age cannot be negative", null);
        }
        this.age = age;
    }
}

// Cause 2: Status transition not allowed
public class Order {
    private String status;

    public void setStatus(String status) throws PropertyVetoException {
        if ("CANCELLED".equals(this.status)) {
            throw new PropertyVetoException(
                "Cannot change status of cancelled order", null
            );
        }
        this.status = status;
    }
}

// Cause 3: Value range exceeded
public class Temperature {
    private double celsius;

    public void setCelsius(double celsius) throws PropertyVetoException {
        if (celsius < -273.15) {
            throw new PropertyVetoException(
                "Temperature below absolute zero", null
            );
        }
        this.celsius = celsius;
    }
}

// Cause 4: Concurrent modification conflict
public class SharedResource {
    private String value;

    public void setValue(String value) throws PropertyVetoException {
        // Another thread changed value while this was being set
        // Veto to prevent inconsistent state
        throw new PropertyVetoException("Concurrent modification detected", null);
    }
}
```

## Solutions

### Fix 1: Implement VetoableChangeListener with validation

```java
import java.beans.*;

public class ValidatedBean {
    private int age;
    private String name;

    public ValidatedBean() {
        // Register veto listener for age property
        addVetoableChangeListener(evt -> {
            if ("age".equals(evt.getPropertyName())) {
                int newAge = (int) evt.getNewValue();
                if (newAge < 0 || newAge > 150) {
                    throw new PropertyVetoException(
                        "Age must be between 0 and 150, got: " + newAge,
                        evt
                    );
                }
            }
        });
    }

    // Property change support
    private final PropertyChangeSupport pcs = new PropertyChangeSupport(this);

    public void addPropertyChangeListener(PropertyChangeListener listener) {
        pcs.addPropertyChangeListener(listener);
    }

    public void addVetoableChangeListener(VetoableChangeListener listener) {
        // Use PropertyChangeSupport for veto support
        pcs.addPropertyChangeListener(listener);
    }

    public int getAge() { return age; }

    public void setAge(int age) throws PropertyVetoException {
        int oldAge = this.age;
        pcs.fireVetoableChange("age", oldAge, age);
        this.age = age;
        pcs.firePropertyChange("age", oldAge, age);
    }

    public String getName() { return name; }

    public void setName(String name) {
        String oldName = this.name;
        this.name = name;
        pcs.firePropertyChange("name", oldName, name);
    }
}
```

### Fix 2: Handle PropertyVetoException gracefully

```java
import java.beans.*;

public class SafePropertySetter {
    public static boolean setPropertySafely(Object bean, String property, Object value) {
        try {
            java.beans.BeanInfo info = java.beans.Introspector.getBeanInfo(bean.getClass());
            for (java.beans.PropertyDescriptor pd : info.getPropertyDescriptors()) {
                if (pd.getName().equals(property)) {
                    java.lang.reflect.Method setter = pd.getWriteMethod();
                    if (setter != null) {
                        setter.invoke(bean, value);
                        return true;
                    }
                }
            }
        } catch (java.beans.PropertyVetoException e) {
            System.err.println("Property change vetoed for '"
                + property + "': " + e.getMessage());
            return false;
        } catch (Exception e) {
            System.err.println("Error setting property: " + e.getMessage());
            return false;
        }
        return false;
    }
}
```

### Fix 3: Chain veto listeners for complex validation

```java
import java.beans.*;

public class BankAccount {
    private double balance;
    private String status = "ACTIVE";
    private final VetoableChangeSupport vcs = new VetoableChangeSupport(this);

    public BankAccount() {
        // Listener 1: Balance cannot be negative
        vcs.addVetoableChangeListener(evt -> {
            if ("balance".equals(evt.getPropertyName())) {
                double newBalance = (double) evt.getNewValue();
                if (newBalance < 0) {
                    throw new PropertyVetoException(
                        "Balance cannot be negative: " + newBalance, evt
                    );
                }
            }
        });

        // Listener 2: Cannot change status of closed account
        vcs.addVetoableChangeListener(evt -> {
            if ("status".equals(evt.getPropertyName())) {
                if ("CLOSED".equals(this.status)) {
                    throw new PropertyVetoException(
                        "Cannot modify closed account", evt
                    );
                }
            }
        });
    }

    public void addVetoableChangeListener(VetoableChangeListener listener) {
        vcs.addVetoableChangeListener(listener);
    }

    public double getBalance() { return balance; }

    public void setBalance(double balance) throws PropertyVetoException {
        double oldBalance = this.balance;
        vcs.fireVetoableChange("balance", oldBalance, balance);
        this.balance = balance;
    }

    public String getStatus() { return status; }

    public void setStatus(String status) throws PropertyVetoException {
        String oldStatus = this.status;
        vcs.fireVetoableChange("status", oldStatus, status);
        this.status = status;
    }
}
```

### Fix 4: Retry logic when veto occurs

```java
import java.beans.*;

public class RetryPropertySetter {
    public static <T> void setWithRetry(
        Object bean, String property, T value, int maxRetries
    ) throws PropertyVetoException {
        for (int attempt = 1; attempt <= maxRetries; attempt++) {
            try {
                java.beans.BeanInfo info = java.beans.Introspector.getBeanInfo(
                    bean.getClass()
                );
                for (java.beans.PropertyDescriptor pd : info.getPropertyDescriptors()) {
                    if (pd.getName().equals(property)) {
                        pd.getWriteMethod().invoke(bean, value);
                        return;
                    }
                }
                throw new IllegalArgumentException(
                    "Property not found: " + property
                );
            } catch (PropertyVetoException e) {
                if (attempt == maxRetries) {
                    System.err.println("Property vetoed after " + maxRetries
                        + " attempts: " + e.getMessage());
                    throw e;
                }
                System.err.println("Attempt " + attempt + " vetoed: "
                    + e.getMessage() + " — retrying");
            } catch (Exception e) {
                throw new RuntimeException("Error setting property", e);
            }
        }
    }
}
```

### Fix 5: Custom veto exception with detailed reason

```java
import java.beans.*;

public class CustomPropertyVetoException extends PropertyVetoException {
    private final String reason;
    private final String property;

    public CustomPropertyVetoException(String reason, String property, PropertyChangeEvent evt) {
        super(reason, evt);
        this.reason = reason;
        this.property = property;
    }

    public String getReason() { return reason; }
    public String getProperty() { return property; }

    @Override
    public String toString() {
        return "PropertyVetoException{property='" + property + "', reason='" + reason + "'}";
    }
}

// Usage
public class ValidatedConfig {
    private int port;
    private final VetoableChangeSupport vcs = new VetoableChangeSupport(this);

    public void setPort(int port) throws PropertyVetoException {
        int oldPort = this.port;
        if (port < 1 || port > 65535) {
            throw new CustomPropertyVetoException(
                "Port must be 1-65535", "port",
                new PropertyChangeEvent(this, "port", oldPort, port)
            );
        }
        vcs.fireVetoableChange("port", oldPort, port);
        this.port = port;
    }
}
```

## Prevention Checklist

- Always catch `PropertyVetoException` when calling `fireVetoableChange()`.
- Provide clear, descriptive messages in `PropertyVetoException`.
- Use `PropertyChangeEvent` to pass context to veto listeners.
- Document which properties are vetoable and their constraints.
- Implement proper rollback when veto occurs.
- Test veto scenarios in unit tests.

## Related Errors

- [IntrospectionException](../introspectionexception) — bean introspection failure.
- [IllegalArgumentException](../illegalargumentexception) — invalid property value.
- [PropertyChangeEvent](#) — property change notification (not an exception).
