---
title: "[Solution] DynamoDB Projection Expression Error — How to Fix"
description: "Fix DynamoDB projection expression errors by using correct attribute name syntax, escaping reserved words with expression attribute names, and referencing nested map fields properly."
tools: ["dynamodb"]
error-types: ["projection-error"]
severities: ["error"]
weight: 5
comments: true
---

A `ValidationException` related to projection expressions occurs when you specify an invalid attribute name, use a DynamoDB reserved word without escaping, or reference nested attributes incorrectly in a query or scan operation.

## What This Error Means

Projection expressions in DynamoDB let you specify which attributes to return from a read operation. Without a projection expression, DynamoDB returns all attributes. With a projection expression, you provide a comma-separated list of attribute names. Errors occur when the expression syntax is invalid or references attributes that cannot be resolved.

Unlike filter expressions that run after data is read, projection expressions control what data is returned from DynamoDB's internal storage, so they must be syntactically valid at parse time.

## Why It Happens

- Using a DynamoDB reserved word (e.g., `Status`, `Name`, `Group`, `Order`) as an attribute name without escaping
- Incorrect syntax for nested attribute references in maps
- Referencing attributes that do not exist in the item schema
- Using spaces or special characters in attribute names without proper escaping
- Exceeding the maximum projection expression length
- Mixing projection expression syntax with filter expression syntax

## Common Error Messages

```
ValidationException: Invalid ProjectionExpression: Attribute name is a reserved word
# or
Invalid ProjectionExpression: Syntax error at position X
# or
An error occurred parsing expression: Invalid token in ProjectionExpression
# or
ProjectionExpression contains a reference to an attribute that does not exist
```

## How to Fix It

### 1. Use ExpressionAttributeNames for Reserved Words

```python
import boto3

client = boto3.client('dynamodb')

# Incorrect - 'Status' is a reserved word
# response = client.query(
#     TableName='my-table',
#     KeyConditionExpression='pk = :pk',
#     ProjectionExpression='Status, Name',
#     ExpressionAttributeValues={':pk': {'S': 'user#123'}}
# )

# Correct - escape reserved words with ExpressionAttributeNames
response = client.query(
    TableName='my-table',
    KeyConditionExpression='pk = :pk',
    ProjectionExpression='#status, #name',
    ExpressionAttributeNames={
        '#status': 'Status',
        '#name': 'Name'
    },
    ExpressionAttributeValues={':pk': {'S': 'user#123'}}
)
```

### 2. Reference Nested Map Attributes Correctly

```python
import boto3

client = boto3.client('dynamodb')

# Access nested map attributes with dot notation
response = client.query(
    TableName='my-table',
    KeyConditionExpression='pk = :pk',
    ProjectionExpression='pk, address.city, address.zip',
    ExpressionAttributeNames={
        '#addr': 'address'
    },
    ExpressionAttributeValues={':pk': {'S': 'user#123'}}
)

# For top-level reserved words that contain nested fields:
response = client.query(
    TableName='my-table',
    KeyConditionExpression='pk = :pk',
    ProjectionExpression='pk, #meta.name, #meta.role',
    ExpressionAttributeNames={
        '#meta': 'Metadata'
    },
    ExpressionAttributeValues={':pk': {'S': 'user#123'}}
)
```

### 3. List All Reserved Words to Avoid

