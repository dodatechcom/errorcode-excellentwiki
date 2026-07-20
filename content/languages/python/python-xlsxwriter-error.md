---
title: "[Solution] Python XlsxWriter Error — File Creation, Format & Chart Errors"
description: "Fix Python XlsxWriter errors by resolving file creation issues, format conflicts, and chart configuration problems. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 411
---

# Python XlsxWriter Error — File Creation, Format & Chart Errors

XlsxWriter errors occur when attempting to overwrite existing files, using invalid format properties, configuring charts incorrectly, or writing to read-only file handles. Unlike openpyxl, XlsxWriter can only create new files, not modify existing ones.

## Common Causes

```python
import xlsxwriter

# 1. Attempting to overwrite existing file
wb = xlsxwriter.Workbook("existing.xlsx")  # FileExistsError
```

```python
# 2. Invalid format property
wb = xlsxwriter.Workbook("out.xlsx")
ws = wb.add_worksheet()
format = wb.add_format({"bold": "invalid"})  # TypeError
```

```python
# 3. Writing to closed workbook
wb = xlsxwriter.Workbook("out.xlsx")
wb.close()
ws = wb.get_worksheet_by_name("Sheet1")  # IndexError
ws.write("A1", "data")  # FileHandleError
```

```python
# 4. Chart with invalid series data
chart = wb.add_chart({"type": "column"})
chart.add_series({"values": "Sheet1!A1:A10", "categories": "MISSING"})  # ValueError
```

```python
# 5. Duplicate worksheet name
wb = xlsxwriter.Workbook("out.xlsx")
wb.add_worksheet("Data")
wb.add_worksheet("Data")  # DuplicatedTableName
```

## How to Fix

### Fix 1: Remove or rename existing file before creating

```python
import xlsxwriter
import os

filepath = "report.xlsx"
if os.path.exists(filepath):
    os.remove(filepath)

wb = xlsxwriter.Workbook(filepath)
ws = wb.add_worksheet()
ws.write("A1", "Hello")
wb.close()
```

### Fix 2: Use correct format property types

```python
import xlsxwriter

wb = xlsxwriter.Workbook("out.xlsx")
ws = wb.add_worksheet()

# Valid format properties
header_fmt = wb.add_format({
    "bold": True,
    "font_size": 12,
    "bg_color": "#D9E1F2",
    "border": 1,
    "align": "center",
    "num_format": "#,##0.00",
})

ws.write("A1", "Revenue", header_fmt)
ws.write("B1", 12345.67, header_fmt)
wb.close()
```

### Fix 3: Keep workbook open until all writing is done

```python
import xlsxwriter

wb = xlsxwriter.Workbook("output.xlsx")
ws = wb.add_worksheet()

# Write all data before closing
for row in range(100):
    ws.write(row, 0, f"Row {row}")
    ws.write(row, 1, row * 10)

# Only close after all operations complete
wb.close()
```

### Fix 4: Create charts with valid data references

```python
import xlsxwriter

wb = xlsxwriter.Workbook("charts.xlsx")
ws = wb.add_worksheet()

# Write data
headers = ["Month", "Sales"]
data = [["Jan", 100], ["Feb", 150], ["Mar", 200], ["Apr", 175]]
for col, h in enumerate(headers):
    ws.write(0, col, h)
for row, (month, sales) in enumerate(data, 1):
    ws.write(row, 0, month)
    ws.write(row, 1, sales)

# Create chart with correct references
chart = wb.add_chart({"type": "column"})
chart.add_series({
    "name": "Sales",
    "categories": "=Sheet1!$A$2:$A$5",
    "values": "=Sheet1!$B$2:$B$5",
    "fill": {"color": "#4472C4"},
})
chart.set_title({"name": "Monthly Sales"})
chart.set_x_axis({"name": "Month"})
chart.set_y_axis({"name": "Sales ($)"})
ws.insert_chart("D2", chart)

wb.close()
```

## Examples

```python
import xlsxwriter

# Complete workbook with multiple sheets and formatting
wb = xlsxwriter.Workbook("dashboard.xlsx")

# Formats
title_fmt = wb.add_format({"bold": True, "font_size": 16, "align": "center"})
money_fmt = wb.add_format({"num_format": "$#,##0.00"})
pct_fmt = wb.add_format({"num_format": "0.0%"})

# Revenue sheet
ws1 = wb.add_worksheet("Revenue")
ws1.write("A1", "Revenue Report", title_fmt)
headers = ["Product", "Revenue", "Margin"]
for col, h in enumerate(headers):
    ws1.write(2, col, h)

revenue_data = [
    ["Widget", 50000, 0.35],
    ["Gadget", 75000, 0.42],
    ["Doohickey", 30000, 0.28],
]
for row, (prod, rev, margin) in enumerate(revenue_data, 3):
    ws1.write(row, 0, prod)
    ws1.write(row, 1, rev, money_fmt)
    ws1.write(row, 2, margin, pct_fmt)

wb.close()
```

## Related Errors

- [FileExistsError](/languages/python/fileexistserror/) — file already exists
- [TypeError](/languages/python/typeerror/) — invalid format type
- [PermissionError](/languages/python/permissionerror/) — no write access
