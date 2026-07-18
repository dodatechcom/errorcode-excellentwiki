---
title: "[Solution] Poetry Project Scaffolding Failed Error — How to Fix"
description: "Fix Poetry new and init command failures when creating project scaffolding. Resolve directory creation errors and template generation issues in Poetry."
tools: ["poetry"]
error-types: ["new-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means `poetry new` or `poetry init` failed to create the project structure. The command could not create directories, write files, or the target path already exists without the `--force` flag.

## Why It Happens

- The target directory already exists and `--force` was not specified
- Permission issues prevent creating the directory or files
- The project name contains characters that are invalid for directory or Python package names
- `poetry init` is run in a directory that already contains a `pyproject.toml`
- The current working directory is read-only
- Disk space is full and files cannot be written

## Common Error Messages

```
RuntimeError

Directory "my-project" already exists.
```

```
PermissionError

[Errno 13] Permission denied: '/home/user/my-project/pyproject.toml'
```

```
ValueError

Project name "my project" is not valid.
Use only letters, numbers, hyphens, and underscores.
```

```
FileExistsError

[Errno 17] File exists: '/home/user/my-project/pyproject.toml'
```

## How to Fix It

### 1. Use `--force` to Overwrite

```bash
poetry new my-project --force
```

This removes the existing directory and recreates it.

### 2. Check Permissions

```bash
ls -la $(dirname $(pwd))
whoami
```

If you do not have write permission:

```bash
# Create in a writable location
mkdir -p ~/projects
poetry new ~/projects/my-project
```

### 3. Use a Valid Project Name

```bash
# Valid names
poetry new my-project
poetry new my_project
poetry new MyProject123

# Invalid names (avoid spaces and special characters)
poetry new "my project"    # use hyphens instead
poetry new "my/project"    # use hyphens instead
```

### 4. Use `poetry init` in an Existing Directory

```bash
mkdir my-project
cd my-project
poetry init --name my-project
```

`poetry init` creates `pyproject.toml` in the current directory without creating subdirectories.

### 5. Force Reinitialize an Existing Project

```bash
cd existing-project
poetry init --name my-project --force
```

### 6. Create in a Temp Directory First

```bash
poetry new /tmp/my-project
cp -r /tmp/my-project/* ~/projects/my-project/
```

### 7. Set Custom Python Version During Creation

```bash
poetry new my-project --python ^3.11
```

## Common Scenarios

**Permission denied on shared systems.** Create the project in your home directory:

```bash
poetry new ~/projects/my-project
```

**Re-initializing an existing project.** If the project already has a `pyproject.toml`, use `--force`:

```bash
poetry init --force --name existing-project
```

**Creating a project with a custom structure.** Use `--src` for src layout:

```bash
poetry new my-project --src
```

This creates a `src/my_project/` layout instead of the flat layout.

## Prevent It

1. Always verify the target directory does not exist before running `poetry new` to avoid unexpected overwrites
2. Use lowercase names with hyphens (`my-project`) to ensure compatibility across operating systems
3. Create projects in a dedicated `~/projects/` directory to keep permissions and organization simple