```python
import boto3

# DynamoDB reserved words include: ABORT, ABSOLUTE, ACTION, ADD, AFTER,
# AGENT, AGGREGATE, ALL, ALLOCATE, ALTER, ANALYZE, AND, ANY, ARCHIVE,
# ARE, AS, ASC, ASOF, ASSERTION, ATOMIC, ATTACH, ATTRIBUTE, AUDIT,
# AUTHORIZATION, AUTHORIZE, AUTO, AVG, BACKUP, BAD, BATCH, BEFORE,
# BEGIN, BETWEEN, BINARY, BIT, BLOCK, BOOLEAN, BOTH, BREADTH, BUCKET,
# BY, BYTE, CACHE, CALL, CALLED, CAPACITY, CASCADE, CASCADED, CASE,
# CAST, CATALOG, COLLECTION, COLUMN, COMMENT, COMMIT, COUNT, CREATE,
# CROSS, CURRENT, DATA, DATABASE, DATE, DATETIME, DAY, DEALLOCATE,
# DEC, DECIMAL, DECLARE, DEFAULT, DEFERRABLE, DEFERRED, DEFINED,
# DEFINITION, DELETE, DELIMITED, DEPTH, DEREF, DESC, DESCRIBE,
# DESCRIPTOR, DETERMINISTIC, DIAGNOSTICS, DIRECTORY, DISABLE,
# DISCONNECT, DISTINCT, DISTRIBUTE, DOMAIN, DOUBLE, DROP, DURATION,
# DYNAMIC, EACH, ELEMENT, ELSE, ELSEIF, EMPTY, ENABLE, ENCODING,
# ENCRYPTION, END, END-EXEC, EQUALS, ERROR, ESCAPE, EVERY, EXCEPT,
# EXCEPTION, EXCLUDING, EXCLUSIVE, EXECUTE, EXISTS, EXPLAIN, FAIL,
# FALSE, FETCH, FILTER, FIRST, FLOAT, FOLLOWING, FOR, FORCE, FOREIGN,
# FOUND, FREE, FROM, FULL, FUNCTION, GENERAL, GENERATED, GET, GLOB,
# GLOBAL, GO, GOTO, GRANT, GROUP, GROUPING, HANDLER, HASH, HAVING,
# HIDDEN, HOLD, HOUR, IDENTITY, IF, IMMEDIATE, IN, INCLUDING, INDEX,
# INDICATOR, INITIALLY, INNER, INOUT, INPUT, INSENSITIVE, INSERT,
# INTERSECT, INTERVAL, INTO, IS, ISOLATION, ITERATE, JOIN, KEY, KEYS,
# LARGE, LAST, LATERAL, LEADING, LEAVE, LEFT, LEVEL, LIKE, LIMIT,
# LIST, LOCAL, LOCALTIME, LOCALTIMESTAMP, LOCATOR, LOCK, LOWER, MAP,
# MAPPING, MATCH, MAX, MAXVALUE, MEMBER, MERGE, MESSAGE, METHOD,
# MIN, MINUTE, MOD, MODIFIES, MODIFY, MODULE, MONTH, MULTISET, NAME,
# NAMES, NATIONAL, NATURAL, NCHAR, NCLOB, NEW, NEXT, NO, NONE, NOT,
# NULL, NUMBER, OBJECT, OF, OFFSET, OLD, ON, ONLY, OPEN, OPERATION,
# OPTION, OR, ORDER, ORDINALITY, OTHER, OUT, OUTER, OUTPUT, OVER,
# OVERLAPS, OVERRIDE, OWNER, PAD, PARAMETER, PARAMETERS, PARTIAL,
# PARTITION, PATH, PERCENT, PERCENTILE, POSITION, PRECISION, PREPARE,
# PRESERVE, PRIMARY, PRIOR, PRIVILEGES, PROCEDURE, PUBLIC, RANGE,
# READ, READS, REAL, RECURSIVE, REDUCE, REF, REFERENCE, REFERENCES,
# REGEXP, RELATIVE, RELEASE, RENAME, REPEAT, REPLACE, REQUEST,
# RESULT, RETURN, RETURNING, REVOKE, RIGHT, ROLE, ROLLBACK, ROLLUP,
# ROUTINE, ROW, ROWS, RULE, SAMPLE, SCHEMA, SCOPE, SCROLL, SEARCH,
# SECOND, SECTION, SECURITY, SEEK, SELECT, SELF, SENSITIVE, SEQUENCE,
# SERIALIZABLE, SESSION, SET, SHOW, SIGNED, SIMILAR, SIZE, SMALLINT,
# SOME, SOURCE, SPACE, SPECIFIC, SPECIFICTYPE, SQL, SQLCODE,
# SQLERROR, SQLEXCEPTION, SQLSTATE, SQLWARNING, START, STATE,
# STATIC, STATUS, STRUCT, STYLE, SUBLIST, SUBMULTISET, SUBPARTITION,
# SUBSTRING, SUBTYPE, SUM, SUPER, SYMMETRIC, SYNONYM, TABLE, TABLESAMPLE,
# TEMP, TEMPORARY, TERMINATE, TEXT, THAN, THEN, THROUGHPUT, TIME,
# TIMESTAMP, TIMEZONE_HOUR, TIMEZONE_MINUTE, TO, TRAILING, TRANSACTION,
# TRANSFORM, TRANSLATE, TRANSLATION, TREAT, TRIGGER, TRIM, TRUE,
# TYPE, UNBOUNDED, UNDER, UNDO, UNION, UNIQUE, UNIT, UNKNOWN,
# UNNEST, UNPIVOT, UNSIGNED, UNTIL, UPDATE, UPPER, USAGE, USER,
# USING, VACUUM, VALUE, VALUES, VARCHAR, VARIABLE, VARYING, VIEW,
# VIRTUAL, WHEN, WHENEVER, WHERE, WHILE, WINDOW, WITH, WITHIN,
# WITHOUT, WORK, WRITE, YEAR, ZONE
```

