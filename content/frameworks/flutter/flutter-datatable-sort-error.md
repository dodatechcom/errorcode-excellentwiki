---
title: "[Solution] Flutter DataTable Sort Error"
description: "Fix Flutter DataTable sorting errors when columns are not sortable or sort indicator displays incorrectly."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A DataTable sort error in Flutter occurs when the `DataTable` column sorting does not work correctly, the sort indicator points in the wrong direction, or the data does not reorder after tapping a column header.

## Common Causes

- `onSort` callback not implemented on `DataColumn`
- `sortColumnIndex` and `sortAscending` not updated in state
- Data list not sorted after changing sort state
- Column index mismatch between `sortColumnIndex` and columns
- Numeric data sorted as strings

## How to Fix

1. Implement column sorting with state:

```dart
class _TableScreenState extends State<TableScreen> {
  List<User> _users = [];
  int? _sortColumnIndex;
  bool _sortAscending = true;

  void _sort<T>(Comparable<T> Function(User) getField, int columnIndex, bool ascending) {
    setState(() {
      _sortColumnIndex = columnIndex;
      _sortAscending = ascending;
      _users.sort((a, b) {
        final aVal = getField(a);
        final bVal = getField(b);
        return ascending
          ? Comparable.compare(aVal as Comparable, bVal as Comparable)
          : (Comparable.compare(bVal as Comparable, aVal as Comparable));
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return DataTable(
      sortColumnIndex: _sortColumnIndex,
      sortAscending: _sortAscending,
      columns: [
        DataColumn(
          label: const Text('Name'),
          onSort: (index, ascending) => _sort<String>((u) => u.name, index, ascending),
        ),
        DataColumn(
          label: const Text('Age'),
          numeric: true,
          onSort: (index, ascending) => _sort<int>((u) => u.age, index, ascending),
        ),
      ],
      rows: _users.map((user) => DataRow(cells: [
        DataCell(Text(user.name)),
        DataCell(Text(user.age.toString())),
      ])).toList(),
    );
  }
}
```

2. Sort data correctly with type comparison:

```dart
void _sortByName(int index, bool ascending) {
  setState(() {
    _sortColumnIndex = index;
    _sortAscending = ascending;
    _data.sort((a, b) {
      final comparison = a.name.compareTo(b.name);
      return ascending ? comparison : -comparison;
    });
  });
}

void _sortByAge(int index, bool ascending) {
  setState(() {
    _sortColumnIndex = index;
    _sortAscending = ascending;
    _data.sort((a, b) {
      final comparison = a.age.compareTo(b.age);
      return ascending ? comparison : -comparison;
    });
  });
}
```

## Examples

```dart
// Bug: onSort not implemented -- tapping does nothing
DataColumn(label: Text('Name')) // Missing onSort

// Fixed
DataColumn(
  label: Text('Name'),
  onSort: (index, ascending) {
    setState(() {
      _sortColumnIndex = index;
      _sortAscending = ascending;
      _users.sort((a, b) => a.name.compareTo(b.name));
    });
  },
);
```

```text
DataTable's sortColumnIndex must be within the range of columns
```
