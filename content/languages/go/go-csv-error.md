---
title: "[Solution] encoding/csv Record Error Fix"
description: "Fix Go CSV record errors. Handle malformed CSV, field count mismatches, and encoding issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# encoding/csv Record Error

The `encoding/csv` package fails when the CSV file has inconsistent column counts, wrong delimiter, malformed quoted fields, or the input contains invalid UTF-8. CSV parsing is strict about record structure — every row must have the same number of fields as the header.

## Common Causes

```go
// Cause 1: Inconsistent column count
// Header: name,email,age
// Row: Alice,alice@example.com
// record on line 2: wrong number of fields

// Cause 2: Unquoted field contains delimiter
// name,email
// "Alice, Jr.",alice@example.com
// The comma inside quotes confuses the parser

// Cause 3: Wrong delimiter specified
reader := csv.NewReader(file)
reader.Comma = '\t' // tab-delimited
// But file uses comma delimiter

// Cause 4: Invalid UTF-8 in CSV
reader := csv.NewReader(file)
reader.LazyQuotes = false // strict mode
// parse error on line 3: invalid UTF-8

// Cause 5: Empty file or missing header
reader := csv.NewReader(file)
records, _ := reader.ReadAll()
// records is empty — no header row
```

## How to Fix

### Fix 1: Read CSV with proper configuration

```go
import (
    "encoding/csv"
    "fmt"
    "io"
    "os"
    "strings"
)

func readCSV(path string) ([][]string, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    reader := csv.NewReader(file)
    reader.Comma = ','
    reader.LazyQuotes = true // be lenient with quotes
    reader.TrimLeadingSpace = true

    records, err := reader.ReadAll()
    if err != nil {
        return nil, fmt.Errorf("parse csv: %w", err)
    }
    return records, nil
}
```

### Fix 2: Write CSV with proper quoting

```go
func writeCSV(path string, data [][]string) error {
    file, err := os.Create(path)
    if err != nil {
        return err
    }
    defer file.Close()

    writer := csv.NewWriter(file)
    defer writer.Flush()

    for _, record := range data {
        if err := writer.Write(record); err != nil {
            return fmt.Errorf("write record: %w", err)
        }
    }
    return writer.Error()
}
```

### Fix 3: Use streaming for large CSV files

```go
func processLargeCSV(r io.Reader) error {
    reader := csv.NewReader(r)
    reader.Comma = ','

    for {
        record, err := reader.Read()
        if err == io.EOF {
            break
        }
        if err != nil {
            return fmt.Errorf("read record: %w", err)
        }
        processRecord(record)
    }
    return nil
}
```

## Examples

```go
package main

import (
    "encoding/csv"
    "fmt"
    "log"
    "os"
    "strings"
)

type User struct {
    Name  string
    Email string
    Age   string
}

func main() {
    csvData := `name,email,age
Alice,alice@example.com,30
Bob,bob@example.com,25`

    reader := csv.NewReader(strings.NewReader(csvData))
    records, err := reader.ReadAll()
    if err != nil {
        log.Fatal(err)
    }

    // Skip header
    for _, record := range records[1:] {
        fmt.Printf("Name: %s, Email: %s, Age: %s\n",
            record[0], record[1], record[2])
    }
}
```

## Related Errors

- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — structured data parsing errors
- [io-eof]({{< relref "/languages/go/io-eof" >}}) — unexpected end of CSV stream
- [encoding-binary]({{< relref "/languages/go/go-binary-error" >}}) — binary data parsing similar issues
