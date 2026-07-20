---
title: "[Solution] csv Reader Error Fix"
description: "Fix CSV reader errors. Handle malformed CSV, delimiter issues, and encoding problems."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# CSV Reader Error

CSV reader errors occur when using the `csv` crate for parsing CSV data — delimiter issues, quote handling, and type deserialization failures.

## Common Causes

```rust
use csv::ReaderBuilder;

// Wrong delimiter
let mut rdr = ReaderBuilder::new()
    .delimiter(b',')
    .from_path("data.tsv")?.from_reader(/* ... */);
// TSV files use tabs, not commas

// Missing header row
let mut rdr = ReaderBuilder::new()
    .has_headers(true) // Default — but file has no header
    .from_path("data.csv")?;

// Type mismatch in deserialization
use serde::Deserialize;
#[derive(Deserialize)]
struct Record { id: u32, name: String }

// CSV has non-numeric value in id column
```

## How to Fix

1. **Configure delimiter correctly**

```rust
use csv::ReaderBuilder;

// For tab-separated
let mut rdr = ReaderBuilder::new()
    .delimiter(b'\t')
    .from_path("data.tsv")?;

// For pipe-separated
let mut rdr = ReaderBuilder::new()
    .delimiter(b'|')
    .from_path("data.csv")?;
```

2. **Handle missing headers**

```rust
use csv::ReaderBuilder;

let mut rdr = ReaderBuilder::new()
    .has_headers(false)
    .from_path("data.csv")?;

for result in rdr.records() {
    let record = result?;
    println!("{:?}", record);
}
```

3. **Use proper deserialization with defaults**

```rust
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct Record {
    id: u32,
    name: String,
    #[serde(default)]
    value: f64,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut rdr = csv::Reader::from_path("data.csv")?;
    for result in rdr.deserialize() {
        let record: Record = result?;
        println!("{:?}", record);
    }
    Ok(())
}
```

## Examples

```rust
use csv::{ReaderBuilder, WriterBuilder};
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
struct Record {
    name: String,
    age: u32,
    city: String,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Write CSV
    let mut wtr = WriterBuilder::new().from_path("output.csv")?;
    wtr.serialize(Record { name: "Alice".into(), age: 30, city: "NYC".into() })?;
    wtr.serialize(Record { name: "Bob".into(), age: 25, city: "LA".into() })?;
    wtr.flush()?;

    // Read CSV
    let mut rdr = ReaderBuilder::new().from_path("output.csv")?;
    for result in rdr.deserialize() {
        let record: Record = result?;
        println!("{:?}", record);
    }
    Ok(())
}
```

## Related Errors

- [Serde Error]({{< relref "/languages/rust/rust-serde-error-rs" >}}) — deserialization
- [Regex Error]({{< relref "/languages/rust/regex-error" >}}) — pattern matching
- [TOML Error]({{< relref "/languages/rust/toml-error" >}}) — config parsing
