---
title: "[Solution] Perl DBI Database Handle Error"
description: "Fix Perl DBI database errors including connection failures, query errors, and handle management issues."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A DBI error occurs when the Perl Database Interface fails during database operations. This includes connection failures, query execution errors, and handle management issues.

## Common Causes

- Database connection failure (wrong credentials, server down)
- SQL syntax error
- Missing database driver (DBD module)
- Handle not properly initialized
- Transaction not committed or rolled back

## How to Fix

```perl
# WRONG: No error checking on connect
use DBI;
my $dbh = DBI->connect("dbi:mysql:database=test", "user", "pass");
# May return undef without checking

# CORRECT: Check connection
use DBI;
my $dbh = DBI->connect(
    "dbi:mysql:database=test;host=localhost",
    "user",
    "pass",
    { RaiseError => 1, AutoCommit => 1 }
) or die "Cannot connect: " . DBI->errstr;
```

```perl
# WRONG: Not using placeholders (SQL injection risk)
my $name = "Alice";
my $sth = $dbh->prepare("SELECT * FROM users WHERE name = '$name'");

# CORRECT: Use placeholders
my $sth = $dbh->prepare("SELECT * FROM users WHERE name = ?");
$sth->execute($name);
```

```perl
# WRONG: Not checking query results
$sth->execute();
my @row = $sth->fetchrow_array();  # May be empty

# CORRECT: Check row count
$sth->execute();
if ($sth->rows > 0) {
    my @row = $sth->fetchrow_array();
} else {
    print "No results found\n";
}
```

## Examples

```perl
# Example 1: Complete DBI pattern
use DBI;
use strict;
use warnings;

my $dbh = DBI->connect(
    "dbi:Pg:dbname=mydb;host=localhost",
    "user", "pass",
    { RaiseError => 1, AutoCommit => 0 }
) or die DBI->errstr;

eval {
    my $sth = $dbh->prepare("INSERT INTO logs (msg) VALUES (?)");
    $sth->execute("Hello");
    $dbh->commit;
};
if ($@) {
    $dbh->rollback;
    die "Transaction failed: $@";
}

# Example 2: Disconnect properly
END {
    $dbh->disconnect() if $dbh;
}

# Example 3: DBI trace for debugging
DBI->trace(2);  # Enable tracing
```

## Related Errors

- [perl-file-not-found]({{< relref "/languages/perl/perl-file-not-found" >}}) — file not found
- [perl-runtime-error]({{< relref "/languages/perl/perl-runtime-error" >}}) — runtime error
- [perl-socket-error]({{< relref "/languages/perl/perl-socket-error" >}}) — socket error
