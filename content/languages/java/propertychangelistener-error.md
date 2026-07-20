---
title: "[Solution] Java PropertyChangeEvent — PropertyChangeListener Error"
description: "Fix Java PropertyChangeEvent and PropertyChangeListener errors by checking event source, verifying property names, and handling listener removal."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 21
---

# PropertyChangeEvent — PropertyChangeListener Error

Errors related to `PropertyChangeEvent` and `PropertyChangeListener` occur when property change notifications fail, fire with incorrect data, or cause unexpected behavior in listener chains.

## Description

Java Beans property change support allows objects to notify listeners when a bound property changes. Errors arise when listeners receive stale events, property names mismatch, the event source is null, or listeners are not properly removed causing memory leaks or stale references.

Common message variants:

- `java.lang.NullPointerException: source is null in PropertyChangeEvent`
- `PropertyChangeEvent with unknown property name`
- `Listener already added — duplicate notification`
- `ConcurrentModificationException during property change notification`
- `StackOverflowError from circular property change listeners`

## Common Causes

```java
// Cause 1: Firing change event with null source
PropertyChangeEvent evt = new PropertyChangeEvent(null, "name", "old", "new");
// NullPointerException when listeners check evt.getSource()

// Cause 2: Mismatched property name in listener
bean.addPropertyChangeListener("firstName", e -> { });
bean.firePropertyChange("lastname", null, "Doe");  // Listener never fires

// Cause 3: Circular listener causing stack overflow
bean.addPropertyChangeListener(e -> {
    bean.setName("triggered");  // Re-fires event inside listener
});

// Cause 4: Listener not removed, holding reference to disposed object
frame.addWindowListener(new WindowAdapter() {
    public void windowClosed(WindowEvent e) {
        // Listener still registered, frame leaked
    }
});

// Cause 5: Concurrent modification of listener list
new Thread(() -> bean.firePropertyChange("x", 0, 1)).start();
new Thread(() -> bean.addPropertyChangeListener(e -> { })).start();
// ConcurrentModificationException
```

## Solutions

### Fix 1: Always check the event source

```java
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;

public class SafePropertyListener implements PropertyChangeListener {
    private final Object expectedSource;

    public SafePropertyListener(Object expectedSource) {
        this.expectedSource = expectedSource;
    }

    @Override
    public void propertyChange(PropertyChangeEvent evt) {
        if (evt.getSource() != expectedSource) {
            return;  // Ignore events from wrong source
        }

        String propertyName = evt.getPropertyName();
        Object oldValue = evt.getOldValue();
        Object newValue = evt.getNewValue();

        System.out.println(propertyName + ": " + oldValue + " -> " + newValue);
    }
}
```

### Fix 2: Verify property name before handling

```java
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;

public class TypedPropertyListener implements PropertyChangeListener {
    @Override
    public void propertyChange(PropertyChangeEvent evt) {
        if (!"active".equals(evt.getPropertyName())) {
            return;
        }

        if (evt.getNewValue() instanceof Boolean) {
            boolean isActive = (Boolean) evt.getNewValue();
            System.out.println("Active state changed to: " + isActive);
        }
    }
}

// Usage
beanshell.addPropertyChangeListener("active", new TypedPropertyListener());
```

### Fix 3: Properly remove listeners to prevent leaks

```java
import java.beans.PropertyChangeListener;
import javax.swing.*;

public class CleanUpExample {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Example");
        JLabel label = new JLabel("Hello");

        PropertyChangeListener listener = evt ->
            label.setText("Value: " + evt.getNewValue());

        model.addPropertyChangeListener(listener);

        // When done, remove the listener
        model.removePropertyChangeListener(listener);

        // Or remove all listeners for a property
        model.removePropertyChangeListener("value", listener);

        frame.dispose();
    }
}
```

### Fix 4: Use SwingPropertyChangeSupport for thread safety

```java
import java.beans.PropertyChangeListener;
import java.beans.SwingPropertyChangeSupport;
import javax.swing.SwingUtilities;

public class ThreadSafeBean {
    private final SwingPropertyChangeSupport support =
        new SwingPropertyChangeSupport(this);
    private String value;

    public void addListener(PropertyChangeListener listener) {
        support.addPropertyChangeListener(listener);
    }

    public void removeListener(PropertyChangeListener listener) {
        support.removePropertyChangeListener(listener);
    }

    public void setValue(String newValue) {
        String oldValue = this.value;
        this.value = newValue;
        // SwingPropertyChangeSupport fires on EDT automatically
        support.firePropertyChange("value", oldValue, newValue);
    }
}
```

### Fix 5: Guard against circular listener chains

```java
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;

public class SafeCircularHandler {
    private boolean updating = false;

    public void onNameChanged(PropertyChangeEvent evt) {
        if (updating) {
            return;  // Prevent re-entrant fire
        }
        updating = true;
        try {
            String name = (String) evt.getNewValue();
            displayNameField.setText(name);
        } finally {
            updating = false;
        }
    }
}
```

## Prevention Checklist

- Always check `evt.getSource()` and `evt.getPropertyName()` in listeners.
- Remove listeners when the owning component is disposed.
- Use `SwingPropertyChangeSupport` for thread-safe property changes in Swing.
- Guard against re-entrant property change events with a boolean flag.
- Avoid firing property change events inside change listeners.
- Prefer typed property names (constants) to avoid string mismatches.

## Related Errors

- [NullPointerException](../nullpointerexception) — null source in PropertyChangeEvent.
- [ConcurrentModificationException](../concurrentmodificationexception) — concurrent listener list access.
- [StackOverflowError](../stackoverflowerror) — circular listener chains.
