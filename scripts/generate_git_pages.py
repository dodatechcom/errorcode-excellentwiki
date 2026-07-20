#!/usr/bin/env python3
"""Generate new Git error pages"""
import os

EXISTING = {f.replace('.md', '') for f in os.listdir('/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/git/') if f.endswith('.md')}

PAGES = [
    {
        "slug": "fatal-not-a-repository",
        "title": "Git fatal: Not a git repository",
        "desc": "Fix 'fatal: not a git repository' error. Resolve cases where Git commands fail because the current directory is not a Git repository.",
        "body": """fatal: Not a git repository (or any of the parent directories): .git

This error occurs when you run a Git command in a directory that is not part of a Git repository. Git cannot find a `.git` directory in the current path or any parent directory.

## Common Causes

- Running Git commands outside a repository
- The `.git` directory was deleted or corrupted
- Working in a subdirectory that was not initialized
- The repository was cloned but you changed directories
- Wrong working directory in terminal

## How to Fix

### Initialize a New Repository

```bash
git init
```

### Clone an Existing Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### Check for .git Directory

```bash
ls -la .git
```

If missing, the repository metadata has been lost.

### Navigate to Repository Root

```bash
git rev-parse --show-toplevel
cd $(git rev-parse --show-toplevel)
```

## Examples

```bash
# Example 1: Running git log outside a repo
cd /tmp
git log
# fatal: not a git repository (or any of the parent directories): .git
# Fix: cd into your repository first

# Example 2: Deleted .git directory
rm -rf .git
git status
# fatal: not a git repository (or any of the parent directories): .git
# Fix: git init (loses history) or git clone fresh copy

# Example 3: Initialize a new project
mkdir myproject && cd myproject
git init
# Initialized empty Git repository in /path/to/myproject/.git/
```"""
    },
    {
        "slug": "fatal-refusing-merge-unrelated-histories",
        "title": "Git fatal: Refusing to merge unrelated histories",
        "desc": "Fix 'refusing to merge unrelated histories' error. Resolve Git merge failures when branches have no common commit ancestor.",
        "body": """fatal: refusing to merge unrelated histories

This error occurs when you attempt to merge two branches or repositories that do not share a common commit ancestor. Git refuses the merge to prevent creating a broken history.

## Common Causes

- Merging two independent repositories
- Adding a new repository as a remote with no common history
- Rebasing a branch onto an unrelated branch
- Force-pushed a rewritten history that diverged completely

## How to Fix

### Allow Unrelated Histories (Merge)

```bash
git merge --allow-unrelated-histories <branch>
```

### Allow Unrelated Histories (Pull)

```bash
git pull origin <branch> --allow-unrelated-histories
```

### Fetch and Check History First

```bash
git fetch origin
git log --oneline --graph HEAD..origin/main | head -5
```

## Examples

```bash
# Example 1: Merge unrelated repository
git remote add upstream https://github.com/user/repo.git
git fetch upstream
git merge upstream/main
# fatal: refusing to merge unrelated histories
# Fix: git merge --allow-unrelated-histories upstream/main

# Example 2: Pull into fresh init
git init
git remote add origin https://github.com/user/repo.git
git pull origin main
# fatal: refusing to merge unrelated histories
# Fix: git pull origin main --allow-unrelated-histories

# Example 3: After force push rewrite
git pull origin main
# fatal: refusing to merge unrelated histories
# Fix: git fetch origin && git reset --hard origin/main
```"""
    },
    {
        "slug": "fatal-remote-origin-already-exists",
        "title": "Git fatal: Remote origin already exists",
        "desc": "Fix 'remote origin already exists' error. Resolve Git remote configuration conflicts when adding a remote that is already defined.",
        "body": """fatal: remote origin already exists.

This error occurs when you try to add a remote named `origin` that already exists in your repository configuration. Git enforces unique remote names.

## Common Causes

- `origin` remote is already configured
- Trying to change the remote URL without updating
- Cloned a repository (origin is set automatically)
- Multiple attempts to add the same remote

## How to Fix

### Update the Existing Remote URL

```bash
git remote set-url origin <new-url>
```

### Remove and Re-add the Remote

```bash
git remote remove origin
git remote add origin <url>
```

### View Current Remote Configuration

```bash
git remote -v
```

### Rename Remote Instead

```bash
git remote rename origin upstream
git remote add origin <new-url>
```

## Examples

```bash
# Example 1: Change remote URL
git remote add origin https://github.com/user/new-repo.git
# fatal: remote origin already exists.
# Fix: git remote set-url origin https://github.com/user/new-repo.git

# Example 2: Wrong remote URL, need to fix
git remote set-url origin https://github.com/user/correct-repo.git

# Example 3: Rename and add new
git remote rename origin upstream
git remote add origin https://github.com/user/repo.git
```"""
    },
    {
        "slug": "fatal-no-upstream-branch",
        "title": "Git fatal: No upstream branch configured",
        "desc": "Fix 'no upstream branch configured' error. Resolve Git push failures when the current branch has no remote tracking branch set.",
        "body": """fatal: The current branch <branch> has no upstream branch.

This error occurs when you try to push a branch that has no remote tracking branch configured. Git does not know where to push your changes.

## Common Causes

- Created a new local branch without pushing
- Removed the remote tracking branch
- Cloned without checking out a branch
- Switched to a branch without a remote counterpart

## How to Fix

### Push with Upstream

```bash
git push -u origin <branch>
```

### Set Upstream for Current Branch

```bash
git branch --set-upstream-to=origin/<branch> <branch>
```

### Push to Current Branch Automatically

```bash
git config --global push.default current
```

## Examples

```bash
# Example 1: New local branch
git checkout -b feature/new-api
git push
# fatal: The current branch feature/new-api has no upstream branch.
# Fix: git push -u origin feature/new-api

# Example 2: Set upstream after the fact
git branch --set-upstream-to=origin/feature/new-api feature/new-api

# Example 3: Configure automatic upstream
git push -u origin main
# Next time: git push (works without arguments)
```"""
    },
    {
        "slug": "fatal-could-not-read-from-remote",
        "title": "Git fatal: Could not read from remote repository",
        "desc": "Fix 'could not read from remote repository' error. Resolve Git remote connection failures and authentication issues.",
        "body": """fatal: Could not read from remote repository.

This error occurs when Git cannot connect to or read data from a remote repository. The issue is typically related to network connectivity, authentication, or repository access permissions.

## Common Causes

- Repository URL is incorrect
- No network connection or proxy issues
- SSH key is missing or not configured
- Insufficient permissions to access the repository
- Repository has been moved or deleted

## How to Fix

### Verify Remote URL

```bash
git remote -v
```

### Test Connection

```bash
ssh -T git@github.com
```

### Update Remote URL

```bash
git remote set-url origin <correct-url>
```

### Use HTTPS Instead of SSH

```bash
git remote set-url origin https://github.com/user/repo.git
```

### Check Network Connectivity

```bash
ping github.com
curl -I https://github.com
```

## Examples

```bash
# Example 1: Wrong remote URL
git remote -v
# origin  https://github.com/wrong/repo.git
# Fix: git remote set-url origin https://github.com/correct/repo.git

# Example 2: SSH key not added to ssh-agent
ssh-add -l
# The agent has no identities.
# Fix: ssh-add ~/.ssh/id_rsa

# Example 3: Repository access denied
git pull origin main
# fatal: Could not read from remote repository.
# Fix: verify you have access or use https://user:token@github.com/user/repo.git
```"""
    },
    {
        "slug": "fatal-src-refspec-master-does-not-match",
        "title": "Git fatal: src refspec master does not match any",
        "desc": "Fix 'src refspec master does not match any' error. Resolve Git push failures when the source branch does not exist locally.",
        "body": """error: src refspec master does not match any

This error occurs when you try to push a branch that does not exist in your local repository. Git cannot find the commit or branch you specified as the source.

## Common Causes

- The branch name is misspelled (master vs main)
- No commits have been made yet in the repository
- The branch was deleted locally but still exists remotely
- Wrong branch name specified in the push command

## How to Fix

### Check Existing Branches

```bash
git branch -a
```

### Create an Initial Commit

```bash
git add .
git commit -m "Initial commit"
```

### Use Correct Branch Name

```bash
# Check default branch name
git symbolic-ref HEAD
# Push with correct name
git push origin main
```

### Rename Branch

```bash
git branch -m master main
git push origin main
```

## Examples

```bash
# Example 1: No commits yet
git init
git push origin master
# error: src refspec master does not match any
# Fix: git add . && git commit -m "Initial commit" && git push origin master

# Example 2: Wrong branch name (main vs master)
git push origin master
# error: src refspec master does not match any
# Fix: git push origin main

# Example 3: Branch was deleted
git branch -D feature/x
git push origin feature/x
# error: src refspec feature/x does not match any
# Fix: recreate branch or delete remote reference
```"""
    },
    {
        "slug": "fatal-authentication-failed",
        "title": "Git fatal: Authentication failed",
        "desc": "Fix 'Authentication failed' error. Resolve Git credential issues when pushing, pulling, or cloning from remote repositories.",
        "body": """fatal: Authentication failed for 'https://github.com/user/repo.git'

This error occurs when Git cannot authenticate your identity with the remote server. This typically happens with incorrect credentials, expired tokens, or SSH key issues.

## Common Causes

- Incorrect username or password
- Expired or revoked personal access token
- Two-factor authentication enabled without a token
- SSH key not added to your GitHub/GitLab account
- Credential helper has stale or wrong credentials

## How to Fix

### Use a Personal Access Token

```bash
git remote set-url origin https://<token>@github.com/user/repo.git
```

### Update Credential Helper

```bash
git credential reject
git credential approve
```

### Switch to SSH Authentication

```bash
git remote set-url origin git@github.com:user/repo.git
```

### Clear Cached Credentials

```bash
git config --global --unset credential.helper
git config --global credential.helper cache
```

## Examples

```bash
# Example 1: Token expired
git push origin main
# fatal: Authentication failed for 'https://github.com/user/repo.git'
# Fix: generate new token at GitHub Settings > Developer settings > Personal access tokens

# Example 2: Switch to SSH
git remote set-url origin git@github.com:user/repo.git
git push origin main

# Example 3: macOS Keychain reset
git credential-osxkeychain erase
```"""
    },
    {
        "slug": "fatal-pathspec-did-not-match",
        "title": "Git fatal: Pathspec did not match any files",
        "desc": "Fix 'pathspec did not match any files' error. Resolve Git command failures when a specified file path does not exist in the repository.",
        "body": """fatal: pathspec '<file>' did not match any files

This error occurs when you reference a file path in a Git command that does not exist in the working tree or index. Git cannot find the specified path in the current repository state.

## Common Causes

- Typo in the file name or path
- File was deleted or never committed
- File exists but in a different directory
- File is untracked and not staged
- Case sensitivity mismatch on Linux

## How to Fix

### List Files in Directory

```bash
ls -la
git ls-files
```

### Check if File is Tracked

```bash
git ls-files <file>
```

### Use Tab Completion

```bash
git add <tab><tab>
```

### Check for Whitespace or Special Characters

```bash
git status --short
```

## Examples

```bash
# Example 1: Typo in filename
git add src/myflie.js
# fatal: pathspec 'src/myflie.js' did not match any files
# Fix: git add src/myfile.js

# Example 2: File not committed yet
git checkout -- index.html
# fatal: pathspec 'index.html' did not match any files
# Fix: git add index.html first, or verify the file exists

# Example 3: Case sensitivity (Linux vs macOS)
git add Src/App.js
# fatal: pathspec 'Src/App.js' did not match any files
# Fix: git add src/App.js
```"""
    },
    {
        "slug": "fatal-permission-denied-publickey",
        "title": "Git fatal: Permission denied (publickey)",
        "desc": "Fix 'Permission denied (publickey)' error. Resolve Git SSH authentication failures when connecting to remote repositories.",
        "body": """Permission denied (publickey).

This error occurs when Git's SSH connection attempt fails because no valid SSH key is provided or the key is not authorized on the remote server.

## Common Causes

- SSH key is not generated on your machine
- Public key is not added to GitHub/GitLab/Bitbucket
- Wrong SSH key is being used
- ssh-agent is not running or has no keys loaded
- Wrong remote URL format (using HTTPS instead of SSH)

## How to Fix

### Generate an SSH Key

```bash
ssh-keygen -t ed25519 -C "your@email.com"
```

### Add Key to ssh-agent

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### Copy Public Key to Clipboard

```bash
cat ~/.ssh/id_ed25519.pub
```

Add this key to your GitHub account under Settings > SSH and GPG keys.

### Test Connection

```bash
ssh -T git@github.com
```

## Examples

```bash
# Example 1: No SSH key
git clone git@github.com:user/repo.git
# Permission denied (publickey).
# Fix: ssh-keygen -t ed25519 -C "your@email.com" && cat ~/.ssh/id_ed25519.pub

# Example 2: Key not added to GitHub
ssh -T git@github.com
# Permission denied (publickey).
# Fix: add public key to GitHub account

# Example 3: Wrong key loaded
ssh-add -l
# 256 SHA256:xxx wrong-key@host (ED25519)
# Fix: ssh-add ~/.ssh/id_rsa && ssh -T git@github.com
```"""
    },
    {
        "slug": "fatal-ambiguous-argument",
        "title": "Git fatal: Ambiguous argument",
        "desc": "Fix 'ambiguous argument' error. Resolve Git command failures when a reference name matches both a branch and a file or tag.",
        "body": """fatal: ambiguous argument '<ref>': unknown revision or path not in the working tree.

This error occurs when Git cannot determine whether a given argument refers to a revision (branch/tag/commit) or a file path. The argument matches both.

## Common Causes

- A branch and a file share the same name
- A tag name conflicts with a branch name
- A commit SHA is incomplete or ambiguous
- Special characters in argument not quoted

## How to Fix

### Disambiguate with `--`

```bash
git show <name> --   # treat as revision
git show -- <name>   # treat as path
```

### Use Full Reference Names

```bash
git show refs/heads/<branch>
git show refs/tags/<tag>
```

### Quote Arguments with Special Characters

```bash
git log "HEAD~1"
```

## Examples

```bash
# Example 1: Branch and file named 'test'
git log test
# fatal: ambiguous argument 'test': unknown revision or path not in the working tree.
# Fix: git log test --     (revision)  or  git log -- test     (path)

# Example 2: Tag and branch conflict
git show v1
# fatal: ambiguous argument 'v1'
# Fix: git show refs/tags/v1  or  git show refs/heads/v1

# Example 3: Incomplete SHA
git show abc123
# fatal: ambiguous argument 'abc123'
# Fix: git show abc1234 (use at least 4-7 hex digits that are unique)
```"""
    },
    {
        "slug": "fatal-could-not-find-remote-ref",
        "title": "Git fatal: Could not find remote ref",
        "desc": "Fix 'could not find remote ref' error. Resolve Git fetch and pull failures when a remote branch reference does not exist.",
        "body": """fatal: Could not find remote ref <ref>.

This error occurs when you try to fetch or pull a remote reference (branch or tag) that does not exist on the remote server.

## Common Causes

- The branch was deleted on the remote
- Typo in the branch or tag name
- The branch exists under a different name
- Remote has not been fetched recently
- Tag name is incorrect

## How to Fix

### List Remote Branches

```bash
git ls-remote --heads origin
```

### List Remote Tags

```bash
git ls-remote --tags origin
```

### Fetch All Remote References

```bash
git fetch origin
```

### Verify Branch Name

```bash
git branch -r
```

## Examples

```bash
# Example 1: Deleted remote branch
git fetch origin feature/deleted-branch
# fatal: Could not find remote ref feature/deleted-branch
# Fix: check active branches with git branch -r

# Example 2: Typo in branch name
git pull origin featuer/login
# fatal: Could not find remote ref featuer/login
# Fix: git pull origin feature/login

# Example 3: Tag name mismatch
git fetch origin v1.0
# fatal: Could not find remote ref v1.0
# Fix: git ls-remote --tags origin to list available tags
```"""
    },
    {
        "slug": "error-local-changes-would-be-overwritten",
        "title": "Git error: Your local changes would be overwritten",
        "desc": "Fix 'Your local changes would be overwritten' error. Resolve Git checkout, merge, or pull failures due to unstaged changes.",
        "body": """error: Your local changes to the following files would be overwritten by checkout/merge/pull

This error occurs when Git operations would overwrite files that have uncommitted changes. Git protects your work by refusing to proceed.

## Common Causes

- Uncommitted changes in files that the merge/pull modifies
- Trying to checkout a branch that changes tracked files
- Stashing before switching branches
- Pulling changes that conflict with local modifications

## How to Fix

### Commit Your Changes

```bash
git add .
git commit -m "Save progress"
git pull
```

### Stash Your Changes

```bash
git stash
git pull
git stash pop
```

### Discard Local Changes (careful)

```bash
git checkout -- <file>
```

### Force Checkout (discard all local changes)

```bash
git checkout --force <branch>
```

## Examples

```bash
# Example 1: Pull with local changes
git pull origin main
# error: Your local changes to 'config.js' would be overwritten by merge.
# Fix: git stash && git pull && git stash pop

# Example 2: Switch branches with changes
git checkout feature/login
# error: Your local changes would be overwritten by checkout.
# Fix: git stash && git checkout feature/login

# Example 3: Discard and pull
git checkout -- config.js
git pull origin main
```"""
    },
    {
        "slug": "fatal-not-possible-fast-forward",
        "title": "Git fatal: Not possible to fast-forward",
        "desc": "Fix 'not possible to fast-forward' error. Resolve Git merge failures when a fast-forward merge is required but not possible.",
        "body": """fatal: Not possible to fast-forward, aborting.

This error occurs when you attempt a merge with `--ff-only` flag but the branches have diverged and cannot be merged with a fast-forward.

## Common Causes

- Branches have diverged with different commits
- `git merge --ff-only` is configured as default
- Remote branch has commits not in local branch
- Local branch has commits not in remote branch

## How to Fix

### Allow a Merge Commit

```bash
git merge --no-ff <branch>
```

### Rebase Instead

```bash
git checkout <branch>
git rebase main
git checkout main
git merge <branch>
```

### Pull with Rebase

```bash
git pull --rebase origin main
```

## Examples

```bash
# Example 1: ff-only merge fails
git merge --ff-only feature/branch
# fatal: Not possible to fast-forward, aborting.
# Fix: git merge --no-ff feature/branch

# Example 2: Rebase before merge
git checkout feature/login
git rebase main
git checkout main
git merge feature/login

# Example 3: Pull with rebase to avoid merge commits
git pull --rebase origin main
```"""
    },
    {
        "slug": "fatal-cannot-rebase-unstaged-changes",
        "title": "Git fatal: Cannot rebase with unstaged changes",
        "desc": "Fix 'cannot rebase: You have unstaged changes' error. Resolve Git rebase failures when working directory is not clean.",
        "body": """Cannot rebase: You have unstaged changes.

This error occurs when you try to rebase with uncommitted or unstaged changes in your working directory. Git requires a clean working tree for rebasing.

## Common Causes

- Uncommitted file modifications
- Untracked files present
- Staged but uncommitted changes
- In-progress work not yet saved

## How to Fix

### Commit Your Changes

```bash
git add .
git commit -m "WIP: save progress before rebase"
git rebase <branch>
```

### Stash Your Changes

```bash
git stash
git rebase <branch>
git stash pop
```

### Discard Changes (careful)

```bash
git reset --hard HEAD
git rebase <branch>
```

## Examples

```bash
# Example 1: Stash and rebase
git stash
git rebase main
git stash pop

# Example 2: Commit and rebase
git add -A
git commit -m "Save before rebase"
git rebase main

# Example 3: Interactive rebase with changes
git stash
git rebase -i HEAD~3
git stash pop
```"""
    },
    {
        "slug": "fatal-need-specify-reconcile-divergent",
        "title": "Git fatal: Need to specify how to reconcile divergent branches",
        "desc": "Fix 'need to specify how to reconcile divergent branches' error. Resolve Git pull failures when branches have diverged and pull strategy is not set.",
        "body": """fatal: Need to specify how to reconcile divergent branches.

This error occurs in Git 2.27+ when `pull.rebase` is not configured and you try to pull changes from a divergent branch. Git requires you to choose a merge strategy.

## Common Causes

- Git version 2.27 or newer with default configuration
- Local and remote branches have diverged
- `pull.rebase` or `pull.ff` not configured
- No explicit merge strategy specified

## How to Fix

### Configure Pull to Use Rebase

```bash
git config --global pull.rebase true
```

### Configure Pull to Use Merge

```bash
git config --global pull.rebase false
```

### Configure Fast-Forward Only

```bash
git config --global pull.ff only
```

### Specify Strategy Per Command

```bash
git pull --rebase origin main
git pull --no-rebase origin main
```

## Examples

```bash
# Example 1: Git 2.27+ pull fails
git pull origin main
# fatal: Need to specify how to reconcile divergent branches.
# Fix: git config --global pull.rebase true

# Example 2: Pull with explicit strategy
git pull --rebase origin main

# Example 3: Fast-forward only
git config --global pull.ff only
git pull origin main
```"""
    },
    {
        "slug": "fatal-unable-to-access",
        "title": "Git fatal: Unable to access URL",
        "desc": "Fix 'unable to access' error. Resolve Git HTTP/HTTPS connection failures when accessing remote repositories.",
        "body": """fatal: unable to access 'https://github.com/user/repo.git/'

This error occurs when Git cannot establish an HTTP or HTTPS connection to the remote repository URL. This is a network-level connectivity issue.

## Common Causes

- No internet connection or DNS resolution failure
- Proxy server blocking or requiring configuration
- Firewall blocking outbound connections
- SSL/TLS certificate verification failure
- Repository URL is malformed

## How to Fix

### Check Internet Connectivity

```bash
ping github.com
```

### Configure Git Proxy

```bash
git config --global http.proxy http://proxy:8080
git config --global https.proxy http://proxy:8080
```

### Disable SSL Verification (temporary)

```bash
git config --global http.sslVerify false
```

### Check DNS Resolution

```bash
nslookup github.com
```

### Use Correct URL Format

```bash
git remote set-url origin https://github.com/user/repo.git
```

## Examples

```bash
# Example 1: Proxy required at work
git clone https://github.com/user/repo.git
# fatal: unable to access 'https://github.com/user/repo.git/'
# Fix: git config --global http.proxy http://proxy.company.com:8080

# Example 2: SSL certificate issue
git config --global http.sslVerify false
# Or set correct CA bundle:
git config --global http.sslCAInfo /path/to/cert.pem

# Example 3: DNS resolution issue
echo "140.82.112.4 github.com" >> /etc/hosts
```"""
    },
    {
        "slug": "error-rpc-failed-curl",
        "title": "Git error: RPC failed; curl 56 OpenSSL SSL_read",
        "desc": "Fix 'RPC failed; curl 56 OpenSSL SSL_read' error. Resolve Git push failures caused by SSL connection issues during large transfers.",
        "body": """error: RPC failed; curl 56 OpenSSL SSL_read: SSL_ERROR_SYSCALL, errno 0

This error occurs when Git fails to complete a large push or pull over HTTPS. The SSL/TLS connection drops unexpectedly during data transfer.

## Common Causes

- Large file sizes exceeding default buffer
- Slow or unstable network connection
- Server-side timeout during long transfers
- SSL/TLS negotiation failure
- Proxy or firewall interrupting long connections

## How to Fix

### Increase HTTP Post Buffer

```bash
git config --global http.postBuffer 524288000
```

### Use SSH Instead of HTTPS

```bash
git remote set-url origin git@github.com:user/repo.git
```

### Compress Data

```bash
git config --global core.compression 9
```

### Split Large Commits

```bash
git commit --amend -m "Split large files"
```

## Examples

```bash
# Example 1: Large push fails
git push origin main
# error: RPC failed; curl 56 OpenSSL SSL_read: SSL_ERROR_SYSCALL, errno 0
# Fix: git config --global http.postBuffer 524288000

# Example 2: Switch to SSH to avoid SSL issues
git remote set-url origin git@github.com:user/repo.git
git push origin main

# Example 3: Use Git LFS for large files
git lfs track "*.zip"
git add .gitattributes
git commit -m "Track large files with LFS"
```"""
    },
    {
        "slug": "fatal-remote-end-hung-up",
        "title": "Git fatal: The remote end hung up unexpectedly",
        "desc": "Fix 'The remote end hung up unexpectedly' error. Resolve Git connection drops during push, pull, or clone operations.",
        "body": """fatal: The remote end hung up unexpectedly

This error occurs when the remote server closes the connection before the Git operation completes. The server terminated the connection prematurely.

## Common Causes

- Repository size is too large for the server
- Push exceeds server-side limits
- Network timeout or proxy disconnection
- Server-side git hooks rejecting the push
- Insufficient disk space on the server

## How to Fix

### Increase Git Buffer Size

```bash
git config --global http.postBuffer 524288000
```

### Use Shallow Clone

```bash
git clone --depth 1 <repo-url>
```

### Enable Compression

```bash
git config --global core.compression 9
```

### Push in Chunks

```bash
git push origin <branch> --no-progress
```

## Examples

```bash
# Example 1: Large repository push fails
git push origin main
# fatal: The remote end hung up unexpectedly
# Fix: git config --global http.postBuffer 524288000 && git push

# Example 2: Clone large repo
git clone https://github.com/user/large-repo.git
# fatal: The remote end hung up unexpectedly
# Fix: git clone --depth 1 https://github.com/user/large-repo.git

# Example 3: Check server hooks
git ls-remote origin
# If hooks reject push, contact repository admin
```"""
    },
    {
        "slug": "fatal-unable-to-create-temp-file",
        "title": "Git fatal: Unable to create temporary file",
        "desc": "Fix 'unable to create temporary file' error. Resolve Git failures caused by disk space, permission, or temporary directory issues.",
        "body": """fatal: Unable to create temporary file '/path/to/tmp/': Permission denied

This error occurs when Git cannot create temporary files in the system temp directory. The operation fails due to filesystem limitations.

## Common Causes

- Disk space is exhausted
- Temp directory has wrong permissions
- Temp directory is on a read-only filesystem
- System temp directory is full
- Inode exhaustion on the filesystem

## How to Fix

### Check Disk Space

```bash
df -h
```

### Check Temp Directory Permissions

```bash
ls -la /tmp
ls -la /var/tmp
```

### Set Custom Temp Directory

```bash
git config --global core.tmpdir /path/to/large/tmp
```

### Clean Temp Files

```bash
rm -rf /tmp/*
```

### Point TMPDIR Environment Variable

```bash
export TMPDIR=/path/to/tmp
git clone <repo>
```

## Examples

```bash
# Example 1: Disk full
df -h /
# Filesystem  Size  Used Avail Use% Mounted on
# /dev/sda1   50G   50G     0 100% /
# Fix: free up space or use different disk

# Example 2: Temp directory permissions
sudo chmod 1777 /tmp
git pull origin main

# Example 3: Use alternative temp dir
mkdir ~/mytmp
export TMPDIR=~/mytmp
git push origin main
```"""
    },
    {
        "slug": "fatal-lf-will-be-replaced-by-crlf",
        "title": "Git fatal: LF will be replaced by CRLF",
        "desc": "Fix 'LF will be replaced by CRLF' warning. Resolve Git line ending normalization issues across Windows and Unix systems.",
        "body": """warning: LF will be replaced by CRLF in <file>.

This warning (or error with `--strict`) occurs when Git detects that a file uses Unix-style line endings (LF) but the repository or working directory expects Windows-style (CRLF).

## Common Causes

- Collaborating across Windows and Unix/macOS systems
- `core.autocrlf` set inconsistently across team
- File with mixed line endings committed
- Text file detected as binary or vice versa

## How to Fix

### Configure autocrlf (Windows)

```bash
git config --global core.autocrlf true
```

### Configure autocrlf (Unix/macOS)

```bash
git config --global core.autocrlf input
```

### Normalize Line Endings for Repository

```bash
git add --renormalize .
git commit -m "Normalize line endings"
```

### Use .gitattributes

```properties
*.js text eol=lf
*.bat text eol=crlf
*.png binary
```

## Examples

```bash
# Example 1: Windows developer
git config --global core.autocrlf true
git checkout -- .

# Example 2: Linux/macOS developer
git config --global core.autocrlf input

# Example 3: Using .gitattributes
echo "*.sh text eol=lf" >> .gitattributes
echo "*.ps1 text eol=crlf" >> .gitattributes
git add .gitattributes
git commit -m "Add line ending normalization"
```"""
    },
    {
        "slug": "error-your-branch-is-behind",
        "title": "Git error: Your branch is behind",
        "desc": "Fix 'Your branch is behind' error. Resolve Git push failures when the local branch is outdated compared to the remote branch.",
        "body": """Updates were rejected because the remote contains work that you do not have locally.

This error occurs when your local branch has fallen behind the remote branch. You need to integrate the remote changes before pushing.

## Common Causes

- Someone else pushed to the same branch
- You worked on a different machine
- Branch was force-pushed by another contributor
- You forgot to pull before making changes

## How to Fix

### Pull Remote Changes

```bash
git pull origin <branch>
```

### Pull with Rebase

```bash
git pull --rebase origin <branch>
```

### Check Status

```bash
git status
git log --oneline HEAD..origin/<branch>
```

### Force Push (use with caution)

```bash
git push --force-with-lease origin <branch>
```

## Examples

```bash
# Example 1: Behind remote
git push origin main
# ! [rejected] main -> main (fetch first)
# Fix: git pull origin main && git push origin main

# Example 2: Rebase to keep history clean
git pull --rebase origin main
git push origin main

# Example 3: Check divergence
git log --oneline -5 HEAD..origin/main
# Shows commits you're missing
```"""
    },
    {
        "slug": "fatal-branch-already-exists",
        "title": "Git fatal: A branch named already exists",
        "desc": "Fix 'a branch named already exists' error. Resolve Git branch creation failures when a branch with the name already exists.",
        "body": """fatal: A branch named '<branch>' already exists.

This error occurs when you try to create a branch with a name that already exists in your local repository. Branch names must be unique.

## Common Causes

- Branch already exists locally
- Case-insensitive branch name collision
- Trying to recreate a deleted branch without cleaning up
- Remote-tracking branch has same name

## How to Fix

### List Existing Branches

```bash
git branch -a
```

### Check Out Existing Branch

```bash
git checkout <branch>
```

### Delete Local Branch

```bash
git branch -d <branch>
```

### Use a Different Name

```bash
git checkout -b <branch>-v2
```

## Examples

```bash
# Example 1: Branch exists
git branch feature/login
# fatal: A branch named 'feature/login' already exists.
# Fix: git checkout feature/login

# Example 2: Delete and recreate
git branch -d feature/login
git branch feature/login

# Example 3: Case sensitivity
git branch Feature/Login
# fatal: A branch named 'Feature/Login' already exists.
# (if 'feature/login' was created on a case-insensitive filesystem)
```"""
    },
    {
        "slug": "fatal-cannot-update-paths-checkout",
        "title": "Git fatal: Cannot update paths and switch to branch",
        "desc": "Fix 'Cannot update paths and switch to branch' error. Resolve Git checkout failures when paths and branch switching are mixed.",
        "body": """fatal: Cannot update paths and switch to branch 'branch' at the same time.

This error occurs when you mix file paths with a branch name in `git checkout`. You need to separate path updates from branch switching.

## Common Causes

- Running `git checkout <branch> <file>` when you meant to switch branches
- Confusing `git checkout` syntax between branch switching and file restoration
- Path argument matches a branch name
- Incorrect command structure

## How to Fix

### Switch to Branch Only

```bash
git checkout <branch>
```

### Restore File Only

```bash
git checkout -- <file>
```

### Use Modern Commands

```bash
git switch <branch>        # switch branch
git restore <file>         # restore file
```

### Use Double Dash to Disambiguate

```bash
git checkout <branch> --
```

## Examples

```bash
# Example 1: Mixed arguments
git checkout main src/index.js
# fatal: Cannot update paths and switch to branch 'main' at the same time.
# Fix: git checkout main && git checkout -- src/index.js

# Example 2: Using modern commands
git switch main
git restore src/index.js

# Example 3: File named same as branch
git checkout login
# fatal: Cannot update paths and switch to branch 'login'
# Fix: git checkout login --
```"""
    },
    {
        "slug": "fatal-needed-single-revision",
        "title": "Git fatal: Needed a single revision",
        "desc": "Fix 'Needed a single revision' error. Resolve Git command failures when a commit reference resolves to multiple revisions.",
        "body": """fatal: Needed a single revision

This error occurs when a Git command that expects a single commit revision receives a reference that resolves to multiple commits.

## Common Causes

- Using a branch name when a tag name was expected
- Reference matches multiple objects
- Merged branch has multiple parents
- Ambiguous short SHA reference

## How to Fix

### Use a Specific Commit SHA

```bash
git show <full-commit-sha>
```

### Use Explicit Reference Path

```bash
git show refs/heads/<branch>
git show refs/tags/<tag>
```

### Check What the Reference Resolves To

```bash
git rev-parse <ref>
```

## Examples

```bash
# Example 1: Merge commit has multiple parents
git rev-parse HEAD
git show HEAD^
# fatal: Needed a single revision
# Fix: git show HEAD^1 (first parent) or HEAD^2 (second parent)

# Example 2: Ambiguous reference
git show main
# fatal: Needed a single revision
# Fix: git show refs/heads/main

# Example 3: Short SHA collision
git show abcdef1
# fatal: Needed a single revision
# Fix: provide complete SHA
```"""
    },
    {
        "slug": "fatal-not-valid-object-name",
        "title": "Git fatal: Not a valid object name",
        "desc": "Fix 'Not a valid object name' error. Resolve Git command failures when a commit, tree, or blob reference is invalid.",
        "body": """fatal: Not a valid object name '<ref>'.

This error occurs when you reference a Git object (commit, tree, tag, blob) that does not exist or has an invalid format.

## Common Causes

- Typo in commit SHA or reference name
- Reference to a commit from a different repository
- Object was garbage collected
- Corrupted repository objects
- Missing `-` in reference names

## How to Fix

### Verify Object Exists

```bash
git cat-file -t <ref>
```

### List Recent Commits

```bash
git log --oneline -5
```

### Check Reflog for Lost Commits

```bash
git reflog
```

### Verify Tag Names

```bash
git tag -l
```

## Examples

```bash
# Example 1: Typo in commit hash
git show 1a2b3c4
# fatal: Not a valid object name '1a2b3c4'
# Fix: use correct hash git show 1a2b3c4d5e

# Example 2: Reference to deleted commit
git show HEAD@{5}
# fatal: Not a valid object name
# Fix: check reflog for valid references

# Example 3: Wrong tag
git show v1.0.0
# fatal: Not a valid object name 'v1.0.0'
# Fix: git tag -l to list valid tags
```"""
    },
    {
        "slug": "fatal-bad-object",
        "title": "Git fatal: bad object",
        "desc": "Fix 'bad object' error. Resolve Git repository corruption issues where objects are damaged or missing.",
        "body": """fatal: bad object HEAD

This error indicates that a Git object (commit, tree, or blob) in your repository is corrupted or unreadable. The repository integrity is compromised.

## Common Causes

- Hardware failure or disk write errors
- Repository interrupted during a write operation
- Improperly shut down Git operations
- File system corruption
- Manual editing of files in .git directory

## How to Fix

### Run Git Fsck to Diagnose

```bash
git fsck --full
```

### Restore from Reflog

```bash
git reflog
git reset --hard HEAD@{n}
```

### Clone a Fresh Copy

```bash
cd ..
rm -rf corrupted-repo
git clone <url>
```

### Recover from Remote

```bash
git fetch origin
git reset --hard origin/main
```

## Examples

```bash
# Example 1: Corrupted object
git fsck --full
# error: object xxx is a blob, not a commit
# Fix: clone a fresh copy

# Example 2: Bad HEAD
git status
# fatal: bad object HEAD
# Fix: git reflog && git reset --hard HEAD@{n}

# Example 3: After disk failure
cd /tmp
git clone https://github.com/user/repo.git
cp -a repo/.git /path/to/repo/
```"""
    },
    {
        "slug": "fatal-loose-object-corrupt",
        "title": "Git fatal: loose object is corrupt",
        "desc": "Fix 'loose object is corrupt' error. Resolve Git repository object corruption causing data integrity failures.",
        "body": """fatal: loose object <hash> is corrupt

This error occurs when Git encounters a loose object file that is damaged, truncated, or has a checksum mismatch. The object cannot be read.

## Common Causes

- Disk write cache failure during commit
- File system errors
- Manual modification of .git/objects files
- Incomplete copy or backup restoration
- Storage hardware issues

## How to Fix

### Remove the Corrupt Object

```bash
rm -f .git/objects/<xx>/<hash>
```

### Restore from Remote

```bash
git fetch origin
git reset --hard origin/main
```

### Run Git Fsck

```bash
git fsck --full
```

### Clone Fresh Copy

```bash
cd ..
rm -rf repo
git clone <url>
```

## Examples

```bash
# Example 1: Single corrupt object
git fsck --full
# corrupt loose object
# Fix: rm .git/objects/ab/cdef123... && git fetch origin

# Example 2: Multiple corrupt objects
git fsck --full
# Fix: cd .. && rm -rf repo && git clone <url> repo

# Example 3: Restore from backup
cp -a backup/.git/objects/* .git/objects/
git fsck --full
```"""
    },
    {
        "slug": "fatal-out-of-memory",
        "title": "Git fatal: Out of memory",
        "desc": "Fix Git 'out of memory' error. Resolve memory exhaustion failures when processing large repositories or files.",
        "body": """fatal: Out of memory? mmap failed: Cannot allocate memory

This error occurs when Git runs out of available memory while processing large files, big repositories, or complex operations like diffing or packing.

## Common Causes

- Very large files in the repository
- Large number of commits or objects
- System memory limits or swap disabled
- Processing large diffs with many changes
- Running multiple memory-intensive operations

## How to Fix

### Increase Swap Space

```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Use Shallow Clone

```bash
git clone --depth 1 <repo-url>
```

### Limit Git Memory Usage

```bash
git config --global core.deltaBaseCacheLimit 2g
git config --global pack.threads 1
```

### Use Sparse Checkout

```bash
git clone --filter=blob:none <repo>
git sparse-checkout set <path>
```

## Examples

```bash
# Example 1: Large repo clone
git clone https://github.com/user/large-repo.git
# fatal: Out of memory? mmap failed
# Fix: git clone --depth 1 https://github.com/user/large-repo.git

# Example 2: Increase swap
sudo fallocate -l 4G /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile

# Example 3: Sparse checkout
git clone --filter=blob:none https://github.com/user/repo.git
cd repo
git sparse-checkout set src/
```"""
    },
    {
        "slug": "fatal-unable-to-find",
        "title": "Git fatal: Unable to find",
        "desc": "Fix 'Unable to find' error. Resolve Git failures when a required file, commit, or object cannot be located in the repository.",
        "body": """fatal: Unable to find '<path>'.

This error occurs when Git cannot locate a required file or reference in the repository. The specified item may be missing, deleted, or was never committed.

## Common Causes

- Referencing a file that was deleted
- Commit hash does not exist in repository
- Branch reference points to a non-existent commit
- File exists in working tree but not in index
- Repository is in a detached HEAD state without the expected history

## How to Fix

### Search Repository History

```bash
git log --all --full-history -- <file>
```

### Check if File is Tracked

```bash
git ls-files <file>
```

### Find Commit by Message

```bash
git log --all --oneline --grep="<keyword>"
```

### Restore Deleted File

```bash
git checkout <commit-hash>^ -- <file>
```

## Examples

```bash
# Example 1: File not tracked
git show HEAD:src/config.js
# fatal: Unable to find 'src/config.js'
# Fix: add and commit the file first

# Example 2: Deleted file
git log --all --full-history -- src/config.js
# Shows commits where file existed
# Fix: git checkout <hash>^ -- src/config.js

# Example 3: Non-existent commit
git checkout 1a2b3c4
# fatal: Unable to find '1a2b3c4'
# Fix: use git log to find valid commit hashes
```"""
    },
    {
        "slug": "fatal-bad-revision",
        "title": "Git fatal: bad revision",
        "desc": "Fix 'bad revision' error. Resolve Git command failures when a revision specifier is invalid or does not exist.",
        "body": """fatal: bad revision '<ref>'

This error occurs when you provide a revision parameter that Git cannot parse or resolve to a valid commit in the repository.

## Common Causes

- Typo in commit hash, branch name, or tag name
- Using a reference from a different repository
- The commit was garbage collected
- Merged branch no longer exists as a reference
- Invalid revision syntax like `HEAD^^^` with too many carets

## How to Fix

### Check Available Revisions

```bash
git log --oneline -10
```

### Verify Branch and Tag Names

```bash
git branch -a
git tag -l
```

### Use Reflog for Lost References

```bash
git reflog show HEAD
```

### Use Full Commit Hash

```bash
git log --oneline
git show <full-hash>
```

## Examples

```bash
# Example 1: Typo in revision
git log HEAD~~~  # too many carets
# fatal: bad revision 'HEAD~~~'
# Fix: git log HEAD~3

# Example 2: Deleted branch
git show feature/deleted
# fatal: bad revision 'feature/deleted'
# Fix: git reflog | grep feature

# Example 3: Wrong tag name
git diff v1.0 v2.0
# fatal: bad revision 'v2.0'
# Fix: git tag -l to see available tags
```"""
    },
    {
        "slug": "error-untracked-overwritten",
        "title": "Git error: Untracked working tree file would be overwritten",
        "desc": "Fix 'Untracked working tree file would be overwritten' error. Resolve Git checkout and merge failures from untracked file conflicts.",
        "body": """error: Untracked working tree file '<file>' would be overwritten by merge/checkout.

This error occurs when an untracked file in your working directory has the same path as a file that a Git operation (checkout or merge) needs to create.

## Common Causes

- Untracked file exists at the same path as a tracked file in the target branch
- Generated or build artifacts not in .gitignore
- Temporary files left in the working tree
- IDE or editor files not properly ignored

## How to Fix

### Remove the Untracked File

```bash
rm <file>
```

### Move the File to a Safe Location

```bash
mv <file> <file>.bak
```

### Check What Will Be Overwritten

```bash
git checkout --overlay <branch>
```

### Stash Untracked Files

```bash
git stash --include-untracked
git checkout <branch>
```

## Examples

```bash
# Example 1: Untracked file blocking checkout
git checkout feature/login
# error: Untracked working tree file 'config.js' would be overwritten
# Fix: mv config.js config.js.bak && git checkout feature/login

# Example 2: Merge with untracked files
git merge feature/login
# error: Untracked working tree file 'dist/bundle.js' would be overwritten
# Fix: rm dist/bundle.js && git merge feature/login

# Example 3: Stash untracked files
git stash --include-untracked
git pull origin main
git stash pop
```"""
    },
    {
        "slug": "fatal-origin-not-appear-repository",
        "title": "Git fatal: origin does not appear to be a git repository",
        "desc": "Fix 'origin does not appear to be a git repository' error. Resolve Git remote configuration issues when the remote is missing or invalid.",
        "body": """fatal: '<remote>' does not appear to be a git repository

This error occurs when you try to use a remote name that is not configured or a URL that does not point to a valid Git repository.

## Common Causes

- Remote name was never added or was removed
- Typo in the remote name
- Remote URL is incorrect or the repository was moved/deleted
- Wrong case sensitivity in remote name
- Repository was initialized without a remote

## How to Fix

### View Configured Remotes

```bash
git remote -v
```

### Add the Remote

```bash
git remote add origin <repository-url>
```

### Correct the Remote URL

```bash
git remote set-url origin <correct-url>
```

### Remove and Re-add

```bash
git remote remove origin
git remote add origin <url>
```

## Examples

```bash
# Example 1: No remote configured
git remote -v
# (empty)
# Fix: git remote add origin https://github.com/user/repo.git

# Example 2: Typo in remote name
git push orign main
# fatal: 'orign' does not appear to be a git repository
# Fix: git push origin main

# Example 3: Wrong URL
git remote set-url origin https://github.com/user/wrong-repo.git
git push origin main
# fatal: 'origin' does not appear to be a git repository
# Fix: git remote set-url origin https://github.com/user/correct-repo.git
```"""
    },
    {
        "slug": "fatal-unable-to-look-up",
        "title": "Git fatal: unable to look up",
        "desc": "Fix 'unable to look up' error. Resolve Git DNS resolution failures when connecting to remote repositories.",
        "body": """fatal: unable to look up '<hostname>' (port 9418) (Name or service not known)

This error occurs when Git cannot resolve the hostname of your remote repository server to an IP address. DNS resolution has failed.

## Common Causes

- No network connection or DNS server unreachable
- Hostname is incorrect
- DNS cache is stale or corrupted
- VPN not connected (for internal repositories)
- Network interface is down

## How to Fix

### Test DNS Resolution

```bash
nslookup github.com
dig github.com
```

### Check Network Connectivity

```bash
ping -c 4 8.8.8.8
```

### Use IP Address Instead

```bash
git remote set-url origin http://<ip-address>/user/repo.git
```

### Flush DNS Cache

```bash
# Linux
sudo systemctl restart systemd-resolved
# macOS
sudo dscacheutil -flushcache && sudo killall -HUP mDNSResponder
# Windows
ipconfig /flushdns
```

### Add to Hosts File

```bash
echo "<ip-address> github.com" >> /etc/hosts
```

## Examples

```bash
# Example 1: DNS resolution failure
git clone https://github.com/user/repo.git
# fatal: unable to look up github.com (port 443) (Name or service not known)
# Fix: check internet connection or use VPN

# Example 2: Corporate network DNS
nslookup github.com
# ** server can't find github.com: NXDOMAIN
# Fix: connect to VPN or use DNS server that resolves external domains

# Example 3: Add to hosts file as workaround
ping github.com  # get IP
echo "140.82.112.4 github.com" | sudo tee -a /etc/hosts
```"""
    },
    {
        "slug": "fatal-unable-to-connect",
        "title": "Git fatal: unable to connect",
        "desc": "Fix 'unable to connect' error. Resolve Git network connection failures to remote repository servers.",
        "body": """fatal: unable to connect to <hostname>

This error occurs when Git cannot establish a TCP connection to the remote server. The server may be down, blocked by a firewall, or unreachable from your network.

## Common Causes

- Remote server is down or unreachable
- Firewall blocking outbound connections
- VPN not connected (for private repositories)
- SSH port (22) or HTTPS port (443) blocked
- Corporate proxy configuration missing

## How to Fix

### Check Connectivity with curl

```bash
curl -I https://github.com
```

### Test SSH Connection

```bash
ssh -T git@github.com
```

### Configure Proxy

```bash
git config --global http.proxy http://proxy:8080
git config --global https.proxy https://proxy:8080
```

### Check Firewall Rules

```bash
sudo iptables -L -n
```

### Use Different Protocol

```bash
# Switch from SSH to HTTPS
git remote set-url origin https://github.com/user/repo.git
```

## Examples

```bash
# Example 1: Server unreachable
git fetch origin
# fatal: unable to connect to github.com
# Fix: check internet connection or try later

# Example 2: SSH port blocked
git clone git@github.com:user/repo.git
# fatal: unable to connect to github.com:22
# Fix: git clone https://github.com/user/repo.git (use HTTPS)

# Example 3: Proxy configuration
git config --global http.proxy http://proxy.company.com:8080
git config --global https.proxy http://proxy.company.com:8080
```"""
    },
    {
        "slug": "error-insufficient-permission-object",
        "title": "Git error: insufficient permission for adding an object",
        "desc": "Fix 'insufficient permission for adding an object' error. Resolve Git permission issues when writing to the repository database.",
        "body": """error: insufficient permission for adding an object to repository database

This error occurs when Git does not have write permissions to the `.git/objects` directory or its subdirectories. The object database cannot be modified.

## Common Causes

- Repository owned by a different user
- Wrong file permissions on .git directory
- sudo used for git init but not for subsequent commands
- Shared repository with multiple users
- NFS or network filesystem permission issues

## How to Fix

### Fix Ownership

```bash
sudo chown -R $USER:$USER .git
```

### Fix Permissions

```bash
chmod -R u+w .git
```

### For Shared Repositories

```bash
git init --shared=group
chmod -R g+ws .git
```

### Run Git as Correct User

```bash
whoami
# Verify you own the repository
ls -la .git/objects
```

## Examples

```bash
# Example 1: Repository owned by root
sudo chown -R $(whoami):$(whoami) .git
git add . && git commit -m "Fix permissions"

# Example 2: Group-shared repository
sudo chgrp -R developers .git
chmod -R g+ws .git
git config core.sharedRepository group

# Example 3: Fix read-only .git
ls -la .git/objects
# drwx------  # too restrictive
chmod -R u+w .git
```"""
    },
    {
        "slug": "fatal-unable-to-create-file",
        "title": "Git fatal: Unable to create file",
        "desc": "Fix 'Unable to create file' error. Resolve Git checkout, merge, and pull failures from filesystem permission or space issues.",
        "body": """fatal: Unable to create file '<path>': Permission denied

This error occurs when Git cannot write a file to the working directory during checkout, merge, or pull operations.

## Common Causes

- File permissions prevent writing
- Disk is full or inode exhausted
- File is locked by another process
- Directory does not exist
- File path is too long for the filesystem

## How to Fix

### Check Disk Space

```bash
df -h .
```

### Check File Permissions

```bash
ls -la <directory>
chmod u+w <directory>
```

### Close Programs Locking the File

```bash
lsof <file>
# Kill the process holding the lock
kill <PID>
```

### Check Inode Usage

```bash
df -i .
```

## Examples

```bash
# Example 1: Permission denied
git checkout feature/branch
# fatal: Unable to create file 'src/config.js': Permission denied
# Fix: chmod u+w src/config.js && git checkout feature/branch

# Example 2: Disk full
df -h .
# Filesystem  Size  Used Avail Use% Mounted on
# /dev/sda1   50G   50G     0 100% /
# Fix: free up disk space

# Example 3: File locked by process
lsof src/config.js
# COMMAND  PID  USER   FD   TYPE DEVICE
# vim     1234 user   4r   REG   ...
# Fix: kill -9 1234 && git checkout src/config.js
```"""
    },
    {
        "slug": "fatal-protocol-error",
        "title": "Git fatal: protocol error",
        "desc": "Fix 'protocol error' error. Resolve Git protocol-level communication failures during network operations.",
        "body": """fatal: protocol error: bad line length <length>

This error occurs when Git receives unexpected or malformed data during communication with a remote server. The protocol handshake or data transfer is corrupted.

## Common Causes

- Proxy or firewall modifying the data stream
- Corrupted network packets
- Incompatible Git versions between client and server
- Server-side hook output interfering with protocol
- SSH session issues

## How to Fix

### Upgrade Git

```bash
git --version
# Install latest Git version
```

### Use HTTPS Instead of Git Protocol

```bash
git remote set-url origin https://github.com/user/repo.git
```

### Disable Compression

```bash
git config --global core.compression 0
```

### Use Shallow Clone

```bash
git clone --depth 1 <url>
```

## Examples

```bash
# Example 1: Protocol error during clone
git clone git://github.com/user/repo.git
# fatal: protocol error: bad line length 65536
# Fix: git clone https://github.com/user/repo.git

# Example 2: SSH protocol error
git clone git@github.com:user/repo.git
# fatal: protocol error
# Fix: upgrade Git or use HTTPS

# Example 3: Proxy modifying stream
git config --global http.proxy ""
git clone https://github.com/user/repo.git
```"""
    },
    {
        "slug": "fatal-early-eof",
        "title": "Git fatal: early EOF",
        "desc": "Fix 'early EOF' error. Resolve Git clone, fetch, or push failures when the connection is terminated before transfer completes.",
        "body": """fatal: early EOF

This error occurs when Git detects end-of-file before the expected data transfer completes. The network connection was terminated prematurely.

## Common Causes

- Unstable network connection
- Repository is too large for available bandwidth
- Server-side timeout
- Proxy or firewall interrupting long transfers
- Insufficient memory on client or server

## How to Fix

### Use Shallow Clone

```bash
git clone --depth 1 <url>
```

### Increase Buffer Size

```bash
git config --global http.postBuffer 524288000
git config --global http.lowSpeedLimit 0
git config --global http.lowSpeedTime 999999
```

### Enable Keep-Alive

```bash
git config --global http.keepAlive 120
```

### Use SSH Instead of HTTPS

```bash
git remote set-url origin git@github.com:user/repo.git
```

## Examples

```bash
# Example 1: Large repository clone
git clone https://github.com/user/large-repo.git
# fatal: early EOF
# Fix: git clone --depth 1 https://github.com/user/large-repo.git

# Example 2: Unstable connection
git config --global http.postBuffer 524288000
git config --global http.lowSpeedTime 300
git fetch origin

# Example 3: Use SSH for large transfers
git remote set-url origin git@github.com:user/repo.git
git fetch origin
```"""
    },
    {
        "slug": "fatal-index-pack-failed",
        "title": "Git fatal: index-pack failed",
        "desc": "Fix 'index-pack failed' error. Resolve Git clone, fetch, or push failures during the pack file indexing process.",
        "body": """fatal: index-pack failed

This error occurs when Git fails to process a pack file during clone, fetch, or push. The pack file could not be indexed or verified.

## Common Causes

- Insufficient memory or disk space
- Network corruption during download
- Pack file exceeds server limits
- Git version incompatibility
- Corrupted pack file on server

## How to Fix

### Increase Memory Limit

```bash
git config --global pack.windowMemory 1g
git config --global pack.packSizeLimit 1g
```

### Use Shallow Clone

```bash
git clone --depth 1 <url>
```

### Disable Pack Bitmaps

```bash
git config --global pack.useBitmaps false
```

### Clone Without Checkout

```bash
git clone --no-checkout <url>
cd <repo>
git checkout HEAD
```

## Examples

```bash
# Example 1: Clone fails with index-pack
git clone https://github.com/user/large-repo.git
# fatal: index-pack failed
# Fix: git clone --depth 1 https://github.com/user/large-repo.git

# Example 2: Memory limit
git config --global pack.windowMemory 2g
git fetch origin

# Example 3: Without pack bitmaps
git config --global pack.useBitmaps false
git fetch origin
```"""
    },
    {
        "slug": "fatal-unable-to-stat",
        "title": "Git fatal: Unable to stat file",
        "desc": "Fix 'Unable to stat' error. Resolve Git failures when it cannot read file attributes from the filesystem.",
        "body": """fatal: Unable to stat '<path>': No such file or directory

This error occurs when Git tries to read file metadata but the file does not exist or the path is invalid.

## Common Causes

- File was deleted after being staged
- Symlink target does not exist
- File path contains special characters
- Network filesystem disconnected
- File moved while Git was processing

## How to Fix

### Reset the File in Index

```bash
git reset HEAD <file>
```

### Remove and Re-add

```bash
git rm --cached <file>
git add <file>
```

### Check File Existence

```bash
ls -la <file>
```

### Clean Working Tree

```bash
git clean -fd
git checkout -- .
```

## Examples

```bash
# Example 1: Deleted staged file
rm src/temp.js
git status
# Changes not staged for delete: src/temp.js
# Fix: git checkout -- src/temp.js or git rm src/temp.js

# Example 2: Broken symlink
ls -la link-to-config
# lrwxrwxrwx  link-to-config -> /nonexistent/path
# Fix: remove symlink git rm link-to-config

# Example 3: Reset and re-add
git reset HEAD src/generated.js
rm src/generated.js
```"""
    },
    {
        "slug": "fatal-cannot-create-directory",
        "title": "Git fatal: cannot create directory",
        "desc": "Fix 'cannot create directory' error. Resolve Git checkout failures when it cannot create required directories in the working tree.",
        "body": """fatal: cannot create directory at '<path>': Permission denied

This error occurs when Git needs to create a directory during checkout, but the filesystem does not allow it or the parent directory has insufficient permissions.

## Common Causes

- Parent directory has incorrect permissions
- Disk is full or read-only
- File system is mounted as read-only
- There is a file with the same name as the required directory
- Path contains characters not supported by the filesystem

## How to Fix

### Check Parent Directory Permissions

```bash
ls -la <parent-directory>
chmod u+w <parent-directory>
```

### Check Disk Space

```bash
df -h .
```

### Remove Conflicting File

```bash
rm <path>
git checkout <branch>
```

### Remount Filesystem for Write

```bash
sudo mount -o remount,rw <mount-point>
```

## Examples

```bash
# Example 1: Read-only parent directory
ls -la /path/to/parent
# dr-xr-xr-x   # missing write permission
# Fix: chmod u+w /path/to/parent
git checkout feature/branch

# Example 2: File blocking directory creation
rm src/utils
git checkout main

# Example 3: Remount filesystem
sudo mount -o remount,rw /mnt/data
git pull origin main
```"""
    },
    {
        "slug": "fatal-index-file-corrupt",
        "title": "Git fatal: index file corrupt",
        "desc": "Fix 'index file corrupt' error. Resolve Git index corruption issues that prevent repository operations.",
        "body": """fatal: index file corrupt

This error occurs when Git's index file (`.git/index`) is corrupted. The index tracks staged changes and working tree state.

## Common Causes

- Improper shutdown during a Git operation
- Disk write error while updating the index
- Manual editing or deletion of `.git/index`
- File system corruption
- Running out of disk space during index update

## How to Fix

### Remove and Rebuild Index

```bash
rm -f .git/index
git reset HEAD
```

### Restore Index from Backup

```bash
# Git stores index backup
git fsck
```

### Reset to Last Commit

```bash
git reset HEAD -- .
```

### Check for Other Corrupt Files

```bash
git fsck --full
```

## Examples

```bash
# Example 1: Corrupted index
git status
# fatal: index file corrupt
# Fix: rm -f .git/index && git reset HEAD

# Example 2: Rebuild from scratch
rm -f .git/index
git add -A
git commit -m "Rebuild index"

# Example 3: After disk full recovery
df -h .
# Free up space
rm -f .git/index
git reset HEAD
```"""
    },
    {
        "slug": "fatal-cannot-lock-ref",
        "title": "Git fatal: cannot lock ref",
        "desc": "Fix 'cannot lock ref' error. Resolve Git reference update failures when the lock file for a reference already exists.",
        "body": """fatal: cannot lock ref '<ref>': is at <hash> but expected <hash>

This error occurs when Git cannot lock a reference (branch or tag) because another process is holding the lock, or the reference state does not match expectations.

## Common Causes

- Another Git process is running in the same repository
- Previous Git operation was interrupted
- Reference state mismatch between local and expected
- Race condition in concurrent Git operations
- Stale lock files in .git directory

## How to Fix

### Remove Stale Lock Files

```bash
rm -f .git/refs/heads/<branch>.lock
rm -f .git/refs/tags/<tag>.lock
rm -f .git/HEAD.lock
rm -f .git/index.lock
```

### Check for Running Git Processes

```bash
ps aux | grep git
kill <pid>
```

### Fetch and Reset

```bash
git fetch origin
git reset --hard origin/<branch>
```

## Examples

```bash
# Example 1: Stale lock file
rm -f .git/refs/heads/main.lock
git push origin main

# Example 2: Remove all lock files
find .git -name "*.lock" -delete
git status

# Example 3: Index lock
rm -f .git/index.lock
git add .
```"""
    },
    {
        "slug": "fatal-bad-config-line",
        "title": "Git fatal: bad config line",
        "desc": "Fix 'bad config line' error. Resolve Git configuration file parsing errors caused by malformed config entries.",
        "body": """fatal: bad config line <number> in file <path>

This error occurs when Git encounters a syntax error while parsing a configuration file. The config file is malformed or contains invalid entries.

## Common Causes

- Manual editing of .git/config or ~/.gitconfig
- Copy-paste introduced invisible characters
- Encoding issues in config file
- Missing or extra quotes in configuration values
- Corrupted config file

## How to Fix

### Locate the Config File

```bash
git config --list --show-origin
```

### Open Config File for Editing

```bash
git config --global --edit
# or
vim ~/.gitconfig
```

### Fix Specific Line

```bash
git config --global --unset <key>
```

### Remove and Recreate

```bash
mv ~/.gitconfig ~/.gitconfig.bak
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

## Examples

```bash
# Example 1: Missing quote in config
git status
# fatal: bad config line 5 in file /home/user/.gitconfig
# Fix: git config --global --edit (fix the line)

# Example 2: Invalid key
git config --global --unset user.emal
# Instead of 'email' -> 'emal' typo

# Example 3: Backup and recreate
mv ~/.gitconfig ~/.gitconfig.bak
git config --global user.name "John Doe"
git config --global user.email "john@example.com"
```"""
    },
    {
        "slug": "fatal-unknown-option",
        "title": "Git fatal: unknown option",
        "desc": "Fix 'unknown option' error. Resolve Git command failures when an invalid or misspelled command-line option is provided.",
        "body": """fatal: unknown option `<option>`

This error occurs when you provide a command-line option to Git that does not exist or is not valid for the specific Git subcommand.

## Common Causes

- Typo in the option name
- Using a single dash `-` instead of double dash `--`
- Option does not exist for the specific subcommand
- Using an alias that includes invalid arguments
- Outdated Git version missing the option

## How to Fix

### Check Available Options

```bash
git <command> --help
```

### Use Correct Dash Style

```bash
# Wrong: git commit -message "test"
# Correct: git commit -m "test"

# Wrong: git log -oneline
# Correct: git log --oneline
```

### Check Git Version

```bash
git --version
```

### Use Full Option Names

```bash
# Instead of short option
git diff --cached
# Instead of git diff -c
```

## Examples

```bash
# Example 1: Typo in option
git commit --mesage "test"
# fatal: unknown option `mesage'
# Fix: git commit --message "test"

# Example 2: Wrong dash
git log -oneline
# fatal: unknown option `oneline'
# Fix: git log --oneline

# Example 3: Option not valid for subcommand
git status --all
# fatal: unknown option `all'
# Fix: git status (or git log --all)
```"""
    },
    {
        "slug": "fatal-could-not-resolve-head",
        "title": "Git fatal: Could not resolve HEAD",
        "desc": "Fix 'Could not resolve HEAD' error. Resolve Git failures when the HEAD reference is missing or points to a non-existent commit.",
        "body": """fatal: Could not resolve HEAD to a commit

This error occurs when Git cannot determine the commit that HEAD points to. This typically happens in a repository with no commits.

## Common Causes

- Repository has no commits yet (fresh `git init`)
- HEAD reference was deleted or corrupted
- Repository was partially initialized
- ORIG_HEAD or other special refs are missing
- Bare repository without an initial commit

## How to Fix

### Create Initial Commit

```bash
git add .
git commit -m "Initial commit"
```

### Check HEAD Content

```bash
cat .git/HEAD
```

### Create an Orphan Branch

```bash
git checkout --orphan main
git add .
git commit -m "Initial commit"
```

### Reinitialize Repository

```bash
rm -rf .git
git init
git add .
git commit -m "Initial commit"
```

## Examples

```bash
# Example 1: Fresh repository
git log
# fatal: Could not resolve HEAD to a commit
# Fix: git add . && git commit -m "Initial commit"

# Example 2: Corrupted HEAD
cat .git/HEAD
# ref: refs/heads/nonexistent
# Fix: echo "ref: refs/heads/main" > .git/HEAD && git commit --allow-empty -m "Init"

# Example 3: Reinitialize
rm -rf .git
git init
git add -A
git commit -m "Initial commit"
```"""
    },
    {
        "slug": "fatal-no-annotated-tags",
        "title": "Git fatal: No annotated tags",
        "desc": "Fix 'No annotated tags' error. Resolve Git describe failures when no annotated tags exist in the repository.",
        "body": """fatal: No annotated tags can describe '<commit>'.

This error occurs when `git describe` cannot find an annotated tag that can be used to describe the current commit.

## Common Causes

- No annotated tags in the repository
- Tags exist but are lightweight (not annotated)
- Current commit is ahead of all existing tags
- Tags were created without the `-a` flag

## How to Fix

### Create an Annotated Tag

```bash
git tag -a v1.0.0 -m "Version 1.0.0"
```

### Use Lightweight Tags with Describe

```bash
git describe --tags
```

### Use --always Flag

```bash
git describe --always
```

### List Existing Tags

```bash
git tag -l
```

## Examples

```bash
# Example 1: No annotated tags
git describe
# fatal: No annotated tags can describe 'abc1234'.
# Fix: git tag -a v1.0.0 -m "Initial release" && git describe

# Example 2: Use --tags flag
git describe --tags
# v1.0.0-5-gabc1234

# Example 3: Use commit hash fallback
git describe --always
# abc1234
```"""
    },
    {
        "slug": "git-lfs-file-not-found",
        "title": "Git LFS: File not found in LFS store",
        "desc": "Fix Git LFS 'file not found' error. Resolve missing LFS objects when pulling or cloning repositories using Git Large File Storage.",
        "body": """Error downloading object: <file> (xx bytes): Smudge error: Error downloading <file> (<hash>): Object not found

This error occurs when Git LFS cannot find a file in the remote LFS storage. The LFS object is missing from the server.

## Common Causes

- LFS object was deleted from the storage server
- LFS storage migration without updating pointers
- Permissions to access the LFS storage are insufficient
- Branch contains LFS objects not pushed to the server
- LFS storage quota exceeded

## How to Fix

### Fetch LFS Objects Manually

```bash
git lfs fetch --all
```

### Check LFS Status

```bash
git lfs status
```

### Pull LFS Objects

```bash
git lfs pull
```

### Point to New LFS Storage

```bash
git config lfs.url <new-lfs-url>
```

## Examples

```bash
# Example 1: Missing LFS object
git lfs pull
# Error downloading object: design.psd (15 MB)
# Fix: git lfs fetch --all origin main

# Example 2: LFS storage migrated
git config lfs.url https://github.com/user/repo.git/info/lfs
git lfs fetch --all

# Example 3: Verify LFS tracked files
git lfs ls-files --all
# Check which files are tracked
```"""
    },
    {
        "slug": "git-lfs-invalid-pointer",
        "title": "Git LFS: Invalid pointer file",
        "desc": "Fix Git LFS 'invalid pointer' error. Resolve LFS pointer file issues when the pointer does not match the expected format.",
        "body": """Error: Invalid Git LFS pointer: <file>

This error occurs when Git LFS encounters a pointer file that does not match the expected LFS pointer format. The file contains LFS metadata but is malformed.

## Common Causes

- Pointer file was manually edited
- File was corrupted during transfer
- LFS tracked pattern was changed after files were committed
- Mixed content: both LFS pointer and actual file content
- Migration from other VCS with different pointer format

## How to Fix

### Recreate the Pointer

```bash
git lfs track <pattern>
git add --renormalize <file>
```

### Check Pointer Content

```bash
git show HEAD:<file> | head -5
```

### Migrate Pointers

```bash
git lfs migrate import --include="<pattern>" --everything
```

### Re-clone the Repository

```bash
cd ..
rm -rf repo
git clone <url>
cd repo
git lfs pull
```

## Examples

```bash
# Example 1: Manual edit broke pointer
git lfs track "*.psd"
git add file.psd
# Error: Invalid Git LFS pointer
# Fix: git add --renormalize file.psd

# Example 2: Migrate pointers
git lfs migrate import --include="*.zip" --everything
git push origin --force

# Example 3: Re-clone to get correct pointers
cd .. && rm -rf repo
git clone <url>
```"""
    },
    {
        "slug": "git-lfs-smudge-error",
        "title": "Git LFS: Smudge error",
        "desc": "Fix Git LFS 'smudge' error. Resolve failures when Git LFS converts LFS pointers to actual file content during checkout.",
        "body": """Smudge error: Error downloading <file>: Server error: 404 Not Found

This error occurs when Git LFS fails to download the actual file content during the smudge filter process (converting pointer to actual file on checkout).

## Common Causes

- Network connectivity issues
- LFS object missing from server
- Authentication failure for LFS storage
- LFS storage URL changed
- File was deleted from LFS storage

## How to Fix

### Skip Smudge During Checkout

```bash
GIT_LFS_SKIP_SMUDGE=1 git checkout <branch>
git lfs pull
```

### Disable LFS Temporarily

```bash
git config filter.lfs.smudge "git lfs smudge --skip"
git checkout <branch>
git config filter.lfs.smudge "git lfs smudge -- %f"
```

### Re-authenticate with LFS

```bash
git lfs login
```

### Check LFS Server URL

```bash
git config lfs.url
```

## Examples

```bash
# Example 1: Skip smudge
GIT_LFS_SKIP_SMUDGE=1 git checkout feature/branch
git lfs pull

# Example 2: Re-authenticate
git lfs login
git lfs pull

# Example 3: Check LFS configuration
git lfs env
# Verify URL and access token
```"""
    },
    {
        "slug": "fatal-cannot-update-ref",
        "title": "Git fatal: cannot update ref",
        "desc": "Fix 'cannot update ref' error. Resolve Git failures when updating branch or tag references due to conflicts or locks.",
        "body": """fatal: cannot update ref '<ref>': trying to write non-commit <hash>

This error occurs when Git tries to update a reference to point to a non-commit object. References like branches should always point to commits.

## Common Causes

- Trying to push a tag that points to a non-commit
- Corrupted reference file
- Manual modification of reference files
- Attempting to point a branch to a tree or blob
- Fast-forward check failure

## How to Fix

### Check Reference Target

```bash
git cat-file -t <ref>
```

### Force Update Reference

```bash
git update-ref -f <ref> <hash>
```

### Delete and Recreate Reference

```bash
git branch -d <branch>
git checkout -b <branch> <hash>
```

### Check Repository Integrity

```bash
git fsck --full
```

## Examples

```bash
# Example 1: Tag pointing to wrong object
git update-ref refs/tags/v1.0 <commit-hash>

# Example 2: Force update branch
git update-ref -f refs/heads/main <commit-hash>

# Example 3: Delete and recreate
git branch -D feature/x
git checkout -b feature/x <correct-commit>
```"""
    },
    {
        "slug": "fatal-multiple-updates-ref",
        "title": "Git fatal: multiple updates for ref",
        "desc": "Fix 'multiple updates for ref' error. Resolve Git push failures when the same reference is updated more than once in a single push.",
        "body": """fatal: multiple updates for ref '<ref>' not allowed.

This error occurs when you try to push multiple updates to the same reference (branch or tag) in a single push command. Git does not allow updating the same ref more than once.

## Common Causes

- Duplicate branch names in git push command
- Pushing both a branch and a tag with the same name
- Script or automation generating duplicate ref specs
- Using both full and short ref names
- `--mirror` push with conflicting refs

## How to Fix

### Remove Duplicate Refspecs

```bash
git push origin main
# Instead of: git push origin main main
```

### Push Separately

```bash
git push origin main
git push origin v1.0
```

### Use Specific Refspecs

```bash
git push origin refs/heads/main:refs/heads/main
```

### Avoid Mirror Pushes

```bash
git push origin main --no-mirror
```

## Examples

```bash
# Example 1: Duplicate in command
git push origin main main
# fatal: multiple updates for ref 'refs/heads/main' not allowed.
# Fix: git push origin main

# Example 2: Branch and tag with same name
git push origin main v1.0
# OK if they are different
# Duplicate if same: git push origin main v1.0

# Example 3: Script issue
# Fix: check push script for duplicate entries
```"""
    },
    {
        "slug": "fatal-expected-string",
        "title": "Git fatal: Expected string",
        "desc": "Fix 'Expected string' error. Resolve Git rebase, merge, or config parsing failures when an unexpected value type is encountered.",
        "body": """fatal: Expected string value for '<key>'

This error occurs when Git expects a string value for a configuration key but receives a non-string value, or when a command receives an unexpected argument type.

## Common Causes

- Configuration file has a numeric value where string is required
- Boolean value used instead of string in config
- Empty value provided for a required parameter
- Incorrect YAML or INI syntax in Git config
- Malformed environment variable

## How to Fix

### Check and Fix Config Value

```bash
git config --global --unset <key>
git config --global <key> "<correct-string-value>"
```

### Edit Config File Directly

```bash
git config --global --edit
```

### Remove Invalid Config

```bash
git config --global --unset <key>
```

## Examples

```bash
# Example 1: Numeric instead of string
git config --global user.name 123
# fatal: Expected string value for 'user.name'
# Fix: git config --global user.name "John Doe"

# Example 2: Empty value
git config --global user.email ""
# Fix: git config --global user.email "john@example.com"

# Example 3: Edit config file
git config --global --edit
# Fix the offending line manually
```"""
    },
    {
        "slug": "git-submodule-add-failed",
        "title": "Git submodule add failed",
        "desc": "Fix 'git submodule add failed' error. Resolve issues when adding a submodule to a Git repository.",
        "body": """fatal: '<path>' already exists in the index

This error occurs when you try to add a Git submodule at a path that is already tracked in the repository.

## Common Causes

- Path already contains tracked files
- Submodule URL is invalid or unreachable
- Path already exists in .gitmodules
- Nested submodule conflicts
- URL is a local path that doesn't exist

## How to Fix

### Remove Existing File at Path

```bash
git rm -r <path>
git submodule add <url> <path>
```

### Update Existing Submodule

```bash
git submodule update --init --recursive
```

### Check .gitmodules

```bash
cat .gitmodules
```

### Fix Submodule URL

```bash
git submodule set-url <path> <new-url>
```

## Examples

```bash
# Example 1: Path already exists
git rm -r lib/utils
git submodule add https://github.com/user/utils.git lib/utils

# Example 2: Invalid URL
git submodule add https://github.com/user/nonexistent.git lib/mylib
# fatal: repository 'https://github.com/user/nonexistent.git' does not exist
# Fix: check the URL and try again

# Example 3: Remove and re-add submodule
git submodule deinit -f lib/mylib
rm -rf .git/modules/lib/mylib
git submodule add https://github.com/user/mylib.git lib/mylib
```"""
    },
    {
        "slug": "git-submodule-update-failed",
        "title": "Git submodule update failed",
        "desc": "Fix 'git submodule update failed' error. Resolve issues when updating Git submodules to their committed versions.",
        "body": """fatal: Needed a single revision
Unable to find current origin/main revision in submodule path '<path>'

This error occurs when `git submodule update` cannot find the expected commit in the submodule's remote repository.

## Common Causes

- Submodule commit not pushed to remote
- Remote URL for submodule has changed
- Submodule commit was force-pushed or rewritten
- Network issues accessing submodule repository
- Submodule path is not properly initialized

## How to Fix

### Initialize Submodules

```bash
git submodule init
git submodule update
```

### Update with Remote

```bash
git submodule update --remote
```

### Synchronize Submodule URLs

```bash
git submodule sync
git submodule update --init --recursive
```

### Manually Check Out Submodule

```bash
cd <submodule-path>
git fetch origin
git checkout <commit-hash>
```

## Examples

```bash
# Example 1: Init and update
git submodule init
git submodule update --recursive

# Example 2: Sync URLs after remote change
git submodule sync --recursive
git submodule update --init --recursive

# Example 3: Manual checkout
cd lib/mysubmodule
git fetch origin
git checkout main
git pull
cd ../..
git add lib/mysubmodule
```"""
    },
    {
        "slug": "git-stash-pop-conflict",
        "title": "Git stash pop conflict",
        "desc": "Fix Git stash pop conflict error. Resolve merge conflicts when applying stashed changes back to the working directory.",
        "body": """CONFLICT (content): Merge conflict in <file>
Auto-merging <file> failed

This error occurs when you run `git stash pop` and your stashed changes conflict with the current state of the working directory.

## Common Causes

- Working directory changed since the stash was created
- Different branch than where stash was created
- Same file modified before and after the stash
- Stash was created long ago and codebase diverged
- Stash applied after pulling remote changes

## How to Fix

### Resolve Conflicts Manually

```bash
git status
# Edit conflicted files
git add <resolved-file>
git stash drop
```

### Skip Conflict Resolution (Drop Stash)

```bash
git stash drop
```

### Apply Stash as a Branch

```bash
git stash branch <new-branch>
```

### Use Stash Apply (Keep Stash)

```bash
git stash apply
# Resolve conflicts, don't drop stash
```

## Examples

```bash
# Example 1: Resolve conflicts
git stash pop
# CONFLICT (content): Merge conflict in src/main.js
# Fix: edit src/main.js, remove markers, git add src/main.js, git stash drop

# Example 2: Create branch from stash
git stash branch fix-conflicts
# Creates branch, applies stash, drops stash

# Example 3: Apply without dropping
git stash apply
# Resolve conflicts
git stash drop  # only when resolved
```"""
    },
    {
        "slug": "git-merge-abort-error",
        "title": "Git merge abort error",
        "desc": "Fix 'git merge --abort' error when aborting a failed merge operation in Git.",
        "body": """fatal: There is no merge to abort (MERGE_HEAD missing).

This error occurs when you run `git merge --abort` but there is no in-progress merge to abort.

## Common Causes

- No merge was started
- Merge already completed or was already aborted
- MERGE_HEAD file was manually deleted
- Conflict was resolved and committed already
- Wrong repository

## How to Fix

### Check Merge Status

```bash
git status
```

### Check for MERGE_HEAD

```bash
ls -la .git/MERGE_HEAD
```

### Reset to Pre-Merge State

```bash
git reset --hard ORIG_HEAD
```

### Verify Repository State

```bash
git log --oneline -1
```

## Examples

```bash
# Example 1: No merge in progress
git merge --abort
# fatal: There is no merge to abort (MERGE_HEAD missing).
# Fix: check git status first

# Example 2: Reset to ORIG_HEAD
git reset --hard ORIG_HEAD

# Example 3: Merge was already committed
# Check latest commit is the merge
git log --oneline -3
```"""
    },
    {
        "slug": "git-rebase-conflict",
        "title": "Git rebase conflict error",
        "desc": "Fix Git rebase conflict error. Resolve merge conflicts that occur during a rebase operation.",
        "body": """CONFLICT (content): Merge conflict in <file>
error: could not apply <hash> <commit-message>

This error occurs when Git encounters conflicts while applying commits during a rebase. The rebase pauses to let you resolve the conflicts.

## Common Causes

- Changes in the rebased branch conflict with the target branch
- Multiple commits in the branch each have different conflicts
- Same file modified in both branches
- Renamed file in one branch modified in the other

## How to Fix

### Resolve Conflicts

```bash
git status
# Edit conflicted files
git add <resolved-file>
git rebase --continue
```

### Skip Problematic Commit

```bash
git rebase --skip
```

### Abort the Rebase

```bash
git rebase --abort
```

### Use Git Mergetool

```bash
git mergetool
git rebase --continue
```

## Examples

```bash
# Example 1: Resolve and continue
git rebase main
# CONFLICT in src/app.js
# Fix: edit src/app.js, git add src/app.js, git rebase --continue

# Example 2: Skip commit
git rebase --skip

# Example 3: Abort rebase
git rebase --abort
# Back to pre-rebase state
```"""
    },
    {
        "slug": "git-revert-merge-commit",
        "title": "Git revert merge commit error",
        "desc": "Fix 'revert a merge' error. Resolve Git revert failures when reverting a merge commit requires specifying the parent number.",
        "body": """fatal: Commit <hash> is a merge but no -m option was given.

This error occurs when you try to revert a merge commit without specifying which parent to follow with the `-m` flag.

## Common Causes

- Running `git revert <merge-commit>` without `-m`
- Merge commit has multiple parents
- Unclear which parent represents the mainline

## How to Fix

### Revert with Parent 1 (Main Branch)

```bash
git revert -m 1 <merge-commit>
```

### Revert with Parent 2 (Feature Branch)

```bash
git revert -m 2 <merge-commit>
```

### View Merge Parents

```bash
git log --oneline --graph <merge-commit>
git cat-file -p <merge-commit> | grep parent
```

## Examples

```bash
# Example 1: Revert a merge
git log --oneline -5
# abc1234 Merge branch 'feature/login' into main
git revert -m 1 abc1234
# Reverts the merge, keeping main's changes

# Example 2: Check parents
git cat-file -p abc1234 | grep parent
# parent def1234... (main)
# parent 789abcd... (feature/login)
# Fix: git revert -m 1 abc1234

# Example 3: Revert merge with commit message
git revert -m 1 abc1234 -n
git commit -m "Revert: feature login merge"
```"""
    },
    {
        "slug": "git-stash-apply-fail",
        "title": "Git stash apply failed",
        "desc": "Fix 'git stash apply failed' error. Resolve issues when applying a stash to the current working directory.",
        "body": """Auto-merging <file>
CONFLICT (content): Merge conflict in <file>

This error occurs when `git stash apply` cannot cleanly apply stashed changes to the current working tree because of conflicts.

## Common Causes

- Current branch differs from where stash was created
- Files modified after stash was made
- Uncommitted changes conflict with stash
- Stash was created long ago and code changed significantly

## How to Fix

### Resolve Conflicts

```bash
git status
# Edit conflicted files
git add <file>
git stash drop  # if satisfied
```

### Create Branch from Stash

```bash
git stash branch <new-branch>
```

### Apply to Different Branch

```bash
git checkout <original-branch>
git stash apply
```

### List and Choose Stash

```bash
git stash list
git stash show -p stash@{n}
```

## Examples

```bash
# Example 1: Resolve conflicts
git stash apply
# Auto-merging src/config.js - CONFLICT
git add src/config.js
git stash drop

# Example 2: Create branch from stash
git stash branch recovery-branch
# Applies stash on new branch at original commit

# Example 3: Apply specific stash
git stash apply stash@{2}
```"""
    },
    {
        "slug": "git-fetch-prune-error",
        "title": "Git fetch prune error",
        "desc": "Fix 'git fetch --prune' error. Resolve issues when pruning stale remote-tracking references during fetch.",
        "body": """fatal: --prune requires a remote

This error occurs when you run `git fetch --prune` without specifying a remote. Git needs to know which remote's tracking branches to prune.

## Common Causes

- Remote name not provided
- No remotes configured in the repository
- Using `--prune` with an invalid remote name
- Typo in the remote name

## How to Fix

### Specify the Remote

```bash
git fetch --prune origin
```

### Prune All Remotes

```bash
git remote prune origin
```

### Configure Automatic Pruning

```bash
git config --global fetch.prune true
```

### Check Configured Remotes

```bash
git remote -v
```

## Examples

```bash
# Example 1: Missing remote
git fetch --prune
# fatal: --prune requires a remote
# Fix: git fetch --prune origin

# Example 2: Configure automatic prune
git config --global fetch.prune true
git fetch origin  # automatically prunes

# Example 3: Prune all stale branches
git remote prune origin --dry-run  # preview
git remote prune origin  # execute
```"""
    },
    {
        "slug": "git-pull-no-remote",
        "title": "Git pull no remote error",
        "desc": "Fix 'git pull without remote' error. Resolve pull failures when no remote is configured for the current branch.",
        "body": """There is no tracking information for the current branch.

This error occurs when you run `git pull` but the current branch has no remote tracking branch configured.

## Common Causes

- New branch created locally without pushing
- Remote tracking configuration removed
- Detached HEAD state
- Repository cloned without default branch checkout

## How to Fix

### Set Upstream Branch

```bash
git branch --set-upstream-to=origin/<branch> <branch>
```

### Pull with Explicit Remote

```bash
git pull origin <branch>
```

### Push with Upstream

```bash
git push -u origin <branch>
```

### Check Remote Configuration

```bash
git remote -v
git branch -vv
```

## Examples

```bash
# Example 1: New branch, no upstream
git checkout -b feature/new
git pull
# There is no tracking information for the current branch.
# Fix: git push -u origin feature/new

# Example 2: Set upstream manually
git branch --set-upstream-to=origin/main main
git pull

# Example 3: Pull with explicit remote
git pull origin feature/new
```"""
    },
    {
        "slug": "git-branch-delete-error",
        "title": "Git branch delete error",
        "desc": "Fix 'git branch -d' error. Resolve failures when trying to delete a Git branch that has unmerged changes.",
        "body": """error: The branch '<branch>' is not fully merged.

This error occurs when you try to delete a branch that has commits not merged into the current branch or its upstream.

## Common Causes

- Branch has unmerged commits
- Wrong branch name specified
- Current branch is the one you're trying to delete
- Merged to a different branch but not current

## How to Fix

### Force Delete Branch

```bash
git branch -D <branch>
```

### Merge Before Deleting

```bash
git merge <branch>
git branch -d <branch>
```

### Check Merge Status

```bash
git branch --merged
git branch --no-merged
```

### Delete Remote Branch

```bash
git push origin --delete <branch>
```

## Examples

```bash
# Example 1: Unmerged branch
git branch -d feature/old
# error: The branch 'feature/old' is not fully merged.
# Fix: git branch -D feature/old

# Example 2: Delete after merge
git checkout main
git merge feature/done
git branch -d feature/done

# Example 3: Check which branches are safe to delete
git branch --merged
# Shows branches that can be deleted with -d
```"""
    },
    {
        "slug": "git-checkout-detached-no-branch",
        "title": "Git checkout detached HEAD no branch",
        "desc": "Fix Git detached HEAD state. Resolve issues when Git HEAD is not attached to any branch, making commits potentially unreachable.",
        "body": """You are in 'detached HEAD' state.

This message occurs when you check out a specific commit, tag, or remote branch, making HEAD point directly to a commit instead of a branch.

## Common Causes

- Checking out a specific commit hash
- Checking out a tag
- Checking out a remote branch without creating a local branch
- Using `git checkout origin/<branch>` instead of just `<branch>`

## How to Fix

### Create a Branch from Detached HEAD

```bash
git switch -c <new-branch>
```

### Check Out Existing Branch

```bash
git checkout <existing-branch>
```

### Keep Changes Made in Detached State

```bash
git checkout -b <new-branch>
git add -A && git commit -m "Changes from detached HEAD"
```

### Discard Changes and Return to Branch

```bash
git checkout main
```

## Examples

```bash
# Example 1: Create branch to save changes
git checkout -b saved-changes
git add -A
git commit -m "Work done in detached HEAD"

# Example 2: Return to main
git checkout main

# Example 3: Checkout tag and make changes
git checkout v1.0
git checkout -b v1.0-patches
```"""
    },
    {
        "slug": "git-config-global-local-conflict",
        "title": "Git config global/local conflict",
        "desc": "Fix Git configuration conflicts between global and local config settings that override expected behavior.",
        "body": """warning: user.name is set in multiple configuration files

This occurs when you have conflicting Git configuration values set at different levels (system, global, local). The local value takes precedence.

## Common Causes

- Different user.name or user.email in global vs local config
- Local repo has different signing key than global config
- Proxy settings differ between global and local
- Conflicting alias definitions

## How to Fix

### List All Config Values

```bash
git config --list --show-origin
```

### Check Specific Key

```bash
git config --global user.name
git config --local user.name
```

### Unset Local Config

```bash
git config --local --unset user.name
```

### Unset Global Config

```bash
git config --global --unset user.name
```

## Examples

```bash
# Example 1: Different user names
git config --global user.name "John Doe"
git config --local user.name "Jane Doe"
# Fix: git config --local --unset user.name

# Example 2: View all origins
git config --list --show-origin

# Example 3: Check which config is winning
git config user.name
# Shows the effective value
```"""
    },
    {
        "slug": "git-update-index-error",
        "title": "Git update-index error",
        "desc": "Fix 'git update-index' error. Resolve issues when manually updating the Git index for file permissions, assume-unchanged, or skip-worktree.",
        "body": """fatal: Unable to mark file <file>

This error occurs when `git update-index` fails to update the index entry for a specified file.

## Common Causes

- File does not exist in the index
- File is not tracked by Git
- Permission denied when writing to index
- File path is invalid
- Index is locked by another process

## How to Fix

### Check File in Index

```bash
git ls-files <file>
```

### Mark File as Assume-unchanged

```bash
git update-index --assume-unchanged <file>
```

### Remove Assume-unchanged Flag

```bash
git update-index --no-assume-unchanged <file>
```

### List Files with Flags

```bash
git ls-files -v | grep ^[a-z]
```

## Examples

```bash
# Example 1: File not in index
git update-index --assume-unchanged untracked.js
# fatal: Unable to mark file untracked.js
# Fix: git add untracked.js first

# Example 2: Mark config file unchanged
git update-index --assume-unchanged config/local.js
git status  # ignores changes to this file

# Example 3: Remove assume-unchanged
git update-index --no-assume-unchanged config/local.js
```"""
    },
    {
        "slug": "git-log-follow-rename",
        "title": "Git log follow rename error",
        "desc": "Fix 'git log --follow' error. Resolve issues when tracking file history across renames with Git log.",
        "body": """fatal: --follow requires exactly one path

This error occurs when you use `--follow` with multiple file paths. The `--follow` option only works with a single file path.

## Common Causes

- Passing multiple file paths to `git log --follow`
- Using a directory path instead of a single file
- Glob pattern expands to multiple files
- Misunderstanding of `--follow` limitations

## How to Fix

### Use Single File Path

```bash
git log --follow src/main.js
```

### Find Renames Manually

```bash
git log --name-only --diff-filter=R
```

### Search All History for Content

```bash
git log --all -S <search-term>
```

### Use Rename Detection

```bash
git log --find-renames -- <path>
```

## Examples

```bash
# Example 1: Multiple paths
git log --follow src/*.js
# fatal: --follow requires exactly one path
# Fix: git log --follow src/app.js

# Example 2: Track renames manually
git log --name-status --follow src/app.js
# R100 src/old.js src/app.js  (shows rename)

# Example 3: Search by content
git log --all -S "functionName" -- "*.js"
```"""
    },
    {
        "slug": "git-clean-error",
        "title": "Git clean error",
        "desc": "Fix 'git clean' error. Resolve issues when removing untracked files and directories from the working tree.",
        "body": """fatal: clean.requireForce and -n or -f not set

This error occurs when you run `git clean` without the force flag and the `clean.requireForce` config is set to true (default).

## Common Causes

- Running `git clean` without `-f` or `-n` flag
- `clean.requireForce` is enabled (default)
- Not previewing files before removing them
- Using `git clean` in a directory with important untracked files

## How to Fix

### Preview Files to Remove

```bash
git clean -n
```

### Force Remove Untracked Files

```bash
git clean -f
```

### Remove Untracked Directories

```bash
git clean -fd
```

### Remove Ignored Files Too

```bash
git clean -xfd
```

### Disable Force Requirement

```bash
git config --global clean.requireForce false
```

## Examples

```bash
# Example 1: Force required
git clean
# fatal: clean.requireForce and -n or -f not set
# Fix: git clean -f

# Example 2: Preview first
git clean -n
# Would remove build/

# Example 3: Remove everything
git clean -xfd
# Removes all untracked and ignored files
```"""
    },
    {
        "slug": "git-am-error",
        "title": "Git am (apply mailbox) error",
        "desc": "Fix 'git am' error. Resolve issues when applying patches from a mailbox file or format-patch output.",
        "body": """Patch failed at <number> <commit-message>

This error occurs when `git am` cannot apply a patch from a mailbox file. The patch may conflict with the current branch state.

## Common Methods

### Resolve Patch Failure

```bash
# Fix conflicts manually
git add <resolved-files>
git am --continue
```

### Skip Failed Patch

```bash
git am --skip
```

### Abort Patch Application

```bash
git am --abort
```

### Apply with Reject Files

```bash
git am --reject <patch-file>
```

## Examples

```bash
# Example 1: Resolve patch conflict
git am patches/0001-fix-bug.patch
# Patch failed at 0001 fix bug
# Fix: edit files, git add ., git am --continue

# Example 2: Skip problematic patch
git am --skip

# Example 3: Apply with 3-way merge
git am --3way patches/*.patch
```"""
    },
    {
        "slug": "git-bisect-error",
        "title": "Git bisect error",
        "desc": "Fix 'git bisect' error. Resolve issues when using Git bisect to find the commit that introduced a bug.",
        "body": """fatal: bisect run failed: exit code <n> from <command>

This error occurs when the bisect run script exits with a non-zero code that is not 0 (good), 1 (bad), or 125 (skip).

## Common Causes

- Bisect script itself has a bug
- Wrong boundaries (good/bad) set incorrectly
- Too many commits to bisect efficiently
- Script environment differs from expected
- Git state issues during bisect

## How to Fix

### Reset Bisect

```bash
git bisect reset
```

### Check Good/Bad Markers

```bash
git bisect log
```

### Restart with Correct Boundaries

```bash
git bisect start
git bisect good <known-good-commit>
git bisect bad <known-bad-commit>
```

### Run Bisect Manually

```bash
git bisect good  # or bad at each step
```

## Examples

```bash
# Example 1: Reset and restart
git bisect reset
git bisect start
git bisect good v1.0
git bisect bad HEAD
git bisect run npm test

# Example 2: Check bisect log
git bisect log

# Example 3: Manual bisect
git bisect start HEAD v1.0
# Test manually at each step
git bisect good  # or git bisect bad
```"""
    },
    {
        "slug": "git-describe-error",
        "title": "Git describe error",
        "desc": "Fix 'git describe' error. Resolve issues when describing a commit using the most recent tag reachable from it.",
        "body": """fatal: No tags can describe '<commit>'.

This error occurs when `git describe` cannot find any tag reachable from the specified commit.

## Common Causes

- No tags exist in the repository
- Current commit is ahead of all tags
- Tags are not reachable from the current commit
- Repository has no tags at all
- Commit is on a different branch without tags

## How to Fix

### Create a Tag

```bash
git tag -a v1.0.0 -m "Initial version"
git describe
```

### Use Tags Flag

```bash
git describe --tags
```

### Use Always Flag

```bash
git describe --always
```

### List All Tags

```bash
git tag -l
```

## Examples

```bash
# Example 1: No tags
git describe HEAD
# fatal: No tags can describe 'abc1234'.
# Fix: git tag -a v1.0.0 -m "Initial release"

# Example 2: Use lightweight tags
git describe --tags
# v1.0.0-5-gabc1234

# Example 3: Fallback to hash
git describe --always
# abc1234
```"""
    },
    {
        "slug": "git-fsck-error",
        "title": "Git fsck (filesystem check) error",
        "desc": "Fix 'git fsck' errors. Resolve repository corruption detected by Git's integrity checking tool.",
        "body": """error: object <hash>: is a blob, not a commit

This error occurs when `git fsck` finds inconsistencies or corruption in the Git object database.

## Common Causes

- Corrupted objects from hardware failure
- Manual manipulation of .git directory
- Incomplete Git operations
- Disk write errors during commits
- File system corruption

## How to Fix

### Run Full Fsck

```bash
git fsck --full
```

### Fix Missing Objects

```bash
git fetch origin
git fsck --full
```

### Restore from Remote

```bash
git fetch origin
git reset --hard origin/main
```

### Clone Fresh Copy

```bash
cd ..
rm -rf repo
git clone <url>
```

## Examples

```bash
# Example 1: Run diagnostics
git fsck --full
# Checking object directories: 100%
# dangling commit abc1234

# Example 2: Fix with fetch
git fetch origin --refetch
git fsck --full

# Example 3: Full recovery
cd /tmp
git clone <url> repo-fresh
mv repo/.git/objects/pack/* repo-fresh/.git/objects/pack/
```"""
    },
    {
        "slug": "git-reflog-error",
        "title": "Git reflog error",
        "desc": "Fix 'git reflog' errors. Resolve issues when Git reflog is missing, corrupted, or has expired entries.",
        "body": """fatal: your current branch appears to be broken

This error occurs when the reflog is corrupted or the HEAD reference points to a non-existent branch.

## Common Causes

- Reflog was manually deleted or corrupted
- Branch was deleted that HEAD pointed to
- Repository was partially restored from backup
- Reflog expiration cleaned all entries
- Garbage collection cleaned reflog

## How to Fix

### Check HEAD Reference

```bash
cat .git/HEAD
```

### Create Reflog

```bash
git reflog expire --expire=now --all
git reflog
```

### Restore from ORIG_HEAD

```bash
git reset --hard ORIG_HEAD
```

### Recover Lost Commits

```bash
git fsck --lost-found
ls -la .git/lost-found/
```

## Examples

```bash
# Example 1: View reflog
git reflog show HEAD
# abc1234 HEAD@{0}: commit: Fix bug
# def5678 HEAD@{1}: commit: Add feature

# Example 2: Recover lost commit
git reflog expire --expire=now --all
git fsck --lost-found
git show .git/lost-found/commit/abc1234

# Example 3: Check HEAD
cat .git/HEAD
# ref: refs/heads/main
```"""
    },
    {
        "slug": "git-reset-hard-mistake",
        "title": "Git reset --hard mistake recovery",
        "desc": "Recover from accidental 'git reset --hard' mistake. Restore lost commits and changes after a hard reset.",
        "body": """Recovering from accidental git reset --hard

Running `git reset --hard` discards all uncommitted changes and moves HEAD to a specified commit. If you reset to the wrong commit, your work is not necessarily lost.

## Recovery Methods

### Use Reflog to Find Lost Commits

```bash
git reflog
git reset --hard HEAD@{n}
```

### Recover Staged Changes

```bash
git fsck --lost-found
git show <lost-commit>
```

### Find Dangling Commits

```bash
git fsck --full --no-dangling
```

## Examples

```bash
# Example 1: Undo reset --hard
git reflog
# abc1234 HEAD@{0}: reset: moving to HEAD~2
# def5678 HEAD@{1}: commit: Important changes
git reset --hard HEAD@{1}

# Example 2: Recover from fsck
git fsck --lost-found
# dangling commit abc1234
git show abc1234
git merge abc1234

# Example 3: ORIG_HEAD recovery
git reset --hard ORIG_HEAD
```"""
    },
    {
        "slug": "git-sparse-checkout-error",
        "title": "Git sparse checkout error",
        "desc": "Fix Git sparse checkout errors. Resolve issues when using partial or sparse checkout to work with a subset of repository files.",
        "body": """fatal: Sparse checkout leaves no entry on working directory

This error occurs when sparse checkout patterns exclude all files, leaving an empty working directory.

## Common Causes

- Sparse checkout patterns match nothing
- Cone mode excludes all directories
- Incorrect path patterns
- No patterns configured after enabling sparse checkout

## How to Fix

### Initialize Sparse Checkout

```bash
git sparse-checkout init --cone
```

### Set Directory to Include

```bash
git sparse-checkout set src/
```

### Add Multiple Directories

```bash
git sparse-checkout add src/ docs/ tests/
```

### Disable Sparse Checkout

```bash
git sparse-checkout disable
```

### List Current Patterns

```bash
git sparse-checkout list
```

## Examples

```bash
# Example 1: Clone only src directory
git clone --filter=blob:none <url>
cd repo
git sparse-checkout init --cone
git sparse-checkout set src/

# Example 2: Add more directories
git sparse-checkout add docs/ tests/

# Example 3: Disable and get everything
git sparse-checkout disable
git checkout main -- .
```"""
    },
    {
        "slug": "git-switch-branch-error",
        "title": "Git switch branch error",
        "desc": "Fix 'git switch' errors. Resolve issues when using the modern 'git switch' command to change branches.",
        "body": """fatal: 'branch' is not a branch

This error occurs when you try to switch to a remote-tracking reference or commit hash using `git switch` without creating a new branch.

## Common Causes

- Trying to switch to a remote branch without creating local
- Using `git switch` with a commit hash
- Branch name doesn't exist
- Using `git switch` for detached HEAD state

## How to Fix

### Create Branch from Remote

```bash
git switch -c <branch> origin/<branch>
```

### Switch to Existing Branch

```bash
git switch <existing-branch>
```

### Create New Branch

```bash
git switch -c <new-branch>
```

### Use Detach for Commits

```bash
git switch --detach <commit>
```

## Examples

```bash
# Example 1: Switch to remote branch
git switch feature/login
# fatal: 'feature/login' is not a branch
# Fix: git switch -c feature/login origin/feature/login

# Example 2: Create and switch
git switch -c new-feature

# Example 3: Switch to commit (detached)
git switch --detach HEAD~3
```"""
    },
    {
        "slug": "git-tag-delete-error",
        "title": "Git tag delete error",
        "desc": "Fix 'git tag -d' error. Resolve failures when trying to delete Git tags.",
        "body": """error: tag '<tag>' not found.

This error occurs when you try to delete a Git tag that does not exist locally.

## Common Causes

- Tag name is misspelled
- Tag exists remotely but not locally
- Tag was already deleted
- Wrong tag name format

## How to Fix

### List Local Tags

```bash
git tag -l
```

### Delete Local Tag

```bash
git tag -d <tag-name>
```

### Delete Remote Tag

```bash
git push origin --delete <tag-name>
```

### Fetch Tags First

```bash
git fetch --tags
git tag -d <tag-name>
```

## Examples

```bash
# Example 1: Tag not found
git tag -d v1.0
# error: tag 'v1.0' not found.
# Fix: git tag -l to see available tags
# Or: git tag -d v1.0.0 (correct name)

# Example 2: Delete local and remote
git tag -d v1.0
git push origin --delete v1.0

# Example 3: Delete remote only
git push origin :refs/tags/v1.0
```"""
    },
    {
        "slug": "git-worktree-add-error",
        "title": "Git worktree add error",
        "desc": "Fix 'git worktree add' error. Resolve issues when adding a new working tree linked to the repository.",
        "body": """fatal: '<path>' already exists

This error occurs when you try to add a Git worktree at a path that already has files or is an existing directory.

## Common Causes

- Target directory already exists and is not empty
- Branch is already checked out in another worktree
- Worktree path is already in use
- Invalid path specified

## How to Fix

### Use a Different Path

```bash
git worktree add ../repo-feature feature-branch
```

### Remove Existing Directory

```bash
rm -rf <path>
git worktree add <path> <branch>
```

### List Existing Worktrees

```bash
git worktree list
```

### Prune Stale Worktrees

```bash
git worktree prune
```

## Examples

```bash
# Example 1: Path already exists
git worktree add ./hotfix hotfix-branch
# fatal: './hotfix' already exists
# Fix: git worktree add ../hotfix hotfix-branch

# Example 2: Check branch usage
git worktree list
# /main-repo          abc1234 [main]
# /feature-worktree   def5678 [feature/login]
# Fix: use different branch for new worktree

# Example 3: Prune stale worktrees
git worktree prune
git worktree add ../new-feature feature/new
```"""
    },
    {
        "slug": "git-push-tag-to-protected-branch",
        "title": "Git push tag to protected branch error",
        "desc": "Fix Git push tag error when pushing to a branch with protected branch rules on GitHub or GitLab.",
        "body": """! [remote rejected] v1.0 -> v1.0 (protected branch)

This error occurs when you try to push a tag to a branch that has protected branch rules configured on the remote server.

## Common Causes

- Branch is protected with push restrictions
- No permission to push tags to the branch
- Branch protection requires pull requests
- Repository admin has restricted direct pushes

## How to Fix

### Push Tags Separately

```bash
git push origin v1.0
```

### Push to Non-Protected Branch

```bash
git push origin feature/branch
```

### Create a Pull Request

```bash
# Push branch and create PR on GitHub
git push origin feature/new
gh pr create
```

### Request Repository Access

```bash
# Contact repository admin for access
```

## Examples

```bash
# Example 1: Tag rejected due to protection
git push origin main --tags
# ! [remote rejected] v1.0 -> v1.0 (protected branch)
# Fix: git push origin v1.0

# Example 2: Push to feature branch
git push origin feature/new-feature

# Example 3: Create PR from command line
git push origin feature/new-feature
gh pr create --title "New feature" --body "Description"
```"""
    },
    {
        "slug": "git-rebase-onto-error",
        "title": "Git rebase --onto error",
        "desc": "Fix 'git rebase --onto' error. Resolve issues when using rebase with the --onto option to transplant commits.",
        "body": """fatal: invalid upstream '<ref>'

This error occurs when you provide an invalid reference to `git rebase --onto`. The upstream or new base reference cannot be found.

## Common Causes

- Typo in branch or reference name
- Reference does not exist
- References from a different repository
- `--onto` arguments in wrong order

## How to Fix

### Check Syntax

```bash
git rebase --onto <new-base> <upstream> <branch>
```

### Verify References Exist

```bash
git branch -a | grep <branch>
git log --oneline -5 <ref>
```

### Use Commits Instead of Branches

```bash
git rebase --onto <commit> <upstream-commit> <branch>
```

## Examples

```bash
# Example 1: Move last 3 commits from feature to main
git rebase --onto main feature~3 feature

# Example 2: Wrong reference
git rebase --onto main nonexistent feature
# fatal: invalid upstream 'nonexistent'
# Fix: git branch -a to find correct name

# Example 3: Correct order
git rebase --onto main feature-branch~3 feature-branch
```"""
    },
    {
        "slug": "git-mergetool-error",
        "title": "Git mergetool error",
        "desc": "Fix 'git mergetool' error. Resolve issues when launching merge conflict resolution tools.",
        "body": """No files need merging

This error occurs when you run `git mergetool` but there are no merge conflicts to resolve in the working tree.

## Common Causes

- No merge or rebase in progress
- All conflicts were already resolved
- Running in a directory without conflicts
- Merge completed successfully without conflicts
- Wrong repository

## How to Fix

### Check for Merge in Progress

```bash
git status
```

### Verify Conflict Files

```bash
git diff --name-only --diff-filter=U
```

### Configure Mergetool

```bash
git config merge.tool vimdiff
git config mergetool.keepBackup false
```

### List Available Tools

```bash
git mergetool --tool-help
```

## Examples

```bash
# Example 1: No conflicts
git mergetool
# No files need merging
# Fix: check git status first

# Example 2: Configure and run
git config merge.tool vimdiff
git config mergetool.keepBackup false
git merge feature/branch
git mergetool
# Opens vimdiff for each conflicted file

# Example 3: Use VS Code as mergetool
git config merge.tool vscode
git config mergetool.vscode.cmd 'code --wait $MERGED'
```"""
    },
    {
        "slug": "git-credential-cache-error",
        "title": "Git credential cache error",
        "desc": "Fix Git credential cache errors. Resolve issues when Git credential caching is not working or fails to save credentials.",
        "body": """fatal: credential-cache unavailable; no unix socket support

This error occurs when the credential cache helper cannot be used because the system does not support Unix sockets (e.g., Windows, or certain container environments).

## Common Causes

- Windows or unsupported environment for credential cache
- Git installed without socket support
- Running in a minimal container
- Credential cache timeout expired
- Permission issues with socket directory

## How to Fix

### Use Store Helper (less secure)

```bash
git config --global credential.helper store
```

### Use Manager (Windows)

```bash
git config --global credential.helper manager
```

### Increase Cache Timeout

```bash
git config --global credential.helper "cache --timeout=86400"
```

### Clear Credential Cache

```bash
git credential-cache exit
```

## Examples

```bash
# Example 1: Windows credential manager
git config --global credential.helper manager-core

# Example 2: Store credentials with timeout
git config --global credential.helper "cache --timeout=3600"

# Example 3: Use plaintext store (Linux)
git config --global credential.helper store
# Credentials saved to ~/.git-credentials
```"""
    },
    {
        "slug": "git-gc-error",
        "title": "Git gc (garbage collection) error",
        "desc": "Fix 'git gc' error. Resolve issues when Git garbage collection fails to clean up or optimize the repository.",
        "body": """error: failed to run git gc

This error occurs when Git garbage collection encounters an issue while cleaning up repository objects or optimizing storage.

## Common Causes

- Another Git process is running
- Insufficient disk space
- Repository corruption
- Lock file from previous GC
- Too large repository with many objects

## How to Fix

### Check for Running Processes

```bash
ps aux | grep git
```

### Remove GC Lock File

```bash
rm -f .git/gc.pid
```

### Run GC with Verbose

```bash
git gc --verbose
```

### Run Aggressive GC

```bash
git gc --aggressive
```

### Check Disk Space

```bash
df -h .
```

## Examples

```bash
# Example 1: GC locked
rm -f .git/gc.pid
git gc --verbose

# Example 2: Aggressive optimization
git gc --aggressive --prune=now
# Optimizes all packs (slower but thorough)

# Example 3: Auto GC
git config gc.auto 500
# Automatically runs GC when object count exceeds 500
```"""
    },
    {
        "slug": "git-format-patch-error",
        "title": "Git format-patch error",
        "desc": "Fix 'git format-patch' error. Resolve issues when creating patch files from commits for email or sharing.",
        "body": """fatal: <commit> does not have any commits

This error occurs when the revision range specified for `git format-patch` does not produce any patches.

## Common Causes

- No commits in the specified range
- Wrong revision range specified
- Branch is up to date with the base
- Empty range or invalid commit references

## How to Fix

### Check Commit Range

```bash
git log --oneline origin/main..HEAD
```

### Use Correct Range

```bash
git format-patch origin/main
```

### Create Patches from Last N Commits

```bash
git format-patch -3
```

### Output to Directory

```bash
git format-patch -o patches/ origin/main
```

## Examples

```bash
# Example 1: No commits since fork
git format-patch origin/main
# No output (no commits to patch)
# Fix: commit some changes first

# Example 2: Last 2 commits
git format-patch -2
# 0001-first-commit.patch
# 0002-second-commit.patch

# Example 3: Output to directory
git format-patch -o patches/ -3
```"""
    },
    {
        "slug": "git-shallow-clone-fetch-error",
        "title": "Git shallow clone fetch error",
        "desc": "Fix Git shallow clone fetch errors. Resolve issues when deepening or unshallowing a shallow clone.",
        "body": """fatal: --depth is ignored in --unshallow

This error occurs when conflicting options are used while trying to deepen or unshallow a shallow clone.

## Common Causes

- Using `--depth` with `--unshallow` simultaneously
- Trying to deepen an already full repository
- Network issues during fetch on a shallow repo
- Server does not support shallow operations

## How to Fix

### Unshallow Completely

```bash
git fetch --unshallow
```

### Deepen by Specific Number

```bash
git fetch --depth=100
```

### Convert to Full Clone

```bash
git fetch --unshallow origin
git pull --all
```

### Check if Repository is Shallow

```bash
cat .git/shallow
```

## Examples

```bash
# Example 1: Unshallow clone
git fetch --unshallow origin
git pull --all

# Example 2: Deepen by 50 commits
git fetch --depth=50

# Example 3: Check shallow status
cat .git/shallow
# If file exists, repo is shallow
```"""
    },
    {
        "slug": "git-notes-error",
        "title": "Git notes error",
        "desc": "Fix 'git notes' error. Resolve issues when adding, appending, or managing Git notes on commits.",
        "body": """fatal: No note found for object <hash>

This error occurs when you try to show or manipulate a Git note on a commit that does not have any notes.

## Common Causes

- No notes have been added to the commit
- Notes ref is set incorrectly
- Notes were garbage collected
- Wrong commit hash specified

## How to Fix

### Add a Note

```bash
git notes add -m "Note content" <commit>
```

### List Notes

```bash
git notes list
```

### Show Notes for Commit

```bash
git notes show HEAD
```

### Configure Notes Display

```bash
git log --show-notes=*
```

## Examples

```bash
# Example 1: Add note
git notes add -m "This commit introduced a regression" abc1234

# Example 2: Append to existing note
git notes append -m "Also affects login flow" abc1234

# Example 3: Show all notes
git log --show-notes=*
# Displays notes alongside commits
```"""
    },
]

def slugify(s):
    return s

count = 0
for page in PAGES:
    if page["slug"] in EXISTING:
        print(f"SKIP (exists): {page['slug']}")
        continue
    content = f"""---
title: "[Solution] {page['title']}"
description: "{page['desc']}"
tools: ["git"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# {page['title']}

{page['body']}

## Related Errors

- [Merge Conflict]({{{{< relref "/tools/git/merge-conflict" >}}}}) — resolve merge conflicts
- [Push Rejected]({{{{< relref "/tools/git/push-rejected" >}}}}) — fix rejected pushes
"""
    path = f"/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/git/{page['slug']}.md"
    with open(path, 'w') as f:
        f.write(content)
    count += 1
    print(f"CREATED: {page['slug']}")

print(f"\nTotal created: {count}")
print(f"Total skipped (existing): {len(PAGES) - count}")
