#!/usr/bin/env python3
"""Generate 100+ SQLite error pages for the error code wiki."""

import os

OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "content",
    "tools",
    "sqlite",
)

PAGES = []

# ─── 1. SQL Error Codes ──────────────────────────────────────────────────────
SQLITE_CODES = [
    (1,  "SQLITE_ERROR",    "Generic SQL error or missing database",            "sql-error"),
    (2,  "SQLITE_INTERNAL", "Internal logic error in the SQLite engine",        "internal-error"),
    (3,  "SQLITE_PERM",     "Access permission denied for an operation",        "permission-error"),
    (4,  "SQLITE_ABORT",    "Operation aborted by callback or interrupt",       "abort-error"),
    (5,  "SQLITE_BUSY",     "Database is locked by another connection",         "locking-error"),
    (6,  "SQLITE_LOCKED",   "Table or index is locked",                         "locking-error"),
    (7,  "SQLITE_NOMEM",    "Out of memory allocation failed",                  "memory-error"),
    (8,  "SQLITE_READONLY", "Attempt to write a read-only database",            "permission-error"),
    (9,  "SQLITE_INTERRUPT","Operation was interrupted",                        "abort-error"),
    (10, "SQLITE_IOERR",    "Disk I/O error occurred",                          "io-error"),
    (11, "SQLITE_CORRUPT",  "Database disk image is malformed",                 "corruption-error"),
    (12, "SQLITE_NOTFOUND", "Table or record not found",                        "not-found-error"),
    (13, "SQLITE_FULL",     "Database or disk is full",                         "disk-error"),
    (14, "SQLITE_CANTOPEN","Unable to open the database file",                  "io-error"),
    (15, "SQLITE_PROTOCOL", "Locking protocol error",                           "locking-error"),
    (16, "SQLITE_EMPTY",    "Internal database is empty",                       "data-error"),
    (17, "SQLITE_SCHEMA",   "Database schema has changed",                      "schema-error"),
    (18, "SQLITE_TOOBIG",   "String or BLOB too big",                           "data-error"),
    (19, "SQLITE_CONSTRAINT","Constraint violation occurred",                   "constraint-error"),
    (20, "SQLITE_MISMATCH", "Data type mismatch in a column",                   "type-error"),
    (21, "SQLITE_MISUSE",   "Library used incorrectly",                         "usage-error"),
    (22, "SQLITE_NOLFS",    "OS feature not available (large file support)",     "os-error"),
    (23, "SQLITE_AUTH",     "Authorization denied",                             "permission-error"),
    (24, "SQLITE_FORMAT",   "Database format error",                            "format-error"),
    (25, "SQLITE_RANGE",    "Bind parameter index out of range",                "range-error"),
    (26, "SQLITE_NOTADB",   "File is not a valid database",                     "corruption-error"),
    (27, "SQLITE_NOTICE",   "Non-fatal notification from the engine",           "notice"),
    (28, "SQLITE_WARNING",  "Non-fatal warning from the engine",                "warning"),
    (100,"SQLITE_ROW",      "Row available from a stepping query",              "row-available"),
    (101,"SQLITE_DONE",     "Statement has finished executing",                 "done"),
]

for code, name, desc, err_type in SQLITE_CODES:
    PAGES.append({
        "slug": f"sqlite-{name.lower()}",
        "title": f"SQLite {name} (Error {code})",
        "desc": f"Understand and resolve SQLite {name} (result code {code}): {desc}.",
        "error_types": [err_type],
        "sections": {
            "description": (
                f"SQLite returns **{name}** (result code {code}) when {desc.lower()}. "
                f"This result code is one of the primary error codes defined in the SQLite C API "
                f"and is commonly encountered when interacting with SQLite databases from applications."
            ),
            "causes": [
                f"The operation triggered an internal {name.lower().replace('sqlite_','')} condition.",
                "Misuse of the SQLite API or incorrect parameter values.",
                "Environmental constraints such as insufficient disk space or permissions.",
            ],
            "fixes": [
                (
                    "Check the exact error message",
                    f"```bash\nsqlite3 mydb.sqlite \"SELECT * FROM test;\"\n-- Read the full error text to pinpoint the issue\n```"
                ),
                (
                    "Use PRAGMA integrity_check to diagnose corruption",
                    f"```sql\nPRAGMA integrity_check;\n```"
                ),
                (
                    "Review your SQL statement for syntax and logic errors",
                    f"```sql\n-- Example: verify table and column names\nPRAGMA table_info(my_table);\n```"
                ),
            ],
            "examples": (
                f"```bash\nsqlite3 mydb.sqlite \"SELECT * FROM nonexistent;\"\n"
                f"-- Error: no such table: nonexistent\n"
                f"-- This can surface as SQLITE_{err_type.upper().replace('-','_')} under certain conditions\n```"
            ),
        },
    })

# ─── 2. Constraint Errors ────────────────────────────────────────────────────
CONSTRAINT_ERRORS = [
    (
        "NOT NULL constraint failed",
        "A NOT NULL column received a NULL value during INSERT or UPDATE.",
        ["constraint-error"],
        ["Attempting to insert NULL into a column defined as NOT NULL.",
         "A trigger sets a column to NULL violating the constraint.",
         "DEFAULT value expression evaluates to NULL when it should not."],
        [
            ("Ensure the column receives a valid non-NULL value",
             "```sql\nINSERT INTO users (id, name) VALUES (1, 'Alice');\n-- 'name' must not be NULL\n```"),
            ("Use a DEFAULT value in the table definition",
             "```sql\nCREATE TABLE users (\n    id INTEGER PRIMARY KEY,\n    name TEXT NOT NULL DEFAULT 'Unknown'\n);\n```"),
            ("Add a CHECK constraint as a safety net",
             "```sql\nALTER TABLE users ADD CONSTRAINT chk_name CHECK (name IS NOT NULL);\n```"),
        ],
        "```sql\nINSERT INTO users (id, name) VALUES (1, NULL);\n-- Error: NOT NULL constraint failed: users.name\n```",
    ),
    (
        "UNIQUE constraint failed",
        "A UNIQUE constraint was violated by an INSERT or UPDATE that would create a duplicate value.",
        ["constraint-error"],
        ["Inserting a row with a duplicate value in a UNIQUE column.",
         "Using INSERT OR REPLACE when the replacement also conflicts.",
         "Concurrent connections inserting the same key without serialization."],
        [
            ("Use INSERT OR IGNORE to skip conflicting rows",
             "```sql\nINSERT OR IGNORE INTO users (id, email) VALUES (1, 'a@b.com');\n```"),
            ("Use UPSERT to update on conflict",
             "```sql\nINSERT INTO users (id, email) VALUES (1, 'a@b.com')\nON CONFLICT(email) DO UPDATE SET email = excluded.email;\n```"),
            ("Check for existing rows before inserting",
             "```sql\nSELECT COUNT(*) FROM users WHERE email = 'a@b.com';\n```"),
        ],
        "```sql\nINSERT INTO users (id, email) VALUES (1, 'a@b.com');\nINSERT INTO users (id, email) VALUES (2, 'a@b.com');\n-- Error: UNIQUE constraint failed: users.email\n```",
    ),
    (
        "PRIMARY KEY constraint failed",
        "An INSERT or UPDATE violated the PRIMARY KEY constraint by inserting a duplicate primary key value.",
        ["constraint-error"],
        ["Inserting a row with an ID that already exists.",
         "Manually specifying a primary key value that conflicts.",
         "Missing AUTOINCREMENT causing manual key management."],
        [
            ("Use AUTOINCREMENT for automatic key generation",
             "```sql\nCREATE TABLE users (\n    id INTEGER PRIMARY KEY AUTOINCREMENT,\n    name TEXT\n);\n```"),
            ("Use INSERT OR REPLACE",
             "```sql\nINSERT OR REPLACE INTO users (id, name) VALUES (1, 'Alice');\n```"),
            ("Let SQLite assign rowid automatically",
             "```sql\nINSERT INTO users (name) VALUES ('Alice');\n-- id is assigned automatically\n```"),
        ],
        "```sql\nINSERT INTO users (id, name) VALUES (1, 'Alice');\nINSERT INTO users (id, name) VALUES (1, 'Bob');\n-- Error: PRIMARY KEY constraint failed: users.id\n```",
    ),
    (
        "CHECK constraint failed",
        "A CHECK constraint evaluated to FALSE during an INSERT or UPDATE operation.",
        ["constraint-error"],
        ["Inserting a value that violates a CHECK condition.",
         "Updating a row to a value that fails the CHECK.",
         "CHECK constraint references a column not yet available in the INSERT."],
        [
            ("Review the CHECK constraint definition",
             "```sql\nSELECT sql FROM sqlite_master WHERE type='table' AND name='my_table';\n```"),
            ("Insert values that satisfy all CHECK constraints",
             "```sql\n-- If CHECK (age >= 18), ensure age >= 18\nINSERT INTO users (id, age) VALUES (1, 21);\n```"),
            ("Temporarily drop the CHECK if legitimate data needs loading",
             "```sql\n-- Recreate the table without the CHECK, load data, then re-add it\n```"),
        ],
        "```sql\nCREATE TABLE products (id INT, price REAL CHECK (price > 0));\nINSERT INTO products VALUES (1, -5.00);\n-- Error: CHECK constraint failed: products\n```",
    ),
    (
        "FOREIGN KEY constraint failed",
        "An INSERT or UPDATE violated a FOREIGN KEY constraint by referencing a non-existent parent row.",
        ["constraint-error"],
        ["Inserting a child row whose FK value has no matching parent row.",
         "Deleting a parent row that still has child rows (without CASCADE).",
         "Foreign key references a table that does not exist."],
        [
            ("Ensure the referenced parent row exists",
             "```sql\nINSERT INTO departments (id, name) VALUES (1, 'Engineering');\nINSERT INTO employees (id, name, dept_id) VALUES (1, 'Alice', 1);\n```"),
            ("Use ON DELETE CASCADE for automatic child cleanup",
             "```sql\nCREATE TABLE employees (\n    id INTEGER PRIMARY KEY,\n    dept_id INTEGER,\n    FOREIGN KEY (dept_id) REFERENCES departments(id) ON DELETE CASCADE\n);\n```"),
            ("Enable foreign key checking explicitly",
             "```sql\nPRAGMA foreign_keys = ON;\n```"),
        ],
        "```sql\nPRAGMA foreign_keys = ON;\nINSERT INTO employees (id, dept_id) VALUES (1, 999);\n-- Error: FOREIGN KEY constraint failed\n```",
    ),
    (
        "Foreign key mismatch error",
        "SQLite detected that a table's foreign key definition does not match the referenced table's structure.",
        ["constraint-error"],
        ["The parent table lacks a matching index on the referenced column.",
         "Column data types or collations do not match between tables.",
         "The referenced table does not exist."],
        [
            ("Add an index on the parent table's referenced column",
             "```sql\nCREATE INDEX idx_dept_id ON departments(id);\n```"),
            ("Verify column types match exactly",
             "```sql\nPRAGMA table_info(departments);\nPRAGMA table_info(employees);\n```"),
            ("Ensure the parent table exists before defining the foreign key",
             "```sql\nCREATE TABLE departments (id INTEGER PRIMARY KEY, name TEXT);\n```"),
        ],
        "```sql\nCREATE TABLE employees (\n    id INTEGER PRIMARY KEY,\n    dept_id TEXT,\n    FOREIGN KEY (dept_id) REFERENCES departments(id)\n);\n-- Error: foreign key mismatch - 'departments' and 'employees' columns differ\n```",
    ),
    (
        "ON CONFLICT clause error",
        "An ON CONFLICT clause is used incorrectly or conflicts with a constraint definition.",
        ["constraint-error"],
        ["ON CONFLICT references a constraint that does not exist.",
         "Multiple ON CONFLICT clauses on the same constraint.",
         "ON CONFLICT used in a context where it is not supported."],
        [
            ("Verify the constraint name exists",
             "```sql\nSELECT name FROM sqlite_master WHERE type='constraint';\n```"),
            ("Use a valid conflict target",
             "```sql\nINSERT INTO users (id, email) VALUES (1, 'a@b.com')\nON CONFLICT(email) DO UPDATE SET email = excluded.email;\n```"),
            ("Check that the column has a UNIQUE or PRIMARY KEY constraint",
             "```sql\nCREATE UNIQUE INDEX idx_email ON users(email);\n```"),
        ],
        "```sql\nINSERT INTO users (id, email) VALUES (1, 'a@b.com')\nON CONFLICT(nonexistent) DO UPDATE SET email = excluded.email;\n-- Error: no such constraint: nonexistent\n```",
    ),
    (
        "Deferrable constraint error",
        "A DEFERRABLE constraint was defined but used in a context that does not support deferred checking.",
        ["constraint-error"],
        ["Using DEFERRABLE INITIALLY DEFERRED with an incompatible PRAGMA.",
         "Deferrable constraint referenced outside a transaction.",
         "Constraint definition syntax error in DEFERRABLE clause."],
        [
            ("Wrap the operation in a transaction for deferred constraints",
             "```sql\nBEGIN DEFERRED;\nINSERT INTO child VALUES (1, 10);\n-- FK checked at COMMIT\nCOMMIT;\n```"),
            ("Use IMMEDIATE for constraints that must be checked right away",
             "```sql\nCREATE TABLE child (\n    id INTEGER,\n    parent_id INTEGER,\n    FOREIGN KEY (parent_id) REFERENCES parent(id) DEFERRABLE INITIALLY IMMEDIATE\n);\n```"),
            ("Verify PRAGMA foreign_keys is enabled",
             "```sql\nPRAGMA foreign_keys = ON;\n```"),
        ],
        "```sql\nCREATE TABLE child (\n    id INTEGER,\n    parent_id INTEGER,\n    FOREIGN KEY (parent_id) REFERENCES parent(id) DEFERRABLE INITIALLY DEFERRED\n);\n-- Outside a transaction, deferred constraints act like immediate\n```",
    ),
    (
        "Immediate vs deferred transaction locking error",
        "Confusion between IMMEDIATE and DEFERRED transaction modes causes unexpected lock behavior.",
        ["locking-error", "constraint-error"],
        ["Using DEFERRED when the first operation is a write.",
         "Using IMMEDIATE when only reads are needed, causing unnecessary contention.",
         "Nested transactions mixing lock modes."],
        [
            ("Use IMMEDIATE for transactions that write early",
             "```sql\nBEGIN IMMEDIATE;\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\nCOMMIT;\n```"),
            ("Use DEFERRED for read-only or late-write transactions",
             "```sql\nBEGIN DEFERRED;\nSELECT * FROM accounts WHERE id = 1;\n-- Write later if needed, then COMMIT\n```"),
            ("Use EXCLUSIVE only when you need full database lock",
             "```sql\nBEGIN EXCLUSIVE;\nVACUUM;\nCOMMIT;\n```"),
        ],
        "```sql\nBEGIN DEFERRED;\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\n-- May get SQLITE_BUSY if another connection is writing\n-- Fix: use BEGIN IMMEDIATE instead\n```",
    ),
]

for title, desc, err_types, causes, fixes, examples in CONSTRAINT_ERRORS:
    slug = "sqlite-constraint-" + title.lower().replace(" ", "-").replace("/", "-")[:60]
    slug = slug.rstrip("-")
    cause_lines = "\n".join(f"- {c}" for c in causes)
    fix_blocks = "\n\n".join(f"### {h}\n\n{b}" for h, b in fixes)
    PAGES.append({
        "slug": slug,
        "title": f"[Solution] SQLite {title}",
        "desc": desc,
        "error_types": err_types,
        "sections": {
            "description": f"SQLite raises a **{title}** error when {desc.lower()} This is one of the most common classes of errors encountered in SQLite databases.",
            "causes": causes,
            "fixes": fixes,
            "examples": examples,
        },
    })

