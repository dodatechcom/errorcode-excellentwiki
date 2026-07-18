---
title: "[Solution] Neo4j Import Error — How to Fix"
description: "Fix Neo4j import errors including CSV import failures, LOAD CSV issues, and neo4j-admin import problems"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Import Error

Import errors in Neo4j occur when using `LOAD CSV`, `neo4j-admin database import`, or other data loading methods. These include file access, format, and performance issues.

## Why It Happens

- The CSV file has format issues (wrong delimiters, encoding)
- The file path is not accessible from the Neo4j server
- `LOAD CSV` is used on a file larger than the configured limit
- The import has duplicate keys or constraint violations
- The data types do not match the expected schema
- The import file uses the wrong line ending format

## Common Error Messages

```
Neo.ClientError.Statement.ExternalResourceFailed:
Could not load external resource from URL 'file:///data/users.csv'
```

```
Neo.ClientError.Statement.SyntaxError:
Invalid CSV format at line 3
```

```
Neo.ClientError.Schema.ConstraintValidationFailed:
Node already exists with label 'Person' and property 'id' = 1
```

```
Neo.TransientError.Configuration.SettingInvalid:
The specified file is too large for LOAD CSV
```

## How to Fix It

### 1. Fix LOAD CSV File Access

```cypher
// Use absolute path
LOAD CSV WITH HEADERS FROM 'file:///var/lib/neo4j/import/users.csv'
AS row
CREATE (n:Person {name: row.name, age: toInteger(row.age)});

// Configure import directory in neo4j.conf
dbms.directories.import=/var/lib/neo4j/import
```

### 2. Fix CSV Format Issues

```cypher
// Use correct delimiter
LOAD CSV WITH HEADERS FROM 'file:///data.csv' FIELDTERMINATOR '|'
AS row RETURN row;

// Handle different line endings
LOAD CSV WITH HEADERS FROM 'file:///data.csv'
AS row RETURN row;

// Check file encoding
// Convert to UTF-8 if needed
// iconv -f ISO-8859-1 -t UTF-8 input.csv > output.csv
```

### 3. Fix Import Performance

```cypher
// Drop constraints and indexes before import
DROP CONSTRAINT person_id IF EXISTS;
DROP INDEX person_name_idx IF EXISTS;

// Use periodic commit for large files
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///large_file.csv'
AS row
CREATE (n:Person {id: toInteger(row.id), name: row.name});

// Recreate constraints after import
CREATE CONSTRAINT person_id FOR (n:Person) REQUIRE n.id IS UNIQUE;
```

### 4. Use neo4j-admin Import for Bulk Load

```bash
# Stop Neo4j first
sudo systemctl stop neo4j

# Import with neo4j-admin
neo4j-admin database import full   --nodes=Person=/import/people.csv   --nodes=Movie=/import/movies.csv   --relationships=ACTED_IN=/import/acted_in.csv   --id-type=INTEGER   neo4j

# Start Neo4j
sudo systemctl start neo4j
```

## Common Scenarios

- **LOAD CSV cannot find file**: Ensure the file is in the import directory and `dbms.directories.import` is set correctly.
- **Import is too slow for millions of rows**: Use `neo4j-admin import` for bulk loading instead of `LOAD CSV`.
- **Import fails with constraint violations**: Drop constraints before import, then recreate after.

## Prevent It

- Use `neo4j-admin import` for initial bulk loading instead of `LOAD CSV`
- Always drop constraints and indexes before large imports
- Test imports on staging with a subset of data first

## Related Pages

- [Neo4j Backup Error](/tools/neo4j/neo4j-backup-error)
- [Neo4j Constraint Error](/tools/neo4j/neo4j-constraint-error)
- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
