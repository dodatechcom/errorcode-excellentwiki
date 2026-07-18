---
title: "[Solution] Cargo Git Error — Fix Failed to Fetch Git Repository"
description: "Fix cargo git dependency fetch failures when Cargo cannot clone or access git repositories. Troubleshoot SSH keys, authentication, and network issues."
tools: ["cargo"]
error-types: ["git-error"]
severities: ["error"]
weight: 5
---

This error means Cargo could not clone or fetch a git repository specified as a dependency in your Cargo.toml. The build fails before any compilation begins.

## What This Error Means

Cargo dependencies can point to git repositories. When Cargo tries to clone or update these:

```
error: failed to fetch into /home/user/.cargo/git/db/my-repo-xxx

Caused by:
  unable to connect to github.com: ssh: connect to host github.com port 22: Connection timed out
```

Or:

```
error: failed to resolve patches for `https://github.com/user/repo`

Caused by:
  failed to load source for dependency `my-dep`
```

## Why It Happens

- The git repository does not exist or the URL is incorrect
- SSH keys are not configured for private repository access
- The repository requires authentication but no credentials are available
- The repository URL changed or was moved
- Your network blocks git protocol or specific hosts (GitHub, GitLab)
- The git reference (branch, tag, commit) no longer exists

## How to Fix It

### Test Git Access

```bash
git clone https://github.com/user/repo.git /tmp/test-clone
```

For SSH:

```bash
ssh -T git@github.com
```

### Use HTTPS Instead of SSH

```toml
# Cargo.toml
[dependencies]
my-dep = { git = "https://github.com/user/repo" }
```

### Configure SSH Keys for Private Repos

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
cat ~/.ssh/id_ed25519.pub
# Add to GitHub/GitLab deploy keys
```

### Use a Git Token for Authentication

```bash
git config --global credential.helper store
# Then clone once to cache the token
```

Or set an environment variable:

```bash
export CARGO_NET_GIT_FETCH_WITH_CLI=true
```

### Clear the Git DB Cache

```bash
rm -rf ~/.cargo/git/db
rm -rf ~/.cargo/git/checkouts
cargo update
```

### Pin to a Specific Commit

```toml
[dependencies]
my-dep = { git = "https://github.com/user/repo", rev = "abc123def" }
```

## Common Mistakes

- Using SSH URLs without configuring SSH keys for the remote host
- Not using `cargo update` after the remote repository changes branches
- Assuming git dependencies are always available without checking access
- Forgetting to add deploy keys for CI/CD pipeline access to private repos

## Related Pages

- [Cargo Network Error]({{< relref "/tools/cargo/cargo-network-error" >}}) -- network issues
- [Cargo Dependency Error]({{< relref "/tools/cargo/cargo-dependency-error" >}}) -- dependency issues
- [Cargo Lock Error]({{< relref "/tools/cargo/cargo-lock-error" >}}) -- lock file problems