# ─── 3. Schema Errors ────────────────────────────────────────────────────────
SCHEMA_ERRORS = [
    (
        "no such table",
        "An SQL statement references a table that does not exist in the current database schema.",
        ["schema-error"],
        ["The table was never created.",
         "A typo in the table name.",
         "The table exists in a different attached database."],
        [
            ("List all tables in the database",
             "```sql\nSELECT name FROM sqlite_master WHERE type='table';\n```"),
            ("Check the correct database name for attached databases",
             "```sql\nSELECT * FROM attached_db.my_table;\n```"),
            ("Verify the table name is spelled correctly",
             "```sql\nSELECT sql FROM sqlite_master WHERE name='users';\n```"),
        ],
        "```sql\nSELECT * FROM userss;\n-- Error: no such table: userss\n```",
    ),
    (
        "no such column",
        "An SQL statement references a column that does not exist in the specified table.",
        ["schema-error"],
        ["The column was never added to the table.",
         "A typo in the column name.",
         "The table schema changed since the query was written."],
        [
            ("Check the table's column definitions",
             "```sql\nPRAGMA table_info(users);\n```"),
            ("Add the missing column",
             "```sql\nALTER TABLE users ADD COLUMN phone TEXT;\n```"),
            ("Use ALTER TABLE to rename if the column was renamed",
             "```sql\nALTER TABLE users RENAME COLUMN old_name TO new_name;\n```"),
        ],
        "```sql\nSELECT username FROM users;\n-- Error: no such column: users.username\n```",
    ),
    (
        "no such index",
        "An SQL statement references an index that does not exist in the database.",
        ["schema-error"],
        ["The index was dropped or never created.",
         "A typo in the index name.",
         "The index exists in a different attached database."],
        [
            ("List all indexes",
             "```sql\nSELECT name FROM sqlite_master WHERE type='index';\n```"),
            ("Recreate the index",
             "```sql\nCREATE INDEX idx_users_email ON users(email);\n```"),
            ("Use EXPLAIN to verify index usage",
             "```sql\nEXPLAIN QUERY PLAN SELECT * FROM users WHERE email = 'a@b.com';\n```"),
        ],
        "```sql\nDROP INDEX idx_nonexistent;\n-- Error: no such index: idx_nonexistent\n```",
    ),
    (
        "no such view",
        "An SQL statement references a view that does not exist in the current database.",
        ["schema-error"],
        ["The view was dropped or never created.",
         "A typo in the view name.",
         "The view exists in a different attached database."],
        [
            ("List all views",
             "```sql\nSELECT name FROM sqlite_master WHERE type='view';\n```"),
            ("Recreate the view",
             "```sql\nCREATE VIEW active_users AS SELECT * FROM users WHERE active = 1;\n```"),
            ("Check the view's underlying query",
             "```sql\nSELECT sql FROM sqlite_master WHERE type='view' AND name='active_users';\n```"),
        ],
        "```sql\nSELECT * FROM active_users_v2;\n-- Error: no such view: active_users_v2\n```",
    ),
    (
        "no such trigger",
        "An SQL statement references a trigger that does not exist in the database.",
        ["schema-error"],
        ["The trigger was dropped or never created.",
         "A typo in the trigger name.",
         "The trigger is defined on a different table."],
        [
            ("List all triggers",
             "```sql\nSELECT name FROM sqlite_master WHERE type='trigger';\n```"),
            ("Recreate the trigger",
             "```sql\nCREATE TRIGGER audit_insert AFTER INSERT ON users\nBEGIN\n    INSERT INTO audit_log (op, rowid) VALUES ('INSERT', new.id);\nEND;\n```"),
            ("Verify the trigger fires on the correct table",
             "```sql\nSELECT sql FROM sqlite_master WHERE type='trigger' AND name='audit_insert';\n```"),
        ],
        "```sql\nSELECT * FROM sqlite_master WHERE type='trigger' AND name='nonexistent';\n-- Returns empty result\n```",
    ),
    (
        "duplicate column name",
        "An ALTER TABLE or CREATE TABLE statement tries to add a column that already exists.",
        ["schema-error"],
        ["The column already exists in the table.",
         "A migration script ran twice.",
         "A CREATE TABLE statement specifies the same column name twice."],
        [
            ("Check existing columns first",
             "```sql\nPRAGMA table_info(users);\n```"),
            ("Skip adding the column if it already exists",
             "```sql\n-- Only run if column does not exist:\nALTER TABLE users ADD COLUMN phone TEXT;\n```"),
            ("Use a migration framework to track applied changes",
             "```bash\n# Record each migration step to avoid duplicate runs\n```"),
        ],
        "```sql\nALTER TABLE users ADD COLUMN email TEXT;\nALTER TABLE users ADD COLUMN email TEXT;\n-- Error: duplicate column name: email\n```",
    ),
    (
        "table already exists",
        "A CREATE TABLE statement tries to create a table that already exists in the database.",
        ["schema-error"],
        ["The table was created by a previous operation.",
         "A migration script ran twice.",
         "Missing IF NOT EXISTS clause."],
        [
            ("Use CREATE TABLE IF NOT EXISTS",
             "```sql\nCREATE TABLE IF NOT EXISTS users (\n    id INTEGER PRIMARY KEY,\n    name TEXT\n);\n```"),
            ("Drop the table first if a fresh copy is needed",
             "```sql\nDROP TABLE IF EXISTS users;\nCREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);\n```"),
            ("Check what tables exist",
             "```sql\nSELECT name FROM sqlite_master WHERE type='table';\n```"),
        ],
        "```sql\nCREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);\nCREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);\n-- Error: table users already exists\n```",
    ),
    (
        "index already exists",
        "A CREATE INDEX statement tries to create an index that already exists.",
        ["schema-error"],
        ["The index was created by a previous operation.",
         "A migration script ran twice.",
         "Missing IF NOT EXISTS clause."],
        [
            ("Use CREATE INDEX IF NOT EXISTS",
             "```sql\nCREATE INDEX IF NOT EXISTS idx_email ON users(email);\n```"),
            ("Drop and recreate the index",
             "```sql\nDROP INDEX IF EXISTS idx_email;\nCREATE INDEX idx_email ON users(email);\n```"),
            ("List existing indexes",
             "```sql\nSELECT name FROM sqlite_master WHERE type='index';\n```"),
        ],
        "```sql\nCREATE INDEX idx_email ON users(email);\nCREATE INDEX idx_email ON users(email);\n-- Error: index idx_email already exists\n```",
    ),
    (
        "view already exists",
        "A CREATE VIEW statement tries to create a view that already exists in the database.",
        ["schema-error"],
        ["The view was created by a previous operation.",
         "A migration script ran twice.",
         "Missing IF NOT EXISTS clause."],
        [
            ("Use CREATE VIEW IF NOT EXISTS",
             "```sql\nCREATE VIEW IF NOT EXISTS active_users AS SELECT * FROM users WHERE active = 1;\n```"),
            ("Drop and recreate the view",
             "```sql\nDROP VIEW IF EXISTS active_users;\nCREATE VIEW active_users AS SELECT * FROM users WHERE active = 1;\n```"),
            ("Check existing views",
             "```sql\nSELECT name FROM sqlite_master WHERE type='view';\n```"),
        ],
        "```sql\nCREATE VIEW active_users AS SELECT * FROM users WHERE active = 1;\nCREATE VIEW active_users AS SELECT * FROM users WHERE active = 1;\n-- Error: view active_users already exists\n```",
    ),
    (
        "trigger already exists",
        "A CREATE TRIGGER statement tries to create a trigger that already exists.",
        ["schema-error"],
        ["The trigger was created by a previous operation.",
         "A migration script ran twice.",
         "Missing IF NOT EXISTS clause."],
        [
            ("Use CREATE TRIGGER IF NOT EXISTS",
             "```sql\nCREATE TRIGGER IF NOT EXISTS audit_insert\nAFTER INSERT ON users\nBEGIN\n    INSERT INTO audit_log (op) VALUES ('INSERT');\nEND;\n```"),
            ("Drop and recreate the trigger",
             "```sql\nDROP TRIGGER IF EXISTS audit_insert;\nCREATE TRIGGER audit_insert AFTER INSERT ON users\nBEGIN\n    INSERT INTO audit_log (op) VALUES ('INSERT');\nEND;\n```"),
            ("List existing triggers",
             "```sql\nSELECT name FROM sqlite_master WHERE type='trigger';\n```"),
        ],
        "```sql\nCREATE TRIGGER audit_insert AFTER INSERT ON users BEGIN SELECT 1; END;\nCREATE TRIGGER audit_insert AFTER INSERT ON users BEGIN SELECT 1; END;\n-- Error: trigger audit_insert already exists\n```",
    ),
    (
        "table has no primary key",
        "An operation requires a PRIMARY KEY but the table does not have one defined.",
        ["schema-error"],
        ["The table was created without a PRIMARY KEY.",
         "The PRIMARY KEY was defined inline and missed.",
         "ROWID tables were expected to behave like INTEGER PRIMARY KEY."],
        [
            ("Add a primary key to the table",
             "```sql\nALTER TABLE users ADD COLUMN id INTEGER PRIMARY KEY;\n```"),
            ("Check the current table structure",
             "```sql\nPRAGMA table_info(users);\n```"),
            ("Use the hidden rowid as a de facto primary key",
             "```sql\nSELECT rowid FROM users;\n```"),
        ],
        "```sql\nCREATE TABLE users (name TEXT);\nPRAGMA table_info(users);\n-- 'pk' column is 0 for all columns — no primary key\n```",
    ),
    (
        "schema version mismatch",
        "The database schema version recorded in the file does not match the expected version.",
        ["schema-error"],
        ["The database was created with a different SQLite version.",
         "A migration did not update the schema version.",
         "The database file was copied from a different environment."],
        [
            ("Check the SQLite library version",
             "```sql\nSELECT sqlite_version();\n```"),
            ("Re-run schema migrations to align versions",
             "```sql\n-- Execute all pending DDL statements\n```"),
            ("Back up and recreate the database if severely mismatched",
             "```bash\nsqlite3 mydb.sqlite '.dump' > dump.sql\nsqlite3 newdb.sqlite < dump.sql\n```"),
        ],
        "```sql\nSELECT sqlite_version();\n-- 3.39.4\n-- But the database was created with 3.40.0 features\n```",
    ),
    (
        "schema changed since last read",
        "A prepared statement is still active while the schema of a table it references was modified.",
        ["schema-error"],
        ["Another connection modified the schema while a query was pending.",
         "An ALTER TABLE was executed in the same connection while stepping through results.",
         "A trigger modified the schema during execution."],
        [
            ("Re-prepare the statement after schema changes",
             "```sql\n-- Re-prepare and re-execute after DDL changes\n```"),
            ("Use sqlite3_reset() before re-executing",
             "```python\ncursor.execute(\"SELECT * FROM users\")\n# schema changes here\ncursor.execute(\"SELECT * FROM users\")  # auto-reset and re-prepare\n```"),
            ("Avoid schema changes while queries are active",
             "```sql\n-- Complete all SELECT operations before running ALTER TABLE\n```"),
        ],
        "```sql\n-- Connection A: prepares a statement\nPREPARE stmt AS SELECT * FROM users;\n-- Connection B: alters the table\nALTER TABLE users ADD COLUMN age INT;\n-- Connection A: tries to step — SQLITE_SCHEMA (17)\n```",
    ),
]

for title, desc, err_types, causes, fixes, examples in SCHEMA_ERRORS:
    slug = "sqlite-" + title.lower().replace(" ", "-").replace("/", "-")[:60]
    slug = slug.rstrip("-")
    fix_blocks = "\n\n".join(f"### {h}\n\n{b}" for h, b in fixes)
    PAGES.append({
        "slug": slug,
        "title": f"[Solution] SQLite {title}",
        "desc": desc,
        "error_types": err_types,
        "sections": {
            "description": f"SQLite raises **'{title}'** when {desc.lower()} This is a common schema-related error that prevents the statement from executing.",
            "causes": causes,
            "fixes": fixes,
            "examples": examples,
        },
    })

