---
title: "[Solution] React Native SQLite Database Error — How to Fix"
description: "Fix React Native SQLite errors. Resolve database connection, query, and migration issues in React Native."
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A React Native SQLite database error occurs when the app cannot open, read from, or write to the local SQLite database. SQLite is used for offline data storage and caching in mobile apps.

## Why It Happens

SQLite operations can fail due to database file corruption, incorrect SQL syntax, version incompatibilities, concurrent access issues, or incorrect library configuration. Errors also occur when the database file is moved or deleted, when the schema changes without migration, or when the transaction handling is incorrect.

## Common Error Messages

```
Error: database not open
```

```
SQLite error: near "SELECT": syntax error
```

```
Error: Table 'users' does not exist
```

```
SQLITE_ERROR: database disk image is malformed
```

## How to Fix It

### 1. Set Up SQLite Correctly

Initialize the database:

```typescript
import SQLite from 'react-native-sqlite-storage';

SQLite.enablePromise(true);

async function openDatabase() {
    try {
        const db = await SQLite.openDatabase({
            name: 'myapp.db',
            location: 'default',
        });
        console.log('Database opened');
        return db;
    } catch (error) {
        console.error('Failed to open database:', error);
    }
}
```

### 2. Create Tables and Run Queries

Implement proper database operations:

```typescript
async function initializeDatabase(db) {
    await db.executeSql(`
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    `);

    await db.executeSql(`
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            content TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    `);
}

async function insertUser(db, name, email) {
    try {
        const [result] = await db.executeSql(
            'INSERT INTO users (name, email) VALUES (?, ?)',
            [name, email]
        );
        return result.insertId;
    } catch (error) {
        console.error('Insert failed:', error);
        throw error;
    }
}

async function getUsers(db) {
    try {
        const [results] = await db.executeSql('SELECT * FROM users');
        const users = [];
        for (let i = 0; i < results.rows.length; i++) {
            users.push(results.rows.item(i));
        }
        return users;
    } catch (error) {
        console.error('Query failed:', error);
        throw error;
    }
}
```

### 3. Use Transactions

Handle transactions for data consistency:

```typescript
async function transferData(db, fromUserId, toUserId, amount) {
    try {
        await db.transaction(async (tx) => {
            await tx.executeSql(
                'UPDATE accounts SET balance = balance - ? WHERE user_id = ?',
                [amount, fromUserId]
            );
            await tx.executeSql(
                'UPDATE accounts SET balance = balance + ? WHERE user_id = ?',
                [amount, toUserId]
            );
        });
        console.log('Transfer completed');
    } catch (error) {
        console.error('Transaction failed:', error);
        // Both operations are rolled back
    }
}
```

### 4. Handle Database Migration

Manage schema changes:

```typescript
async function migrateDatabase(db, currentVersion) {
    if (currentVersion < 2) {
        await db.executeSql('ALTER TABLE users ADD COLUMN phone TEXT');
    }
    if (currentVersion < 3) {
        await db.executeSql(`
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        `);
    }
    // Update version
    await db.executeSql('PRAGMA user_version = 3');
}
```

## Common Scenarios

**Scenario 1: Database not found after app update.**
The database file may be deleted during app update. Use `SQLite.openDatabase` with `createFromLocation` to copy from assets.

**Scenario 2: SQL syntax error in query.**
Use parameterized queries instead of string concatenation to prevent SQL injection and syntax errors.

**Scenario 3: Concurrent access causes errors.**
SQLite supports concurrent reads but not concurrent writes. Use transactions and queue write operations.

## Prevent It

1. **Always use parameterized queries** with `?` placeholders instead of string interpolation.

2. **Wrap related writes in transactions** to ensure atomicity.

3. **Test database migrations** by upgrading from previous schema versions.
