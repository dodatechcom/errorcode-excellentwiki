---
title: "[Solution] Linux Could Not Get Lock /var/lib/dpkg — apt Fix v2"
description: "Fix Linux 'Could not get lock /var/lib/dpkg' errors. Remove stale apt locks, kill hung processes, and resolve package manager contention."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["apt", "dpkg", "lock", "frontend-lock", "package-manager", "apt-get"]
weight: 5
---

# Linux: Could not get lock /var/lib/dpkg

The `E: Could not get lock /var/lib/dpkg/lock` error means the Debian/Ubuntu package manager is already in use by another process. The lock file prevents simultaneous package operations that could corrupt the database. This commonly happens during unattended upgrades, when another terminal runs `apt`, or after a crash left stale lock files.

## What This Error Means

dpkg uses lock files (`/var/lib/dpkg/lock`, `/var/lib/dpkg/lock-frontend`, `/var/lib/apt/lists/lock`) to serialize package operations. When any apt/dpkg command runs, it acquires these locks. If another process already holds a lock, your command will fail with this error. The lock files are in `/var/lib/dpkg/` and `/var/lib/apt/`.

## Common Causes

- Another `apt` or `dpkg` process is already running
- A background unattended-upgrades process is active
- Previous package operation was interrupted (lock file left behind)
- A graphical package manager (Software Center) is running
- Lock file left stale after a crash or forced shutdown

## How to Fix

### 1. Check if Another apt/dpkg Process Is Running

```bash
# Check for running apt or dpkg processes
ps aux | grep -E 'apt|dpkg'

# More detailed view
sudo lsof /var/lib/dpkg/lock*
sudo lsof /var/lib/apt/lists/lock
sudo lsof /var/cache/apt/archives/lock
```

If you see an active process, wait for it to finish. If it's hung, kill it:

```bash
# Kill the hung process
sudo kill -9 <PID>
```

### 2. Remove Stale Lock Files

If no apt process is running but the lock files remain:

```bash
# Remove lock files
sudo rm /var/lib/dpkg/lock
sudo rm /var/lib/dpkg/lock-frontend
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock

# Reconfigure dpkg
sudo dpkg --configure -a
```

### 3. Wait for Unattended Upgrades

```bash
# Check if unattended-upgrades is running
ps aux | grep unattended

# Wait for it to finish, or temporarily disable it
sudo systemctl stop unattended-upgrades

# Disable it
sudo systemctl disable unattended-upgrades
```

### 4. Fix Interrupted Package Operations

```bash
# Fix broken packages from interrupted operations
sudo dpkg --configure -a

# Fix broken dependencies
sudo apt --fix-broken install

# Clean up
sudo apt clean
sudo apt update
```

### 5. Kill Graphical Package Manager

If a GUI package manager is holding the lock:

```bash
# Find and kill it
sudo killall gnome-software
sudo killall synaptic
sudo killall software-center
```

### 6. Use apt with Options to Avoid Waiting

```bash
# Wait for the lock with a timeout
sudo apt -o DPkg::Lock::Timeout=30 update

# Force acquire the lock (dangerous — only if you're sure nothing is running)
sudo apt -o DPkg::Lock::Timeout=-1 update
```

### 7. Prevent Future Lock Conflicts

```bash
# Schedule unattended-upgrades during off-hours
sudo nano /etc/apt/apt.conf.d/20auto-upgrades
# Set: Unattended-Upgrade::Allowed-Origins { ... };

# Limit unattended-upgrades to specific time window
sudo nano /etc/apt/apt.conf.d/50unattended-upgrades
```

## Examples

```bash
$ sudo apt update
E: Could not get lock /var/lib/apt/lists/lock (11: Resource temporarily unavailable)
E: Unable to lock directory /var/lib/apt/lists/

$ ps aux | grep apt
root  1234  0.5  0.2 /usr/bin/apt-get -qq update

$ sudo kill 1234
$ sudo rm /var/lib/apt/lists/lock
$ sudo apt update
Get:1 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
```

```bash
$ sudo dpkg -i package.deb
E: Unable to acquire the dpkg frontend lock
E: Could not get lock /var/lib/dpkg/lock-frontend - open (11: Resource temporarily unavailable)

$ sudo rm /var/lib/dpkg/lock-frontend
$ sudo dpkg --configure -a
$ sudo dpkg -i package.deb
```

## Related Errors

- [dpkg error]({{< relref "/os/linux/linux-dpkg-error" >}}) — Package processing errors
- [apt update failed]({{< relref "/os/linux/linux-apt-update-error" >}}) — Repository sync failures
- [No space left on device]({{< relref "/os/linux/no-space-left" >}}) — Disk full preventing installs