# ─── 4. Data Type Errors ─────────────────────────────────────────────────────
TYPE_ERRORS = [
    (
        "datatype mismatch",
        "A column's actual data type does not match the expected type in an expression or constraint.",
        ["type-error"],
        ["Comparing a TEXT column to an INTEGER value.",
         "A CHECK constraint expects a specific type.",
         "An expression result type differs from the column's declared affinity."],
        [
            ("Cast values to the correct type",
             "```sql\nSELECT * FROM users WHERE age = CAST('25' AS INTEGER);\n```"),
            ("Use typeof() to inspect column types",
             "```sql\nSELECT name, typeof(name) FROM users;\n```"),
            ("Define columns with explicit types",
             "```sql\nCREATE TABLE users (id INTEGER PRIMARY KEY, age INTEGER NOT NULL);\n```"),
        ],
        "```sql\nCREATE TABLE t (x INTEGER);\nINSERT INTO t VALUES ('hello');\n-- SQLite may accept this due to affinity, but comparisons may fail\nSELECT * FROM t WHERE x = 'hello';\n-- Error: datatype mismatch\n```",
    ),
    (
        "string or blob too big",
        "A string or BLOB value exceeds the maximum allowed size (1 billion bytes by default).",
        ["type-error", "data-error"],
        ["Attempting to insert a very large string literal.",
         "Concatenating many strings without checking total size.",
         "Loading a file into a BLOB column without size validation."],
        [
            ("Check the value size before inserting",
             "```sql\nSELECT length(my_column) FROM my_table;\n```"),
            ("Use substr() to truncate long values",
             "```sql\nINSERT INTO logs (msg) VALUES (substr(very_long_string, 1, 1000000));\n```"),
            ("Split large data across multiple rows",
             "```sql\n-- Insert chunks of 1MB each\n```"),
        ],
        "```sql\nINSERT INTO data VALUES (hex(randomblob(1000000000)));\n-- Error: string or blob too big\n```",
    ),
    (
        "integer overflow",
        "An arithmetic operation or cast produced an integer value that exceeds the 64-bit signed integer range.",
        ["type-error", "data-error"],
        ["Adding two very large positive integers.",
         "Multiplying values that produce a result > 2^63-1.",
         "Casting a string that represents a number outside INTEGER range."],
        [
            ("Check value ranges before arithmetic",
             "```sql\nSELECT typeof(value), value FROM big_table WHERE value > 9223372036854775807;\n```"),
            ("Use REAL type for very large numbers",
             "```sql\nCREATE TABLE big_values (val REAL);\n```"),
            ("Validate input before insertion",
             "```sql\n-- Application-level validation recommended\n```"),
        ],
        "```sql\nSELECT 9223372036854775807 + 1;\n-- May overflow depending on context\n```",
    ),
    (
        "floating point precision error",
        "Floating point arithmetic produces unexpected results due to IEEE 754 representation limitations.",
        ["type-error", "data-error"],
        ["Comparing floating point values for exact equality.",
         "Accumulating small floating point additions.",
         "Storing decimal values that cannot be represented exactly in binary."],
        [
            ("Use integer arithmetic for exact values (e.g., cents instead of dollars)",
             "```sql\n-- Store price in cents as INTEGER\nCREATE TABLE products (price_cents INTEGER);\n-- 19.99 becomes 1999\n```"),
            ("Compare with an epsilon tolerance",
             "```sql\nSELECT * FROM t WHERE ABS(x - 0.3) < 0.0000001;\n```"),
            ("Use TEXT for exact decimal storage",
             "```sql\nCREATE TABLE prices (amount TEXT);\nINSERT INTO prices VALUES ('19.99');\n```"),
        ],
        "```sql\nSELECT 0.1 + 0.2 = 0.3;\n-- Returns 0 (FALSE) — floating point precision\n```",
    ),
    (
        "TEXT not allowed in integer context",
        "A TEXT value was used where an INTEGER or NUMERIC value is required.",
        ["type-error"],
        ["Comparing a TEXT column with an arithmetic operator.",
         "Using a TEXT column in a WHERE clause with >, <, >=, <=.",
         "A column declared as INTEGER received text data."],
        [
            ("Cast TEXT to INTEGER explicitly",
             "```sql\nSELECT * FROM t WHERE CAST(age_text AS INTEGER) > 18;\n```"),
            ("Store numeric data in columns with INTEGER affinity",
             "```sql\nALTER TABLE t ADD COLUMN age INTEGER;\nUPDATE t SET age = CAST(age_text AS INTEGER);\n```"),
            ("Validate data types at the application layer",
             "```python\nif not value.isdigit():\n    raise ValueError('Expected integer')\n```"),
        ],
        "```sql\nCREATE TABLE t (x INTEGER);\nINSERT INTO t VALUES ('abc');\nSELECT x + 1 FROM t;\n-- Unexpected result due to type coercion\n```",
    ),
    (
        "BLOB not allowed in boolean context",
        "A BLOB value was used in a context that expects a scalar (e.g., WHERE clause with comparison).",
        ["type-error"],
        ["Comparing a BLOB column using = in a WHERE clause.",
         "Using a BLOB in an aggregate function like SUM().",
         "A BLOB is compared to a string literal."],
        [
            ("Use the hex() function to compare BLOBs",
             "```sql\nSELECT * FROM t WHERE hex(blob_col) = hex(X'010203');\n```"),
            ("Store a hash or length for quick filtering",
             "```sql\nALTER TABLE t ADD COLUMN blob_len INTEGER;\nUPDATE t SET blob_len = length(blob_col);\n```"),
            ("Avoid using BLOBs in WHERE clauses directly",
             "```sql\n-- Instead of: WHERE blob_col = X'...' \n-- Use: WHERE blob_col IS NOT NULL\n```"),
        ],
        "```sql\nSELECT * FROM t WHERE blob_col = 'hello';\n-- BLOB comparison with string may not work as expected\n```",
    ),
    (
        "REAL vs INTEGER affinity conflict",
        "A column declared as INTEGER received floating point data, causing unexpected affinity behavior.",
        ["type-error"],
        ["Inserting a float into an INTEGER affinity column.",
         "A SELECT expression returns REAL but the target column expects INTEGER.",
         "Column affinity rules are misunderstood."],
        [
            ("Understand SQLite affinity rules",
             "```sql\n-- INTEGER affinity: type contains 'INT'\n-- REAL affinity: type contains 'REAL', 'FLOA', or 'DOUB'\n-- TEXT affinity: type contains 'TEXT' or 'CLOB'\n-- BLOB affinity: type contains 'BLOB' or no type\n-- NUMERIC affinity: everything else\n```"),
            ("Use the correct column type for your data",
             "```sql\nCREATE TABLE measurements (value REAL);  -- for floats\nCREATE TABLE counts (value INTEGER);       -- for integers\n```"),
            ("Cast values explicitly when inserting",
             "```sql\nINSERT INTO counts (value) VALUES (CAST(3.14 AS INTEGER));\n-- value becomes 3\n```"),
        ],
        "```sql\nCREATE TABLE t (x INTEGER);\nINSERT INTO t VALUES (3.99);\nSELECT x FROM t;  -- Returns 3 (truncated due to INTEGER affinity)\n```",
    ),
    (
        "affinity type conversion",
        "SQLite silently converts values based on column affinity, leading to unexpected stored values.",
        ["type-error"],
        ["SQLite applies affinity rules during INSERT, silently altering data.",
         "A string like '123abc' is inserted into an INTEGER column and becomes 123.",
         "A REAL value inserted into a TEXT column becomes '3.14' (string)."],
        [
            ("Use CHECK constraints to enforce strict types",
             "```sql\nCREATE TABLE t (\n    x INTEGER CHECK (typeof(x) = 'integer')\n);\n```"),
            ("Validate data before inserting",
             "```sql\n-- Ensure the value matches the expected type\n```"),
            ("Use strict typing via STRICT tables (SQLite 3.37+)",
             "```sql\nCREATE TABLE t (x INTEGER NOT NULL) STRICT;\n```"),
        ],
        "```sql\nCREATE TABLE t (x INTEGER);\nINSERT INTO t VALUES ('123abc');\nSELECT x FROM t;  -- Returns 123 (leading numeric portion)\n```",
    ),
    (
        "type conflict in expression",
        "An expression mixes incompatible types that cannot be implicitly converted.",
        ["type-error"],
        ["Concatenating INTEGER and BLOB in an expression.",
         "Using arithmetic operators on TEXT values.",
         "A CASE expression returns different types for different branches."],
        [
            ("Cast all values to a consistent type",
             "```sql\nSELECT name || ' - ' || CAST(age AS TEXT) FROM users;\n```"),
            ("Use the typeof() function to debug",
             "```sql\nSELECT typeof(col1), typeof(col2) FROM my_table;\n```"),
            ("Ensure CASE branches return compatible types",
             "```sql\nSELECT CASE WHEN active THEN 'Yes' ELSE 'No' END FROM users;\n```"),
        ],
        "```sql\nSELECT 'Age: ' + age FROM users;\n-- Error: type conflict: TEXT and INTEGER in expression\n```",
    ),
]

for title, desc, err_types, causes, fixes, examples in TYPE_ERRORS:
    slug = "sqlite-type-" + title.lower().replace(" ", "-").replace("/", "-")[:60]
    slug = slug.rstrip("-")
    fix_blocks = "\n\n".join(f"### {h}\n\n{b}" for h, b in fixes)
    PAGES.append({
        "slug": slug,
        "title": f"[Solution] SQLite {title}",
        "desc": desc,
        "error_types": err_types,
        "sections": {
            "description": f"SQLite produces a **{title}** error when {desc.lower()} Understanding SQLite's type affinity system helps prevent and resolve these issues.",
            "causes": causes,
            "fixes": fixes,
            "examples": examples,
        },
    })

# ─── 5. Query Errors ─────────────────────────────────────────────────────────
QUERY_ERRORS = [
    (
        "misuse of aggregate function",
        "An aggregate function (SUM, COUNT, AVG, etc.) is used in a context where it is not valid.",
        ["query-error"],
        ["Using an aggregate in a WHERE clause instead of HAVING.",
         "Mixing aggregate and non-aggregate columns without GROUP BY.",
         "Nesting aggregates incorrectly."],
        [
            ("Use HAVING for aggregate conditions",
             "```sql\nSELECT department, COUNT(*) as cnt\nFROM employees\nGROUP BY department\nHAVING COUNT(*) > 5;\n```"),
            ("Include all non-aggregate columns in GROUP BY",
             "```sql\nSELECT department, name, COUNT(*)\nFROM employees\nGROUP BY department, name;\n```"),
            ("Do not nest aggregates",
             "```sql\n-- Wrong: COUNT(SUM(x))\n-- Right: compute step by step in a subquery\nSELECT cnt FROM (SELECT COUNT(*) as cnt FROM t);\n```"),
        ],
        "```sql\nSELECT name, COUNT(*) FROM users;\n-- Error: misuse of aggregate function COUNT()\n```",
    ),
    (
        "GROUP BY clause error",
        "A GROUP BY clause is syntactically incorrect or incompatible with the SELECT list.",
        ["query-error"],
        ["GROUP BY references a column not in the SELECT list (in strict SQL).",
         "GROUP BY is used with an aggregate that makes no sense.",
         "GROUP BY position number is out of range."],
        [
            ("Ensure GROUP BY columns are in the SELECT list",
             "```sql\nSELECT department, COUNT(*)\nFROM employees\nGROUP BY department;\n```"),
            ("Use column positions correctly",
             "```sql\nSELECT department, COUNT(*)\nFROM employees\nGROUP BY 1;  -- groups by first column\n```"),
            ("Check for typos in column names",
             "```sql\n-- Verify column exists:\nPRAGMA table_info(employees);\n```"),
        ],
        "```sql\nSELECT name FROM employees GROUP BY department;\n-- Error: misuse of aggregate or GROUP BY\n```",
    ),
    (
        "HAVING without GROUP BY",
        "A HAVING clause is used without a corresponding GROUP BY clause.",
        ["query-error"],
        ["The query uses HAVING but omits GROUP BY.",
         "The developer intended to filter groups but forgot GROUP BY.",
         "SQLite treats an ungrouped query as a single group, which may be confusing."],
        [
            ("Add a GROUP BY clause",
             "```sql\nSELECT department, COUNT(*)\nFROM employees\nGROUP BY department\nHAVING COUNT(*) > 5;\n```"),
            ("Use WHERE instead if filtering individual rows",
             "```sql\nSELECT * FROM employees WHERE department = 'Engineering';\n```"),
            ("Understand that without GROUP BY, HAVING filters the entire result",
             "```sql\n-- This works but filters all rows as one group:\nSELECT COUNT(*) FROM employees HAVING COUNT(*) > 0;\n```"),
        ],
        "```sql\nSELECT department, COUNT(*) FROM employees HAVING COUNT(*) > 5;\n-- Error: HAVING clause without GROUP BY\n```",
    ),
    (
        "ORDER BY column not found",
        "An ORDER BY clause references a column that does not exist in the result set or table.",
        ["query-error"],
        ["A typo in the column name.",
         "The column was aliased and the original name is used in ORDER BY.",
         "ORDER BY references a column not in SELECT (valid in SQLite but sometimes confusing)."],
        [
            ("Use the alias name in ORDER BY",
             "```sql\nSELECT name, age AS user_age FROM users ORDER BY user_age;\n```"),
            ("Use column position",
             "```sql\nSELECT name, age FROM users ORDER BY 2;  -- orders by age\n```"),
            ("Verify available columns",
             "```sql\nPRAGMA table_info(users);\n```"),
        ],
        "```sql\nSELECT name FROM users ORDER BY username;\n-- Error: ORDER BY column not found: username\n```",
    ),
    (
        "subquery returns more than 1 row",
        "A scalar subquery used in a comparison returns more than one row.",
        ["query-error"],
        ["A subquery in = comparison returns multiple rows.",
         "The subquery should use LIMIT 1 or an aggregate.",
         "IN was forgotten — the developer meant to use IN instead of =."],
        [
            ("Use IN for multi-row subqueries",
             "```sql\nSELECT * FROM employees WHERE dept_id IN (SELECT id FROM departments WHERE active = 1);\n```"),
            ("Add LIMIT 1 for scalar contexts",
             "```sql\nSELECT * FROM employees WHERE dept_id = (SELECT id FROM departments LIMIT 1);\n```"),
            ("Use an aggregate for scalar contexts",
             "```sql\nSELECT * FROM employees WHERE salary = (SELECT MAX(salary) FROM employees);\n```"),
        ],
        "```sql\nSELECT * FROM employees WHERE dept_id = (SELECT id FROM departments);\n-- Error: subquery returns more than 1 row\n```",
    ),
    (
        "correlated subquery error",
        "A correlated subquery references an outer table but is structured incorrectly.",
        ["query-error"],
        ["The subquery references a column from the outer query that does not exist.",
         "The subquery is not correlated but should be (or vice versa).",
         "Performance issue: the correlated subquery executes for every outer row."],
        [
            ("Verify outer column references",
             "```sql\nSELECT e.name FROM employees e\nWHERE e.salary > (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id);\n```"),
            ("Rewrite as a JOIN for better performance",
             "```sql\nSELECT e.name\nFROM employees e\nJOIN (SELECT dept_id, AVG(salary) AS avg_sal FROM employees GROUP BY dept_id) d\n  ON e.dept_id = d.dept_id\nWHERE e.salary > d.avg_sal;\n```"),
            ("Check that the correlated column is qualified with a table alias",
             "```sql\n-- Use e.dept_id, not just dept_id\n```"),
        ],
        "```sql\nSELECT name FROM employees e\nWHERE salary > (SELECT AVG(salary) FROM employees WHERE dept_id = dept_id);\n-- dept_id is ambiguous — may not correlate correctly\n```",
    ),
    (
        "JOIN syntax error",
        "A JOIN clause contains a syntax error or uses incompatible join types.",
        ["query-error"],
        ["Missing ON clause for INNER JOIN.",
         "Incorrect join type keyword.",
         "Parentheses used incorrectly in complex joins."],
        [
            ("Provide an ON clause for INNER JOIN",
             "```sql\nSELECT e.name, d.name\nFROM employees e\nINNER JOIN departments d ON e.dept_id = d.id;\n```"),
            ("Use correct JOIN keywords",
             "```sql\n-- Valid: INNER JOIN, LEFT JOIN, CROSS JOIN, NATURAL JOIN\n-- Invalid: INNER OUTER JOIN\n```"),
            ("Parenthesize complex joins",
             "```sql\nSELECT * FROM (a INNER JOIN b ON a.id = b.a_id) INNER JOIN c ON b.id = c.b_id;\n```"),
        ],
        "```sql\nSELECT * FROM employees JOIN departments;\n-- Error: JOIN without ON clause (in strict mode)\n```",
    ),
    (
        "LEFT JOIN ON clause error",
        "A LEFT JOIN is used without a proper ON clause, or the ON clause references wrong columns.",
        ["query-error"],
        ["Missing ON clause.",
         "ON clause uses = instead of IS when comparing with NULL.",
         "Wrong column references in the ON condition."],
        [
            ("Always provide an ON clause with LEFT JOIN",
             "```sql\nSELECT e.name, d.name AS dept\nFROM employees e\nLEFT JOIN departments d ON e.dept_id = d.id;\n```"),
            ("Use IS NOT NULL for NULL comparisons in ON",
             "```sql\nSELECT * FROM a LEFT JOIN b ON a.id = b.a_id AND b.status IS NOT NULL;\n```"),
            ("Verify column names exist in both tables",
             "```sql\nPRAGMA table_info(employees);\nPRAGMA table_info(departments);\n```"),
        ],
        "```sql\nSELECT * FROM employees LEFT JOIN departments;\n-- Error: LEFT JOIN requires an ON clause\n```",
    ),
    (
        "NATURAL JOIN column conflict",
        "A NATURAL JOIN produces ambiguous column references because both tables share column names not used in the join.",
        ["query-error"],
        ["Both tables have a column with the same name that is not the join key.",
         "SELECT * pulls in duplicate columns from NATURAL JOIN.",
         "Ambiguous column in WHERE or ORDER BY after NATURAL JOIN."],
        [
            ("Use explicit JOIN instead of NATURAL JOIN",
             "```sql\nSELECT e.name, d.name AS dept\nFROM employees e\nJOIN departments d ON e.dept_id = d.id;\n```"),
            ("Select specific columns to avoid ambiguity",
             "```sql\nSELECT e.name, e.dept_id, d.name AS dept_name\nFROM employees e NATURAL JOIN departments d;\n```"),
            ("Use table aliases in all references",
             "```sql\nSELECT e.name, d.name FROM employees e JOIN departments d ON e.dept_id = d.id;\n```"),
        ],
        "```sql\nSELECT * FROM employees NATURAL JOIN departments;\n-- Both tables have 'id' and 'name' — ambiguous\n```",
    ),
    (
        "USING column ambiguous",
        "A JOIN USING clause specifies a column that appears in multiple tables, causing ambiguity.",
        ["query-error"],
        ["Both tables have multiple columns with the same name.",
         "SELECT * after USING makes the shared column ambiguous.",
         "The USING column is referenced by table qualifier in SELECT."],
        [
            ("Use explicit ON instead of USING",
             "```sql\nSELECT e.name, d.name AS dept\nFROM employees e\nJOIN departments d ON e.dept_id = d.id;\n```"),
            ("Reference the USING column without table qualifier",
             "```sql\nSELECT name, dept_id FROM employees JOIN departments USING (dept_id);\n```"),
            ("Select specific columns to avoid ambiguity",
             "```sql\nSELECT e.name, d.name AS dept_name FROM employees e JOIN departments d ON e.dept_id = d.id;\n```"),
        ],
        "```sql\nSELECT employees.name FROM employees JOIN departments USING (id);\n-- Error: ambiguous column name: id\n```",
    ),
    (
        "UNION type mismatch",
        "The corresponding columns in UNION, EXCEPT, or INTERSECT have incompatible types.",
        ["query-error"],
        ["Column 1 of SELECT is INTEGER, column 1 of UNION is TEXT.",
         "Different number of columns in each SELECT.",
         "BLOB compared to TEXT across UNION branches."],
        [
            ("Ensure matching column types across all SELECT statements",
             "```sql\nSELECT id, name FROM users\nUNION\nSELECT id, CAST(name AS TEXT) FROM archived_users;\n```"),
            ("Match the number of columns",
             "```sql\nSELECT id, name, email FROM users\nUNION\nSELECT id, name, '' AS email FROM legacy_users;\n```"),
            ("Use CAST to align types",
             "```sql\nSELECT CAST(id AS TEXT) FROM t1\nUNION\nSELECT id FROM t2;\n```"),
        ],
        "```sql\nSELECT id, name FROM users\nUNION\nSELECT name, id FROM archived_users;\n-- Error: type mismatch (INTEGER vs TEXT in columns)\n```",
    ),
    (
        "EXCEPT/INTERSECT type mismatch",
        "The corresponding columns in EXCEPT or INTERSECT have incompatible data types.",
        ["query-error"],
        ["Column types differ between the two SELECT statements.",
         "One column is NULL and the other is a specific type.",
         "Type affinity rules cause unexpected conversions."],
        [
            ("Align column types using CAST",
             "```sql\nSELECT id FROM active_users\nEXCEPT\nSELECT CAST(id AS TEXT) FROM deleted_users;\n```"),
            ("Verify column types in both queries",
             "```sql\nPRAGMA table_info(active_users);\nPRAGMA table_info(deleted_users);\n```"),
            ("Use consistent types in all SELECT statements",
             "```sql\nSELECT id FROM t1\nINTERSECT\nSELECT id FROM t2;\n-- Both id columns should have matching types\n```"),
        ],
        "```sql\nSELECT id FROM users\nEXCEPT\nSELECT name FROM archived_users;\n-- Error: type mismatch between INTEGER and TEXT\n```",
    ),
    (
        "recursive CTE limit exceeded",
        "A recursive Common Table Expression (CTE) exceeded the maximum recursion depth (default 1000).",
        ["query-error", "runtime-error"],
        ["The recursive CTE has no proper termination condition.",
         "The data contains a cycle that was not handled.",
         "The default recursion limit is too low for the query."],
        [
            ("Add a proper termination condition",
             "```sql\nWITH RECURSIVE cte AS (\n    SELECT id, parent_id, 0 AS depth\n    FROM tree WHERE parent_id IS NULL\n    UNION ALL\n    SELECT t.id, t.parent_id, c.depth + 1\n    FROM tree t JOIN cte c ON t.parent_id = c.id\n    WHERE c.depth < 100  -- termination condition\n)\nSELECT * FROM cte;\n```"),
            ("Increase the recursion limit",
             "```sql\n-- In C API: sqlite3_limit(db, SQLITE_LIMIT_LENGTH, 100000);\n-- In CLI: no direct way, must recompile\n```"),
            ("Handle cycles with a visited set",
             "```sql\n-- Track visited nodes in a temp table to avoid cycles\n```"),
        ],
        "```sql\nWITH RECURSIVE cnt(x) AS (\n    SELECT 1\n    UNION ALL\n    SELECT x + 1 FROM cnt\n)\nSELECT * FROM cnt;\n-- Error: recursion limit of 1000 exceeded\n```",
    ),
]

