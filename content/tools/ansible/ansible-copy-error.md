---
title: "[Solution] Ansible Copy Error — Fix Failed to Copy File / Destination Exists"
description: "Fix Ansible copy errors when transferring files to managed hosts fails. Resolve destination conflicts, permission issues, and directory structure problems."
---

## What This Error Means

Ansible copy errors occur when the `copy` or `template` module cannot write a file to the destination path. The destination may already exist, have wrong permissions, or the parent directory may be missing.

A typical error:

```
fatal: [host1]: FAILED! => {
    "changed": false,
    "msg": "Destination directory /etc/app does not exist"
}
```

Or:

```
fatal: [host1]: FAILED! => {
    "changed": false,
    "msg": "Destination /etc/app/config already exists, refusing to overwrite"
}
```

## Why It Happens

Copy errors happen when:

- **Parent directory does not exist**: The destination directory has not been created.
- **File already exists**: The copy module refuses to overwrite when used with incorrect settings.
- **Permission denied**: The remote user lacks write permission on the destination.
- **SELinux context mismatch**: SELinux prevents writing files with incorrect security context.
- **Disk is full**: No space left on the target device.
- **Source file does not exist**: The local source file specified in the playbook is missing.
- **Read-only filesystem**: The target partition is mounted as read-only.

## How to Fix It

**Step 1: Create the destination directory**

```yaml
- name: Ensure destination directory exists
  file:
    path: /etc/app
    state: directory
    mode: '0755'

- name: Copy configuration file
  copy:
    src: config.conf
    dest: /etc/app/config.conf
```

**Step 2: Force overwrite existing files**

```yaml
- name: Copy with force overwrite
  copy:
    src: config.conf
    dest: /etc/app/config.conf
    force: true
```

**Step 3: Set correct permissions**

```yaml
- name: Copy with ownership
  copy:
    src: config.conf
    dest: /etc/app/config.conf
    owner: root
    group: root
    mode: '0644'
```

**Step 4: Use backup to preserve existing files**

```yaml
- name: Copy with backup
  copy:
    src: config.conf
    dest: /etc/app/config.conf
    backup: yes
```

**Step 5: Set SELinux context**

```yaml
- name: Copy with SELinux context
  copy:
    src: config.conf
    dest: /etc/app/config.conf
    seuser: system_u
    serole: object_r
    setype: etc_t
```

## Common Mistakes

- **Not creating the destination directory first**: The copy module does not create parent directories.
- **Forgetting `force: yes` for idempotent overwrites**: Without force, existing files are not replaced.
- **Using relative source paths without understanding the base directory**: Source is relative to the playbook directory.
- **Not checking disk space before large file transfers**: Use the `df` module or pre-checks.

## Related Pages

- [Ansible Permission Denied](/tools/ansible/ansible-permission-denied/) -- Permission issues
- [Ansible Task Failed](/tools/ansible/ansible-task-failed/) -- Task execution failures
- [Ansible Template Error](/tools/ansible/ansible-template-error/) -- Template issues
