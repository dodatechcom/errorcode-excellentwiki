---
title: "[Solution] Java JTable — Table Model Error"
description: "Fix JTable model errors by implementing TableModel correctly, firing data change events, and handling column/row count properly."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 26
---

# JTable — Table Model Error

Errors related to `JTable` and `TableModel` occur when the model is not implemented correctly, data change events are not fired, or column and row counts are inconsistent.

## Description

`JTable` relies on a `TableModel` to provide data. The model must correctly report row/column counts and fire appropriate events (`fireTableDataChanged`, `fireTableCellUpdated`, etc.) when data changes. Errors arise when model methods return incorrect values, events are not fired, or the model structure is modified without notification.

Common message variants:

- `IndexOutOfBoundsException: row/column index out of range`
- `NullPointerException:TableModel returns null for getValueAt()`
- `IllegalStateException:TableModel inconsistent — column count changed`
- `ArrayIndexOutOfBoundsException in JTable header`
- `TableModelListener not registered — UI not updating`

## Common Causes

```java
// Cause 1: getValueAt returns null
@Override
public Object getValueAt(int row, int col) {
    return null;  // JTable may NPE or display "null" string
}

// Cause 2: Row count method does not match actual data
@Override
public int getRowCount() {
    return data.size();  // But data is modified elsewhere without notification
}

// Cause 3: Not firing events when data changes
public void addItem(String item) {
    dataList.add(item);
    // Missing: fireTableRowsInserted(dataList.size()-1, dataList.size()-1);
}

// Cause 4: Column count changes without notification
@Override
public int getColumnCount() {
    return headers.length;  // headers array resized externally
}

// Cause 5: Index out of range after data modification
model.removeRow(0);
// But forEach loop still iterates old row count
```

## Solutions

### Fix 1: Implement a complete AbstractTableModel

```java
import javax.swing.table.AbstractTableModel;
import java.util.ArrayList;
import java.util.List;

public class PersonTableModel extends AbstractTableModel {
    private final String[] columns = {"Name", "Age", "Email"};
    private final List<Person> data = new ArrayList<>();

    @Override
    public int getRowCount() {
        return data.size();
    }

    @Override
    public int getColumnCount() {
        return columns.length;
    }

    @Override
    public String getColumnName(int col) {
        return columns[col];
    }

    @Override
    public Object getValueAt(int row, int col) {
        if (row < 0 || row >= data.size()) {
            return null;
        }
        Person p = data.get(row);
        return switch (col) {
            case 0 -> p.getName();
            case 1 -> p.getAge();
            case 2 -> p.getEmail();
            default -> null;
        };
    }

    public void addPerson(Person person) {
        data.add(person);
        int row = data.size() - 1;
        fireTableRowsInserted(row, row);
    }

    public void removePerson(int row) {
        if (row >= 0 && row < data.size()) {
            data.remove(row);
            fireTableRowsDeleted(row, row);
        }
    }

    public void updatePerson(int row, Person person) {
        if (row >= 0 && row < data.size()) {
            data.set(row, person);
            fireTableRowsUpdated(row, row);
        }
    }
}
```

### Fix 2: Always fire events after data modification

```java
import javax.swing.table.AbstractTableModel;

public class EditableTableModel extends AbstractTableModel {
    private Object[][] data = new Object[10][3];
    private final String[] columns = {"Col1", "Col2", "Col3"};

    @Override
    public int getRowCount() { return data.length; }

    @Override
    public int getColumnCount() { return columns.length; }

    @Override
    public Object getValueAt(int row, int col) {
        return (row < data.length && col < data[row].length)
            ? data[row][col] : null;
    }

    @Override
    public void setValueAt(Object value, int row, int col) {
        if (row < data.length && col < data[row].length) {
            data[row][col] = value;
            fireTableCellUpdated(row, col);  // Notify JTable
        }
    }

    @Override
    public boolean isCellEditable(int row, int col) {
        return true;
    }

    public void addRow(Object[] rowData) {
        Object[][] newData = new Object[data.length + 1][];
        System.arraycopy(data, 0, newData, 0, data.length);
        newData[data.length] = rowData;
        data = newData;
        fireTableRowsInserted(data.length - 1, data.length - 1);
    }
}
```

### Fix 3: Validate indices before accessing rows/columns

```java
import javax.swing.table.TableModel;

public class SafeTableAccess {
    public static Object safeGetValue(TableModel model, int row, int col) {
        if (row < 0 || row >= model.getRowCount()) {
            throw new IndexOutOfBoundsException(
                "Row " + row + " out of range [0, " + model.getRowCount() + ")");
        }
        if (col < 0 || col >= model.getColumnCount()) {
            throw new IndexOutOfBoundsException(
                "Col " + col + " out of range [0, " + model.getColumnCount() + ")");
        }
        return model.getValueAt(row, col);
    }
}
```

### Fix 4: Synchronize data access with EDT

```java
import javax.swing.table.AbstractTableModel;
import javax.swing.SwingUtilities;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class ThreadSafeTableModel extends AbstractTableModel {
    private final List<Object[]> data = Collections.synchronizedList(new ArrayList<>());
    private final String[] columns = {"ID", "Value"};

    @Override
    public int getRowCount() {
        synchronized (data) {
            return data.size();
        }
    }

    @Override
    public int getColumnCount() { return columns.length; }

    @Override
    public Object getValueAt(int row, int col) {
        synchronized (data) {
            if (row >= 0 && row < data.size()) {
                Object[] row_data = data.get(row);
                return col < row_data.length ? row_data[col] : null;
            }
            return null;
        }
    }

    public void addRowAsync(Object[] rowData) {
        synchronized (data) {
            data.add(rowData);
            int row = data.size() - 1;
            SwingUtilities.invokeLater(() -> fireTableRowsInserted(row, row));
        }
    }
}
```

### Fix 5: Use DefaultTableModel for quick prototyping

```java
import javax.swing.table.DefaultTableModel;

public class QuickTableModel {
    public static DefaultTableModel createModel() {
        String[] columns = {"Name", "Age", "City"};
        DefaultTableModel model = new DefaultTableModel(columns, 0);

        model.addRow(new Object[]{"Alice", 30, "NYC"});
        model.addRow(new Object[]{"Bob", 25, "LA"});

        // DefaultTableModel fires events automatically
        return model;
    }
}
```

## Prevention Checklist

- Extend `AbstractTableModel` and implement all required methods.
- Fire `fireTableRowsInserted`, `fireTableRowsDeleted`, `fireTableRowsUpdated` after every data change.
- Validate row/column indices before accessing data in `getValueAt()`.
- Synchronize data access when multiple threads modify the model.
- Do not store `getRowCount()` in a variable and iterate — re-query the model each time.
- Use `DefaultTableModel` for simple cases; use `AbstractTableModel` for complex models.

## Related Errors

- [IndexOutOfBoundsException](../indexoutofboundsexception) — row/column index out of range.
- [ArrayIndexOutOfBoundsException](../arrayindexoutofboundsexception) — column index exceeds array bounds.
- [NullPointerException](../nullpointerexception) — getValueAt returns null.
- [IllegalStateException](../illegalstateexception) — model state inconsistency.