for title, desc, err_types, causes, fixes, examples in QUERY_ERRORS:
    slug = "sqlite-query-" + title.lower().replace(" ", "-").replace("/", "-")[:60]
    slug = slug.rstrip("-")
    fix_blocks = "\n\n".join(f"### {h}\n\n{b}" for h, b in fixes)
    PAGES.append({
        "slug": slug,
        "title": f"[Solution] SQLite {title}",
        "desc": desc,
        "error_types": err_types,
        "sections": {
            "description": f"SQLite raises **{title}** when {desc.lower()} This error prevents the query from executing correctly.",
            "causes": causes,
            "fixes": fixes,
            "examples": examples,
        },
    })

# ─── 6. Transaction/Locking Errors ──────────────────────────────────────────
TX_LOCK_ERRORS = [
    (
        "database is locked",
        "A connection attempted to access the database while another connection held a write lock.",
        ["locking-error"],
        ["Another process or thread is writing to the database.",
         "A long-running write transaction is blocking readers.",
         "The busy timeout is too short."],
        [
            ("Increase the busy timeout",
             "```sql\nPRAGMA busy_timeout = 5000;  -- 5 seconds\n```"),
            ("Use WAL mode for concurrent reads and writes",
             "```sql\nPRAGMA journal_mode = WAL;\n```"),
            ("Shorten write transactions",
             "```sql\nBEGIN IMMEDIATE;\n-- do fast writes\nCOMMIT;\n```"),
        ],
        "```sql\n-- Session 1:\nBEGIN IMMEDIATE;\nUPDATE users SET name = 'Alice';\n-- Session 2:\nSELECT * FROM users;\n-- Error: database is locked\n```",
    ),
    (
        "cannot start a transaction within a transaction",
        "A new BEGIN was issued while a transaction was already active.",
        ["locking-error"],
        ["The previous transaction was not committed or rolled back.",
         "A COMMIT or ROLLBACK is missing.",
         "Autocommit is off and a transaction is implicitly active."],
        [
            ("Commit or rollback the existing transaction first",
             "```sql\n-- Check if a transaction is active, then:\nCOMMIT;\nBEGIN;\n```"),
            ("Use savepoints for nested operations",
             "```sql\nBEGIN;\nSAVEPOINT sp1;\n-- nested operation\nRELEASE sp1;\nCOMMIT;\n```"),
            ("Ensure autocommit is on between transactions",
             "```python\nconn.autocommit = True\n```"),
        ],
        "```sql\nBEGIN;\nBEGIN;\n-- Error: cannot start a transaction within a transaction\n```",
    ),
    (
        "cannot commit - no transaction is active",
        "A COMMIT statement was issued but no transaction is currently active.",
        ["locking-error"],
        ["The transaction was already committed or rolled back.",
         "Autocommit is on and statements execute immediately.",
         "A prior error caused an implicit rollback."],
        [
            ("Start a transaction before committing",
             "```sql\nBEGIN;\n-- perform operations\nCOMMIT;\n```"),
            ("Check autocommit mode",
             "```python\n# In Python sqlite3, autocommit is on by default\nconn.execute('BEGIN')\n# ... do work ...\nconn.commit()\n```"),
            ("Use savepoints instead of full transactions for nested work",
             "```sql\nBEGIN;\nSAVEPOINT sp1;\nRELEASE sp1;\nCOMMIT;\n```"),
        ],
        "```sql\nCOMMIT;\n-- Error: cannot commit - no transaction is active\n```",
    ),
    (
        "cannot rollback - no transaction is active",
        "A ROLLBACK statement was issued but no transaction is currently active.",
        ["locking-error"],
        ["The transaction was already committed or rolled back.",
         "A previous error caused an automatic rollback.",
         "Autocommit is on."],
        [
            ("Start a transaction before issuing ROLLBACK",
             "```sql\nBEGIN;\n-- operations that may need rollback\nROLLBACK;\n```"),
            ("Check if the transaction was already rolled back by an error",
             "```sql\n-- After an error, the transaction may already be rolled back\n```"),
            ("Use savepoints for granular rollback control",
             "```sql\nBEGIN;\nSAVEPOINT sp1;\n-- operation\nROLLBACK TO sp1;  -- only rolls back to savepoint\nCOMMIT;\n```"),
        ],
        "```sql\nROLLBACK;\n-- Error: cannot rollback - no transaction is active\n```",
    ),
    (
        "deadlock detected",
        "Two or more connections are waiting for each other to release locks, creating a circular dependency.",
        ["locking-error"],
        ["Connection A locks table 1 then tries to lock table 2.",
         "Connection B locks table 2 then tries to lock table 1.",
         "Both connections are waiting indefinitely."],
        [
            ("Lock tables in a consistent order across all connections",
             "```sql\n-- Always lock table A before table B\nBEGIN IMMEDIATE;\nSELECT * FROM table_a;\nSELECT * FROM table_b;\nCOMMIT;\n```"),
            ("Minimize transaction duration",
             "```sql\nBEGIN IMMEDIATE;\n-- fast operations only\nCOMMIT;\n```"),
            ("Use WAL mode to reduce lock contention",
             "```sql\nPRAGMA journal_mode = WAL;\n```"),
        ],
        "```sql\n-- Connection A:\nBEGIN IMMEDIATE;\nUPDATE table_a SET x = 1;  -- locks table_a\nUPDATE table_b SET x = 2;  -- waiting for table_b\n-- Connection B:\nBEGIN IMMEDIATE;\nUPDATE table_b SET x = 3;  -- locks table_b\nUPDATE table_a SET x = 4;  -- waiting for table_a → DEADLOCK\n```",
    ),
    (
        "WAL mode locking error",
        "WAL (Write-Ahead Logging) mode encounters a locking conflict between readers and writers.",
        ["locking-error"],
        ["A writer is active and a new writer tries to begin.",
         "A WAL checkpoint is blocked by long-running readers.",
         "The WAL file has grown too large."],
        [
            ("Use PRAGMA wal_checkpoint to force a checkpoint",
             "```sql\nPRAGMA wal_checkpoint(TRUNCATE);\n```"),
            ("Increase the wal_autocheckpoint interval",
             "```sql\nPRAGMA wal_autocheckpoint = 2000;  -- pages\n```"),
            ("Ensure readers do not hold locks too long",
             "```sql\n-- Keep read transactions short in WAL mode\n```"),
        ],
        "```sql\nPRAGMA journal_mode = WAL;\n-- Two writers cannot proceed simultaneously even in WAL mode\n-- The second writer gets SQLITE_BUSY\n```",
    ),
    (
        "exclusive access required",
        "An operation requires exclusive access to the database but another connection holds a lock.",
        ["locking-error"],
        ["VACUUM requires exclusive access.",
         "ALTER TABLE on some operations needs exclusive lock.",
         "Another connection holds a shared or reserved lock."],
        [
            ("Close all other connections before running exclusive operations",
             "```sql\n-- Ensure no other connections are active\nVACUUM;\n```"),
            ("Use BEGIN EXCLUSIVE for operations requiring full access",
             "```sql\nBEGIN EXCLUSIVE;\n-- exclusive operation\nCOMMIT;\n```"),
            ("Run VACUUM when the database is not in use",
             "```bash\nsqlite3 mydb.sqlite 'VACUUM;'\n```"),
        ],
        "```sql\nVACUUM;\n-- Error: unable to use exclusive lock\n-- Another connection has a shared lock\n```",
    ),
    (
        "shared cache violation",
        "An attempt to use shared-cache mode failed due to incompatible configuration.",
        ["locking-error"],
        ["Shared cache mode is deprecated or improperly configured.",
         "Multiple connections use different cache settings.",
         "Shared cache is used with WAL mode (incompatible in older versions)."],
        [
            ("Avoid shared-cache mode (deprecated since SQLite 3.41)",
             "```sql\n-- Use default private cache mode\n```"),
            ("Use WAL mode instead of shared cache for concurrency",
             "```sql\nPRAGMA journal_mode = WAL;\n```"),
            ("Use separate database connections with private caches",
             "```python\n# Each connection gets its own cache by default\nconn1 = sqlite3.connect('mydb.sqlite')\nconn2 = sqlite3.connect('mydb.sqlite')\n```"),
        ],
        "```sql\n-- SQLite 3.41+: shared cache is disabled by default\n-- Using sqlite3_enable_shared_cache(1) causes errors\n```",
    ),
    (
        "transaction too large",
        "A transaction modified too much data, exceeding internal limits or exhausting memory.",
        ["locking-error", "runtime-error"],
        ["A single transaction inserts millions of rows.",
         "The undo journal grows too large.",
         "Memory is exhausted during a large transaction."],
        [
            ("Commit in batches",
             "```sql\nBEGIN;\nINSERT INTO big_table SELECT * FROM source LIMIT 10000;\nCOMMIT;\nBEGIN;\nINSERT INTO big_table SELECT * FROM source LIMIT 10000 OFFSET 10000;\nCOMMIT;\n```"),
            ("Use PRAGMA journal_size_limit to control journal size",
             "```sql\nPRAGMA journal_size_limit = 1073741824;  -- 1 GB\n```"),
            ("Avoid very large single transactions",
             "```sql\n-- Break work into chunks of 1000-10000 rows\n```"),
        ],
        "```sql\nBEGIN;\nINSERT INTO big_table SELECT * FROM million_row_source;\n-- Error: SQLITE_TOOBIG or out of memory after millions of rows\nCOMMIT;\n```",
    ),
    (
        "savepoint not found",
        "A ROLLBACK TO or RELEASE SAVEPOINT references a savepoint name that does not exist.",
        ["locking-error"],
        ["A typo in the savepoint name.",
         "The savepoint was already released or rolled back.",
         "Savepoints are not nested correctly."],
        [
            ("Use consistent and unique savepoint names",
             "```sql\nBEGIN;\nSAVEPOINT sp_step1;\n-- operations\nRELEASE sp_step1;\nSAVEPOINT sp_step2;\n-- operations\nRELEASE sp_step2;\nCOMMIT;\n```"),
            ("Check available savepoints",
             "```sql\n-- SQLite does not list savepoints; track them in your application logic\n```"),
            ("Use ROLLBACK TO and RELEASE carefully",
             "```sql\nSAVEPOINT sp1;\n-- operations\nROLLBACK TO sp1;  -- undo operations but keep transaction\nRELEASE sp1;       -- remove the savepoint\n```"),
        ],
        "```sql\nBEGIN;\nSAVEPOINT sp1;\nROLLBACK TO sp2;\n-- Error: no such savepoint: sp2\n```",
    ),
    (
        "release savepoint error",
        "A RELEASE SAVEPOINT statement references a savepoint that was already released or does not exist.",
        ["locking-error"],
        ["The savepoint was already released.",
         "A typo in the savepoint name.",
         "The savepoint was already rolled back."],
        [
            ("Track savepoint names carefully",
             "```sql\nSAVEPOINT sp1;\n-- ... do work ...\nRELEASE sp1;  -- only release once\n```"),
            ("Use ROLLBACK TO before RELEASE for cleanup",
             "```sql\nSAVEPOINT sp1;\n-- risky operation\nROLLBACK TO sp1;  -- undo if needed\nRELEASE sp1;\n```"),
            ("Avoid reusing savepoint names within the same transaction",
             "```sql\nSAVEPOINT sp_v1;\nRELEASE sp_v1;\nSAVEPOINT sp_v2;  -- use a new name\n```"),
        ],
        "```sql\nSAVEPOINT sp1;\nRELEASE sp1;\nRELEASE sp1;\n-- Error: no such savepoint: sp1\n```",
    ),
    (
        "implicit transaction error",
        "A statement that modifies data was executed without an explicit transaction, and the implicit transaction failed.",
        ["locking-error"],
        ["Autocommit is on and each statement is its own transaction.",
         "A statement in an implicit transaction failed, rolling back partial changes.",
         "The developer expected multiple statements to be atomic."],
        [
            ("Wrap related statements in an explicit transaction",
             "```sql\nBEGIN;\nINSERT INTO accounts (id, balance) VALUES (1, 1000);\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\nCOMMIT;\n```"),
            ("Use savepoints for sub-operations",
             "```sql\nBEGIN;\nSAVEPOINT sp1;\nINSERT INTO log VALUES ('step1');\nRELEASE sp1;\nCOMMIT;\n```"),
            ("Understand that each statement in autocommit mode is atomic by itself",
             "```python\n# With autocommit=True, each execute() is its own transaction\n```"),
        ],
        "```sql\n-- Without explicit transaction:\nINSERT INTO accounts VALUES (1, 1000);\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\n-- If UPDATE fails, INSERT is NOT rolled back (different transactions)\n```",
    ),
]

