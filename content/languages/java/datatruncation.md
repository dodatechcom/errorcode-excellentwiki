---
title: "[Solution] Java DataTruncation — Data Value Truncated Fix"
description: "Fix Java DataTruncation by checking column sizes, using appropriate JDBC types, increasing buffer sizes, and handling truncation gracefully."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 421
---

# DataTruncation — Data Value Truncated Fix

A `DataTruncation` is thrown when a data value is unexpectedly truncated on read or write. It may be reported as a `SQLWarning` (for truncation during writes) or as an exception (for truncation during reads).

## Description

`java.sql.DataTruncation` extends `SQLException` and indicates that the driver reports that a data truncation has occurred. During a write, truncation is typically reported as a warning. During a read, it may be thrown as an exception if the truncation is significant.

Common message variants:

- `DataTruncation: Data truncation: Data too long for column`
- `DataTruncation: value '...' is too long`
- `DataTruncation: truncating result set column`
- `DataTruncation: Unable to read data due to truncation`

## Common Causes

```java
// Cause 1: Inserting a string longer than the VARCHAR column allows
PreparedStatement ps = conn.prepareStatement("INSERT INTO users (name) VALUES (?)");
ps.setString(1, "A".repeat(500));  // Column is VARCHAR(255)
ps.executeUpdate();  // DataTruncation warning

// Cause 2: Reading binary data into a buffer that is too small
PreparedStatement ps = conn.prepareStatement("SELECT large_blob FROM files WHERE id = ?");
ps.setInt(1, 1);
ResultSet rs = ps.executeQuery();
rs.next();
InputStream is = rs.getBinaryStream(1);
byte[] buffer = new byte[1024];
int bytesRead = is.read(buffer);  // DataTruncation if blob > 1024 bytes

// Cause 3: Integer overflow from column value exceeding Java type range
ResultSet rs = stmt.executeQuery("SELECT huge_number FROM big_table");
rs.next();
long value = rs.getLong(1);  // DataTruncation if value exceeds Long.MAX_VALUE

// Cause 4: Character encoding mismatch causing data loss
PreparedStatement ps = conn.prepareStatement("INSERT INTO text_col (val) VALUES (?)");
ps.setString(1, "Unicode: \u00e4\u00f6\u00fc \u4e16\u754c");
// DataTruncation if column uses ASCII encoding

// Cause 5: BLOB/FLOB truncation during retrieval
ResultSet rs = stmt.executeQuery("SELECT file_data FROM documents WHERE id = ?");
rs.next();
byte[] data = rs.getBytes(1);  // DataTruncation if blob exceeds default max
```

## Solutions

### Fix 1: Check column metadata before inserting data

```java
public static void safeInsert(Connection conn, String tableName, String columnName, String value) throws SQLException {
    try (Statement stmt = conn.createStatement();
         ResultSet rs = stmt.executeQuery(
             "SELECT CHARACTER_MAXIMUM_LENGTH FROM INFORMATION_SCHEMA.COLUMNS " +
             "WHERE TABLE_NAME = '" + tableName + "' AND COLUMN_NAME = '" + columnName + "'")) {
        if (rs.next()) {
            int maxLength = rs.getInt(1);
            if (maxLength > 0 && value.length() > maxLength) {
                System.err.println("Value exceeds column length " + maxLength + ", truncating to fit");
                value = value.substring(0, maxLength);
            }
        }
    }

    try (PreparedStatement ps = conn.prepareStatement("INSERT INTO " + tableName + " (" + columnName + ") VALUES (?)")) {
        ps.setString(1, value);
        ps.executeUpdate();
    }
}
```

### Fix 2: Use appropriate JDBC types and set max field sizes

```java
// Configure maximum field sizes for result sets
Statement stmt = conn.createStatement();
stmt.setMaxFieldSize(65535);  // Set max column size in bytes
stmt.setMaxRows(10000);       // Limit result set rows

try {
    ResultSet rs = stmt.executeQuery("SELECT * FROM large_table");
    while (rs.next()) {
        String value = rs.getString("text_column");
        System.out.println(value);
    }
} catch (DataTruncation e) {
    System.err.println("Truncation occurred: " + e.getMessage());
    System.err.println("Bytes read: " + e.getDatasize());
    System.err.println("Bytes expected: " + e.getTransferSize());
}
```

### Fix 3: Use streaming result sets for large data

```java
// For large BLOBs, use streaming instead of loading into memory
Statement stmt = conn.createStatement();
stmt.setFetchSize(Integer.MIN_VALUE);  // Enable streaming for MySQL

ResultSet rs = stmt.executeQuery("SELECT id, large_blob FROM documents");
while (rs.next()) {
    int id = rs.getInt(1);
    InputStream blobStream = rs.getBinaryStream(2);

    try (OutputStream out = new FileOutputStream("output_" + id + ".bin")) {
        byte[] buffer = new byte[4096];
        int bytesRead;
        while ((bytesRead = blobStream.read(buffer)) != -1) {
            out.write(buffer, 0, bytesRead);
        }
    }
}
```

### Fix 4: Handle truncation gracefully with fallback

```java
public static String readStringSafe(ResultSet rs, int columnIndex, int maxLength) throws SQLException {
    String value = rs.getString(columnIndex);
    if (value == null) return null;

    // Check for truncation via warnings
    SQLWarning warning = rs.getWarnings();
    while (warning != null) {
        if (warning instanceof DataTruncation) {
            DataTruncation dt = (DataTruncation) warning;
            System.err.println("Column " + columnIndex + " truncated: " +
                dt.getDatasize() + " bytes needed, " + dt.getTransferSize() + " available");
        }
        warning = warning.getNextWarning();
    }

    // Return truncated or full value as appropriate
    return value.length() > maxLength ? value.substring(0, maxLength) : value;
}
```

### Fix 5: Use CLOB/BLOB types for large data

```java
// Instead of VARCHAR for large text, use CLOB
PreparedStatement ps = conn.prepareStatement("INSERT INTO articles (content) VALUES (?)");
String longText = "A".repeat(100000);
ps.setCharacterStream(1, new StringReader(longText), longText.length());
ps.executeUpdate();

// Read CLOB safely
ResultSet rs = stmt.executeQuery("SELECT content FROM articles WHERE id = 1");
rs.next();
Clob clob = rs.getClob(1);
String text = clob.getSubString(1, (int) clob.length());
```

## Prevention Checklist

- Check column sizes from metadata before inserting data.
- Use CLOB/BLOB types for large text and binary data instead of VARCHAR/VARBINARY.
- Set `setMaxFieldSize()` on statements to control memory usage.
- Use streaming result sets for large result data.
- Monitor for `DataTruncation` warnings even when operations appear to succeed.

## Related Errors

- [SQLWarning](../sqlwarning) — non-fatal database warnings.
- [SQLDataException](../sqldataexception) — data-related SQL error.
- [SQLException](../sql-exception) — parent class for SQL failures.
