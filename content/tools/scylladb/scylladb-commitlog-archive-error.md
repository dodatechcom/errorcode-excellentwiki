---
title: "[Solution] ScyllaDB Commitlog Archive Error — How to Fix"
description: "Fix ScyllaDB commitlog archive errors when archived commitlog segments cannot be replayed or archived"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Commitlog Archive Error

Commitlog archive errors occur when ScyllaDB cannot archive or replay commitlog segments, affecting point-in-time recovery capabilities.

## Why It Happens

- Archive directory does not exist or has wrong permissions
- Commitlog_archive_command is not configured in scylla.yaml
- Archived segment is corrupted during copy
- Archive disk is full
- Replay from archive fails due to version mismatch

## Common Error Messages

```
commitlog: unable to archive segment: permission denied
```

```
CommitlogArchiver: archive command failed with exit code 1
```

```
error: cannot replay archived segment, version mismatch
```

## How to Fix It

### 1. Configure Commitlog Archive

```yaml
# In scylla.yaml
commitlog_archiving:
  enabled: true
  archive_command: "cp %from %to"
  restore_command: "cp %from %to"
  archive_compress: false
```

### 2. Create Archive Directory

```bash
sudo mkdir -p /var/lib/scylla/commitlog_archive
sudo chown scylla:scylla /var/lib/scylla/commitlog_archive
```

### 3. Check Archive Disk Space

```bash
df -h /var/lib/scylla/commitlog_archive
```

### 4. Test Archive Command

```bash
# Test the archive command manually
cp /var/lib/scylla/commitlog/CommitLog-1234-00000001.log /var/lib/scylla/commitlog_archive/
```

## Examples

```
$ ls /var/lib/scylla/commitlog_archive/
CommitLog-1234-00000001.log
CommitLog-1234-00000002.log
```

## Prevent It

- Ensure archive disk has sufficient space
- Monitor archive command execution status
- Test archive and restore procedures regularly

## Related Pages

- [ScyllaDB Commitlog Error](/tools/scylladb/scylladb-commitlog-error)
- [ScyllaDB Commitlog Corruption Error](/tools/scylladb/scylladb-commitlog-corruption-error)
- [ScyllaDB Backup Error](/tools/scylladb/scylladb-backup-error)