for title, desc, err_types, causes, fixes, examples in TX_LOCK_ERRORS:
    slug = "sqlite-" + title.lower().replace(" ", "-").replace("/", "-")[:60]
    slug = slug.rstrip("-")
    fix_blocks = "\n\n".join(f"### {h}\n\n{b}" for h, b in fixes)
    PAGES.append({
        "slug": slug,
        "title": f"[Solution] SQLite {title}",
        "desc": desc,
        "error_types": err_types,
        "sections": {
            "description": f"SQLite reports **{title}** when {desc.lower()} Proper transaction management is essential for data integrity.",
            "causes": causes,
            "fixes": fixes,
            "examples": examples,
        },
    })

# ─── 7. Attach/Detach Errors ─────────────────────────────────────────────────
ATTACH_ERRORS = [
    (
        "cannot attach database",
        "The ATTACH DATABASE statement failed to attach an external database file.",
        ["database-error"],
        ["The file does not exist or is not a valid database.",
         "Insufficient permissions to open the file.",
         "The database is already attached."],
        [
            ("Verify the file path is correct",
             "```bash\nls -la /path/to/database.sqlite\n```"),
            ("Check file permissions",
             "```bash\nchmod 644 /path/to/database.sqlite\n```"),
            ("Ensure the file is a valid SQLite database",
             "```bash\nfile /path/to/database.sqlite\n# Should say: SQLite 3.x database\n```"),
        ],
        "```sql\nATTACH DATABASE '/nonexistent/path/db.sqlite' AS extra;\n-- Error: unable to open database file\n```",
    ),
    (
        "database already attached",
        "An ATTACH DATABASE statement tried to attach a database using an alias that is already in use.",
        ["database-error"],
        ["The database was previously attached with the same alias.",
         "The previous ATTACH was not followed by DETACH.",
         "A migration script ran the ATTACH statement twice."],
        [
            ("Detach the database first",
             "```sql\nDETACH DATABASE extra;\nATTACH DATABASE '/path/to/db.sqlite' AS extra;\n```"),
            ("Use a different alias",
             "```sql\nATTACH DATABASE '/path/to/db.sqlite' AS extra2;\n```"),
            ("Check currently attached databases",
             "```sql\nSELECT * FROM pragma_database_list;\n```"),
        ],
        "```sql\nATTACH DATABASE 'a.sqlite' AS mydb;\nATTACH DATABASE 'b.sqlite' AS mydb;\n-- Error: database mydb already exists\n```",
    ),
    (
        "database not attached",
        "An SQL statement references an attached database that is no longer available.",
        ["database-error"],
        ["The database was DETACHed before the query.",
         "The connection was closed and reopened without re-attaching.",
         "The alias name is incorrect."],
        [
            ("Re-attach the database",
             "```sql\nATTACH DATABASE '/path/to/db.sqlite' AS extra;\nSELECT * FROM extra.my_table;\n```"),
            ("Check attached databases",
             "```sql\nSELECT * FROM pragma_database_list;\n```"),
            ("Use fully qualified table names",
             "```sql\nSELECT * FROM extra.my_table WHERE extra.my_table.id = 1;\n```"),
        ],
        "```sql\nDETACH DATABASE extra;\nSELECT * FROM extra.my_table;\n-- Error: no such database: extra\n```",
    ),
    (
        "attach filename not found",
        "The ATTACH DATABASE statement cannot find the specified database file.",
        ["database-error"],
        ["The file path is incorrect.",
         "The file does not exist.",
         "The path contains special characters or spaces."],
        [
            ("Use the absolute path",
             "```sql\nATTACH DATABASE '/home/user/data/mydb.sqlite' AS extra;\n```"),
            ("Quote paths with spaces",
             "```sql\nATTACH DATABASE '/path with spaces/db.sqlite' AS extra;\n```"),
            ("Verify the file exists",
             "```bash\nls -la /path/to/db.sqlite\n```"),
        ],
        "```sql\nATTACH DATABASE 'missing.sqlite' AS extra;\n-- Error: unable to open database file\n```",
    ),
    (
        "ATTACH expression error",
        "The ATTACH DATABASE expression has a syntax error or invalid parameters.",
        ["database-error"],
        ["Incorrect syntax for the ATTACH statement.",
         "The database name is not a valid identifier.",
         "An expression is used where a string literal is expected."],
        [
            ("Use correct ATTACH syntax",
             "```sql\nATTACH DATABASE 'filename' AS schema_name;\n```"),
            ("Use a valid schema name",
             "```sql\n-- Valid: alphanumeric and underscores\nATTACH DATABASE 'db.sqlite' AS my_schema;\n```"),
            ("Use a string literal for the filename",
             "```sql\nATTACH DATABASE 'db.sqlite' AS extra;  -- not a variable\n```"),
        ],
        "```sql\nATTACH db.sqlite AS extra;\n-- Error: near \"db\": syntax error\n-- Need quotes around the filename\n```",
    ),
    (
        "DETACH not allowed in transaction",
        "A DETACH DATABASE statement was issued while in the middle of a transaction that modified the attached database.",
        ["database-error", "locking-error"],
        ["DETACH is attempted during an active transaction on the attached database.",
         "The attached database has uncommitted changes.",
         "A trigger or callback holds a reference to the attached database."],
        [
            ("Commit or rollback the transaction first",
             "```sql\nCOMMIT;  -- or ROLLBACK\nDETACH DATABASE extra;\n```"),
            ("Avoid attaching databases that are being modified in the same transaction",
             "```sql\n-- Attach only for read-only queries, then detach\n```"),
            ("Use separate connections for separate databases",
             "```python\nconn_main = sqlite3.connect('main.db')\nconn_extra = sqlite3.connect('extra.db')\n```"),
        ],
        "```sql\nBEGIN;\nATTACH DATABASE 'other.sqlite' AS extra;\nINSERT INTO extra.my_table VALUES (1);\nDETACH DATABASE extra;\n-- Error: cannot detach database in transaction\n```",
    ),
    (
        "attached database encryption not supported",
        "An attempt to attach an encrypted database file failed because SQLite does not support encryption natively.",
        ["database-error"],
        ["The database file is encrypted with SQLCipher or similar.",
         "The SQLite library was not compiled with encryption support.",
         "The encryption key was not provided."],
        [
            ("Use SQLCipher for encrypted databases",
             "```bash\n# Compile SQLite with SQLCipher support\n# Or use a SQLCipher-enabled build\n```"),
            ("Provide the encryption key before attaching",
             "```sql\nPRAGMA key = 'your-encryption-key';\nATTACH DATABASE 'encrypted.db' AS secure;\n```"),
            ("Use an unencrypted copy for non-sensitive operations",
             "```bash\nsqlcipher encrypted.db \".dump\" > decrypted.sql\nsqlite3 plain.db < decrypted.sql\n```"),
        ],
        "```sql\nATTACH DATABASE 'encrypted.db' AS secure;\n-- Error: file is not a database (if encryption not supported)\n```",
    ),
    (
        "memory database attach error",
        "An attempt to attach a :memory: database in a context that does not support it.",
        ["database-error"],
        ["Using :memory: with ATTACH in a context that requires a file.",
         "Trying to attach multiple :memory: databases with the same name.",
         "A :memory: database is not available after connection close."],
        [
            ("Use unique names for multiple memory databases",
             "```sql\nATTACH DATABASE ':memory:' AS mem1;\nATTACH DATABASE ':memory:' AS mem2;\n```"),
            ("Use file-based databases for persistence",
             "```sql\nATTACH DATABASE '/tmp/temp.sqlite' AS temp;\n```"),
            ("Understand that :memory: databases exist only for the connection lifetime",
             "```python\nconn = sqlite3.connect(':memory:')\n# Data lost when conn is closed\n```"),
        ],
        "```sql\nATTACH DATABASE ':memory:' AS main;\n-- Error: cannot attach memory database as 'main'\n```",
    ),
]

for title, desc, err_types, causes, fixes, examples in ATTACH_ERRORS:
    slug = "sqlite-" + title.lower().replace(" ", "-").replace("/", "-")[:60]
    slug = slug.rstrip("-")
    fix_blocks = "\n\n".join(f"### {h}\n\n{b}" for h, b in fixes)
    PAGES.append({
        "slug": slug,
        "title": f"[Solution] SQLite {title}",
        "desc": desc,
        "error_types": err_types,
        "sections": {
            "description": f"SQLite produces **{title}** when {desc.lower()} The ATTACH/DETACH mechanism allows working with multiple databases simultaneously.",
            "causes": causes,
            "fixes": fixes,
            "examples": examples,
        },
    })

# ─── 8. VACUUM/PRAGMA Errors ─────────────────────────────────────────────────
VACUUM_PRAGMA_ERRORS = [
    (
        "VACUUM failed - database locked",
        "VACUUM could not run because the database was locked by another connection.",
        ["database-error", "locking-error"],
        ["Another connection holds a lock on the database.",
         "A long-running read transaction is preventing VACUUM.",
         "VACUUM requires exclusive access."],
        [
            ("Close all other connections before running VACUUM",
             "```bash\nsqlite3 mydb.sqlite 'VACUUM;'\n```"),
            ("Use PRAGMA wal_checkpoint to release WAL locks",
             "```sql\nPRAGMA wal_checkpoint(TRUNCATE);\nVACUUM;\n```"),
            ("Schedule VACUUM during low-traffic periods",
             "```bash\n# Run during maintenance window\n```"),
        ],
        "```sql\n-- Session 1: holding a read lock\nBEGIN;\nSELECT * FROM large_table;\n-- Session 2:\nVACUUM;\n-- Error: database is locked\n```",
    ),
    (
        "VACUUM not allowed in transaction",
        "VACUUM was executed inside an active transaction.",
        ["database-error"],
        ["VACUUM cannot run inside a BEGIN...COMMIT block.",
         "The VACUUM statement was part of a script that began a transaction."],
        [
            ("Ensure no transaction is active",
             "```sql\nCOMMIT;  -- finish any active transaction\nVACUUM;\n```"),
            ("Run VACUUM outside of transactions",
             "```bash\nsqlite3 mydb.sqlite 'VACUUM;'\n```"),
            ("Use auto_vacuum instead for continuous space reclamation",
             "```sql\nPRAGMA auto_vacuum = INCREMENTAL;\n```"),
        ],
        "```sql\nBEGIN;\nVACUUM;\n-- Error: cannot VACUUM from within a transaction\n```",
    ),
    (
        "PRAGMA not recognized",
        "An unrecognized PRAGMA name was used.",
        ["database-error"],
        ["A typo in the PRAGMA name.",
         "The PRAGMA is not supported in the current SQLite version.",
         "An extension PRAGMA is used without loading the extension."],
        [
            ("Check the SQLite documentation for valid PRAGMA names",
             "```sql\nPRAGMA compile_options;  -- lists available features\n```"),
            ("Verify the PRAGMA name spelling",
             "```sql\nPRAGMA journal_mode;  -- correct\nPRAGMA journl_mode;   -- typo\n```"),
            ("Check the SQLite version",
             "```sql\nSELECT sqlite_version();\n```"),
        ],
        "```sql\nPRAGMA journl_mode = WAL;\n-- Error: unrecognized pragma name: journl_mode\n```",
    ),
    (
        "PRAGMA value out of range",
        "A PRAGMA was assigned a value that is outside the acceptable range.",
        ["database-error"],
        ["The value exceeds the minimum or maximum allowed.",
         "A negative value was given where only positives are valid.",
         "The value type is wrong (string where integer is expected)."],
        [
            ("Check the valid range for the PRAGMA",
             "```sql\n-- page_size: 512 to 65536 (must be power of 2)\n-- cache_size: negative = KB, positive = pages\n-- busy_timeout: milliseconds (0+)\n```"),
            ("Use valid values",
             "```sql\nPRAGMA page_size = 4096;  -- valid power of 2\nPRAGMA cache_size = -8000;  -- 8000 KB\n```"),
            ("Use the default if unsure",
             "```sql\nPRAGMA cache_size = -2000;  -- default ~2MB\n```"),
        ],
        "```sql\nPRAGMA page_size = 1000;\n-- Error: page_size must be a power of two between 512 and 65536\n```",
    ),
    (
        "journal_mode change failed",
        "The PRAGMA journal_mode could not be changed to the requested mode.",
        ["database-error"],
        ["Another connection has an active transaction.",
         "The database is on a read-only filesystem.",
         "The requested journal mode is not supported by the filesystem."],
        [
            ("Ensure no active transactions exist",
             "```sql\nCOMMIT;\nPRAGMA journal_mode = WAL;\n```"),
            ("Check filesystem permissions",
             "```bash\nls -la mydb.sqlite mydb.sqlite-wal mydb.sqlite-shm\n```"),
            ("Use the correct journal mode name",
             "```sql\n-- Valid: DELETE, TRUNCATE, PERSIST, MEMORY, WAL, OFF\nPRAGMA journal_mode = WAL;\n```"),
        ],
        "```sql\nBEGIN;\nPRAGMA journal_mode = WAL;\n-- Error: cannot change journal_mode in a transaction\n```",
    ),
    (
        "synchronous mode change failed",
        "The PRAGMA synchronous could not be changed to the requested level.",
        ["database-error"],
        ["Another connection holds a lock.",
         "The database is read-only.",
         "The value is not one of the valid synchronous modes."],
        [
            ("Use a valid synchronous mode",
             "```sql\n-- 0 = OFF, 1 = NORMAL, 2 = FULL, 3 = EXTRA\nPRAGMA synchronous = NORMAL;\n```"),
            ("Change synchronous mode when no other connections are active",
             "```sql\nPRAGMA synchronous = NORMAL;\n```"),
            ("Understand the trade-offs",
             "```sql\n-- OFF: fastest but less safe\n-- NORMAL: good balance for WAL mode\n-- FULL: safest, recommended for DELETE journal mode\n```"),
        ],
        "```sql\nPRAGMA synchronous = 5;\n-- Error: bad value for synchronous: 5\n```",
    ),
    (
        "page_size too small",
        "The PRAGMA page_size was set to a value below the minimum allowed (512 bytes).",
        ["database-error"],
        ["The value is less than 512.",
         "The value is not a power of 2.",
         "page_size was set after the database already has tables."],
        [
            ("Use a valid page size (power of 2, 512-65536)",
             "```sql\nPRAGMA page_size = 4096;  -- 4KB is common default\n```"),
            ("Set page_size on an empty database only",
             "```sql\n-- Create a fresh database, set page_size, then create tables\nPRAGMA page_size = 8192;\nCREATE TABLE t (x INTEGER);\n```"),
            ("Use VACUUM to change page_size of existing database",
             "```sql\nVACUUM;  -- rebuilds with current page_size\n```"),
        ],
        "```sql\nCREATE TABLE t (x INTEGER);\nPRAGMA page_size = 512;\n-- Error: page_size must be set before any tables are created\n```",
    ),
    (
        "cache_size invalid",
        "The PRAGMA cache_size was assigned an invalid value.",
        ["database-error"],
        ["The value is zero or negative in an unexpected way.",
         "The value exceeds memory limits.",
         "The value type is incorrect."],
        [
            ("Use a positive value for page count or negative for KB",
             "```sql\nPRAGMA cache_size = 2000;  -- 2000 pages\nPRAGMA cache_size = -8000;  -- 8000 KB\n```"),
            ("Set a reasonable cache size",
             "```sql\n-- Default is ~2MB (-2000)\n-- For large databases, increase to 64MB:\nPRAGMA cache_size = -65536;\n```"),
            ("Verify the current cache size",
             "```sql\nPRAGMA cache_size;\n```"),
        ],
        "```sql\nPRAGMA cache_size = 0;\n-- Error: cache_size must be greater than 0\n```",
    ),
    (
        "mmap_size limit exceeded",
        "The PRAGMA mmap_size was set higher than the system limit or available memory.",
        ["database-error"],
        ["The value exceeds /proc/sys/vm/mmap_max_bytes.",
         "Insufficient virtual address space.",
         "The database file is smaller than the mmap size."],
        [
            ("Check the system mmap limit",
             "```bash\ncat /proc/sys/vm/mmap_max_bytes\n```"),
            ("Set mmap_size to a reasonable value",
             "```sql\nPRAGMA mmap_size = 268435456;  -- 256 MB\n```"),
            ("Disable mmap if not needed",
             "```sql\nPRAGMA mmap_size = 0;\n```"),
        ],
        "```sql\nPRAGMA mmap_size = 10737418240;\n-- Error: mmap size exceeds system limit\n```",
    ),
]

