---
title: "[Solution] Go GORM Error — How to Fix"
description: "Fix Go GORM errors. Handle connection pooling, migration failures, query timeouts, association errors, and scope issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go GORM Error

Fix Go GORM errors. Handle connection pooling, migration failures, query timeouts, association errors, and scope issues.

## Why It Happens

- Database connection pool is not configured leading to too many open connections
- GORM model tags are incorrect causing migration or query failures
- Query scopes are applied in the wrong order producing unexpected SQL
- Association operations fail because of foreign key constraints

## Common Error Messages

```
sql: connection pool is closed
```
```
gorm: model required for migration
```
```
record not found
```
```
gorm: invalid association
```

## How to Fix It

### Solution 1: Configure connection pool properly

```go
db, _ := gorm.Open(postgres.Open(dsn), &gorm.Config{})
sqlDB, _ := db.DB()
sqlDB.SetMaxOpenConns(25)
sqlDB.SetMaxIdleConns(10)
sqlDB.SetConnMaxLifetime(5 * time.Minute)
```

### Solution 2: Use proper model tags

```go
type User struct {
    gorm.Model
    Name  string `gorm:"size:100;not null"`
    Email string `gorm:"uniqueIndex;size:200"`
}
```

### Solution 3: Handle GORM errors with errors.Is

```go
var user User
result := db.Where("email = ?", email).First(&user)
if errors.Is(result.Error, gorm.ErrRecordNotFound) {
    // Handle not found
}
```

### Solution 4: Use transactions for multi-table operations

```go
err := db.Transaction(func(tx *gorm.DB) error {
    if err := tx.Create(&order).Error; err != nil { return err }
    if err := tx.Create(&payment).Error; err != nil { return err }
    return nil
})
```

## Common Scenarios

- A GORM query returns all rows instead of just one because Where clause is missing
- Migration creates wrong column types because struct tags are missing
- Concurrent database operations cause connection pool exhaustion

## Prevent It

- Configure MaxOpenConns and MaxIdleConns on the underlying sql.DB
- Always check for gorm.ErrRecordNotFound instead of checking for nil
- Use db.Transaction() for operations that must be atomic