### 4. Use ExpressionAttributeNames for Any Attribute with Special Characters

```python
import boto3

client = boto3.client('dynamodb')

# Attributes with hyphens, dots, or spaces need escaping
response = client.query(
    TableName='my-table',
    KeyConditionExpression='pk = :pk',
    ProjectionExpression='#a, #b, #c',
    ExpressionAttributeNames={
        '#a': 'my-attribute',    # Hyphen
        '#b': 'nested.field',    # Dot in name
        '#c': 'attribute with spaces'
    },
    ExpressionAttributeValues={':pk': {'S': 'user#123'}}
)
```

### 5. Validate Projection Expressions Before Execution

```python
def validate_projection_expression(projection):
    """Basic validation of projection expression syntax."""
    import re
    
    if not projection:
        return True
    
    parts = [p.strip() for p in projection.split(',')]
    
    for part in parts:
        # Check for spaces in attribute names (should use ExpressionAttributeNames)
        if ' ' in part and not part.startswith('#'):
            print(f"Warning: '{part}' contains spaces and may need escaping")
        
        # Check for common reserved words
        reserved = {'STATUS', 'NAME', 'GROUP', 'ORDER', 'COUNT', 'DATE'}
        if part.upper() in reserved and not part.startswith('#'):
            print(f"Warning: '{part}' is a reserved word and needs escaping")
    
    return True
```

## Common Scenarios

### Migrating from Select to ProjectionExpression

An existing application uses the older `Select` parameter with `SPECIFIC_ATTRIBUTES`. After migrating to `ProjectionExpression`, the application starts throwing syntax errors because attribute names like `Status` and `Name` are reserved words. The fix is to add `ExpressionAttributeNames` to escape all reserved words.

### Nested Map Attributes in Large Documents

A DynamoDB item contains deeply nested map attributes. The projection expression `address.billing.city.street` is incorrectly typed as `address.billing.city,street` (missing the dot in the last segment), causing a syntax error. Verify dot-delimited paths match the actual item structure.

### DynamoDB Streams with Projection Expressions

A Lambda function processing DynamoDB Streams uses a projection expression in the stream record filter. The expression references `NewImage.Metadata` where `Metadata` is a reserved word. Escape it using `ExpressionAttributeNames` in the stream configuration.

## Prevent It

- Always check the DynamoDB reserved words list before writing projection expressions
- Use `ExpressionAttributeNames` for all attribute names to avoid reserved word issues
- Validate projection expressions with a linter or test harness before production use
- Keep projection expressions simple and avoid deeply nested references
- Use shorter, non-reserved attribute names in your data model
- Test query and scan operations with projection expressions in a development environment
- Add CI checks that parse and validate expression syntax

## Related Pages

- [DynamoDB Filter Expression Error](/tools/dynamodb/dynamodb-filter-error)
- [DynamoDB Type Mismatch Error](/tools/dynamodb/dynamodb-type-error)
- [DynamoDB Page Size Error](/tools/dynamodb/dynamodb-page-size-error)