for title, desc, err_types, causes, fixes, examples in VACUUM_PRAGMA_ERRORS:
    slug = "sqlite-" + title.lower().replace(" ", "-").replace("/", "-")[:60]
    slug = slug.rstrip("-")
    fix_blocks = "\n\n".join(f"### {h}\n\n{b}" for h, b in fixes)
    PAGES.append({
        "slug": slug,
        "title": f"[Solution] SQLite {title}",
        "desc": desc,
        "error_types": err_types,
        "sections": {
            "description": f"SQLite reports **{title}** when {desc.lower()} VACUUM and PRAGMA are powerful maintenance tools that require careful use.",
            "causes": causes,
            "fixes": fixes,
            "examples": examples,
        },
    })

# ─── 9. File I/O Errors ─────────────────────────────────────────────────────
IO_ERRORS = [
    (
        "disk I/O error",
        "SQLite encountered an error while performing a disk read or write operation.",
        ["io-error"],
        ["Disk is full.",
         "File system corruption.",
         "Hardware failure (bad sectors)."],
        [
            ("Check disk space",
             "```bash\ndf -h .\n```"),
            ("Verify file system integrity",
             "```bash\n# Linux:\nfsck /dev/sda1\n# macOS:\ndiskutil verifyVolume /\n```"),
            ("Run PRAGMA integrity_check",
             "```sql\nPRAGMA integrity_check;\n```"),
        ],
        "```bash\nsqlite3 mydb.sqlite \"INSERT INTO t VALUES (1);\"\n-- Error: disk I/O error\n```",
    ),
    (
        "unable to open database file",
        "SQLite cannot open the specified database file.",
        ["io-error"],
        ["The file does not exist.",
         "Insufficient file system permissions.",
         "The directory does not exist."],
        [
            ("Verify the file path",
             "```bash\nls -la /path/to/database.sqlite\n```"),
            ("Check directory permissions",
             "```bash\nls -ld /path/to/\nchmod 755 /path/to/\n```"),
            ("Check file permissions",
             "```bash\nchmod 644 /path/to/database.sqlite\n```"),
        ],
        "```bash\nsqlite3 /nonexistent/mydb.sqlite \"SELECT 1;\"\n-- Error: unable to open database file\n```",
    ),
    (
        "database disk image is malformed",
        "The database file has been corrupted and SQLite cannot read it correctly.",
        ["corruption-error", "io-error"],
        ["Disk failure or bad sectors.",
         "The database was copied while being written to.",
         "Power failure during a write operation."],
        [
            ("Try to recover data with .dump",
             "```bash\nsqlite3 mydb.sqlite '.dump' > recovered.sql\nsqlite3 newdb.sqlite < recovered.sql\n```"),
            ("Use PRAGMA integrity_check to find corruption",
             "```sql\nPRAGMA integrity_check;\n```"),
            ("Restore from a backup",
             "```bash\ncp backup.db mydb.sqlite\n```"),
        ],
        "```bash\nsqlite3 mydb.sqlite \"SELECT * FROM users;\"\n-- Error: database disk image is malformed\n```",
    ),
    (
        "file is not a database",
        "The file opened by SQLite does not contain a valid SQLite database header.",
        ["corruption-error", "io-error"],
        ["The file is not a SQLite database (e.g., it is a CSV or text file).",
         "The file was truncated or partially written.",
         "A non-SQLite file was renamed to .sqlite."],
        [
            ("Verify the file type",
             "```bash\nfile mydb.sqlite\n# Should say: SQLite 3.x database\n```"),
            ("Check the file header",
             "```bash\nxxd mydb.sqlite | head -1\n# Should start with: 53 51 4c 69 74 65 20 66 6f 72 6d 61 74 20 31 00\n```"),
            ("Restore from backup if the file is corrupted",
             "```bash\ncp backup.db mydb.sqlite\n```"),
        ],
        "```bash\nsqlite3 fake.sqlite \"SELECT 1;\"\n-- Error: file is not a database\n```",
    ),
    (
        "file already exists",
        "An attempt to create a database failed because the file already exists and was not expected to.",
        ["io-error"],
        ["The database file was already created.",
         "A previous creation attempt left the file.",
         "Missing IF NOT EXISTS equivalent (SQLite does not have this for file creation)."],
        [
            ("Remove the existing file if a fresh database is needed",
             "```bash\nrm -f mydb.sqlite\nsqlite3 mydb.sqlite \"CREATE TABLE t (x INTEGER);\"\n```"),
            ("Check if the existing file is valid",
             "```bash\nsqlite3 mydb.sqlite '.tables'\n```"),
            ("Use a different filename",
             "```bash\nsqlite3 mydb_v2.sqlite \"CREATE TABLE t (x INTEGER);\"\n```"),
        ],
        "```bash\ntouch mydb.sqlite\nsqlite3 mydb.sqlite \"CREATE TABLE t (x INTEGER);\"\n# File exists but may be empty — SQLite will try to open it\n```",
    ),
    (
        "file not found",
        "The database file specified in the connection string does not exist.",
        ["io-error"],
        ["The file path is incorrect.",
         "The file was deleted.",
         "The file is in a different directory than expected."],
        [
            ("Use the absolute path",
             "```bash\nsqlite3 /full/path/to/mydb.sqlite\n```"),
            ("Check the current directory",
             "```bash\npwd\nls *.sqlite\n```"),
            ("Create the file if it should exist",
             "```bash\nsqlite3 mydb.sqlite \"SELECT 1;\"\n# Creates the file if it does not exist\n```"),
        ],
        "```bash\nsqlite3 /wrong/path/mydb.sqlite\n-- Error: unable to open database file\n```",
    ),
    (
        "permission denied on database file",
        "The operating system denied access to the database file due to insufficient permissions.",
        ["io-error", "permission-error"],
        ["The file is owned by a different user.",
         "File permissions do not allow read/write.",
         "The directory permissions prevent access."],
        [
            ("Check and fix file permissions",
             "```bash\nls -la mydb.sqlite\nchmod 644 mydb.sqlite\nchown $(whoami) mydb.sqlite\n```"),
            ("Check directory permissions",
             "```bash\nls -ld /path/to/directory/\nchmod 755 /path/to/directory/\n```"),
            ("Run as the correct user",
             "```bash\nsudo chown $(whoami) mydb.sqlite\n```"),
        ],
        "```bash\nsqlite3 /root/mydb.sqlite \"SELECT 1;\"\n-- Error: unable to open database file (permission denied)\n```",
    ),
    (
        "WAL file corrupted",
        "The Write-Ahead Logging (WAL) file has become corrupted.",
        ["corruption-error", "io-error"],
        ["Power failure during WAL write.",
         "Disk failure corrupted the WAL file.",
         "A bug in the application caused WAL corruption."],
        [
            ("Delete the WAL file to recover",
             "```bash\nrm -f mydb.sqlite-wal\n# SQLite will recreate the WAL on next open\n```"),
            ("Force a WAL checkpoint",
             "```sql\nPRAGMA wal_checkpoint(TRUNCATE);\n```"),
            ("Restore from backup",
             "```bash\ncp backup.db mydb.sqlite\nrm -f mydb.sqlite-wal mydb.sqlite-shm\n```"),
        ],
        "```bash\nsqlite3 mydb.sqlite \"SELECT * FROM t;\"\n-- Error: WAL file corrupted\nrm mydb.sqlite-wal\nsqlite3 mydb.sqlite \"PRAGMA integrity_check;\"\n```",
    ),
    (
        "SHM file corrupted",
        "The shared memory (SHM) file used by WAL mode has become corrupted.",
        ["corruption-error", "io-error"],
        ["Concurrent access caused SHM corruption.",
         "The SHM file was on a network filesystem (not supported).",
         "Process crash left the SHM file in a bad state."],
        [
            ("Delete the SHM file",
             "```bash\nrm -f mydb.sqlite-shm\n# SQLite will recreate it on next open\n```"),
            ("Avoid using SQLite on NFS for WAL mode",
             "```bash\n# Use local storage for SQLite databases\n```"),
            ("Use PRAGMA locking_mode = EXCLUSIVE to avoid SHM issues",
             "```sql\nPRAGMA locking_mode = EXCLUSIVE;\n```"),
        ],
        "```bash\nrm -f mydb.sqlite-shm\nsqlite3 mydb.sqlite \"PRAGMA journal_mode = WAL;\"\n```",
    ),
    (
        "journal file corrupted",
        "The rollback journal file has become corrupted.",
        ["corruption-error", "io-error"],
        ["Power failure during journal write.",
         "Disk failure corrupted the journal file.",
         "Concurrent access corrupted the journal."],
        [
            ("Delete the journal file to recover",
             "```bash\nrm -f mydb.sqlite-journal\n# SQLite will detect corruption and may recover\n```"),
            ("Use PRAGMA integrity_check",
             "```sql\nPRAGMA integrity_check;\n```"),
            ("Switch to WAL mode for better crash recovery",
             "```sql\nPRAGMA journal_mode = WAL;\n```"),
        ],
        "```bash\nsqlite3 mydb.sqlite \"SELECT * FROM t;\"\n-- Error: journal file corrupted\nrm mydb.sqlite-journal\nsqlite3 mydb.sqlite \"PRAGMA integrity_check;\"\n```",
    ),
    (
        "hot journal detected",
        "SQLite found a hot journal that indicates a previous transaction was not properly committed.",
        ["corruption-error", "io-error"],
        ["A crash occurred during a write transaction.",
         "The process was killed while writing.",
         "A power failure left an incomplete journal."],
        [
            ("Let SQLite replay the journal automatically",
             "```sql\n-- Opening the database should automatically replay the journal\nPRAGMA journal_mode = WAL;\n```"),
            ("Use PRAGMA integrity_check after recovery",
             "```sql\nPRAGMA integrity_check;\n```"),
            ("Delete the journal only if recovery fails",
             "```bash\n# WARNING: may lose uncommitted data\nrm mydb.sqlite-journal\n```"),
        ],
        "```bash\nsqlite3 mydb.sqlite \"PRAGMA journal_mode;\"\n-- Hot journal detected — SQLite will recover automatically\n```",
    ),
    (
        "recovery failed",
        "SQLite was unable to recover the database from a corrupted state.",
        ["corruption-error", "io-error"],
        ["The corruption is too severe for automatic recovery.",
         "Both the database and journal files are corrupted.",
         "Critical data pages are damaged."],
        [
            ("Try to dump whatever is recoverable",
             "```bash\nsqlite3 mydb.sqlite '.dump' > partial_recovery.sql\n```"),
            ("Use the recover extension (SQLite 3.40+)",
             "```sql\n-- If available:\n-- .recover command in the CLI\n```"),
            ("Restore from a known-good backup",
             "```bash\ncp backup.db mydb.sqlite\n```"),
        ],
        "```bash\nsqlite3 mydb.sqlite '.recover' > recovery.sql\n# If .recover also fails, restore from backup\n```",
    ),
]

for title, desc, err_types, causes, fixes, examples in IO_ERRORS:
    slug = "sqlite-" + title.lower().replace(" ", "-").replace("/", "-")[:60]
    slug = slug.rstrip("-")
    fix_blocks = "\n\n".join(f"### {h}\n\n{b}" for h, b in fixes)
    PAGES.append({
        "slug": slug,
        "title": f"[Solution] SQLite {title}",
        "desc": desc,
        "error_types": err_types,
        "sections": {
            "description": f"SQLite encounters **{title}** when {desc.lower()} These errors typically relate to the underlying file system and require careful recovery steps.",
            "causes": causes,
            "fixes": fixes,
            "examples": examples,
        },
    })

