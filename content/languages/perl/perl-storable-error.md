---
title: "[Solution] Perl Storable Error"
description: "Fix Perl Storable errors when serializing or deserializing data structures with nstore or retrieve."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Storable errors occur when the Storable module fails to serialize data structures due to circular references, code references, or incompatible versions.

## Common Causes

- Circular references in data structure
- Code references (subroutines) in storable data
- Version mismatch between nstore and retrieve
- File corrupted during write

## How to Fix

### 1. Remove circular references before storing

```perl
use Storable;

# WRONG: Circular reference
my %data;
$data{self} = \%data;
nstore \%data, 'data.dat';  # may fail

# CORRECT: Break cycles
delete $data{self};
nstore \%data, 'data.dat';
```

### 2. Use nstore for portable binary format

```perl
use Storable qw(nstore retrieve);

nstore \%hash, 'file.stor';
my $ref = retrieve('file.stor');
```

## Examples

```perl
use strict;
use warnings;
use Storable qw(nstore retrieve);

my %config = (
    name => 'server1',
    port => 8080,
    debug => 0,
);

nstore \%config, 'config.stor' or die "Cannot store: $!";
my $loaded = retrieve('config.stor') or die "Cannot retrieve: $!";
print "Name: $loaded->{name}\n";
```

## Related Errors

- [Reference error](/languages/perl/reference-error)
- [Runtime error](/languages/perl/perl-runtime-error)
- [File not found](/languages/perl/perl-file-not-found)
