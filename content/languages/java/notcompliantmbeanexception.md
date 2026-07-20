---
title: "[Solution] Java NotCompliantMBeanException — MBean Interface Fix"
description: "Fix Java javax.management.NotCompliantMBeanException by implementing MBean interfaces correctly, checking attribute methods, and verifying the notification model."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 7
---

# NotCompliantMBeanException — MBean Interface Fix

A `NotCompliantMBeanException` is thrown when an object that is not a valid MBean is registered with the MBean Server. This occurs when the class does not implement a valid JMX MBean interface or does not follow the standard naming conventions.

## Description

The `javax.management.NotCompliantMBeanException` extends `javax.management.JMException` and is thrown by `MBeanServer.registerMBean()` when the object being registered does not conform to JMX standards. An MBean must either implement a standard MBean interface (naming convention: `ClassName` implements `ClassNameMBean`) or extend `StandardMBean`. The JMX introspection mechanism validates the interface before allowing registration.

Common message variants:

- `javax.management.NotCompliantMBeanException: Class is not a JMX compliant MBean`
- `javax.management.NotCompliantMBeanException: MBean not compliant: [class name]`

Class hierarchy:

```
java.lang.Object
  └── java.lang.Throwable
        └── java.lang.Exception
              └── javax.management.JMException
                    └── javax.management.NotCompliantMBeanException
```

## Common Causes

```java
// Cause 1: Wrong interface naming convention
public class MyService {
    public void start() {}
    public void stop() {}
}
// Should be: MyServiceMBean interface, or extend StandardMBean

// Cause 2: Missing required getter/setter methods
public interface MyServiceMBean {
    String getName();
    // Missing: void setName(String name) for writable attribute
}

// Cause 3: Class does not implement any MBean interface
public class MyServiceImpl implements Runnable {
    public void run() {}
    // No MyServiceMBean or StandardMBean
}

// Cause 4: Non-standard interface name
public interface MyServiceOps {
    void start();
}
public class MyServiceImpl implements MyServiceOps {
    // Interface name doesn't end with "MBean"
}

// Cause 5: Incorrect StandardMBean generic parameter
public class MyService extends StandardMBean<String> {
    // Should extend StandardMBean<MyServiceMBean>
    protected MyService() {
        super(String.class);  // Wrong class parameter
    }
}
```

## Solutions

### Fix 1: Create proper Standard MBean interface

```java
// Correct — Standard MBean with proper naming
public interface CacheManagerMBean {
    int getEntryCount();
    void clear();
    long getHitCount();
    boolean isEnabled();
    void setEnabled(boolean enabled);
}

public class CacheManagerImpl implements CacheManagerMBean {
    private int entryCount = 0;
    private long hitCount = 0;
    private boolean enabled = true;

    @Override
    public int getEntryCount() { return entryCount; }

    @Override
    public void clear() { entryCount = 0; }

    @Override
    public long getHitCount() { return hitCount; }

    @Override
    public boolean isEnabled() { return enabled; }

    @Override
    public void setEnabled(boolean enabled) { this.enabled = enabled; }
}

// Register
ObjectName name = new ObjectName("app:type=CacheManager");
mbs.registerMBean(new CacheManagerImpl(), name);
```

### Fix 2: Extend StandardMBean for dynamic MBeans

```java
// Correct — using StandardMBean
public class MyService {
    private String status = "stopped";

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public void start() { status = "running"; }
}

// MBean interface
public interface MyServiceMBean {
    String getStatus();
    void setStatus(String status);
    void start();
}

// Implementation
public class MyServiceImpl extends StandardMBean<MyServiceMBean>
        implements MyServiceMBean {
    private String status = "stopped";

    protected MyServiceImpl() {
        super(MyServiceMBean.class);
    }

    @Override
    public String getStatus() { return status; }

    @Override
    public void setStatus(String status) { this.status = status; }

    @Override
    public void start() { status = "running"; }
}
```

### Fix 3: Verify attribute methods match naming conventions

```java
// Correct — attribute methods follow JavaBean conventions
public interface SystemMonitorMBean {
    // Read-only attribute: getPort()
    int getPort();

    // Read-write attribute: getTimeout() / setTimeout()
    long getTimeout();
    void setTimeout(long timeout);

    // Read-only boolean: isRunning()
    boolean isRunning();

    // Operation (not an attribute): no matching getter/setter
    void reset();
}
```

### Fix 4: Check class hierarchy before registration

```java
// Correct — validate MBean compliance before registering
public void safeRegisterMBean(MBeanServer mbs, Object impl, ObjectName name)
        throws Exception {
    // Check if class implements any MBean interface
    Class<?> clazz = impl.getClass();
    boolean compliant = false;

    // Check for StandardMBean
    if (impl instanceof StandardMBean) {
        compliant = true;
    }

    // Check for interface ending with "MBean"
    for (Class<?> iface : clazz.getInterfaces()) {
        if (iface.getName().endsWith("MBean")) {
            compliant = true;
            break;
        }
    }

    if (!compliant) {
        throw new IllegalArgumentException(
            clazz.getName() + " does not implement a JMX MBean interface");
    }

    mbs.registerMBean(impl, name);
}
```

### Fix 5: Use @MXBean annotation for non-standard types

```java
// Correct — use @MXBean for types that don't follow JavaBean naming
public interface MyPlatformMBean {
    // Uses @MXBean for complex return types
    @MXBean
    MyPlatformInfo getPlatformInfo();
}

public class MyPlatformImpl extends StandardMBean<MyPlatformMBean>
        implements MyPlatformMBean {
    protected MyPlatformImpl() {
        super(MyPlatformMBean.class);
    }

    @Override
    public MyPlatformInfo getPlatformInfo() {
        return new MyPlatformInfo("1.0", "running");
    }
}
```

## Prevention Checklist

- Always implement an interface ending with `MBean` or extend `StandardMBean`.
- Follow JavaBean naming conventions: `getXxx()`/`setXxx()` for attributes, `isXxx()` for booleans.
- Verify MBean compliance by checking for proper interface before calling `registerMBean()`.
- Use `@MXBean` annotation when attribute types don't follow standard JavaBean conventions.
- Test MBean registration in unit tests to catch compliance issues early.
- Verify that all operations (non-attribute methods) are intentionally defined.

## Related Errors

- [InstanceAlreadyExistsException](../instancealreadyexistsexception) — MBean already registered.
- [MBeanRegistrationException](../mbeanregistrationexception) — lifecycle callback error.
- [MBeanException](../mbeanexception) — wraps exceptions from MBean methods.
