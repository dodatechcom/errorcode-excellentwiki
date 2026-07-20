#!/usr/bin/env python3
"""Generate GitHub Actions error pages"""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/github-actions'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}

def make_page(title, desc, body):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["github-actions"]',
        'error-types: ["tool-error"]',
        'severities: ["error"]',
        '---',
        '',
        body,
    ]
    return '\n'.join(lines)

def md(title, desc, body):
    return (title, desc, body)

def slug(title):
    return title.lower().replace(' ', '-').replace('/', '-').replace("'", '').replace('"', '').replace('(', '').replace(')', '').replace(',', '').replace(':', '').replace('--', '-').strip('-')

PAGES = [
    # =========================================================================
    # 1. WORKFLOW SYNTAX ERRORS
    # =========================================================================
    md("Workflow YAML Unexpected Key Error",
       "Fix GitHub Actions workflow YAML unexpected key errors in workflow files.",
       """## Error Description

Unexpected key errors occur when the workflow YAML contains keys that GitHub Actions does not recognize:

```
Error: .github/workflows/build.yml: Unexpected key 'bulid'
```

## Common Causes

- Typo in YAML key names (e.g., `bulid` instead of `build`).
- Indentation issues causing keys to be at the wrong level.
- Copy-pasting from documentation with incorrect keys.
- Using keys from an older or newer GitHub Actions version.

## How to Fix

**Use a YAML linter to catch typos:**

```bash
yamllint .github/workflows/build.yml
```

**Validate the workflow:**

```bash
actionlint .github/workflows/build.yml
```

**Correct YAML structure:**

```yaml
name: Build
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
# Wrong - misspelled key
name: Build
on: push
jods:
  build:
    runs-on: ubuntu-latest

# Correct
name: Build
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```
"""),

    md("Workflow Invalid Event Trigger",
       "Fix GitHub Actions invalid event trigger errors when the 'on' event is not recognized.",
       """## Error Description

Invalid event trigger errors occur when the `on` key references an event GitHub Actions does not support:

```
Error: .github/workflows/ci.yml: on: Invalid event type 'pussh'
```

## Common Causes

- Misspelled event name in the `on` trigger.
- Using a custom event without defining a `repository_dispatch` properly.
- Capitalization errors (event names are case-sensitive in some contexts).

## How to Fix

**Use valid event names:**

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:
```

**Check available events:**

```bash
actionlint .github/workflows/ci.yml
```

## Examples

```yaml
# Wrong - 'pussh' is not a valid event
on:
  pussh:
    branches: [main]

# Correct
on:
  push:
    branches: [main]
```
"""),

    md("Workflow Jobs Syntax Error",
       "Fix GitHub Actions jobs syntax errors when the jobs section is malformed.",
       """## Error Description

Jobs syntax errors occur when the `jobs` section of the workflow is invalid:

```
Error: Invalid workflow file .github/workflows/ci.yml
jobs should be a map, got a string
```

## Common Causes

- `jobs` is defined as a string instead of a map of job objects.
- Missing job name or ID.
- Incorrect nesting under `jobs`.

## How to Fix

**Ensure `jobs` is a map:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
# Wrong - jobs is a string
jobs: "build"

# Correct - jobs is a map
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```
"""),

    md("Workflow Steps Requires Uses Or Run Error",
       "Fix GitHub Actions error when steps must have either 'uses' or 'run'.",
       """## Error Description

Each step in a GitHub Actions workflow must contain either a `uses` (for actions) or `run` (for shell commands) key:

```
Error: .github/workflows/ci.yml: steps[0] must have one of 'uses' or 'run'
```

## Common Causes

- Step defined without `uses` or `run`.
- `uses` and `run` are both missing due to a typo.
- Step has `name` only with no executable content.

## How to Fix

**Add either `uses` or `run` to every step:**

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v4

  - name: Run tests
    run: npm test

  - name: Build project
    run: npm run build
```

## Examples

```yaml
# Wrong - no uses or run
steps:
  - name: Checkout code

# Correct - has uses
steps:
  - name: Checkout code
    uses: actions/checkout@v4

# Correct - has run
steps:
  - name: Print hello
    run: echo "Hello"
```
"""),

    md("Workflow Missing workflow_dispatch Trigger",
       "Fix GitHub Actions missing workflow_dispatch trigger for manual workflow runs.",
       """## Error Description

Workflows that need manual triggering require the `workflow_dispatch` event, but it is missing:

```
Error: Workflow does not support manual triggering.
Use 'on: workflow_dispatch' to enable manual runs.
```

## Common Causes

- The `workflow_dispatch` event was not added to the `on` trigger.
- Developer expects to trigger manually but only push/pull_request are defined.

## How to Fix

**Add workflow_dispatch to the on trigger:**

```yaml
on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deploy target'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production
```

## Examples

```yaml
# Without inputs
on:
  workflow_dispatch:

# With inputs
on:
  workflow_dispatch:
    inputs:
      debug:
        description: 'Enable debug logging'
        required: false
        default: 'false'
        type: boolean
```
"""),

    md("Workflow Invalid On Value Error",
       "Fix GitHub Actions invalid 'on' value errors when the event trigger value is malformed.",
       """## Error Description

Invalid `on` value errors occur when the event trigger is not a valid string, map, or list:

```
Error: .github/workflows/ci.yml: Invalid type for 'on'
```

## Common Causes

- `on` is set to a string instead of a map.
- `on` uses invalid YAML types.
- Mixed list and map syntax under `on`.

## How to Fix

**Use proper map syntax under `on`:**

```yaml
on:
  push:
    branches:
      - main
      - develop
  pull_request:
    types: [opened, synchronize]
```

## Examples

```yaml
# Wrong - 'on' is a string
on: push

# Correct - 'on' is a map
on:
  push:
    branches: [main]
```
"""),

    md("Workflow Matrix Strategy Syntax Error",
       "Fix GitHub Actions matrix strategy syntax errors in workflow YAML.",
       """## Error Description

Matrix strategy syntax errors occur when the `strategy.matrix` block is malformed:

```
Error: Invalid matrix configuration
```

## Common Causes

- Matrix values are not lists.
- Nested matrix definitions are incorrect.
- `include` or `exclude` are used incorrectly.

## How to Fix

**Use proper matrix syntax:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16, 18, 20]
        os: [ubuntu-latest, windows-latest]
```

## Examples

```yaml
# Wrong - matrix values not lists
strategy:
  matrix:
    node-version: 18

# Correct
strategy:
  matrix:
    node-version: [16, 18, 20]
```
"""),

    md("Workflow If Condition Expression Error",
       "Fix GitHub Actions 'if' condition expression errors in workflow steps or jobs.",
       """## Error Description

If condition expression errors occur when an `if` condition contains invalid expression syntax:

```
Error: .github/workflows/ci.yml: Invalid expression in if condition
```

## Common Causes

- Using `${{ }}` syntax inside an `if` that already evaluates expressions.
- Incorrect operator usage (`==` vs `=`).
- Referencing undefined variables or contexts.

## How to Fix

**Use the expression syntax correctly:**

```yaml
steps:
  - name: Deploy
    if: github.ref == 'refs/heads/main' && success()
    run: echo "Deploying"

  - name: Skip
    if: ${{ !cancelled() }}
    run: echo "Runs even if earlier steps fail"
```

## Examples

```yaml
# Wrong - invalid operator
if: github.event_name = 'push'

# Correct
if: github.event_name == 'push'
```
"""),

    md("Workflow Env Context Not Available Error",
       "Fix GitHub Actions env context not available errors in workflow expressions.",
       """## Error Description

The `env` context is not available in certain parts of the workflow file:

```
Error: env context is not available here
```

## Common Causes

- Using `${{ env.VARIABLE }}` in the `on` trigger (env is only available in steps).
- Referencing `env` at the workflow level before any step sets it.
- Using `env` in `jobs.<job_id>.runs-on`.

## How to Fix

**Env is available in steps, not in on trigger:**

```yaml
env:
  NODE_VERSION: 20

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Use Node.js
        run: node --version
        # env.VARIABLE is available here
```

## Examples

```yaml
# Wrong - env not available in on trigger
on:
  push:
    branches: [main]
env:
  MY_VAR: hello
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo ${{ env.MY_VAR }}  # OK in steps
```
"""),

    md("Workflow Secrets Context Invalid Error",
       "Fix GitHub Actions secrets context invalid errors when accessing secrets.",
       """## Error Description

Secrets context errors occur when secrets are accessed incorrectly or in unauthorized contexts:

```
Error: secrets context is not available here
```

## Common Causes

- Accessing `secrets` in the `on` trigger (not supported).
- Secret name contains invalid characters.
- Secret not set in the repository or organization settings.

## How to Fix

**Access secrets only in steps:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy
        run: echo "Deploying with token"
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

**Set the secret via CLI:**

```bash
gh secret set DEPLOY_TOKEN --body "your-token-here"
```

## Examples

```yaml
# Wrong - secrets not available in on trigger
on:
  push:
    branches: [secrets.BRANCH]

# Correct - secrets in steps
steps:
  - run: echo ${{ secrets.API_KEY }}
    env:
      API_KEY: ${{ secrets.API_KEY }}
```
"""),

    md("Workflow Needs Dependency Cycle Error",
       "Fix GitHub Actions needs dependency cycle errors in workflow jobs.",
       """## Error Description

Dependency cycle errors occur when jobs reference each other in a circular `needs` chain:

```
Error: Job 'test' needs job 'deploy', but job 'deploy' also needs 'test'
Cycle detected: build -> test -> deploy -> build
```

## Common Causes

- Job A needs Job B, and Job B needs Job A.
- Complex dependency chains that inadvertently create cycles.

## How to Fix

**Restructure jobs to remove the cycle:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

  deploy:
    needs: [build, test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
# Wrong - circular dependency
jobs:
  test:
    needs: deploy
  deploy:
    needs: test

# Correct - linear dependency
jobs:
  test:
    runs-on: ubuntu-latest
  deploy:
    needs: test
    runs-on: ubuntu-latest
```
"""),

    md("Workflow Runs-On Invalid Value Error",
       "Fix GitHub Actions runs-on invalid value errors when the runner label is not recognized.",
       """## Error Description

The `runs-on` value must be a valid runner label or group:

```
Error: .github/workflows/ci.yml: runs-on 'ubnutu-latest' is not a valid runner
```

## Common Causes

- Typo in the runner label (e.g., `ubnutu-latest`).
- Using a self-hosted runner label that is not registered.
- Using a deprecated runner image.

## How to Fix

**Use valid runner labels:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
# Wrong
runs-on: ubnutu-latest

# Correct
runs-on: ubuntu-latest

# Self-hosted with labels
runs-on: [self-hosted, linux, x64]
```
"""),

    md("Workflow Container Syntax Error",
       "Fix GitHub Actions container syntax errors in job configuration.",
       """## Error Description

Container syntax errors occur when the `container` configuration is malformed:

```
Error: .github/workflows/ci.yml: Invalid container configuration
```

## Common Causes

- Missing `image` key under `container`.
- Invalid `credentials` format.
- Port mapping syntax errors.

## How to Fix

**Use proper container syntax:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    container:
      image: node:20
      env:
        NODE_ENV: test
      ports:
        - 8080:8080
      volumes:
        - /tmp:/tmp
      options: --cpus 1
    steps:
      - uses: actions/checkout@v4
      - run: node --version
```

## Examples

```yaml
# Wrong - missing image
container:
  env:
    NODE_ENV: test

# Correct
container:
  image: node:20
  env:
    NODE_ENV: test
```
"""),

    md("Workflow Service Container Error",
       "Fix GitHub Actions service container configuration errors.",
       """## Error Description

Service container errors occur when the `services` configuration is invalid:

```
Error: .github/workflows/ci.yml: services.postgres.image is required
```

## Common Causes

- Missing `image` key for a service.
- Invalid port mapping format.
- Service name conflicts with built-in names.

## How to Fix

**Define services properly:**

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - run: pg_isready -h localhost -p 5432
```

## Examples

```yaml
# Wrong - missing image
services:
  redis:
    ports:
      - 6379:6379

# Correct
services:
  redis:
    image: redis:7
    ports:
      - 6379:6379
```
"""),

    # =========================================================================
    # 2. RUNNER ERRORS
    # =========================================================================
    md("GitHub Actions Self-Hosted Runner Not Found",
       "Fix GitHub Actions self-hosted runner not found errors when the runner cannot be located.",
       """## Error Description

Self-hosted runner not found errors occur when the workflow references a runner that is not registered:

```
Error: The self-hosted runner 'my-runner' is not available for this repository.
```

## Common Causes

- Runner was removed from the repository or organization.
- Runner label does not match any registered runner.
- Runner was registered to a different repository.

## How to Fix

**Check registered runners:**

```bash
gh api repos/{owner}/{repo}/actions/runners
```

**Re-register the runner:**

```bash
./config.sh --url https://github.com/{owner}/{repo} --token {REGISTRATION_TOKEN}
```

## Examples

```yaml
# Wrong - runner label does not match
runs-on: my-custom-runner-v2

# Correct - use a label that exists
runs-on: self-hosted
```
"""),

    md("GitHub Actions Runner Offline Error",
       "Fix GitHub Actions runner offline errors when the runner is not responding.",
       """## Error Description

Runner offline errors occur when a registered runner is not connected:

```
Error: The self-hosted runner is offline. Workflow run was cancelled.
```

## Common Causes

- Runner machine is powered off.
- Runner process crashed or was stopped.
- Network connectivity issues between runner and GitHub.

## How to Fix

**Start the runner manually:**

```bash
cd /actions-runner
./run.sh
```

**Run as a service:**

```bash
sudo ./svc.sh install
sudo ./svc.sh start
```

**Check runner status:**

```bash
gh api repos/{owner}/{repo}/actions/runners --jq '.runners[] | {name: .name, status: .status}'
```

## Examples

```bash
# Check runner process
ps aux | grep Runner.Listener

# Restart runner service
sudo ./svc.sh stop
sudo ./svc.sh start
```
"""),

    md("GitHub Actions Runner Not Compatible Error",
       "Fix GitHub Actions runner not compatible errors due to version or OS mismatch.",
       """## Error Description

Runner not compatible errors occur when the runner version or OS does not meet workflow requirements:

```
Error: Runner version 2.300.0 is not compatible with required version 2.310.0
```

## Common Causes

- Runner binary is outdated.
- Workflow requires features from a newer runner version.
- OS-specific actions running on incompatible runner OS.

## How to Fix

**Update the runner:**

```bash
cd /actions-runner
./config.sh remove
curl -O https://github.com/actions/runner/releases/download/v2.310.0/actions-runner-linux-x64-2.310.0.tar.gz
tar xzf actions-runner-linux-x64-2.310.0.tar.gz
./config.sh --url https://github.com/{owner}/{repo} --token {TOKEN}
```

## Examples

```yaml
runs-on: ubuntu-latest
```
"""),

    md("GitHub Actions No Runner Matching Labels Error",
       "Fix GitHub Actions no runner matching labels errors.",
       """## Error Description

No runner matching labels errors occur when no registered runner has the requested labels:

```
Error: No runner matching the specified labels was found: gpu, cuda-12
```

## Common Causes

- Labels are too specific and no runner has them.
- Runner was removed but label is still in the workflow.
- Typo in label names.

## How to Fix

**Check available runner labels:**

```bash
gh api repos/{owner}/{repo}/actions/runners --jq '.runners[].labels[].name'
```

**Add labels to a runner:**

```bash
./config.sh --labels "gpu,cuda-12" --url https://github.com/{owner}/{repo} --token {TOKEN}
```

## Examples

```yaml
# Wrong - labels no runner has
runs-on: [self-hosted, gpu, cuda-12, arm64]

# Correct - labels runners actually have
runs-on: [self-hosted, linux, x64]
```
"""),

    md("GitHub Actions Runner Already Registered Error",
       "Fix GitHub Actions runner already registered errors when re-registering a runner.",
       """## Error Description

Runner already registered errors occur when attempting to register a runner that is already configured:

```
Error: Runner with name 'build-runner-01' is already registered
```

## Common Causes

- Attempting to register a runner that was not properly removed first.
- Previous registration attempt left partial configuration.

## How to Fix

**Remove and re-register:**

```bash
./config.sh remove
./config.sh --url https://github.com/{owner}/{repo} --token {NEW_TOKEN}
```

**Remove via API:**

```bash
gh api repos/{owner}/{repo}/actions/runners/{RUNNER_ID} -X DELETE
```

## Examples

```bash
# Check existing runners
gh api repos/{owner}/{repo}/actions/runners | jq '.runners[].name'

# Remove specific runner
./config.sh remove
```
"""),

    md("GitHub Actions Runner Removal Failed Error",
       "Fix GitHub Actions runner removal failed errors.",
       """## Error Description

Runner removal failures occur when the runner cannot be cleanly unregistered:

```
Error: Failed to remove runner: Runner is currently executing a job
```

## Common Causes

- Runner is actively executing a job.
- Network issues preventing communication with GitHub API.
- Insufficient permissions to remove the runner.

## How to Fix

**Wait for running jobs to finish:**

```bash
sleep 30
./config.sh remove
```

**Force remove via API:**

```bash
gh api repos/{owner}/{repo}/actions/runners/{RUNNER_ID} -X DELETE
```

## Examples

```bash
# Check if runner is busy
gh api repos/{owner}/{repo}/actions/runners/{RUNNER_ID} | jq '.status'
```
"""),

    md("GitHub Actions Runner Disk Full Error",
       "Fix GitHub Actions runner disk full errors causing workflow failures.",
       """## Error Description

Runner disk full errors occur when the runner machine runs out of disk space:

```
Error: ENOSPC: System limit for number of file descriptors reached
No space left on device
```

## Common Causes

- Docker images and layers consuming disk space.
- Build artifacts accumulating over time.
- Logs and temporary files not being cleaned up.

## How to Fix

**Clean Docker resources:**

```bash
docker system prune -af
docker volume prune -f
```

**Add cleanup step to workflow:**

```yaml
steps:
  - name: Free disk space
    if: always()
    run: |
      rm -rf node_modules .next dist build
      docker system prune -f
```

## Examples

```yaml
# Add free disk space step
steps:
  - name: Free disk space
    uses: jlumbroso/free-disk-space@main
    with:
      docker-images: true
      swap-storage: true
```
"""),

    md("GitHub Actions Runner OOM Killed Error",
       "Fix GitHub Actions runner out of memory killed errors.",
       """## Error Description

Runner OOM killed errors occur when the runner process or job runs out of memory:

```
Error: The runner has received a shutdown signal. This can happen
when the runner is running out of memory.
```

## Common Causes

- Job requires more memory than the runner has available.
- Memory leak in the build or test process.
- Running too many parallel jobs on a small runner.

## How to Fix

**Limit parallel jobs on self-hosted runner:**

```bash
./config.sh --concurrent 1
```

**Reduce memory usage in workflow:**

```yaml
steps:
  - name: Build with limited memory
    run: NODE_OPTIONS="--max-old-space-size=2048" npm run build
```

## Examples

```yaml
# Use larger runner
runs-on: ubuntu-latest-4-cores

# Limit Node.js memory
env:
  NODE_OPTIONS: "--max-old-space-size=4096"
```
"""),

    md("GitHub Actions Runner Network Timeout Error",
       "Fix GitHub Actions runner network timeout errors during workflow execution.",
       """## Error Description

Network timeout errors occur when the runner cannot reach external services:

```
Error: network timeout while connecting to github.com:443
fatal: unable to access 'https://github.com/': Could not resolve host
```

## Common Causes

- DNS resolution failure on the runner.
- Firewall blocking outbound connections.
- Corporate proxy not configured.

## How to Fix

**Configure DNS:**

```bash
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

**Set environment variables for the workflow:**

```yaml
env:
  HTTP_PROXY: http://proxy.example.com:8080
  HTTPS_PROXY: http://proxy.example.com:8080
steps:
  - uses: actions/checkout@v4
```

## Examples

```bash
# Test connectivity
curl -I https://github.com
```
"""),

    md("GitHub Actions Action Download Failed Error",
       "Fix GitHub Actions action download failed errors.",
       """## Error Description

Action download failures occur when GitHub Actions cannot download the referenced action:

```
Error: Failed to download action 'actions/checkout@v4'
Error: connect ECONNREFUSED 140.82.121.4:443
```

## Common Causes

- Network connectivity issues.
- GitHub API rate limit exceeded.
- Action repository is private without proper auth.

## How to Fix

**Use a specific SHA for reliability:**

```yaml
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11
```

**Check action availability:**

```bash
gh api repos/actions/checkout/releases/latest | jq '.tag_name'
```

## Examples

```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 0
```
"""),

    md("GitHub Actions Tool Cache Miss Error",
       "Fix GitHub Actions tool cache miss errors when required tools are not cached.",
       """## Error Description

Tool cache miss errors occur when a required tool is not available in the runner's tool cache:

```
Error: Unable to find any version of node matching: 21.x
```

## Common Causes

- Requested tool version is not pre-installed on the runner.
- Tool version was recently released and not yet added to the runner image.

## How to Fix

**Use setup actions that handle caching:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
```

## Examples

```yaml
# Use a version that is available
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: '20'
```
"""),

    md("GitHub Actions Hosted Runner Deprecation Error",
       "Fix GitHub Actions hosted runner deprecation warnings and errors.",
       """## Error Description

Deprecation errors occur when a workflow uses a runner image version that is being deprecated:

```
Warning: The ubuntu-18.04 runner image is being deprecated.
Please switch to ubuntu-latest or ubuntu-22.04
```

## Common Causes

- Workflow references an older runner image (e.g., `ubuntu-18.04`).
- Runner image reached end-of-life.

## How to Fix

**Update to the latest runner image:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
# Wrong - deprecated
runs-on: ubuntu-18.04

# Correct - latest
runs-on: ubuntu-latest
```
"""),

    md("GitHub Actions macOS Runner Not Available Error",
       "Fix GitHub Actions macOS runner availability errors.",
       """## Error Description

macOS runner not available errors occur when macOS runners cannot be assigned:

```
Error: No runner matching the specified labels was found: macos-latest
```

## Common Causes

- macOS runner capacity is exhausted.
- Organization plan does not include macOS runners.

## How to Fix

**Use `continue-on-error` to handle unavailability:**

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, macos-latest]
runs-on: ${{ matrix.os }}
continue-on-error: ${{ matrix.os == 'macos-latest' }}
```

## Examples

```yaml
jobs:
  build:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v4
```
"""),

    md("GitHub Actions Windows Runner Error",
       "Fix GitHub Actions Windows runner specific errors and quirks.",
       """## Error Description

Windows runner errors can include path separator issues, shell differences, and missing tools:

```
Error: The term 'apt-get' is not recognized as a name of a cmdlet
```

## Common Causes

- Using Linux commands on a Windows runner.
- Path separators: Windows uses `\\\\` while Linux uses `/`.
- Shell defaults to PowerShell, not bash.

## How to Fix

**Use the `shell` key to specify bash:**

```yaml
steps:
  - name: Run in bash
    shell: bash
    run: echo "Using bash shell"
```

## Examples

```yaml
# Wrong - apt-get does not exist on Windows
steps:
  - run: apt-get install -y curl

# Correct - use platform-specific approach
steps:
  - shell: bash
    run: echo "Platform: $RUNNER_OS"
```
"""),

    # =========================================================================
    # 3. CHECKOUT/CLONE ERRORS
    # =========================================================================
    md("GitHub Actions Checkout Action Failed",
       "Fix GitHub Actions actions/checkout failures during workflow execution.",
       """## Error Description

Checkout failures occur when the `actions/checkout` step fails:

```
Error: fatal: could not create leading directories: No such file or directory
```

## Common Causes

- Repository is large and checkout times out.
- Permissions insufficient for the repository.
- Submodules or LFS are not configured.

## How to Fix

**Shallow clone for faster checkout:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 1
```

**Fetch all branches and tags:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
      fetch-tags: true
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 1
      lfs: true
      submodules: recursive
```
"""),

    md("GitHub Actions Git Fetch Depth Error",
       "Fix GitHub Actions git fetch depth errors when commit history is insufficient.",
       """## Error Description

Fetch depth errors occur when the shallow clone does not include enough commit history:

```
Error: detached HEAD; you are on branch 'main' but your commit
does not have enough history
```

## Common Causes

- Default `fetch-depth: 1` only fetches the latest commit.
- Steps that need `git log` or diff comparison require more depth.

## How to Fix

**Increase fetch depth:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 10
```

**Fetch full history:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
      fetch-tags: true
```
"""),

    md("GitHub Actions LFS Not Installed Error",
       "Fix GitHub Actions LFS not installed errors when working with Git LFS files.",
       """## Error Description

LFS errors occur when the runner does not have Git LFS installed or configured:

```
Error: This repository is configured for Git LFS but 'git-lfs' was not found
```

## Common Causes

- Git LFS is not pre-installed on the runner.
- `actions/checkout` does not have `lfs: true` set.

## How to Fix

**Enable LFS in checkout:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      lfs: true
```

**Install LFS manually:**

```yaml
steps:
  - name: Install Git LFS
    run: |
      sudo apt-get update
      sudo apt-get install -y git-lfs
      git lfs install
  - uses: actions/checkout@v4
    with:
      lfs: true
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      lfs: true
  - run: git lfs ls-files
```
"""),

    md("GitHub Actions Submodule Not Found Error",
       "Fix GitHub Actions submodule not found errors during checkout.",
       """## Error Description

Submodule errors occur when submodules are not initialized during checkout:

```
Error: warning: failed to load submodule 'vendor/lib'
fatal: could not find remote ref refs/heads/main
```

## Common Causes

- Submodules not configured in the checkout step.
- Submodule URL uses SSH and no SSH key is available.

## How to Fix

**Checkout with submodules:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      submodules: recursive
      token: ${{ secrets.GITHUB_TOKEN }}
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      submodules: true
      fetch-depth: 0
```
"""),

    md("GitHub Actions Token Not Available For Checkout",
       "Fix GitHub Actions token not available errors during repository checkout.",
       """## Error Description

Token errors occur when checkout requires authentication but the token is missing:

```
Error: fatal: unable to access 'https://github.com/private-org/repo.git/':
The requested URL returned error: 403
```

## Common Causes

- Default `GITHUB_TOKEN` does not have sufficient permissions.
- Checking out a different private repository.

## How to Fix

**Use a PAT or GitHub App token for cross-repo checkout:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      repository: private-org/private-repo
      token: ${{ secrets.PAT_TOKEN }}
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      token: ${{ secrets.PAT_TOKEN }}
      fetch-depth: 0
```
"""),

    md("GitHub Actions Sparse Checkout Error",
       "Fix GitHub Actions sparse checkout configuration errors.",
       """## Error Description

Sparse checkout errors occur when the sparse-checkout configuration is invalid:

```
Error: fatal: invalid path 'src/index.ts' from sparse checkout
```

## Common Causes

- Incorrect path patterns in sparse-checkout.
- Trying to checkout a path that does not exist.

## How to Fix

**Configure sparse checkout properly:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      sparse-checkout: |
        src/
        package.json
      sparse-checkout-cone-mode: false
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      sparse-checkout: |
        packages/core
        packages/utils
      sparse-checkout-cone-mode: true
```
"""),

    md("GitHub Actions Ref Not Found Error",
       "Fix GitHub Actions ref not found errors when the specified branch or tag does not exist.",
       """## Error Description

Ref not found errors occur when the specified branch, tag, or commit does not exist:

```
Error: fatal: Remote branch release/v2 not found in upstream origin
```

## Common Causes

- Branch or tag was deleted.
- Typo in the ref name.

## How to Fix

**Use fallback ref:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      ref: ${{ github.head_ref || github.ref_name }}
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      ref: main
      fetch-depth: 0
```
"""),

    md("GitHub Actions Repository Not Found Error",
       "Fix GitHub Actions repository not found errors during checkout.",
       """## Error Description

Repository not found errors occur when trying to access a repository that does not exist or is inaccessible:

```
Error: fatal: repository 'https://github.com/org/missing-repo.git/' not found
```

## Common Causes

- Repository name is incorrect.
- Repository was deleted or renamed.
- Repository is private and token lacks access.

## How to Fix

**Verify the repository exists:**

```bash
gh repo view {owner}/{repo} --json name,visibility
```

**Ensure token has repo access:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      repository: owner/repo
      token: ${{ secrets.CROSS_REPO_TOKEN }}
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      repository: owner/repo
```
"""),

    md("GitHub Actions Checkout Insufficient Permissions",
       "Fix GitHub Actions checkout insufficient permissions errors.",
       """## Error Description

Insufficient permissions errors occur when the token cannot access the repository:

```
Error: Permission denied to repository
fatal: unable to access: The requested URL returned error: 403
```

## Common Causes

- Repository permissions are restricted.
- `GITHUB_TOKEN` lacks required scopes.

## How to Fix

**Set required permissions in workflow:**

```yaml
permissions:
  contents: read
  packages: read

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
permissions:
  contents: read
  issues: write
  pull-requests: write
```
"""),

    md("GitHub Actions HEAD Detached Error",
       "Fix GitHub Actions HEAD detached errors during workflow checkout.",
       """## Error Description

HEAD detached errors occur when the checkout results in a detached HEAD state:

```
Warning: You are in 'detached HEAD' state
```

## Common Causes

- Checking out a specific commit SHA instead of a branch.
- Fetch-depth too shallow for the target ref.

## How to Fix

**Checkout the branch explicitly:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      ref: ${{ github.head_ref }}
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      ref: ${{ github.event.pull_request.head.ref }}
      fetch-depth: 0
```
"""),

    md("GitHub Actions Merge Conflict During Checkout",
       "Fix GitHub Actions merge conflict errors during checkout in CI.",
       """## Error Description

Merge conflict errors occur when automatic merge during checkout fails:

```
error: Your local changes to the following files would be overwritten
Merge failed; fix conflicts and then commit the result.
```

## Common Causes

- Concurrent workflow runs modifying the same branch.
- Auto-merge feature attempted to merge conflicting changes.

## How to Fix

**Check for conflicts before running:**

```bash
git fetch origin main
git merge --no-commit --no-ff origin/main || {
  echo "Merge conflict detected"
  exit 1
}
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
  - name: Check for merge conflicts
    run: |
      git fetch origin ${{ github.base_ref }}
      git merge-tree $(git merge-base HEAD origin/${{ github.base_ref }}) HEAD origin/${{ github.base_ref }}
```
"""),

    md("GitHub Actions Rebase Error During Workflow",
       "Fix GitHub Actions rebase errors during workflow execution.",
       """## Error Description

Rebase errors occur when a rebase operation in the workflow fails:

```
error: cannot rebase: You have unstaged changes in your working directory
```

## Common Causes

- Uncommitted changes exist before rebase.
- Conflicts during interactive rebase.

## How to Fix

**Stash changes before rebase:**

```yaml
steps:
  - uses: actions/checkout@v4
  - name: Rebase
    run: |
      git config user.name "github-actions"
      git config user.email "github-actions@github.com"
      git fetch origin main
      git rebase origin/main
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
  - name: Rebase
    run: |
      git rebase origin/main || git rebase --abort
```
"""),

    md("GitHub Actions Tag Checkout Failed",
       "Fix GitHub Actions tag checkout failures during workflow execution.",
       """## Error Description

Tag checkout failures occur when the workflow cannot checkout a specific tag:

```
error: pathspec 'v1.0.0' did not match any(s) known to git
```

## Common Causes

- Tag does not exist in the repository.
- Tags were not fetched (shallow clone).

## How to Fix

**Fetch tags explicitly:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
      fetch-tags: true
      ref: v1.0.0
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
  - name: Checkout tag
    run: |
      git tag -l | head -20
      git checkout v1.0.0
```
"""),

    # =========================================================================
    # 4. BUILD/TEST ERRORS
    # =========================================================================
    md("GitHub Actions NPM CI Failed",
       "Fix GitHub Actions npm ci failures during Node.js workflow.",
       """## Error Description

npm ci failures occur during the dependency installation step:

```
Error: npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree
```

## Common Causes

- Dependency version conflicts in package-lock.json.
- Node.js version incompatible with some dependencies.
- Corrupted or stale package-lock.json.

## How to Fix

**Ensure Node.js version matches:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci
```

**Fix dependency conflicts:**

```bash
npm install --legacy-peer-deps
```

## Examples

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci --prefer-offline
  - run: npm run build
  - run: npm test
```
"""),

    md("GitHub Actions NPM Run Build Error",
       "Fix GitHub Actions npm run build failures in CI workflow.",
       """## Error Description

Build errors occur when `npm run build` fails in the workflow:

```
Error: Build failed with 2 errors
src/index.ts(1,20): error TS2307: Cannot find module 'lodash'
```

## Common Causes

- Dependencies not installed before build.
- TypeScript compilation errors.
- Missing environment variables needed at build time.

## How to Fix

**Set build environment variables:**

```yaml
env:
  NODE_OPTIONS: "--max-old-space-size=4096"
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci
  - run: npm run build
```

## Examples

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
  - run: npm ci
  - run: npm run build
    env:
      NODE_OPTIONS: "--max-old-space-size=4096"
```
"""),

    md("GitHub Actions Pip Install Failed",
       "Fix GitHub Actions pip install failures in Python workflow.",
       """## Error Description

pip install failures occur during Python dependency installation:

```
Error: ERROR: Could not find a version that satisfies the requirement
django>=4.2 (from -r requirements.txt)
```

## Common Causes

- Package version not available for the Python version.
- Missing system dependencies (e.g., C extensions).

## How to Fix

**Use proper Python setup:**

```yaml
steps:
  - uses: actions/setup-python@v5
    with:
      python-version: '3.11'
      cache: 'pip'
  - run: pip install -r requirements.txt
```

## Examples

```yaml
steps:
  - uses: actions/setup-python@v5
    with:
      python-version: '3.11'
      cache: 'pip'
  - run: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
```
"""),

    md("GitHub Actions Yarn Install Error",
       "Fix GitHub Actions yarn install failures in CI workflow.",
       """## Error Description

Yarn install errors occur when dependencies cannot be installed:

```
error An unexpected error occurred: "EACCES: permission denied"
```

## Common Causes

- Yarn lock file out of sync with package.json.
- Permission issues with node_modules.

## How to Fix

**Use proper Yarn setup:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'yarn'
  - run: yarn install --frozen-lockfile
```

## Examples

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'yarn'
  - run: yarn install --frozen-lockfile
  - run: yarn build
  - run: yarn test
```
"""),

    md("GitHub Actions Go Build Failed",
       "Fix GitHub Actions Go build failures in CI workflow.",
       """## Error Description

Go build failures occur during Go compilation in the workflow:

```
Error: ./main.go:10:2: cannot find package "github.com/example/pkg"
```

## Common Causes

- Go modules not properly initialized.
- go.sum file is out of date.
- Go version mismatch.

## How to Fix

**Set up Go properly:**

```yaml
steps:
  - uses: actions/setup-go@v5
    with:
      go-version: '1.21'
      cache: true
  - run: go mod download
  - run: go build ./...
```

## Examples

```yaml
steps:
  - uses: actions/setup-go@v5
    with:
      go-version: '1.21'
      cache: true
  - run: go vet ./...
  - run: go build -o bin/app ./cmd/app
```
"""),

    md("GitHub Actions Cargo Build Error",
       "Fix GitHub Actions cargo build failures in Rust workflow.",
       """## Error Description

Cargo build errors occur during Rust compilation in the workflow:

```
error[E0433]: failed to resolve: use of undeclared crate or module
```

## Common Causes

- Missing Rust toolchain setup.
- Dependencies not downloaded.
- Missing system libraries for native crates.

## How to Fix

**Set up Rust properly:**

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: dtolnay/rust-toolchain@stable
  - uses: Swatinem/rust-cache@v2
  - run: cargo build --release
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: dtolnay/rust-toolchain@stable
    with:
      components: clippy, rustfmt
  - uses: Swatinem/rust-cache@v2
  - run: cargo clippy -- -D warnings
```
"""),

    md("GitHub Actions DotNet Build Failed",
       "Fix GitHub Actions .NET build failures in CI workflow.",
       """## Error Description

dotnet build failures occur during .NET compilation:

```
Error: error CS0246: The type or namespace name 'Serilog' could not be found
```

## Common Causes

- .NET SDK version mismatch.
- NuGet package restore failed.

## How to Fix

**Set up .NET properly:**

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-dotnet@v4
    with:
      dotnet-version: '8.0.x'
  - run: dotnet restore
  - run: dotnet build --no-restore
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-dotnet@v4
    with:
      dotnet-version: '8.0.x'
      cache: true
  - run: dotnet restore
  - run: dotnet build --configuration Release
```
"""),

    md("GitHub Actions Test Runner Exit Code 1",
       "Fix GitHub Actions test runner exit code 1 failures.",
       """## Error Description

Test runner failures return exit code 1, indicating test failures:

```
Error: Process completed with exit code 1.
FAIL src/__tests__/auth.test.ts (12.345 s)
```

## Common Causes

- Test assertions failing.
- Flaky tests due to timing or network issues.
- Missing test environment configuration.

## How to Fix

**Configure test environment:**

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
        ports:
          - 5432:5432
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
        env:
          DATABASE_URL: postgres://postgres:test@localhost:5432/test
```

## Examples

```yaml
steps:
  - run: npm test -- --reporter=junit --output-reporter=test-results.xml
  - uses: actions/upload-artifact@v4
    if: failure()
    with:
      name: test-results
      path: test-results.xml
```
"""),

    md("GitHub Actions Coverage Report Not Found",
       "Fix GitHub Actions coverage report not found errors after tests.",
       """## Error Description

Coverage report errors occur when the expected coverage file is not generated:

```
Error: No coverage report found at ./coverage/lcov.info
```

## Common Causes

- Test command does not generate coverage.
- Wrong path for coverage report.

## How to Fix

**Configure coverage in your test command:**

```yaml
steps:
  - run: npm test -- --coverage --coverageReporters=lcov
  - uses: codecov/codecov-action@v4
    with:
      files: ./coverage/lcov.info
```

## Examples

```yaml
steps:
  - run: pytest --cov=src --cov-report=xml
  - uses: codecov/codecov-action@v4
    with:
      files: coverage.xml
```
"""),

    md("GitHub Actions Pytest Failure",
       "Fix GitHub Actions pytest failure errors in Python workflow.",
       """## Error Description

Pytest failures occur when Python tests fail:

```
FAILED tests/test_app.py::test_login - AssertionError
===== 1 failed, 42 passed in 0.5s =====
```

## Common Causes

- Test assertions failing.
- Missing test fixtures or setup.
- Database not available.

## How to Fix

**Run pytest with proper configuration:**

```yaml
steps:
  - uses: actions/setup-python@v5
    with:
      python-version: '3.11'
      cache: 'pip'
  - run: pip install -r requirements.txt
  - run: pytest --tb=short --junitxml=results.xml
```

## Examples

```yaml
steps:
  - run: pytest -v --tb=short -x
    env:
      DATABASE_URL: postgres://user:pass@localhost/test
```
"""),

    md("GitHub Actions Jest Failure",
       "Fix GitHub Actions Jest test failure errors.",
       """## Error Description

Jest failures occur when JavaScript/TypeScript tests fail:

```
FAIL src/__tests__/api.test.js
  GET /api/users should return 200
    expect(received).toBe(expected)
```

## Common Causes

- Async operations not properly awaited.
- Mock setup issues.
- Flaky tests due to timing.

## How to Fix

**Run Jest with CI-specific options:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci
  - run: npx jest --ci --forceExit --detectOpenHandles
```

## Examples

```yaml
steps:
  - run: npx jest --ci --coverage --forceExit
  - uses: actions/upload-artifact@v4
    if: failure()
    with:
      name: jest-screenshots
      path: coverage/
```
"""),

    md("GitHub Actions ESLint Error",
       "Fix GitHub Actions ESLint errors in CI workflow.",
       """## Error Description

ESLint errors cause CI failures when code does not pass linting:

```
Error: src/index.ts
  10:5  error  Unexpected any  @typescript-eslint/no-explicit-any
```

## Common Causes

- New lint rules added to the project.
- Code pushed without running linter locally.

## How to Fix

**Run ESLint in the workflow:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci
  - run: npx eslint . --ext .ts,.js
```

## Examples

```yaml
steps:
  - run: npx eslint . --max-warnings=0
  - run: npx prettier --check .
```
"""),

    md("GitHub Actions Prettier Check Failed",
       "Fix GitHub Actions Prettier formatting check failures.",
       """## Error Description

Prettier check failures occur when code formatting does not match standards:

```
Error: [warn] src/index.ts
Code style issues found in the above file(s). Forgot to run Prettier?
```

## Common Causes

- Code committed without running Prettier.
- Prettier version differs between local and CI.

## How to Fix

**Run Prettier check in CI:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci
  - run: npx prettier --check .
```

## Examples

```yaml
steps:
  - run: npx prettier --check "src/**/*.{ts,tsx,js,jsx,json,css,md}"
```
"""),

    md("GitHub Actions Husky Git Hook Error",
       "Fix GitHub Actions Husky git hook errors in CI.",
       """## Error Description

Husky errors occur when git hooks interfere with CI operations:

```
Error: husky - .git/husky/pre-commit command not found
```

## Common Causes

- Husky hooks not disabled in CI.
- Hook script references local tools not installed.

## How to Fix

**Disable Husky in CI:**

```yaml
env:
  HUSKY: 0
steps:
  - uses: actions/checkout@v4
  - run: npm ci
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
  - run: npm ci
    env:
      HUSKY: 0
```
"""),

    # =========================================================================
    # 5. CACHE ERRORS
    # =========================================================================
    md("GitHub Actions Cache Failed",
       "Fix GitHub Actions actions/cache failures in workflow.",
       """## Error Description

Cache action failures occur when `actions/cache` cannot save or restore:

```
Error: Cache not found for key: Linux-npm-abc123
```

## Common Causes

- Cache key does not match any existing cache.
- Cache size exceeds the 10GB limit.
- Network issues during cache upload.

## How to Fix

**Use setup actions with built-in caching:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
```

**Add cache with fallback:**

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-
```

## Examples

```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.npm
      node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```
"""),

    md("GitHub Actions Cache Not Found",
       "Fix GitHub Actions cache not found warnings during restore.",
       """## Error Description

Cache not found warnings occur when no existing cache matches the key:

```
Warning: Cache not found for key: Linux-npm-abc123
```

## Common Causes

- First run of the workflow (no cache exists yet).
- Cache key changed due to lock file update.
- Cache expired (90-day retention limit).

## How to Fix

**Use restore-keys for fallback:**

```yaml
- uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

## Examples

```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.cache/pip
      node_modules
    key: ${{ runner.os }}-${{ hashFiles('**/requirements.txt') }}-${{ hashFiles('**/package-lock.json') }}
```
"""),

    md("GitHub Actions Cache Hit Miss Logic Error",
       "Fix GitHub Actions cache hit/miss logic errors in workflow.",
       """## Error Description

Cache hit/miss logic errors occur when the workflow does not handle cache states correctly:

```
Warning: cache-hit was expected but not found
```

## Common Causes

- Workflow expects cache hit but key does not match.
- Conditional steps based on cache-hit use incorrect syntax.

## How to Fix

**Properly handle cache-hit output:**

```yaml
- uses: actions/cache@v4
  id: cache-deps
  with:
    path: node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}

- run: npm ci
  if: steps.cache-deps.outputs.cache-hit != 'true'

- run: npm run build
```

## Examples

```yaml
steps:
  - uses: actions/cache@v4
    id: cache
    with:
      path: ~/.cache/go-build
      key: ${{ runner.os }}-go-${{ hashFiles('**/go.sum') }}

  - run: go build ./...
```
"""),

    md("GitHub Actions Cache Key Not Matching",
       "Fix GitHub Actions cache key mismatch issues.",
       """## Error Description

Cache key not matching errors occur when the computed key does not match any stored cache:

```
Cache key mismatch: expected 'Linux-npm-abc123', found none
```

## Common Causes

- Hash of lock file changed.
- Operating system label changed.
- Cache key format inconsistent across runs.

## How to Fix

**Use a stable cache key format:**

```yaml
- uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

## Examples

```yaml
key: ${{ runner.os }}-node-${{ matrix.node-version }}-${{ hashFiles('**/package-lock.json') }}
```
"""),

    md("GitHub Actions Restore Key Failed",
       "Fix GitHub Actions restore-keys fallback failures.",
       """## Error Description

Restore key failures occur when no fallback keys match any cached data:

```
Warning: Failed to restore cache for key: Linux-npm-
```

## Common Causes

- No cache exists for any matching prefix.
- Cache was evicted due to storage limits.

## How to Fix

**Use broader restore keys:**

```yaml
- uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-
      ${{ runner.os }}-
```

## Examples

```yaml
restore-keys: |
  Linux-npm-1.2.3
  Linux-npm-
  Linux-
```
"""),

    md("GitHub Actions Save Cache Failed",
       "Fix GitHub Actions save cache failures after job completion.",
       """## Error Description

Save cache failures occur when the cache action cannot write the cache:

```
Warning: Failed to save cache: unable to create cache
```

## Common Causes

- Cache size exceeds the 10 GB limit.
- Network issues during upload.

## How to Fix

**Reduce cache size:**

```yaml
steps:
  - name: Prune before caching
    run: |
      rm -rf node_modules/.cache
      npm prune
  - uses: actions/cache@v4
    with:
      path: node_modules
      key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

## Examples

```yaml
# Cache only the npm global store
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```
"""),

    md("GitHub Actions Cache Size Limit Exceeded",
       "Fix GitHub Actions cache size limit exceeded errors.",
       """## Error Description

Cache size limit errors occur when the total cached data exceeds GitHub's limit:

```
Error: Cache size of 11.5 GB exceeds the maximum cache size of 10 GB
```

## Common Causes

- Large node_modules directory.
- Multiple large cache entries across workflows.

## How to Fix

**Prune unnecessary files before caching:**

```yaml
steps:
  - name: Clean before cache
    run: |
      rm -rf node_modules/.cache
      rm -rf .next/cache
  - uses: actions/cache@v4
    with:
      path: node_modules
      key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

## Examples

```yaml
- uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```
"""),

    md("GitHub Actions Cache Path Not Found",
       "Fix GitHub Actions cache path not found errors.",
       """## Error Description

Cache path not found errors occur when the specified cache path does not exist:

```
Warning: Path to cache does not exist: ./node_modules
```

## Common Causes

- Dependencies not installed before caching.
- Incorrect path in the cache configuration.

## How to Fix

**Ensure path exists before caching:**

```yaml
steps:
  - uses: actions/checkout@v4
  - run: npm ci
  - uses: actions/cache@v4
    with:
      path: node_modules
      key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

## Examples

```yaml
- run: ls -la node_modules || echo "node_modules not found"
```
"""),

    md("GitHub Actions Cache Upload Rejected",
       "Fix GitHub Actions cache upload rejected errors during save.",
       """## Error Description

Cache upload rejected errors occur when the cache service rejects the upload:

```
Error: Cache upload failed: 413 Request Entity Too Large
```

## Common Causes

- Individual cache entry too large.
- Rate limiting from cache service.

## How to Fix

**Split large caches into smaller entries:**

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}

- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
```

## Examples

```yaml
- uses: actions/cache@v4
  continue-on-error: true
  with:
    path: ~/.cache
    key: build-${{ github.sha }}
```
"""),

    md("GitHub Actions Cross-Branch Cache Not Available",
       "Fix GitHub Actions cross-branch cache scope limitations.",
       """## Error Description

Cross-branch cache limitations prevent workflows from accessing caches from other branches:

```
Warning: Cache not found for key from branch: feature-x
```

## Common Causes

- Default cache scope is limited to the current branch.
- PR from a fork cannot access the base branch cache.

## How to Fix

**Use cache from the default branch:**

```yaml
env:
  CACHE_KEY_PREFIX: ${{ github.ref == 'refs/heads/main' && 'main' || 'pr' }}
steps:
  - uses: actions/cache@v4
    with:
      path: node_modules
      key: ${{ runner.os }}-npm-${{ env.CACHE_KEY_PREFIX }}-${{ hashFiles('**/package-lock.json') }}
      restore-keys: |
        ${{ runner.os }}-npm-main-
```

## Examples

```yaml
# Use base branch for PRs
- uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-${{ github.base_ref }}-
```
"""),

    md("GitHub Actions Restore Keys Pattern Error",
       "Fix GitHub Actions restore-keys pattern matching errors.",
       """## Error Description

Restore keys pattern errors occur when restore-keys patterns do not match correctly:

```
Warning: No cache found for restore-keys: ['Linux-npm-', 'Linux-']
```

## Common Causes

- restore-keys prefix does not match actual cache key format.
- Case sensitivity in key names.

## How to Fix

**Verify cache key structure:**

```yaml
- uses: actions/cache@v4
  id: cache
  with:
    path: node_modules
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-
```

## Examples

```yaml
key: Linux-npm-abc123
restore-keys: |
  Linux-npm-
  Linux-
```
"""),

    md("GitHub Actions Dependencies Hash Mismatch",
       "Fix GitHub Actions cache hash mismatch issues in dependency caching.",
       """## Error Description

Hash mismatch errors occur when the lock file hash changes unexpectedly:

```
Warning: Cache key hash mismatch - expected abc123, got def456
```

## Common Causes

- Lock file regenerated between cache save and restore.
- Different package manager versions producing different hashes.

## How to Fix

**Ensure consistent lock file generation:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci
```

## Examples

```yaml
key: ${{ runner.os }}-npm-${{ hashFiles('package-lock.json') }}
```
"""),

    # =========================================================================
    # 6. SECRETS/ENVIRONMENT ERRORS
    # =========================================================================
    md("GitHub Actions Secrets Not Available In Forked PR",
       "Fix GitHub Actions secrets not available in forked PR workflows.",
       """## Error Description

Secrets are not available in workflows triggered by forked PRs:

```
Error: The secret 'DEPLOY_TOKEN' is not available
Forked workflows do not have access to repository secrets
```

## Common Causes

- Security feature: secrets are not exposed to forked PRs.
- Workflow expects secrets but trigger is a pull_request from a fork.

## How to Fix

**Use pull_request_target for fork PRs:**

```yaml
on:
  pull_request_target:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha }}
```

## Examples

```yaml
steps:
  - name: Check secrets
    id: check
    run: |
      if [ -n "${{ secrets.DEPLOY_TOKEN }}" ]; then
        echo "has_secret=true" >> $GITHUB_OUTPUT
      else
        echo "has_secret=false" >> $GITHUB_OUTPUT
      fi
```
"""),

    md("GitHub Actions Secret Not Set In Environment",
       "Fix GitHub Actions secret not set errors in environment protection rules.",
       """## Error Description

Secrets may not be available when environment protection rules block deployment:

```
Error: Environment 'production' protection rule failed
```

## Common Causes

- Environment requires manual approval.
- Required reviewers have not approved.

## How to Fix

**Configure environment in the job:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://example.com
    steps:
      - uses: actions/checkout@v4
      - name: Deploy
        run: deploy.sh
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

## Examples

```yaml
environment:
  name: production
  url: https://example.com
```
"""),

    md("GitHub Actions Context Error Accessing Secrets",
       "Fix GitHub Actions context errors when accessing secrets in expressions.",
       """## Error Description

Context errors occur when secrets are referenced incorrectly:

```
Error: Invalid context access: 'secrets.UNDEFINED_SECRET'
```

## Common Causes

- Secret name does not exist in the repository.
- Typo in secret name (case-sensitive).

## How to Fix

**Verify the secret exists:**

```bash
gh secret list
```

**Use correct context syntax:**

```yaml
steps:
  - name: Deploy
    env:
      API_KEY: ${{ secrets.API_KEY }}
    run: echo "Using API key"
```

## Examples

```yaml
env:
  MY_SECRET: ${{ secrets.MY_SECRET }}
```
"""),

    md("GitHub Actions GITHUB_TOKEN Not Available",
       "Fix GitHub Actions GITHUB_TOKEN not available errors.",
       """## Error Description

GITHUB_TOKEN not available errors occur when the default token is missing or restricted:

```
Error: HttpError: Not Found
Resource not accessible by integration
```

## Common Causes

- Token does not have sufficient permissions for the operation.
- Workflow does not have `permissions` configured.

## How to Fix

**Set explicit permissions:**

```yaml
permissions:
  contents: read
  issues: write
  pull-requests: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
permissions:
  contents: read
  packages: write
  issues: write
```
"""),

    md("GitHub Actions PAT Not Configured",
       "Fix GitHub Actions personal access token not configured errors.",
       """## Error Description

PAT errors occur when a workflow requires a personal access token but it is not set:

```
Error: HttpError: Not Found
Resource not accessible by personal access token
```

## Common Causes

- PAT not added as a repository secret.
- PAT has expired.
- PAT lacks required scopes.

## How to Fix

**Create and store a PAT:**

```bash
gh secret set PAT_TOKEN --body "ghp_xxxxxxxxxxxx"
```

**Use PAT in workflow:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      token: ${{ secrets.PAT_TOKEN }}
      fetch-depth: 0
```

## Examples

```yaml
# Required scopes for common operations
# repo - Full repository access
# workflow - Update workflows
```
"""),

    md("GitHub Actions Environment Protection Rule Error",
       "Fix GitHub Actions environment protection rule failures.",
       """## Error Description

Environment protection rule errors occur when deployment requires manual approval:

```
Error: Deployment blocked: protection rule for environment 'production' failed
```

## Common Causes

- Required reviewers have not approved.
- Wait timer not elapsed.
- Branch policy not satisfied.

## How to Fix

**Configure environment protection rules:**

Go to repository Settings > Environments > production and configure:
- Required reviewers
- Wait timer
- Deployment branches

## Examples

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - run: deploy.sh
```
"""),

    md("GitHub Actions Required Reviewers Not Approved",
       "Fix GitHub Actions required reviewers approval errors.",
       """## Error Description

Required reviewers not approved errors block deployment:

```
Error: Waiting for required reviewers to approve deployment
```

## Common Causes

- No reviewers have approved the deployment.
- Reviewers are unavailable.

## How to Fix

**Wait for manual approval:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
jobs:
  deploy:
    environment:
      name: production
```
"""),

    md("GitHub Actions Environment Variable Not Set",
       "Fix GitHub Actions environment variable not set errors.",
       """## Error Description

Environment variable not set errors occur when the workflow references undefined env vars:

```
Error: $MY_VAR: unbound variable
```

## Common Causes

- Variable not defined in workflow, job, or step level.
- Variable set in wrong scope.
- Variable name typo.

## How to Fix

**Define env vars at the appropriate level:**

```yaml
env:
  GLOBAL_VAR: "value"

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      JOB_VAR: "job-value"
    steps:
      - run: echo $GLOBAL_VAR $JOB_VAR
        env:
          STEP_VAR: "step-value"
```

## Examples

```yaml
env:
  NODE_ENV: production

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo $NODE_ENV
```
"""),

    md("GitHub Actions Encrypted Secret Too Long",
       "Fix GitHub Actions encrypted secret value too long errors.",
       """## Error Description

Encrypted secret too long errors occur when a secret value exceeds the size limit:

```
Error: Secret value exceeds maximum length of 48KB
```

## Common Causes

- Secret contains a large certificate or key.
- Secret value includes excessive whitespace or newlines.

## How to Fix

**Split large secrets:**

```yaml
steps:
  - name: Setup certs
    run: |
      echo "${{ secrets.CERT_PART1 }}" > cert1.pem
      echo "${{ secrets.CERT_PART2 }}" > cert2.pem
      cat cert1.pem cert2.pem > cert.pem
```

## Examples

```yaml
env:
  CERT_B64: ${{ secrets.CERT_BASE64 }}
steps:
  - run: echo "$CERT_B64" | base64 -d > cert.pem
```
"""),

    md("GitHub Actions Secret Name Invalid",
       "Fix GitHub Actions secret name invalid errors when storing or referencing secrets.",
       """## Error Description

Secret name invalid errors occur when the secret name contains invalid characters:

```
Error: Secret name 'MY-SECRET_NAME' is not valid
```

## Common Causes

- Secret name contains spaces or special characters.
- Secret name starts with GITHUB_ (reserved prefix).

## How to Fix

**Use valid secret names:**

```bash
gh secret set MY_SECRET_NAME --body "value"
```

## Examples

```bash
# Valid secret names
API_KEY
DATABASE_URL
DEPLOY_TOKEN_2024

# Invalid names
MY SECRET (space)
MY-SECRET (hyphen)
GITHUB_TOKEN (reserved)
```
"""),

    # =========================================================================
    # 7. DEPLOYMENT ERRORS
    # =========================================================================
    md("GitHub Actions Deployment Failed",
       "Fix GitHub Actions deployment failures in CI/CD pipeline.",
       """## Error Description

Deployment failures occur when the deployment step fails:

```
Error: Deployment failed: exit code 127
Command not found: deploy.sh
```

## Common Causes

- Deploy script does not exist or is not executable.
- Missing credentials for deployment target.

## How to Fix

**Ensure deploy script is executable:**

```yaml
steps:
  - uses: actions/checkout@v4
  - run: chmod +x deploy.sh
  - run: ./deploy.sh
    env:
      DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

## Examples

```yaml
steps:
  - name: Deploy
    uses: peaceiris/actions-gh-pages@v3
    with:
      github_token: ${{ secrets.GITHUB_TOKEN }}
      publish_dir: ./dist
```
"""),

    md("GitHub Actions Environment Not Found",
       "Fix GitHub Actions environment not found errors.",
       """## Error Description

Environment not found errors occur when the workflow references a non-existent environment:

```
Error: Environment 'staging' not found in repository
```

## Common Causes

- Environment was not created in repository settings.
- Typo in environment name.

## How to Fix

**Create the environment:**

```bash
gh api repos/{owner}/{repo}/environments -f name=staging
```

## Examples

```yaml
jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    environment: staging
  deploy-production:
    runs-on: ubuntu-latest
    environment: production
    needs: deploy-staging
```
"""),

    md("GitHub Actions Environment Protection Active",
       "Fix GitHub Actions environment protection rules blocking deployments.",
       """## Error Description

Environment protection rules can block deployments when not satisfied:

```
Error: Deployment blocked by environment protection rules
```

## Common Causes

- Required reviewers not configured or not approved.
- Wait timer not elapsed.
- Restricted to certain branches only.

## How to Fix

**Check environment settings:**

```bash
gh api repos/{owner}/{repo}/environments/production
```

## Examples

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://example.com
    steps:
      - uses: actions/checkout@v4
```
"""),

    md("GitHub Actions Deployment Branch Mismatch",
       "Fix GitHub Actions deployment branch policy mismatch errors.",
       """## Error Description

Branch mismatch errors occur when the deployment branch does not match environment policies:

```
Error: Branch 'feature-x' is not allowed to deploy to 'production'
```

## Common Causes

- Environment restricted to specific branches (e.g., main only).
- Deployment triggered from a non-allowed branch.

## How to Fix

**Configure branch policy:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
jobs:
  deploy:
    if: github.ref == 'refs/heads/main'
    environment: production
```
"""),

    md("GitHub Actions Waiting On Deployment",
       "Fix GitHub Actions deployment waiting status errors.",
       """## Error Description

Deployment waiting errors occur when the workflow is stuck waiting for approval:

```
Error: Deployment is waiting for environment protection rules
```

## Common Causes

- Required reviewers have not acted on the deployment request.

## How to Fix

**Set deployment timeout:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
- name: Check deployment
  run: |
    gh api repos/{owner}/{repo}/actions/runs/${{ github.run_id }}/deployments | jq '.[].environment'
```
"""),

    md("GitHub Actions Deployment Rejected",
       "Fix GitHub Actions deployment rejected by environment protection.",
       """## Error Description

Deployment rejected errors occur when the environment protection rules reject the deployment:

```
Error: Deployment rejected by required reviewer
```

## Common Causes

- Reviewer explicitly rejected the deployment.
- Deployment does not meet required criteria.

## How to Fix

**Re-run the deployment:**

```yaml
steps:
  - name: Report status
    if: failure()
    run: |
      gh pr comment ${{ github.event.pull_request.number }} \
        --body "Deployment was rejected. Please review environment protection rules."
```

## Examples

```yaml
steps:
  - name: Retry deployment
    run: |
      gh api repos/{owner}/{repo}/actions/runs/${{ github.run_id }}/deployment-faults
```
"""),

    md("GitHub Actions Job Timeout",
       "Fix GitHub Actions job timeout exceeded errors.",
       """## Error Description

Job timeout errors occur when a job exceeds the default 6-hour timeout:

```
Error: The job running on runner has exceeded the maximum execution time
```

## Common Causes

- Long-running test suite.
- Infinite loop in workflow script.
- Network timeout causing hang.

## How to Fix

**Set explicit timeout:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
```

## Examples

```yaml
# Default is 360 minutes (6 hours)
jobs:
  test:
    timeout-minutes: 60
```
"""),

    md("GitHub Actions Deployment Status Check Failed",
       "Fix GitHub Actions deployment status check failures.",
       """## Error Description

Deployment status check errors occur when status checks fail during deployment:

```
Error: Required status check 'deploy/production' is not successful
```

## Common Causes

- Required status check was not triggered.
- Deployment workflow failed.

## How to Fix

**Ensure deployment job has correct name:**

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - run: deploy.sh
```

## Examples

```yaml
# Configure branch protection with status checks
# Settings > Branches > Branch protection rules > Require status checks
```
"""),

    md("GitHub Actions Required Status Check Failed",
       "Fix GitHub Actions required status check failures blocking merge.",
       """## Error Description

Required status check failures prevent PR merging:

```
Error: 1 required status check is expected: build
```

## Common Causes

- CI workflow failed.
- Status check not triggered (e.g., wrong event type).

## How to Fix

**Ensure CI runs on pull_request:**

```yaml
on:
  pull_request:
    branches: [main]
```

## Examples

```yaml
on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
```
"""),

    md("GitHub Actions Merge Queue Error",
       "Fix GitHub Actions merge queue configuration errors.",
       """## Error Description

Merge queue errors occur when the merge queue is not properly configured:

```
Error: Merge queue is not enabled for this repository
```

## Common Causes

- Merge queue not enabled in repository settings.
- Workflow does not support merge queue events.

## How to Fix

**Add merge_group event to workflow:**

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  merge_group:
```

## Examples

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  merge_group:
    types: [checks-requested]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```
"""),

    md("GitHub Actions Staging Production Mismatch",
       "Fix GitHub Actions staging/production environment mismatch errors.",
       """## Error Description

Staging/production mismatch errors occur when deployments to different environments conflict:

```
Error: Environment 'production' deployment differs from 'staging'
```

## Common Causes

- Different versions deployed to staging vs production.
- Configuration drift between environments.

## How to Fix

**Use consistent environment promotion:**

```yaml
jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - uses: actions/checkout@v4
      - run: deploy-staging.sh

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - run: deploy-production.sh
```

## Examples

```yaml
jobs:
  deploy-staging:
    environment: staging
  deploy-production:
    needs: deploy-staging
    environment: production
```
"""),

    # =========================================================================
    # 8. ARTIFACT ERRORS
    # =========================================================================
    md("GitHub Actions Upload Artifact Failed",
       "Fix GitHub Actions upload-artifact action failures.",
       """## Error Description

Upload artifact failures occur when the artifact cannot be uploaded:

```
Error: Artifact upload failed: 413 Request Entity Too Large
```

## Common Causes

- Artifact exceeds the 10GB size limit.
- Artifact path does not exist.
- Artifact name conflict with existing artifact.

## How to Fix

**Compress before uploading:**

```yaml
steps:
  - name: Create artifact
    run: tar -czf artifact.tar.gz ./dist
  - uses: actions/upload-artifact@v4
    with:
      name: build-output
      path: artifact.tar.gz
      retention-days: 1
```

## Examples

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: ./dist
    retention-days: 7
    compression-level: 6
```
"""),

    md("GitHub Actions Download Artifact Not Found",
       "Fix GitHub Actions download-artifact not found errors.",
       """## Error Description

Download artifact not found errors occur when the artifact does not exist:

```
Error: Artifact 'my-artifact' not found
```

## Common Causes

- Artifact was not uploaded in a previous job.
- Artifact name is incorrect.
- Artifact expired (retention period exceeded).

## How to Fix

**Use correct artifact name:**

```yaml
steps:
  - uses: actions/download-artifact@v4
    with:
      name: my-artifact
      path: ./artifacts
```

## Examples

```yaml
# Download from specific workflow run
- uses: actions/download-artifact@v4
  with:
    name: build-output
    github-token: ${{ secrets.GITHUB_TOKEN }}
    run-id: ${{ github.event.workflow_run.id }}
```
"""),

    md("GitHub Actions Artifact Name Conflict",
       "Fix GitHub Actions artifact name conflict errors.",
       """## Error Description

Artifact name conflicts occur when uploading an artifact with a name that already exists:

```
Error: Artifact with name 'my-artifact' already exists
```

## Common Causes

- Multiple jobs uploading artifacts with the same name.
- Using a static name without including unique identifiers.

## How to Fix

**Use unique artifact names:**

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: build-${{ runner.os }}-${{ github.run_id }}
    path: ./dist
```

## Examples

```yaml
# Dynamic name with matrix
name: test-results-${{ matrix.os }}-${{ matrix.node-version }}
```
"""),

    md("GitHub Actions Artifact Retention Exceeded",
       "Fix GitHub Actions artifact retention period exceeded errors.",
       """## Error Description

Retention exceeded errors occur when artifacts are accessed after their retention period:

```
Error: Artifact has expired and is no longer available
```

## Common Causes

- Default retention is 90 days.
- Artifact was uploaded with short retention.

## How to Fix

**Set longer retention period:**

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: important-build
    path: ./dist
    retention-days: 365
```

## Examples

```yaml
# Maximum retention (90 days for free, 400 for enterprise)
retention-days: 90
```
"""),

    md("GitHub Actions Artifact Path Invalid",
       "Fix GitHub Actions artifact path invalid errors.",
       """## Error Description

Invalid path errors occur when the artifact upload path is incorrect:

```
Error: No files were found with the provided path: ./nonexistent-dir
```

## Common Causes

- Directory or file does not exist at the specified path.
- Build step did not produce the expected output.

## How to Fix

**Verify path exists before upload:**

```yaml
steps:
  - run: npm run build
  - run: ls -la ./dist || echo "dist directory not found"
  - uses: actions/upload-artifact@v4
    with:
      name: build
      path: ./dist
```

## Examples

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: coverage
    path: |
      coverage/
      !coverage/tmp/
```
"""),

    md("GitHub Actions Upload Speed Limit",
       "Fix GitHub Actions artifact upload speed limit and timeout errors.",
       """## Error Description

Upload speed limit errors occur during large artifact uploads:

```
Error: Artifact upload timed out after 3600 seconds
```

## Common Causes

- Very large artifact being uploaded.
- Many small files instead of one archive.

## How to Fix

**Compress before upload:**

```yaml
steps:
  - run: tar -czf artifacts.tar.gz ./dist ./test-results
  - uses: actions/upload-artifact@v4
    with:
      name: compressed-build
      path: artifacts.tar.gz
```

## Examples

```yaml
- run: zip -r build.zip ./dist
- uses: actions/upload-artifact@v4
  with:
    name: build
    path: build.zip
```
"""),

    md("GitHub Actions Download Canceled",
       "Fix GitHub Actions artifact download canceled errors.",
       """## Error Description

Download canceled errors occur when artifact download is interrupted:

```
Error: Download canceled by user
```

## Common Causes

- User manually canceled the workflow run.
- Network interruption during download.

## How to Fix

**Handle cancellation gracefully:**

```yaml
steps:
  - uses: actions/download-artifact@v4
    if: ${{ !cancelled() }}
    with:
      name: build-output
```

## Examples

```yaml
steps:
  - uses: actions/download-artifact@v4
    continue-on-error: true
    with:
      name: optional-artifact
```
"""),

    md("GitHub Actions Artifact Zip Corrupt",
       "Fix GitHub Actions corrupt artifact zip errors.",
       """## Error Description

Corrupt artifact errors occur when the downloaded artifact is damaged:

```
Error: zip: not a valid zip file
```

## Common Causes

- Upload was interrupted.
- Storage backend corruption.

## How to Fix

**Verify artifact integrity:**

```yaml
- run: |
    sha256sum ./artifact.zip
    unzip -t ./artifact.zip
```

## Examples

```yaml
- run: echo "${{ steps.upload.outputs.checksum }}" > checksum.txt
```
"""),

    md("GitHub Actions Artifact Expired",
       "Fix GitHub Actions artifact expired and unavailable errors.",
       """## Error Description

Artifact expired errors occur when artifacts are past their retention period:

```
Error: Artifact has expired and cannot be downloaded
```

## Common Causes

- Artifact retention period reached.
- Organization-level retention policies.

## How to Fix

**Upload with appropriate retention:**

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: long-lived-artifact
    path: ./dist
    retention-days: 90
```

## Examples

```yaml
retention-days: 30  # Short-term
retention-days: 90  # Long-term
```
"""),

    md("GitHub Actions Cross-Workflow Artifact Not Available",
       "Fix GitHub Actions artifact not available across different workflow runs.",
       """## Error Description

Cross-workflow artifact errors occur when trying to access artifacts from a different workflow:

```
Error: Artifact from different workflow run is not accessible
```

## Common Causes

- Artifacts are scoped to the current workflow run by default.
- Different workflow trying to access artifacts.

## How to Fix

**Use workflow_run to access artifacts:**

```yaml
on:
  workflow_run:
    workflows: ["Build"]
    types: [completed]

jobs:
  download:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build-output
          github-token: ${{ secrets.GITHUB_TOKEN }}
          run-id: ${{ github.event.workflow_run.id }}
```

## Examples

```yaml
- uses: actions/download-artifact@v4
  with:
    name: build-output
    github-token: ${{ github.token }}
    run-id: 12345678
```
"""),

    # =========================================================================
    # 9. MATRIX/STRATEGY ERRORS
    # =========================================================================
    md("GitHub Actions Matrix Not Defined",
       "Fix GitHub Actions matrix not defined errors when matrix strategy is referenced but missing.",
       """## Error Description

Matrix not defined errors occur when a matrix variable is referenced but not defined:

```
Error: Matrix variable 'node-version' is not defined
```

## Common Causes

- Variable referenced as `${{ matrix.node-version }}` but `strategy.matrix` is missing.
- Typo in the matrix variable name.

## How to Fix

**Define matrix in the job:**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16, 18, 20]
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
```

## Examples

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
```
"""),

    md("GitHub Actions Matrix Combination Empty",
       "Fix GitHub Actions matrix empty combination errors.",
       """## Error Description

Empty combination errors occur when the matrix generates no valid combinations:

```
Error: Matrix produced zero combinations
```

## Common Causes

- All matrix combinations are excluded.
- Matrix values are empty lists.

## How to Fix

**Verify matrix combinations:**

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
    exclude:
      - node-version: 16
        os: windows-latest
```

## Examples

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
    exclude:
      - node-version: 16
        os: windows-latest
```
"""),

    md("GitHub Actions Matrix Include Strategy Error",
       "Fix GitHub Actions matrix include strategy errors.",
       """## Error Description

Matrix include strategy errors occur when `include` adds invalid combinations:

```
Error: Invalid matrix include: unknown key 'node-verion'
```

## Common Causes

- Typo in include keys (must match matrix keys).
- Include adds values not in the matrix.

## How to Fix

**Use include correctly:**

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
    include:
      - node-version: 20
        os: ubuntu-latest
        experimental: true
```

## Examples

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
    include:
      - node-version: 20
        npm-version: 'latest'
```
"""),

    md("GitHub Actions Matrix Exclude Conflict",
       "Fix GitHub Actions matrix exclude conflict errors.",
       """## Error Description

Matrix exclude conflicts occur when exclusion rules are contradictory:

```
Error: Matrix exclude conflict: cannot exclude all combinations
```

## Common Causes

- Exclude rules remove all valid combinations.
- Overly broad exclude patterns.

## How to Fix

**Review exclude rules:**

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    node-version: [16, 18, 20]
    exclude:
      - os: macos-latest
        node-version: 16
```

## Examples

```yaml
exclude:
  - os: macos-latest
    node-version: 16
  - os: windows-latest
    node-version: 18
```
"""),

    md("GitHub Actions Fail-Fast Error",
       "Fix GitHub Actions fail-fast strategy errors in matrix builds.",
       """## Error Description

Fail-fast errors occur when `fail-fast` causes unexpected early termination:

```
Error: Build cancelled because one matrix job failed (fail-fast: true)
```

## Common Causes

- Default `fail-fast: true` cancels all jobs on first failure.
- Flaky test in one matrix combination kills all others.

## How to Fix

**Disable fail-fast:**

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    node-version: [16, 18, 20]
```

## Examples

```yaml
strategy:
  fail-fast: false
  matrix:
    node-version: [16, 18, 20]
```
"""),

    md("GitHub Actions Max Parallel Exceeded",
       "Fix GitHub Actions max-parallel exceeded errors.",
       """## Error Description

Max-parallel errors occur when too many matrix jobs run concurrently:

```
Error: Maximum concurrent jobs (200) exceeded for this repository
```

## Common Causes

- Large matrix creating many jobs.
- Multiple workflows running simultaneously.

## How to Fix

**Limit parallel jobs:**

```yaml
strategy:
  max-parallel: 5
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    node-version: [16, 18, 20]
```

## Examples

```yaml
strategy:
  max-parallel: 3
  matrix:
    shard: [1, 2, 3, 4, 5, 6]
```
"""),

    md("GitHub Actions Continue On Error Behavior",
       "Fix GitHub Actions continue-on-error behavior issues.",
       """## Error Description

continue-on-error behavior issues occur when the error handling does not work as expected:

```
Warning: continue-on-error is true but the job still failed
```

## Common Causes

- `continue-on-error` only affects the step, not dependent jobs.
- Job-level `continue-on-error` does not prevent the workflow from reporting failure.

## How to Fix

**Use step-level continue-on-error:**

```yaml
steps:
  - name: Optional step
    continue-on-error: true
    run: flaky-command.sh
```

## Examples

```yaml
strategy:
  matrix:
    include:
      - node-version: 20
        experimental: false
      - node-version: 22
        experimental: true
  fail-fast: false
steps:
  - run: npm test
    continue-on-error: ${{ matrix.experimental }}
```
"""),

    md("GitHub Actions Matrix Axis Unsupported",
       "Fix GitHub Actions unsupported matrix axis errors.",
       """## Error Description

Unsupported matrix axis errors occur when a matrix key is not valid:

```
Error: Invalid matrix key 'os-name': must not contain hyphens
```

## Common Causes

- Matrix key contains invalid characters.
- Matrix key conflicts with built-in variables.

## How to Fix

**Use valid matrix key names:**

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [16, 18, 20]
    include:
      - os: ubuntu-latest
        node: 20
        experimental: false
```

## Examples

```yaml
matrix:
  os: [ubuntu-latest, windows-latest]
  node-version: [16, 18, 20]
  python-version: ['3.9', '3.10', '3.11']
```
"""),

    md("GitHub Actions Strategy Fallback",
       "Fix GitHub Actions strategy fallback errors when matrix strategy has issues.",
       """## Error Description

Strategy fallback errors occur when the matrix strategy cannot be resolved:

```
Error: Strategy matrix could not be resolved
```

## Common Causes

- Matrix values reference undefined variables.
- Expression in matrix value is invalid.

## How to Fix

**Use static matrix values:**

```yaml
strategy:
  matrix:
    node-version: [16, 18, 20]
```

## Examples

```yaml
# Static matrix
strategy:
  matrix:
    node: [16, 18, 20]

# Dynamic matrix
strategy:
  matrix: ${{ fromJSON(needs.set-matrix.outputs.matrix) }}
```
"""),

    md("GitHub Actions Matrix Job Cancelled",
       "Fix GitHub Actions matrix job cancelled unexpectedly.",
       """## Error Description

Matrix job cancellation occurs when a matrix job is unexpectedly cancelled:

```
Error: The operation was cancelled
```

## Common Causes

- Workflow was manually cancelled.
- Concurrency group cancelled the job.
- `fail-fast: true` cancelled other jobs.

## How to Fix

**Use concurrency groups carefully:**

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}
```

## Examples

```yaml
concurrency:
  group: build-${{ github.ref }}
  cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}
```
"""),

    # =========================================================================
    # 10. BILLING/MINUTES ERRORS
    # =========================================================================
    md("GitHub Actions Minutes Exhausted",
       "Fix GitHub Actions minutes exhausted errors.",
       """## Error Description

Minutes exhausted errors occur when the billing minutes limit is reached:

```
Error: GitHub Actions: usage quota has been exceeded
```

## Common Causes

- Monthly minutes limit reached.
- Large matrix builds consuming many minutes.

## How to Fix

**Optimize workflow to use fewer minutes:**

```yaml
steps:
  - uses: actions/cache@v4
    with:
      path: node_modules
      key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

**Use concurrency to avoid duplicate runs:**

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

## Examples

```yaml
# Check billing at
# https://github.com/settings/billing
```
"""),

    md("GitHub Actions Concurrent Jobs Limit",
       "Fix GitHub Actions concurrent jobs limit exceeded errors.",
       """## Error Description

Concurrent jobs limit errors occur when too many jobs run simultaneously:

```
Error: Maximum number of concurrent jobs reached (20)
```

## Common Causes

- Multiple workflows triggering at the same time.
- Large matrix strategies.

## How to Fix

**Limit concurrency:**

```yaml
concurrency:
  group: build-${{ github.ref }}
  cancel-in-progress: true
```

## Examples

```yaml
concurrency:
  group: deploy-production
  cancel-in-progress: false
```
"""),

    md("GitHub Actions Spending Limit Reached",
       "Fix GitHub Actions spending limit reached errors.",
       """## Error Description

Spending limit errors occur when the billing spending limit is hit:

```
Error: GitHub Actions: spending limit reached
```

## Common Causes

- Organization spending limit set too low.
- Unexpected surge in workflow runs.

## How to Fix

**Check and adjust spending limit:**

Go to Settings > Billing > Spending limit

## Examples

```yaml
- run: |
    gh api github.com/repos/{owner}/{repo}/actions/workflows \
      --jq '.workflows[] | {name: .name, state: .state}'
```
"""),

    md("GitHub Actions Runner Minutes Not Available",
       "Fix GitHub Actions runner minutes not available errors.",
       """## Error Description

Runner minutes not available errors occur when self-hosted runners have billing issues:

```
Error: No runners available for this workflow
```

## Common Causes

- Self-hosted runner machine is down.
- Runner group permissions changed.

## How to Fix

**Check runner availability:**

```bash
gh api repos/{owner}/{repo}/actions/runners --jq '.runners[] | {name: .name, status: .status}'
```

## Examples

```yaml
runs-on: ${{ github.repository_owner == 'myorg' && 'self-hosted' || 'ubuntu-latest' }}
```
"""),

    md("GitHub Actions macOS Minutes Expensive",
       "Fix GitHub Actions macOS runner minutes cost concerns.",
       """## Error Description

macOS minutes are billed at a higher rate, causing billing surprises:

```
Warning: macOS runner minutes are charged at 10x the Linux rate
```

## Common Causes

- macOS runners cost 10x Linux minutes.
- Large matrix with macOS targets.

## How to Fix

**Limit macOS builds:**

```yaml
strategy:
  matrix:
    os: [ubuntu-latest]
    include:
      - os: macos-latest
        node-version: 20
```

## Examples

```yaml
jobs:
  macos-test:
    runs-on: macos-latest
    if: github.ref == 'refs/heads/main'
```
"""),

    md("GitHub Actions GPU Minutes Not Available",
       "Fix GitHub Actions GPU runner minutes not available errors.",
       """## Error Description

GPU minutes not available errors occur when GPU runners are not accessible:

```
Error: GPU runner not available for this repository
```

## Common Causes

- GPU runners require special access.
- Organization does not have GPU runners provisioned.

## How to Fix

**Request GPU runner access:**

```yaml
runs-on: [self-hosted, gpu, cuda-12]
```

## Examples

```yaml
runs-on: [self-hosted, gpu, nvidia-a100]
```
"""),

    md("GitHub Actions Billing Not Set Up",
       "Fix GitHub Actions billing not configured errors.",
       """## Error Description

Billing not set up errors occur when the organization does not have billing configured:

```
Error: GitHub Actions requires a billing account
```

## Common Causes

- Free tier limits reached.
- Organization does not have a payment method.

## How to Fix

**Set up billing:**

Go to Settings > Billing > Add payment method

## Examples

```yaml
# Free tier: 2000 minutes/month for private repos
# Pro: 3000 minutes/month
# Team: 3000 minutes/month per member
```
"""),

    md("GitHub Actions Usage Limit Exceeded",
       "Fix GitHub Actions usage limit exceeded errors.",
       """## Error Description

Usage limit exceeded errors occur when workflow limits are hit:

```
Error: Maximum workflow run limit exceeded (1000 per day)
```

## Common Causes

- Too many workflow runs triggered.
- Workflow run trigger loop.
- Scheduled workflows running too frequently.

## How to Fix

**Limit scheduled workflows:**

```yaml
on:
  schedule:
    - cron: '0 0 * * 1'
```

## Examples

```yaml
on:
  push:
    paths-ignore:
      - '**.md'
      - 'docs/**'
```
"""),

    md("GitHub Actions Workflow Run Queued",
       "Fix GitHub Actions workflow run queued and not starting errors.",
       """## Error Description

Workflow run queued errors occur when the workflow does not start:

```
Status: Queued
```

## Common Causes

- All runners are busy.
- Runner group has no available runners.
- Concurrency limit reached.

## How to Fix

**Check queue status:**

```bash
gh api repos/{owner}/{repo}/actions/runs --jq '.workflow_runs[] | select(.status=="queued") | .id'
```

## Examples

```yaml
- run: gh run view ${{ github.run_id }}
```
"""),

    md("GitHub Actions Rate Limit Exceeded",
       "Fix GitHub Actions API rate limit exceeded errors.",
       """## Error Description

Rate limit errors occur when too many API calls are made:

```
Error: API rate limit exceeded for user
```

## Common Causes

- Too many GitHub API calls in the workflow.
- Using `gh` CLI excessively.

## How to Fix

**Check rate limit:**

```bash
gh api rate_limit | jq '.rate'
```

## Examples

```yaml
- run: |
    RATE=$(gh api rate_limit --jq '.rate.remaining')
    if [ "$RATE" -lt 10 ]; then
      echo "Rate limit low, skipping"
      exit 0
    fi
```
"""),

    # =========================================================================
    # 11. OIDC/AUTH ERRORS
    # =========================================================================
    md("GitHub Actions OIDC Token Not Available",
       "Fix GitHub Actions OIDC token not available errors.",
       """## Error Description

OIDC token not available errors occur when the OIDC token cannot be obtained:

```
Error: OIDC token request failed: not authorized
```

## Common Causes

- OIDC not enabled in repository settings.
- `id-token: write` permission not set.

## How to Fix

**Enable OIDC and set permissions:**

```yaml
permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/github-actions
          aws-region: us-east-1
```

## Examples

```yaml
permissions:
  id-token: write
  contents: read
```
"""),

    md("GitHub Actions ID Token Permission Missing",
       "Fix GitHub Actions id-token permission missing errors.",
       """## Error Description

ID token permission errors occur when the `id-token` permission is not granted:

```
Error: The id-token permission is required for OIDC
```

## Common Causes

- Workflow does not include `id-token: write` in permissions.

## How to Fix

**Add id-token permission:**

```yaml
permissions:
  id-token: write
  contents: read

jobs:
  authenticate:
    runs-on: ubuntu-latest
    steps:
      - name: Get OIDC token
        run: |
          TOKEN=$(curl -H "Authorization: bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" \
            "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=https://example.com" | jq -r '.value')
          echo "Token: $TOKEN"
```

## Examples

```yaml
permissions:
  id-token: write
  contents: read
```
"""),

    md("GitHub Actions Cloud Auth Failed",
       "Fix GitHub Actions cloud authentication failures in OIDC workflows.",
       """## Error Description

Cloud auth failures occur when OIDC authentication to cloud providers fails:

```
Error: Cloud provider rejected the OIDC token
```

## Common Causes

- OIDC provider not configured in cloud account.
- Trust policy does not match GitHub OIDC claims.

## How to Fix

**Configure AWS OIDC trust:**

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789012:role/github-actions
      aws-region: us-east-1
```

## Examples

```json
{
  "Effect": "Allow",
  "Principal": {
    "Federated": "arn:aws:iam::123456789012:oidc-provider/token.actions.githubusercontent.com"
  },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
    "StringEquals": {
      "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
    },
    "StringLike": {
      "token.actions.githubusercontent.com:sub": "repo:owner/repo:*"
    }
  }
}
```
"""),

    md("GitHub Actions AWS Credential Error",
       "Fix GitHub Actions AWS credential configuration errors.",
       """## Error Description

AWS credential errors occur when the workflow cannot authenticate with AWS:

```
Error: Unable to locate credentials
```

## Common Causes

- AWS credentials not configured.
- IAM role not assumed via OIDC.

## How to Fix

**Configure AWS credentials via OIDC:**

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
      aws-region: us-east-1
  - run: aws s3 ls
```

## Examples

```yaml
# OIDC approach (preferred)
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
      aws-region: us-east-1
```
"""),

    md("GitHub Actions Azure Login Failed",
       "Fix GitHub Actions Azure login failures in CI workflow.",
       """## Error Description

Azure login failures occur when the workflow cannot authenticate with Azure:

```
Error: Error: az login failed
```

## Common Causes

- Azure credentials not configured.
- Service principal expired.
- Tenant/subscription ID incorrect.

## How to Fix

**Use OIDC with Azure:**

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: azure/login@v2
    with:
      client-id: ${{ secrets.AZURE_CLIENT_ID }}
      tenant-id: ${{ secrets.AZURE_TENANT_ID }}
      subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
```

## Examples

```yaml
steps:
  - uses: azure/login@v2
    with:
      client-id: ${{ secrets.AZURE_CLIENT_ID }}
      tenant-id: ${{ secrets.AZURE_TENANT_ID }}
      subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
  - run: az webapp list --query "[].name"
```
"""),

    md("GitHub Actions GCP Auth Error",
       "Fix GitHub Actions GCP authentication errors in CI workflow.",
       """## Error Description

GCP auth errors occur when the workflow cannot authenticate with Google Cloud:

```
Error: ERROR: (gcloud.auth) No project detected
```

## Common Causes

- Workload Identity Federation not configured.
- Service account key not provided.

## How to Fix

**Use Workload Identity Federation:**

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: google-github-actions/auth@v2
    with:
      workload_identity_provider: 'projects/123/locations/global/workloadIdentityPools/github-pool/providers/github'
      service_account: 'github-actions@my-project.iam.gserviceaccount.com'
  - run: gcloud compute instances list
```

## Examples

```yaml
steps:
  - uses: google-github-actions/auth@v2
    with:
      credentials_json: ${{ secrets.GCP_SA_KEY }}
```
"""),

    md("GitHub Actions Assume Role Failed",
       "Fix GitHub Actions assume role failures in cloud workflows.",
       """## Error Description

Assume role failures occur when the workflow cannot assume an IAM role:

```
Error: AccessDenied: User is not authorized to assume role
```

## Common Causes

- IAM role trust policy does not allow the GitHub OIDC provider.
- Role ARN is incorrect.
- Role does not exist.

## How to Fix

**Verify role trust policy:**

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789012:role/github-actions
      aws-region: us-east-1
```

## Examples

```bash
# Verify the role exists
aws iam get-role --role-name github-actions
```
"""),

    md("GitHub Actions Federation Not Configured",
       "Fix GitHub Actions federation not configured errors for cloud providers.",
       """## Error Description

Federation not configured errors occur when OIDC federation is not set up:

```
Error: OIDC provider not found for this repository
```

## Common Causes

- OIDC provider not created in the cloud account.
- Repository not added to the trust policy.

## How to Fix

**Set up OIDC federation:**

```bash
# AWS
aws iam create-open-id-connect-provider \
  --url https://token.actions.githubusercontent.com \
  --thumbprint-list 6938fd4d98bab03faadb97b34396831e3780aea1 \
  --client-id-list sts.amazonaws.com
```

## Examples

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
      aws-region: us-east-1
```
"""),

    md("GitHub Actions Token Exchange Error",
       "Fix GitHub Actions token exchange errors in OIDC workflows.",
       """## Error Description

Token exchange errors occur when the OIDC token cannot be exchanged for cloud credentials:

```
Error: token exchange failed: invalid_grant
```

## Common Causes

- OIDC token expired.
- Audience claim does not match.
- Token format is invalid.

## How to Fix

**Verify audience configuration:**

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
      aws-region: us-east-1
```

## Examples

```yaml
# Verify the token is being requested correctly
- name: Debug OIDC
  run: |
    TOKEN=$(curl -s -H "Authorization: bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" \
      "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=https://sts.amazonaws.com" | jq -r '.value')
    echo "Token length: ${#TOKEN}"
```
"""),

    md("GitHub Actions Audience Claim Mismatch",
       "Fix GitHub Actions audience claim mismatch errors in OIDC tokens.",
       """## Error Description

Audience claim mismatch errors occur when the OIDC token audience does not match:

```
Error: audience claim does not match expected value
```

## Common Causes

- OIDC token audience is not set correctly.
- Cloud provider expects a different audience.

## How to Fix

**Set correct audience in cloud configuration:**

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
      aws-region: us-east-1
```

## Examples

```yaml
# AWS expects sts.amazonaws.com as audience
# Azure expects api://AzureADTokenExchange
```
"""),

    # =========================================================================
    # 12. ACTIONS MARKETPLACE ERRORS
    # =========================================================================
    md("GitHub Actions Action Not Found",
       "Fix GitHub Actions action not found errors when using marketplace actions.",
       """## Error Description

Action not found errors occur when a referenced action does not exist:

```
Error: Can't find action 'actions/chekout@v4'
```

## Common Causes

- Action reference is misspelled.
- Action was removed or renamed.
- Private action requires authentication.

## How to Fix

**Verify the action exists:**

```yaml
- uses: actions/checkout@v4
```

**Use a local action:**

```yaml
- uses: ./.github/actions/my-action
```

## Examples

```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 0
```
"""),

    md("GitHub Actions Action Version Not Pinned",
       "Fix GitHub Actions action version not pinned warnings and security concerns.",
       """## Error Description

Unpinned action versions can lead to unexpected behavior and security risks:

```
Warning: Action 'actions/checkout' is not pinned to a full length commit SHA
```

## Common Causes

- Using branch names or tags instead of commit SHAs.
- Supply chain attack risk with unpinned actions.

## How to Fix

**Pin to a full commit SHA:**

```yaml
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11
  # v4.1.1
```

**Use tags for convenience (less secure):**

```yaml
- uses: actions/checkout@v4
```

## Examples

```yaml
# Most secure - full SHA
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11

# Less secure but convenient
- uses: actions/checkout@v4
```
"""),

    md("GitHub Actions Action Requires Major Version",
       "Fix GitHub Actions action requires major version warnings.",
       """## Error Description

Major version warnings occur when an action requires a specific major version:

```
Warning: Action requires Node.js 16, which is not supported
```

## Common Causes

- Action uses an outdated Node.js runtime.
- Action version incompatible with runner.

## How to Fix

**Update to a newer version of the action:**

```yaml
- uses: actions/checkout@v4  # v4 uses Node 20
```

## Examples

```yaml
# Outdated - uses Node 16
- uses: actions/checkout@v3

# Current - uses Node 20
- uses: actions/checkout@v4
```
"""),

    md("GitHub Actions Deprecated Action",
       "Fix GitHub Actions deprecated action warnings and errors.",
       """## Error Description

Deprecated action errors occur when using actions that are no longer maintained:

```
Warning: This action is deprecated. Please use actions/checkout@v4
```

## Common Causes

- Using an old version of an action.
- Action has been replaced by a newer version.

## How to Fix

**Update to the latest version:**

```yaml
# Old
- uses: actions/checkout@v3

# New
- uses: actions/checkout@v4
```

## Examples

```yaml
# Check for deprecation warnings
- uses: actions/checkout@v4
  with:
    fetch-depth: 0
```
"""),

    md("GitHub Actions Action Not Compatible With Node Version",
       "Fix GitHub Actions action not compatible with Node.js version errors.",
       """## Error Description

Node.js version incompatibility errors occur when actions use unsupported Node.js versions:

```
Error: Action 'deprecated-action@v1' is not compatible with Node.js 20
```

## Common Causes

- Action was built for Node 12 or Node 16.
- Runner has moved to Node 20.

## How to Fix

**Update the action to a Node 20 compatible version:**

```yaml
- uses: actions/checkout@v4
```

## Examples

```yaml
# Node 16 compatible (deprecated)
- uses: actions/checkout@v3

# Node 20 compatible (current)
- uses: actions/checkout@v4
```
"""),

    md("GitHub Actions Composite Action Error",
       "Fix GitHub Actions composite action configuration errors.",
       """## Error Description

Composite action errors occur when the action YAML is malformed:

```
Error: Invalid composite action: 'runs' section is required
```

## Common Causes

- Missing `runs` section.
- Invalid `using` value.
- Incorrect step syntax in composite action.

## How to Fix

**Use proper composite action format:**

```yaml
name: 'My Composite Action'
description: 'A composite action'
inputs:
  node-version:
    description: 'Node.js version'
    required: true
    default: '20'
runs:
  using: 'composite'
  steps:
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ inputs.node-version }}
    - run: npm ci
      shell: bash
```

## Examples

```yaml
# .github/actions/my-action/action.yml
name: 'Build and Test'
description: 'Runs build and tests'
inputs:
  config:
    required: false
    default: 'default'
runs:
  using: 'composite'
  steps:
    - run: echo "Config: ${{ inputs.config }}"
      shell: bash
```
"""),

    md("GitHub Actions Docker Action Build Failed",
       "Fix GitHub Actions Docker action build failures.",
       """## Error Description

Docker action build failures occur when the Docker image cannot be built:

```
Error: failed to solve: rpc error: code = Unknown desc = error reading from server: EOF
```

## Common Causes

- Dockerfile has syntax errors.
- Base image not available.
- Build context too large.
- Network issues pulling base images.

## How to Fix

**Build the Docker image locally first:**

```bash
docker build -t my-action:latest .
```

**Use a simpler Dockerfile:**

```dockerfile
FROM node:20-slim
COPY . /action
WORKDIR /action
RUN npm install --production
ENTRYPOINT ["node", "/action/index.js"]
```

**Reference the Docker action in workflow:**

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: ./.github/actions/my-docker-action
```

## Examples

```dockerfile
# Minimal Dockerfile for a GitHub Action
FROM node:20-slim
COPY package*.json ./
RUN npm ci --production
COPY . .
ENTRYPOINT ["node", "index.js"]
```
"""),

    md("GitHub Actions JavaScript Action Missing",
       "Fix GitHub Actions JavaScript action missing required files.",
       """## Error Description

JavaScript action missing errors occur when the action directory does not contain required files:

```
Error: Unable to find action 'my-action' in /github/workspace/
```

## Common Causes

- `action.yml` or `action.yaml` is missing.
- `index.js` entry point is missing.
- `node_modules` not committed.

## How to Fix

**Create proper action.yml:**

```yaml
name: 'My JavaScript Action'
description: 'Does something useful'
runs:
  using: 'node20'
  main: 'dist/index.js'
inputs:
  name:
    description: 'Input name'
    required: true
outputs:
  result:
    description: 'Output result'
```

**Build and commit dist:**

```bash
npm run build
git add dist/
git commit -m "Build action"
```

## Examples

```yaml
# action.yml structure
name: 'My Action'
runs:
  using: 'node20'
  main: 'dist/index.js'
inputs:
  input1:
    required: true
```
"""),

    md("GitHub Actions Action Deprecation Warning",
       "Fix GitHub Actions action deprecation warnings.",
       """## Error Description

Action deprecation warnings indicate the action is using outdated features:

```
Warning: The 'set-output' command is deprecated
```

## Common Causes

- Action uses deprecated workflow commands.
- Action uses deprecated Node.js version.

## How to Fix

**Update workflow commands:**

```yaml
# Old (deprecated)
- run: echo "::set-output name=result::value"

# New
- run: echo "result=value" >> $GITHUB_OUTPUT
```

**Update the action version:**

```yaml
# Old
- uses: actions/checkout@v3

# New
- uses: actions/checkout@v4
```

## Examples

```yaml
# Modern output syntax
steps:
  - id: step1
    run: echo "result=success" >> $GITHUB_OUTPUT
  - run: echo ${{ steps.step1.outputs.result }}
```
"""),

    md("GitHub Actions Third-Party Action Review",
       "Fix GitHub Actions third-party action security review concerns.",
       """## Error Description

Third-party action security review concerns require careful evaluation:

```
Warning: Using untrusted third-party action 'unknown-org/action@v1'
```

## Common Causes

- Action from unknown or untrusted source.
- Action has not been audited.
- Supply chain attack risk.

## How to Fix

**Pin to a specific commit SHA:**

```yaml
- uses: trusted-org/trusted-action@a1b2c3d4e5f6
```

**Use only verified creators:**

```yaml
# GitHub verified creators
- uses: actions/checkout@v4
- uses: actions/setup-node@v4
- uses: actions/upload-artifact@v4
```

**Review the action source:**

```bash
# Check the action repository
gh api repos/{owner}/{repo}/contents/action.yml
```

## Examples

```yaml
# Verified actions from GitHub
- uses: actions/checkout@v4
  with:
    fetch-depth: 0

# Pin to SHA for third-party
- uses: peaceiris/actions-gh-pages@068c335e4633200b3e176b5c14b4fefc074658c3
```
"""),
]

count = 0
skipped = 0
for title, desc, body in PAGES:
    s = slug(title)
    if s in EXISTING:
        skipped += 1
        continue
    content = make_page(title, desc, body)
    path = os.path.join(BASE, f'{s}.md')
    with open(path, 'w') as f:
        f.write(content)
    count += 1

print(f'Generated: {count} pages')
print(f'Skipped (existing): {skipped} pages')
print(f'Total pages in PAGES list: {len(PAGES)}')