# ─── 10. FTS (Full Text Search) Errors ───────────────────────────────────────
FTS_ERRORS = [
    (
        "FTS3/FTS4 tokenizer error",
        "The FTS3 or FTS4 full-text search engine encountered an error with its tokenizer configuration.",
        ["query-error"],
        ["An invalid tokenizer was specified during table creation.",
         "A custom tokenizer module failed to initialize.",
         "The tokenizer does not support the required Unicode features."],
        [
            ("Use a built-in tokenizer",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content, tokenize='porter unicode61');\n```"),
            ("Verify available tokenizers",
             "```sql\n-- Available: simple, porter, unicode61, ascii\n```"),
            ("Check tokenizer parameters",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content, tokenize='unicode61 remove_diacritics 2');\n```"),
        ],
        "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content, tokenize='invalid_tokenizer');\n-- Error: no such tokenizer: invalid_tokenizer\n```",
    ),
    (
        "FTS5 syntax error",
        "An FTS5 query contains invalid syntax.",
        ["query-error"],
        ["Malformed FTS5 query expression.",
         "Invalid use of FTS5 operators (AND, OR, NOT).",
         "Mismatched parentheses in the query."],
        [
            ("Check FTS5 query syntax",
             "```sql\n-- Valid: simple terms, AND, OR, NOT, phrases, prefixes\nSELECT * FROM docs WHERE docs MATCH 'error AND fix';\n```"),
            ("Quote phrases with double quotes",
             "```sql\nSELECT * FROM docs WHERE docs MATCH '\"disk I/O\"';\n```"),
            ("Use column filters correctly",
             "```sql\nSELECT * FROM docs WHERE docs MATCH 'title:error OR body:fix';\n```"),
        ],
        "```sql\nSELECT * FROM docs WHERE docs MATCH 'error AND OR fix';\n-- Error: FTS5 syntax error near \"OR\"\n```",
    ),
    (
        "FTS content table not found",
        "An FTS table references a content table that does not exist.",
        ["query-error", "schema-error"],
        ["The content table was dropped.",
         "The content= parameter references a non-existent table.",
         "A typo in the content table name."],
        [
            ("Verify the content table exists",
             "```sql\nSELECT name FROM sqlite_master WHERE type='table' AND name='my_content';\n```"),
            ("Create the content table",
             "```sql\nCREATE TABLE my_content (id INTEGER PRIMARY KEY, title TEXT, body TEXT);\n```"),
            ("Use contentless FTS if no content table is needed",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content='');\n```"),
        ],
        "```sql\nCREATE VIRTUAL TABLE docs USING fts5(title, body, content=my_nonexistent);\n-- Error: no such table: my_nonexistent\n```",
    ),
    (
        "FTS content_rowid missing",
        "An FTS table configured with content= requires a content_rowid= that was not provided.",
        ["query-error"],
        ["The content_rowid= parameter is missing.",
         "The content_rowid column does not exist in the content table.",
         "The content_rowid type is incompatible."],
        [
            ("Provide content_rowid when using content=",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(title, body, content=my_table, content_rowid=id);\n```"),
            ("Ensure the content_rowid column exists in the content table",
             "```sql\nPRAGMA table_info(my_table);\n```"),
            ("Use rowid if no explicit ID column exists",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(title, body, content=my_table, content_rowid=rowid);\n```"),
        ],
        "```sql\nCREATE VIRTUAL TABLE docs USING fts5(title, content=my_table);\n-- Error: content_rowid required when content= is specified\n```",
    ),
    (
        "FTS languageid column error",
        "An FTS table's languageid column configuration is incorrect.",
        ["query-error"],
        ["The languageid column does not exist in the content table.",
         "The languageid value is not a valid integer.",
         "The languageid configuration is duplicated."],
        [
            ("Provide a valid languageid column",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(title, body, content=my_table, content_rowid=id, languageid=lang_id);\n```"),
            ("Ensure the column exists and is INTEGER",
             "```sql\nALTER TABLE my_table ADD COLUMN lang_id INTEGER DEFAULT 0;\n```"),
            ("Use the default languageid if multi-language is not needed",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(title, body);\n```"),
        ],
        "```sql\nCREATE VIRTUAL TABLE docs USING fts5(title, languageid=nonexistent);\n-- Error: no such column: nonexistent\n```",
    ),
    (
        "FTS prefix parameter invalid",
        "An FTS5 prefix= parameter specifies an invalid prefix length.",
        ["query-error"],
        ["The prefix value is zero or negative.",
         "The prefix value exceeds the token length.",
         "The prefix value is not an integer."],
        [
            ("Use valid prefix values (1 or more)",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content, prefix='2 3');\n```"),
            ("Use reasonable prefix values",
             "```sql\n-- prefix='2' indexes 2-character prefixes\n-- prefix='2 3' indexes 2 and 3 character prefixes\n```"),
            ("Check prefix configuration",
             "```sql\n-- Prefix must be a space-separated list of positive integers\n```"),
        ],
        "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content, prefix='0');\n-- Error: prefix must be a positive integer\n```",
    ),
    (
        "FTS unicode61 tokenizer error",
        "The unicode61 tokenizer encountered an error during tokenization.",
        ["query-error"],
        ["An invalid remove_diacritics value was specified.",
         "The tokenizer configuration is incorrect.",
         "The input text contains invalid Unicode."],
        [
            ("Use valid remove_diacritics values (0, 1, or 2)",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content, tokenize='unicode61 remove_diacritics 2');\n```"),
            ("Use default unicode61 settings",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content, tokenize='unicode61');\n```"),
            ("Check token separators",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content, tokenize='unicode61 tokenchars \".-\");\n```"),
        ],
        "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content, tokenize='unicode61 remove_diacritics 5');\n-- Error: invalid remove_diacritics value\n```",
    ),
    (
        "FTS porter stemmer error",
        "The Porter stemming algorithm used by FTS encountered an error during processing.",
        ["query-error"],
        ["The input word could not be stemmed.",
         "The Porter stemmer is combined with incompatible tokenizer options.",
         "An invalid character sequence was passed to the stemmer."],
        [
            ("Combine porter with a valid base tokenizer",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content, tokenize='porter unicode61');\n```"),
            ("Handle stemming errors at the application layer",
             "```python\n# FTS handles stemming internally; errors are rare\n# Ensure input text is valid UTF-8\n```"),
            ("Use simple tokenizer if porter causes issues",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content, tokenize='simple');\n```"),
        ],
        "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content, tokenize='porter');\n-- Porter stemmer requires a secondary tokenizer like unicode61\n```",
    ),
    (
        "FTS table corruption",
        "An FTS index has become corrupted and search results may be incorrect or queries may fail.",
        ["corruption-error", "query-error"],
        ["The FTS segment files are damaged.",
         "A crash during FTS update corrupted the index.",
         "The underlying content table was modified outside of FTS."],
        [
            ("Rebuild the FTS index",
             "```sql\nINSERT INTO docs(docs) VALUES('rebuild');\n```"),
            ("Drop and recreate the FTS table",
             "```sql\nDROP TABLE IF EXISTS docs;\nCREATE VIRTUAL TABLE docs USING fts5(title, body);\n-- Re-populate from content table\n```"),
            ("Use contentless-auto-delete for simpler rebuilds",
             "```sql\nCREATE VIRTUAL TABLE docs USING fts5(title, body, contentless_delete=1);\n```"),
        ],
        "```sql\nINSERT INTO docs(docs) VALUES('rebuild');\n-- Rebuilds the FTS index from the content table\n```",
    ),
    (
        "FTS MATCH syntax error",
        "An FTS MATCH query contains a syntax error.",
        ["query-error"],
        ["Invalid characters in the MATCH expression.",
         "Incorrect use of FTS operators.",
         "A phrase is not properly quoted."],
        [
            ("Use correct FTS MATCH syntax",
             "```sql\nSELECT * FROM docs WHERE docs MATCH 'search term';\n```"),
            ("Quote phrases with double quotes",
             "```sql\nSELECT * FROM docs WHERE docs MATCH '\"exact phrase\"';\n```"),
            ("Use column filters",
             "```sql\nSELECT * FROM docs WHERE docs MATCH 'title:search OR body:term';\n```"),
        ],
        "```sql\nSELECT * FROM docs WHERE docs MATCH '\"unclosed phrase;\n-- Error: FTS5 syntax error near \"unclosed\n```",
    ),
]

for title, desc, err_types, causes, fixes, examples in FTS_ERRORS:
    slug = "sqlite-" + title.lower().replace(" ", "-").replace("/", "-")[:60]
    slug = slug.rstrip("-")
    fix_blocks = "\n\n".join(f"### {h}\n\n{b}" for h, b in fixes)
    PAGES.append({
        "slug": slug,
        "title": f"[Solution] SQLite {title}",
        "desc": desc,
        "error_types": err_types,
        "sections": {
            "description": f"SQLite FTS raises **{title}** when {desc.lower()} Full-text search is a powerful extension but requires correct configuration.",
            "causes": causes,
            "fixes": fixes,
            "examples": examples,
        },
    })

# ─── 11. JSON1 Extension Errors ─────────────────────────────────────────────
JSON_ERRORS = [
    (
        "json() parse error",
        "The json() function could not parse the input string as valid JSON.",
        ["query-error"],
        ["The input string is not valid JSON.",
         "Trailing commas or missing quotes.",
         "The JSON contains invalid escape sequences."],
        [
            ("Validate JSON input before calling json()",
             "```sql\nSELECT json_valid('{\"a\": 1}');  -- returns 1 (true)\n```"),
            ("Fix common JSON syntax issues",
             "```sql\n-- Wrong: {a: 1}\n-- Right: {\"a\": 1}\nSELECT json('{\"a\": 1}');\n```"),
            ("Use json_valid() as a guard",
             "```sql\nSELECT CASE WHEN json_valid(col) THEN json(col) ELSE NULL END FROM t;\n```"),
        ],
        "```sql\nSELECT json('{a: 1}');\n-- Error: malformed JSON\n```",
    ),
    (
        "json_extract() path error",
        "The json_extract() function received an invalid JSON path.",
        ["query-error"],
        ["The path syntax is incorrect.",
         "The path references a non-existent element.",
         "The path uses incorrect operators."],
        [
            ("Use correct JSON path syntax",
             "```sql\nSELECT json_extract('{\"a\": 1}', '$.a');  -- returns 1\n```"),
            ("Use bracket notation for array elements",
             "```sql\nSELECT json_extract('[1,2,3]', '$[0]');  -- returns 1\n```"),
            ("Use wildcard for all array elements",
             "```sql\nSELECT json_extract('[1,2,3]', '$[*]');  -- returns '1,2,3'\n```"),
        ],
        "```sql\nSELECT json_extract('{\"a\": 1}', 'a');\n-- Error: invalid JSON path: must start with '$'\n```",
    ),
    (
        "json_set() not valid",
        "The json_set() function received invalid arguments or produced invalid JSON.",
        ["query-error"],
        ["The value to set is not valid JSON.",
         "The path does not exist and cannot be created.",
         "The arguments have incorrect types."],
        [
            ("Provide valid JSON values",
             "```sql\nSELECT json_set('{\"a\": 1}', '$.a', 2);  -- {\"a\": 2}\n```"),
            ("Use json_insert() to add new keys",
             "```sql\nSELECT json_insert('{}', '$.b', 3);  -- {\"b\": 3}\n```"),
            ("Use json_remove() then json_set() for replacements",
             "```sql\nSELECT json_set(json_remove('{\"a\":1}', '$.a'), '$.a', 2);\n```"),
        ],
        "```sql\nSELECT json_set('{\"a\": 1}', '$.a', json('invalid'));\n-- Error: invalid JSON value\n```",
    ),
    (
        "json_array()/json_object() syntax error",
        "The json_array() or json_object() function received incorrect arguments.",
        ["query-error"],
        ["An odd number of arguments for json_object().",
         "An argument is not a valid JSON value.",
         "A key in json_object() is not a string."],
        [
            ("Ensure json_object() has an even number of arguments",
             "```sql\nSELECT json_object('name', 'Alice', 'age', 30);\n```"),
            ("Use json_array() for ordered lists",
             "```sql\nSELECT json_array(1, 'two', 3.0, NULL);\n```"),
            ("Validate argument types",
             "```sql\n-- Keys must be strings, values can be any JSON type\n```"),
        ],
        "```sql\nSELECT json_object('name', 'Alice', 'age');\n-- Error: json_object() requires an even number of arguments\n```",
    ),
    (
        "json_each()/json_tree() not table",
        "The json_each() or json_tree() function is used in a context that does not return a table.",
        ["query-error"],
        ["The function is not used in a FROM clause.",
         "The input is not valid JSON.",
         "The path argument is incorrect."],
        [
            ("Use json_each() in a FROM clause",
             "```sql\nSELECT * FROM json_each('[1,2,3]');\n```"),
            ("Use json_tree() for recursive traversal",
             "```sql\nSELECT * FROM json_tree('{\"a\": {\"b\": 1}}');\n```"),
            ("Provide valid JSON input",
             "```sql\nSELECT * FROM json_each('{\"a\": 1, \"b\": 2}');\n```"),
        ],
        "```sql\nSELECT json_each('[1,2,3]');\n-- Error: json_each() can only be used in the FROM clause of a SELECT\n```",
    ),
    (
        "json_type() invalid argument",
        "The json_type() function received an invalid JSON value or path.",
        ["query-error"],
        ["The input is not valid JSON.",
         "The path references a non-existent element.",
         "The function is used with wrong number of arguments."],
        [
            ("Provide valid JSON input",
             "```sql\nSELECT json_type('{\"a\": 1}', '$.a');  -- returns 'integer'\n```"),
            ("Check for null results",
             "```sql\nSELECT json_type('{\"a\": 1}', '$.b');  -- returns NULL (not an error)\n```"),
            ("Use json_type() to validate before processing",
             "```sql\nSELECT CASE json_type(col, '$.value')\n    WHEN 'integer' THEN 'number'\n    WHEN 'text' THEN 'string'\n    ELSE 'other'\nEND FROM t;\n```"),
        ],
        "```sql\nSELECT json_type('not json');\n-- Error: invalid JSON input\n```",
    ),
    (
        "json_valid() not Boolean",
        "The json_valid() function did not receive arguments it can evaluate.",
        ["query-error"],
        ["The input is NULL.",
         "The function is used in a context expecting a different type.",
         "The argument count is wrong."],
        [
            ("Pass a single string argument",
             "```sql\nSELECT json_valid('{\"a\": 1}');  -- returns 1\nSELECT json_valid('not json');    -- returns 0\n```"),
            ("Handle NULL input",
             "```sql\nSELECT json_valid(COALESCE(col, ''));\n```"),
            ("Use in WHERE clause to filter valid JSON",
             "```sql\nSELECT * FROM t WHERE json_valid(json_col);\n```"),
        ],
        "```sql\nSELECT json_valid(NULL);\n-- Returns NULL (not an error, but unexpected)\n```",
    ),
    (
        "JSON path syntax error",
        "A JSON path expression uses invalid syntax for the JSON1 extension.",
        ["query-error"],
        ["The path does not start with $.",
         "The path contains invalid characters.",
         "The path uses incorrect bracket notation."],
        [
            ("Use correct JSON path syntax",
             "```sql\n-- Valid paths: $.key, $[0], $.key.subkey, $[0].key\nSELECT json_extract('{\"a\":{\"b\":1}}', '$.a.b');\n```"),
            ("Use bracket notation for array indices",
             "```sql\nSELECT json_extract('[1,2,3]', '$[1]');  -- returns 2\n```"),
            ("Use wildcard for array elements",
             "```sql\nSELECT json_extract('[1,2,3]', '$[*]');  -- returns all\n```"),
        ],
        "```sql\nSELECT json_extract('{\"a\": 1}', 'a');\n-- Error: invalid JSON path: must begin with '$'\n```",
    ),
    (
        "nested JSON too deep",
        "A JSON string has nesting depth that exceeds SQLite's internal limit.",
        ["query-error", "runtime-error"],
        ["The JSON is deeply nested (e.g., generated by a recursive process).",
         "The nesting exceeds SQLite's internal limit (default 1000).",
         "A malformed JSON string creates artificial nesting."],
        [
            ("Flatten deeply nested JSON structures",
             "```sql\n-- Use json_tree() to extract values at specific depths\nSELECT * FROM json_tree('{\"a\":{\"b\":{\"c\":1}}}', '$.a.b');\n```"),
            ("Reduce nesting in the application layer",
             "```python\n# Flatten nested dicts before inserting into SQLite\n```"),
            ("Use multiple rows instead of deep nesting",
             "```sql\n-- Instead of {\"a\":{\"b\":{\"c\":1}}}\n-- Use: a.b.c = 1 (flat key-value pairs)\n```"),
        ],
        "```sql\nSELECT json_extract('{\"a\":{\"b\":{\"c\":{\"d\":{...}}}}}', '$.a.b.c.d');\n-- Error: JSON too deeply nested\n```",
    ),
    (
        "json_group_array() error",
        "The json_group_array() aggregate function received an invalid argument or context.",
        ["query-error"],
        ["The function is used outside an aggregate context.",
         "The input values are not valid JSON.",
         "The function is nested incorrectly."],
        [
            ("Use json_group_array() with GROUP BY",
             "```sql\nSELECT dept, json_group_array(name) AS members\nFROM employees\nGROUP BY dept;\n```"),
            ("Ensure input values are valid JSON",
             "```sql\nSELECT json_group_array(json_object('id', id, 'name', name))\nFROM employees;\n```"),
            ("Use json_group_object() for key-value aggregation",
             "```sql\nSELECT json_group_object(id, name) FROM employees;\n```"),
        ],
        "```sql\nSELECT json_group_array(name) FROM employees;\n-- Error: misuse of aggregate function json_group_array()\n-- Must have GROUP BY or use in aggregate context\n```",
    ),
]

for title, desc, err_types, causes, fixes, examples in JSON_ERRORS:
    slug = "sqlite-json-" + title.lower().replace("(", "").replace(")", "").replace("/", "-").replace(" ", "-")[:60]
    slug = slug.rstrip("-")
    fix_blocks = "\n\n".join(f"### {h}\n\n{b}" for h, b in fixes)
    PAGES.append({
        "slug": slug,
        "title": f"[Solution] SQLite {title}",
        "desc": desc,
        "error_types": err_types,
        "sections": {
            "description": f"SQLite JSON1 extension produces **{title}** when {desc.lower()} The JSON1 extension provides powerful JSON manipulation functions for SQLite.",
            "causes": causes,
            "fixes": fixes,
            "examples": examples,
        },
    })

# ─── 12. Miscellaneous Errors ────────────────────────────────────────────────
MISC_ERRORS = [
    (
        "function not found",
        "An SQL statement references a function that does not exist in the current SQLite build.",
        ["query-error"],
        ["The function requires an extension that is not loaded.",
         "A typo in the function name.",
         "The function is not available in the compiled SQLite version."],
        [
            ("Load the required extension",
             "```sql\nSELECT load_extension('extension_name');\n```"),
            ("Check available functions",
             "```sql\nPRAGMA compile_options;  -- lists compiled features\n```"),
            ("Use an equivalent built-in function",
             "```sql\n-- Instead of custom: use SUBSTR, INSTR, etc.\n```"),
        ],
        "```sql\nSELECT REGEXP('abc', 'b');\n-- Error: no such function: REGEXP\n```",
    ),
    (
        "collation not found",
        "An SQL statement references a collation sequence that does not exist.",
        ["query-error"],
        ["The collation was defined in a different connection.",
         "A custom collation was not registered.",
         "A typo in the collation name."],
        [
            ("Use a built-in collation",
             "```sql\n-- Built-in: BINARY, NOCASE, RTRIM\nSELECT * FROM users ORDER BY name COLLATE NOCASE;\n```"),
            ("Register a custom collation in the application",
             "```python\nconn.create_collation('MY_COLLATE', lambda a, b: (a > b) - (a < b))\n```"),
            ("Check available collations",
             "```sql\nSELECT * FROM pragma_collation_list;\n```"),
        ],
        "```sql\nSELECT * FROM users ORDER BY name COLLATE MY_CUSTOM;\n-- Error: no such collation sequence: MY_CUSTOM\n```",
    ),
    (
        "LIKE pattern too complex",
        "A LIKE pattern exceeds SQLite's internal pattern complexity limit.",
        ["query-error"],
        ["The LIKE pattern has too many wildcards (% or _).",
         "The pattern is extremely long.",
         "The pattern contains nested wildcards."],
        [
            ("Simplify the LIKE pattern",
             "```sql\n-- Instead of: LIKE '%a%b%c%d%e%f%g%h%i%j%k%l%m%n%o%p%q%r%s%t%u%v%w%x%y%z%'\n-- Use: LIKE '%abc%'\n```"),
            ("Use multiple simpler LIKE conditions",
             "```sql\nSELECT * FROM t WHERE name LIKE '%foo%' AND name LIKE '%bar%';\n```"),
            ("Use GLOB for simpler pattern matching",
             "```sql\nSELECT * FROM t WHERE name GLOB '*foo*';\n```"),
        ],
        "```sql\nSELECT * FROM t WHERE name LIKE '%a%b%c%d%e%f%g%h%i%j%k%l%m%n%o%p%q%r%s%t%u%v%w%x%y%z%';\n-- May exceed pattern complexity limit\n```",
    ),
    (
        "GLOB syntax error",
        "A GLOB pattern contains invalid syntax.",
        ["query-error"],
        ["The GLOB pattern has unmatched brackets.",
         "Invalid characters in the pattern.",
         "The GLOB pattern is empty."],
        [
            ("Use correct GLOB syntax",
             "```sql\nSELECT * FROM t WHERE name GLOB '[A-Z]*';\n```"),
            ("Escape special characters",
             "```sql\n-- Use backslash to escape: \\*, \\?, \\[\\nSELECT * FROM t WHERE name GLOB 'test\\*';\n```"),
            ("Verify the pattern is not empty",
             "```sql\nSELECT * FROM t WHERE name GLOB '*';  -- matches everything\n```"),
        ],
        "```sql\nSELECT * FROM t WHERE name GLOB '[A-Z*';\n-- Error: unmatched bracket in GLOB pattern\n```",
    ),
    (
        "REGEXP not defined",
        "The REGEXP operator is used but no REGEXP function has been registered.",
        ["query-error"],
        ["SQLite does not include REGEXP by default.",
         "A custom REGEXP function was not loaded.",
         "The regexp extension was not compiled in."],
        [
            ("Load the regexp extension",
             "```sql\n-- In application code:\nimport re\nconn.create_function('regexp', 2, lambda pattern, string: 1 if re.search(pattern, string) else 0)\n```"),
            ("Use LIKE or GLOB instead of REGEXP",
             "```sql\nSELECT * FROM t WHERE name LIKE '%error%';\nSELECT * FROM t WHERE name GLOB '*error*';\n```"),
            ("Install a regexp extension",
             "```bash\n# Compile SQLite with regexp support or load a shared library\n```"),
        ],
        "```sql\nSELECT * FROM t WHERE name REGEXP '^[A-Z]';\n-- Error: no such function: regexp\n```",
    ),
    (
        "IN() list too large",
        "An IN() list contains more elements than SQLite can process.",
        ["query-error", "runtime-error"],
        ["The IN() list has thousands of elements.",
         "The list exceeds the expression depth limit.",
         "Memory allocation for the list fails."],
        [
            ("Use a temporary table instead",
             "```sql\nCREATE TEMPORARY TABLE filter_ids (id INTEGER);\nINSERT INTO filter_ids VALUES (1), (2), (3), ...;\nSELECT * FROM main_table WHERE id IN (SELECT id FROM filter_ids);\n```"),
            ("Use a VALUES clause in a subquery",
             "```sql\nSELECT * FROM main_table WHERE id IN (VALUES (1), (2), (3), ...);\n```"),
            ("Batch the queries",
             "```sql\n-- Split into chunks of 500-1000 elements\n```"),
        ],
        "```sql\nSELECT * FROM t WHERE id IN (1, 2, 3, ..., 10000);\n-- May exceed expression depth limit\n```",
    ),
    (
        "UNION ALL vs UNION syntax error",
        "A UNION or UNION ALL query has a syntax error.",
        ["query-error"],
        ["Mismatched number of columns in SELECT statements.",
         "Incorrect UNION syntax.",
         "Missing parentheses around subqueries."],
        [
            ("Ensure matching column counts",
             "```sql\nSELECT id, name FROM users\nUNION ALL\nSELECT id, name FROM archived_users;\n```"),
            ("Use UNION for distinct results",
             "```sql\nSELECT id, name FROM users\nUNION\nSELECT id, name FROM archived_users;\n```"),
            ("Parenthesize complex UNION queries",
             "```sql\n(SELECT id FROM users WHERE active = 1)\nUNION\n(SELECT id FROM users WHERE active = 0);\n```"),
        ],
        "```sql\nSELECT id FROM users\nUNION ALL\nSELECT id, name FROM archived_users;\n-- Error: SELECTs must have the same number of columns\n```",
    ),
    (
        "LIMIT/OFFSET out of range",
        "A LIMIT or OFFSET value is negative or exceeds the maximum allowed value.",
        ["query-error"],
        ["A negative LIMIT or OFFSET value.",
         "The OFFSET exceeds the number of available rows.",
         "The value exceeds the maximum integer limit."],
        [
            ("Use non-negative values",
             "```sql\nSELECT * FROM t LIMIT 10 OFFSET 0;\n```"),
            ("Handle OFFSET exceeding row count",
             "```sql\nSELECT * FROM t LIMIT 10 OFFSET 1000;\n-- Returns fewer than 10 rows if table has fewer than 1010 rows\n```"),
            ("Use valid integer values",
             "```sql\n-- LIMIT must be >= 0\n-- OFFSET must be >= 0\nSELECT * FROM t LIMIT 10 OFFSET 5;\n```"),
        ],
        "```sql\nSELECT * FROM t LIMIT -1;\n-- Error: LIMIT value must be non-negative\n```",
    ),
    (
        "INSTEAD OF trigger on view error",
        "An INSTEAD OF trigger fired on a view but the trigger body has an error.",
        ["query-error", "schema-error"],
        ["The INSTEAD OF trigger does not handle the operation correctly.",
         "The trigger tries to modify a read-only view.",
         "The trigger body references invalid columns."],
        [
            ("Create proper INSTEAD OF triggers for views",
             "```sql\nCREATE TRIGGER insert_users INSTEAD OF INSERT ON user_view\nBEGIN\n    INSERT INTO users (id, name) VALUES (new.id, new.name);\nEND;\n```"),
            ("Handle INSERT, UPDATE, and DELETE operations",
             "```sql\nCREATE TRIGGER delete_users INSTEAD OF DELETE ON user_view\nBEGIN\n    DELETE FROM users WHERE id = old.id;\nEND;\n```"),
            ("Verify the trigger references valid columns",
             "```sql\n-- Use new.* for INSERT/UPDATE, old.* for UPDATE/DELETE\n```"),
        ],
        "```sql\nCREATE VIEW user_view AS SELECT id, name FROM users;\n-- Without an INSTEAD OF trigger, INSERT into user_view fails\n```",
    ),
    (
        "virtual table not available",
        "A virtual table module is not available or not loaded.",
        ["query-error"],
        ["The FTS5 or other virtual table extension is not compiled in.",
         "A custom virtual table module was not loaded.",
         "The module name is misspelled."],
        [
            ("Load the required extension",
             "```sql\nSELECT load_extension('fts5');\n```"),
            ("Check available virtual table modules",
             "```sql\nPRAGMA compile_options;\n-- Look for ENABLE_FTS5, etc.\n```"),
            ("Use a built-in virtual table",
             "```sql\nCREATE VIRTUAL TABLE t USING fts5(content);\n```"),
        ],
        "```sql\nCREATE VIRTUAL TABLE docs USING fts5(content);\n-- Error: no such module: fts5 (if FTS5 not compiled)\n```",
    ),
    (
        "module not loadable",
        "The load_extension() function could not load the specified extension module.",
        ["query-error"],
        ["The extension file does not exist.",
         "The extension is not compatible with the SQLite version.",
         "Extension loading is disabled for security."],
        [
            ("Verify the extension file path",
             "```bash\nls -la /path/to/extension.so\n```"),
            ("Enable extension loading",
             "```sql\n-- In application code:\n-- conn.enable_load_extension(True)\n```"),
            ("Check SQLite version compatibility",
             "```sql\nSELECT sqlite_version();\n```"),
        ],
        "```sql\nSELECT load_extension('nonexistent_extension');\n-- Error: unable to load extension\n```",
    ),
    (
        "extension_init() failed",
        "An extension's initialization function returned an error.",
        ["query-error"],
        ["The extension encountered an internal error during initialization.",
         "The extension is not compatible with the current SQLite build.",
         "A required dependency is missing."],
        [
            ("Check the SQLite version",
             "```sql\nSELECT sqlite_version();\n```"),
            ("Try a different version of the extension",
             "```bash\n# Download a compatible extension version\n```"),
            ("Check for missing dependencies",
             "```bash\nldd /path/to/extension.so\n```"),
        ],
        "```sql\nSELECT load_extension('my_extension');\n-- Error: extension initialization failed\n```",
    ),
]

for title, desc, err_types, causes, fixes, examples in MISC_ERRORS:
    slug = "sqlite-" + title.lower().replace("(", "").replace(")", "").replace("/", "-").replace(" ", "-")[:60]
    slug = slug.rstrip("-")
    fix_blocks = "\n\n".join(f"### {h}\n\n{b}" for h, b in fixes)
    PAGES.append({
        "slug": slug,
        "title": f"[Solution] SQLite {title}",
        "desc": desc,
        "error_types": err_types,
        "sections": {
            "description": f"SQLite produces **{title}** when {desc.lower()} This error can occur in various contexts and requires understanding the specific trigger.",
            "causes": causes,
            "fixes": fixes,
            "examples": examples,
        },
    })


# ─── Page Generator ──────────────────────────────────────────────────────────

def build_page(page: dict) -> str:
    """Build a markdown page from a page dict."""
    s = page["sections"]
    cause_lines = "\n".join(f"- {c}" for c in s["causes"])

    fix_blocks = []
    for heading, code_block in s["fixes"]:
        fix_blocks.append(f"### {heading}\n\n{code_block}")
    fix_text = "\n\n".join(fix_blocks)

    err_type_tag = page.get("error_types", ["database-error"])[0]

    frontmatter = (
        f"---\n"
        f'title: "{page["title"]}"\n'
        f'description: "{page["desc"]}"\n'
        f'tools: ["sqlite"]\n'
        f'error-types: ["{err_type_tag}"]\n'
        f'severities: ["error"]\n'
        f"---\n"
    )

    body = f"""{frontmatter}

# {page['title']}

{s['description']}

## Common Causes

{cause_lines}

## How to Fix

{fix_text}

## Examples

{s['examples']}

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
"""
    return body


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    written = 0
    slugs_seen = set()

    for page in PAGES:
        slug = page["slug"]
        if slug in slugs_seen:
            # deduplicate
            i = 2
            while f"{slug}-v{i}" in slugs_seen:
                i += 1
            slug = f"{slug}-v{i}"
            page["slug"] = slug
        slugs_seen.add(slug)

        filepath = os.path.join(OUTPUT_DIR, f"{slug}.md")
        content = build_page(page)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        written += 1

    print(f"Generated {written} SQLite error pages in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
