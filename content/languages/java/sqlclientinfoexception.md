---
title: "[Solution] Java SQLClientInfoException — Client Info Properties Fix"
description: "Fix Java SQLClientInfoException by checking supported properties, handling partial success, and verifying driver capabilities."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 422
---

# SQLClientInfoException — Client Info Properties Fix

An `SQLClientInfoException` is thrown when one or more client info properties cannot be set on the `Connection` object. This exception provides both the failed properties and the set of properties that could not be set.

## Description

`java.sql.SQLClientInfoException` extends `SQLException` and is thrown by `Connection.setClientInfo()` when the JDBC driver cannot set one or more client info properties. The driver may support partial success, meaning some properties were set while others failed.

Common message variants:

- `SQLClientInfoException: Unable to set client info properties`
- `SQLClientInfoException: Property 'X' is not supported`
- `SQLClientInfoException: Connection closed`
- `SQLClientInfoException: Partial failure setting client info`

## Common Causes

```java
// Cause 1: Setting unsupported client info properties
Properties props = new Properties();
props.setProperty("ApplicationName", "MyApp");
props.setProperty("CustomProp1", "value1");  // Driver doesn't support this
conn.setClientInfo(props);  // SQLClientInfoException

// Cause 2: Setting client info on a closed connection
Connection conn = dataSource.getConnection();
conn.close();
conn.setClientInfo("ApplicationName", "MyApp");  // SQLClientInfoException

// Cause 3: Setting client info after connection has been recycled by pool
Connection conn = dataSource.getConnection();
conn.close();  // Returned to pool
// Pool may clear client info — setting on stale reference
conn.setClientInfo("ApplicationName", "MyApp");  // SQLClientInfoException

// Cause 4: Driver doesn't implement client info methods
// Some drivers throw UnsupportedOperationException wrapped in SQLClientInfoException
conn.setClientInfo("User", "admin");  // Driver lacks implementation

// Cause 5: Partial failure — some properties set, others failed
Properties props = new Properties();
props.setProperty("ApplicationName", "MyApp");  // Supported
props.setProperty("TraceLevel", "DEBUG");       // Not supported
conn.setClientInfo(props);  // SQLClientInfoException with failed properties
```

## Solutions

### Fix 1: Check supported properties before setting them

```java
public static void safeSetClientInfo(Connection conn, Properties clientProps) throws SQLClientInfoException {
    // Query the driver for supported client info properties
    try {
        Properties supportedProps = conn.getClientInfo();
        System.out.println("Supported properties: " + supportedProps.stringPropertyNames());

        // Only set properties that the driver supports
        Properties toSet = new Properties();
        for (String key : clientProps.stringPropertyNames()) {
            if (supportedProps.containsKey(key) || supportedProps.containsKey("ClientInfoPrefix" + key)) {
                toSet.setProperty(key, clientProps.getProperty(key));
            } else {
                System.err.println("Warning: Property '" + key + "' not supported by driver");
            }
        }
        conn.setClientInfo(toSet);
    } catch (SQLException e) {
        System.err.println("Could not query supported properties: " + e.getMessage());
    }
}
```

### Fix 2: Handle partial success in client info setting

```java
public static void setClientInfoWithPartialHandling(Connection conn, Properties props) {
    try {
        conn.setClientInfo(props);
        System.out.println("All client info properties set successfully");
    } catch (SQLClientInfoException e) {
        // Check which properties were actually set
        Properties failedProperties = e.getFailedProperties();
        System.err.println("Failed to set these properties:");
        for (String key : failedProperties.stringPropertyNames()) {
            System.err.println("  " + key + " = " + failedProperties.getProperty(key));
        }

        // Retry with only supported properties
        Properties remaining = new Properties();
        for (String key : props.stringPropertyNames()) {
            if (!failedProperties.containsKey(key)) {
                remaining.setProperty(key, props.getProperty(key));
            }
        }
        if (!remaining.isEmpty()) {
            System.err.println("Retrying with " + remaining.size() + " properties");
        }
    }
}
```

### Fix 3: Use individual setClientInfo calls for better error isolation

```java
public static void setClientInfoIndividually(Connection conn, String appName, String userName) {
    try {
        conn.setClientInfo("ApplicationName", appName);
    } catch (SQLClientInfoException e) {
        System.err.println("Could not set ApplicationName: " + e.getMessage());
    }

    try {
        conn.setClientInfo("ClientUserName", userName);
    } catch (SQLClientInfoException e) {
        System.err.println("Could not set ClientUserName: " + e.getMessage());
    }
}
```

### Fix 4: Validate connection state before setting client info

```java
public static void safeSetClientInfoWithValidation(Connection conn, Properties props) {
    try {
        if (conn == null || conn.isClosed()) {
            System.err.println("Cannot set client info: connection is null or closed");
            return;
        }
        conn.setClientInfo(props);
    } catch (SQLClientInfoException e) {
        System.err.println("SQLClientInfoException: " + e.getMessage());
    } catch (SQLException e) {
        System.err.println("SQL error checking connection: " + e.getMessage());
    }
}
```

### Fix 5: Wrap client info operations in a resilient helper

```java
public class ClientInfoHelper {
    public static void setApplicationInfo(Connection conn, String appName) {
        Properties props = new Properties();
        props.setProperty("ApplicationName", appName);

        try {
            conn.setClientInfo(props);
        } catch (SQLClientInfoException e) {
            // Non-fatal: log and continue
            System.err.println("Warning: Could not set client info — " +
                e.getFailedProperties().stringPropertyNames() + " failed");
        }
    }
}
```

## Prevention Checklist

- Always check `getClientInfo()` to discover which properties the driver supports.
- Handle `SQLClientInfoException` gracefully — it is often non-fatal.
- Never assume all drivers support the same client info properties.
- Validate connection state before calling `setClientInfo()`.
- Use individual `setClientInfo(key, value)` calls for critical properties.

## Related Errors

- [SQLException](../sql-exception) — parent class for SQL failures.
- [SQLRecoverableException](../sqlrecoverableexception) — connection can be recovered.
- [NullPointerException](../nullpointerexception) — null connection reference.
