---
title: "[Solution] Vagrant Snapshot Error"
description: "Fix Vagrant snapshot errors when saving, restoring, or deleting VM snapshots fails."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant Snapshot Error

Vagrant snapshot operations fail during save, restore, or delete.

```
Failed to create snapshot
```

## Common Causes

- VM not stopped for snapshot
- VirtualBox snapshot limit exceeded
- Disk space insufficient
- Snapshot name already exists
- Corrupted snapshot chain

## How to Fix

### List Snapshots

```bash
vagrant snapshot list
```

### Save Snapshot

```bash
vagrant snapshot save before-update

# Save with name
vagrant snapshot save "backup-$(date +%Y%m%d)"
```

### Restore Snapshot

```bash
vagrant snapshot restore before-update

# Force restore
vagrant snapshot restore --force before-update
```

### Delete Snapshot

```bash
vagrant snapshot delete old-backup

# Delete all snapshots
vagrant snapshot list | xargs -I {} vagrant snapshot delete {}
```

### Fix Snapshot Chain

```bash
# Compact disk after snapshot deletion
VBoxManage modifymedium disk .vagrant/machines/default/virtualbox/disk.vdi --compact
```

## Examples

```bash
# Snapshot workflow
vagrant snapshot save "pre-deploy"
vagrant provision
vagrant snapshot restore "pre-deploy"  # Rollback
```

```ruby
# In Vagrantfile
config.trigger.after :up do
  run "vagrant snapshot save auto-snapshot"
end
```
