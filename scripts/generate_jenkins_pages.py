#!/usr/bin/env python3
"""Generate 100+ Jenkins CI/CD error pages."""
import os, textwrap

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "tools", "jenkins")
os.makedirs(OUTPUT_DIR, exist_ok=True)

PAGES = []

def a(slug, title, desc, body):
    PAGES.append({"slug": slug, "title": title, "desc": desc, "body": body})

# 1. Pipeline errors (14)
a("not-serializable-exception", "NotSerializableException in Jenkins Pipeline", "Fix java.io.NotSerializableException in Jenkins pipelines. Resolve serialization errors when passing objects between pipeline steps.", textwrap.dedent("""A `java.io.NotSerializableException` occurs when a Jenkins pipeline tries to serialize an object that does not implement `java.io.Serializable`. Jenkins pipelines run on the CPS-transformed engine which requires all objects crossing step boundaries to be serializable.

## Common Causes

- Using non-serializable types (e.g., `Thread`, `Socket`, `FileInputStream`) as variables in pipeline steps
- Storing closures or lambda references that capture non-serializable state
- Using third-party library objects that are not `Serializable`
- Returning non-serializable objects from `sh` or `bat` steps into Groovy variables

## How to Fix

### Mark Your Class as Serializable

```java
package com.example
import java.io.Serializable
class BuildConfig implements Serializable {
    String version
    String environment
}
```

### Use @NonCPS for Non-Serializable Operations

```groovy
@NonCPS
def parseJson(String text) {
    return new groovy.json.JsonSlurperClassic().parseText(text)
}
```

## Examples

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    def threadName = Thread.currentThread().name
                    echo threadName
                }
            }
        }
    }
}
```"""))

a("expected-stage", "Expected 'stage' Block in Jenkinsfile", "Fix 'expected stage' parsing errors in Jenkins declarative pipelines. Resolve Jenkinsfile structure issues.", textwrap.dedent("""The `expected 'stage'` error means Jenkins declarative pipeline parser encountered an element where it expected a `stage` block inside the `stages` section.

## Common Causes

- Placing non-stage content directly inside `stages { }` without wrapping in a `stage { }`
- Using scripted pipeline syntax inside a declarative pipeline
- Incorrect nesting levels in the Jenkinsfile
- Extra or missing braces causing misaligned blocks

## How to Fix

### Wrap All Blocks in Stage

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'make'
            }
        }
    }
}
```

### Use the Pipeline Linter

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ declarative-linter < Jenkinsfile
```

## Examples

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel') {
            parallel {
                stage('A') { steps { sh 'echo A' } }
                stage('B') { steps { sh 'echo B' } }
            }
        }
    }
}
```"""))

a("expected-steps", "Expected 'steps' Block in Jenkins Stage", "Fix 'expected steps' parsing error in Jenkins pipeline stages. Resolve missing steps blocks in Jenkinsfile.", textwrap.dedent("""The `expected 'steps'` error occurs when a declarative pipeline `stage` block does not contain a valid `steps` section.

## Common Causes

- Stage block contains directives (e.g., `when`, `agent`) but no `steps` block
- Misplaced `sh`, `echo`, or other step calls outside of a `steps` block

## How to Fix

```groovy
stage('Build') {
    steps {
        sh 'make'
    }
}
```

A stage with ONLY parallel does not need steps:

```groovy
stage('Tests') {
    parallel {
        stage('Unit') { steps { sh 'make test-unit' } }
        stage('Integration') { steps { sh 'make test-integration' } }
    }
}
```"""))

a("missing-agent-any", "Missing 'agent any' in Jenkins Pipeline", "Fix missing agent declaration in Jenkins declarative pipeline. Resolve pipeline without agent directive.", textwrap.dedent("""A declarative pipeline requires an `agent` directive either at the top level or per-stage. Without it, Jenkins does not know where to execute the pipeline.

## Common Causes

- Omitted the `agent` directive entirely from the `pipeline` block
- Forgot to add `agent` to individual stages
- Mixed scripted and declarative syntax

## How to Fix

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps { sh 'make build' }
        }
    }
}
```

### Use Per-Stage Agent

```groovy
pipeline {
    stages {
        stage('Build') {
            agent { label 'linux' }
            steps { sh 'make build' }
        }
    }
}
```"""))

a("script-not-allowed", "Script Not Allowed in Declarative Pipeline", "Fix 'script not allowed' error in Jenkins declarative pipeline. Resolve script block restrictions.", textwrap.dedent("""The `script` step is allowed in declarative pipelines but the code inside must conform to CPS transformation rules. Certain operations are restricted.

## Common Causes

- Using `script` block to call methods that are not CPS-transformed
- Attempting to modify pipeline variables outside `script` block
- Using Java reflection or system calls blocked by the sandbox

## How to Fix

```groovy
@NonCPS
def forbiddenOperation() {
    return "result"
}
```

```groovy
stage('Build') {
    steps {
        script {
            def version = readFile('version.txt').trim()
            env.APP_VERSION = version
        }
        sh 'make build'
    }
}
```

## Examples

```groovy
pipeline {
    agent any
    stages {
        stage('Set Version') {
            steps {
                script {
                    env.VERSION = '1.0'
                }
            }
        }
    }
}
```"""))

a("sandbox-security-error", "Jenkins Groovy Sandbox Security Error", "Fix Groovy sandbox security errors in Jenkins pipeline. Resolve ScriptSecurity and CPS transformation issues.", textwrap.dedent("""Jenkins applies a Groovy sandbox to pipeline scripts to prevent arbitrary code execution. When your script tries to access restricted Java classes or methods, the sandbox throws a `RejectedAccessException`.

## Common Causes

- Calling restricted Java APIs (e.g., `Runtime.getRuntime().exec()`)
- Accessing file system outside the Jenkins workspace
- Using dynamic class loading (`Class.forName`)
- Script not yet approved in the Script Approval console

## How to Fix

### Approve Scripts via Script Approval

Go to **Manage Jenkins > In-process Script Approval** and approve pending scripts.

### Use Approved Steps Instead of Raw Java

```groovy
sh 'echo test'
```

## Examples

```groovy
pipeline {
    agent any
    stages {
        stage('Security Test') {
            steps {
                sh 'ls -la'
            }
        }
    }
}
```"""))

a("library-not-found", "@Library Not Found in Jenkins Pipeline", "Fix @Library annotation not found error in Jenkins shared library. Resolve shared library loading failures.", textwrap.dedent("""The `@Library` annotation imports a Jenkins shared library into a pipeline. When the library cannot be found, Jenkins fails to compile the Jenkinsfile.

## Common Causes

- Shared library not configured in Global Pipeline Libraries
- Library name or version does not match the configured name
- Repository URL is incorrect or inaccessible
- Network issues preventing Jenkins from cloning the library

## How to Fix

```bash
# Manage Jenkins > Configure System > Global Pipeline Libraries
# Name: my-shared-lib
# Default version: main
# Source: Git
# Repository URL: https://github.com/org/shared-lib.git
```

```groovy
@Library('my-shared-lib') _
@Library('my-shared-lib@main') _
@Library(['lib1', 'lib2@v2']) _
```"""))

a("load-step-error", "Jenkins Load Step Error in Pipeline", "Fix Jenkins load step errors when loading Groovy scripts dynamically in pipeline.", textwrap.dedent("""The `load` step reads and evaluates a Groovy script file from the workspace. Errors occur when the file path is wrong or the script has compilation errors.

## Common Causes

- File does not exist at the specified path
- Groovy script has syntax or compilation errors
- Script references variables not available in the pipeline context

## How to Fix

```groovy
stage('Load Config') {
    steps {
        script {
            if (fileExists('scripts/config.groovy')) {
                def config = load('scripts/config.groovy')
                config.run()
            } else {
                error 'config.groovy not found'
            }
        }
    }
}
```

### Return a Callable Object

```groovy
// scripts/build.groovy
def call(version) {
    echo "Building version ${version}"
    sh "make VERSION=${version}"
}
return this
```"""))

a("readfile-error", "Jenkins Pipeline readFile Error", "Fix readFile step errors in Jenkins pipeline. Resolve file reading issues in Jenkinsfile and shared libraries.", textwrap.dedent("""The `readFile` step reads a file from the agent's workspace into a String. Errors occur when the file does not exist or permissions are insufficient.

## Common Causes

- File path is incorrect relative to the workspace
- File does not exist on the agent
- File permissions deny read access

## How to Fix

```groovy
stage('Read Config') {
    steps {
        script {
            if (fileExists('config.yml')) {
                def config = readFile 'config.yml'
                echo config
            } else {
                error 'config.yml not found'
            }
        }
    }
}
```"""))

a("writefile-error", "Jenkins Pipeline writeFile Error", "Fix writeFile step errors in Jenkins pipeline. Resolve file writing failures in Jenkinsfile.", textwrap.dedent("""The `writeFile` step writes a String to a file in the agent's workspace. Errors occur when the directory does not exist or permissions are insufficient.

## Common Causes

- Target directory does not exist
- Jenkins agent user lacks write permissions
- File encoding mismatch
- Disk space is full

## How to Fix

```groovy
sh 'mkdir -p output/config'
writeFile file: 'output/config/app.yml', text: 'key: value'
```

```groovy
writeFile file: 'output/report.csv', text: csvContent, encoding: 'UTF-8'
```"""))

a("input-timeout", "Jenkins Pipeline Input Step Timeout", "Fix Jenkins pipeline input step timeout. Resolve manual approval and input waiting failures.", textwrap.dedent("""The `input` step pauses the pipeline and waits for human interaction. A timeout occurs when no one responds within the configured time limit.

## Common Causes

- No one available to approve the deployment
- Timeout value too short for the approval workflow
- Notification not reaching the right team

## How to Fix

```groovy
stage('Approval') {
    steps {
        input message: 'Deploy to production?', ok: 'Deploy', timeout: 30
    }
}
```

```groovy
timeout(time: 1, unit: 'HOURS') {
    input message: 'Approve deployment?', submitter: 'admin,lead-dev'
}
```"""))

a("parallel-step-failed", "Jenkins Pipeline Parallel Step Failed", "Fix Jenkins pipeline parallel step failures. Resolve parallel stage execution and error handling.", textwrap.dedent("""Parallel steps in a Jenkins pipeline run concurrently within a single stage. When one or more parallel branches fail, the entire pipeline can fail.

## Common Causes

- One or more parallel branches encounter errors
- No error handling around parallel steps
- Resource contention between parallel branches

## How to Fix

### Use catchError for Non-Critical Branches

```groovy
stage('Tests') {
    parallel {
        stage('Unit Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE') {
                    sh 'make test-unit'
                }
            }
        }
        stage('Integration Tests') {
            steps {
                sh 'make test-integration'
            }
        }
    }
}
```

### Add Fail Fast Option

```groovy
stage('Tests') {
    failFast true
    parallel {
        stage('A') { steps { sh 'make test-a' } }
        stage('B') { steps { sh 'make test-b' } }
    }
}
```"""))

a("retry-limit-exceeded", "Jenkins Pipeline Retry Limit Exceeded", "Fix retry limit exceeded error in Jenkins pipeline. Resolve retry step exhaustion and transient failure handling.", textwrap.dedent("""The `retry` step re-executes a block of steps up to N times. When all retry attempts are exhausted, the pipeline fails.

## Common Causes

- Transient network failures persist beyond retry count
- External service remains unavailable
- Retry count too low
- Retry applied to a non-transient error

## How to Fix

```groovy
stage('Build') {
    steps {
        retry(5) {
            sh 'make build'
            sleep(time: 10, unit: 'SECONDS')
        }
    }
}
```

### Retry Only on Specific Errors

```groovy
retry(3) {
    try {
        sh 'make build'
    } catch (err) {
        if (err.toString().contains('timeout')) {
            throw err
        }
        error "Non-retryable error: ${err.message}"
    }
}
```"""))

a("timeout-step-error", "Jenkins Pipeline Timeout Step Error", "Fix Jenkins pipeline timeout step errors. Resolve step timeout exceeded and pipeline abort issues.", textwrap.dedent("""The `timeout` step aborts a block of steps if it does not complete within the specified duration.

## Common Causes

- Timeout value too short for the operation
- Pipeline step is deadlocked
- External dependency is unresponsive

## How to Fix

```groovy
stage('Build') {
    steps {
        timeout(time: 30, unit: 'MINUTES') {
            sh 'make build'
        }
    }
}
```

```groovy
timeout(time: 10, unit: 'MINUTES') {
    try {
        sh 'make deploy'
    } finally {
        cleanWs()
    }
}
```"""))

# 2. SCM errors (16)
a("git-fetch-failed", "Git Fetch Failed in Jenkins Pipeline", "Fix git fetch failed errors in Jenkins pipeline. Resolve Git SCM fetch failures and authentication issues.", textwrap.dedent("""A `git fetch failed` error occurs when Jenkins cannot retrieve the latest changes from the remote Git repository.

## Common Causes

- Invalid or expired credentials for the Git remote
- Repository URL is incorrect or moved
- SSH key not added to the agent
- Network firewall blocking outbound connections
- SSL certificate validation failure

## How to Fix

```groovy
checkout([
    $class: 'GitSCM',
    branches: [[name: 'main']],
    userRemoteConfigs: [[
        url: 'https://github.com/org/repo.git',
        credentialsId: 'github-ssh-key'
    ]]
])
```

```bash
mkdir -p ~/.ssh
ssh-keyscan github.com >> ~/.ssh/known_hosts
```

```groovy
withCredentials([sshUserPrivateKey(credentialsId: 'github-ssh-key', keyFileVariable: 'SSH_KEY')]) {
    sh 'GIT_SSH_COMMAND="ssh -i $SSH_KEY" git fetch origin main'
}
```"""))

a("git-clone-failed", "Git Clone Failed in Jenkins Pipeline", "Fix git clone failed errors in Jenkins. Resolve repository clone failures and workspace issues.", textwrap.dedent("""A `git clone failed` error means Jenkins cannot create a new clone of the repository in the workspace.

## Common Causes

- Repository URL is wrong or deleted
- Authentication failure
- Disk space exhausted
- Repository is too large

## How to Fix

```groovy
checkout([
    $class: 'GitSCM',
    extensions: [[$class: 'CloneOption', shallow: true, depth: 1]],
    branches: [[name: 'main']],
    userRemoteConfigs: [[url: 'https://github.com/org/repo.git', credentialsId: 'git-creds']]
])
```"""))

a("no-credentials-scm", "No Credentials Found for SCM in Jenkins", "Fix 'no credentials found' errors for SCM checkout in Jenkins. Resolve missing credential configuration.", textwrap.dedent("""Jenkins requires credentials to access private repositories. When the specified credential ID does not exist, the checkout fails.

## Common Causes

- Credential ID typo in Jenkinsfile
- Credential was deleted
- Credential is in a different scope (folder vs global)

## How to Fix

```bash
# Manage Jenkins > Credentials > System > Global credentials
# Add credentials with the correct ID
```

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ list-credentials system::system::jenkins
```"""))

a("branch-not-found", "Git Branch Not Found in Jenkins Pipeline", "Fix git branch not found errors in Jenkins. Resolve branch checkout failures in multibranch pipelines.", textwrap.dedent("""Jenkins fails when trying to check out a branch that does not exist in the remote repository.

## Common Causes

- Branch was deleted
- Typo in the branch name (`main` vs `master`)
- Default branch name changed

## How to Fix

```groovy
branches: [[name: 'main']]
```

```bash
git ls-remote --heads https://github.com/org/repo.git
```

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'Branch to build')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: params.BRANCH, url: 'https://github.com/org/repo.git'
            }
        }
    }
}
```"""))

a("commit-not-found", "Git Commit Not Found in Jenkins Pipeline", "Fix git commit not found errors in Jenkins pipeline. Resolve SHA checkout failures and ref issues.", textwrap.dedent("""Jenkins fails when trying to check out a specific commit SHA that does not exist.

## Common Causes

- Commit was rebased or force-pushed away
- Shallow clone does not include the target commit
- Webhook payload contains a stale SHA

## How to Fix

```groovy
branches: [[name: 'main']]
```

```groovy
extensions: [
    [$class: 'CloneOption', depth: 0],
    [$class: 'BuildChooserSetting', buildChooser: [$class: 'DefaultBuildChooser']]
]
```"""))

a("scm-polling-failed", "Jenkins SCM Polling Failed", "Fix Jenkins SCM polling failures. Resolve polling errors in Jenkinsfile and scheduled build triggers.", textwrap.dedent("""SCM polling periodically checks the repository for changes. When polling fails, Jenkins cannot detect new commits.

## Common Causes

- Credentials for polling have expired
- Repository URL changed or unavailable
- Network connectivity issues

## How to Fix

```groovy
pipeline {
    triggers { pollSCM('H/5 * * * *') }
    stages {
        stage('Build') {
            steps { checkout scm }
        }
    }
}
```

### Switch to Webhook Triggering

```groovy
pipeline {
    triggers { githubPush() }
    stages { ... }
}
```"""))

a("mercurial-error", "Jenkins Mercurial SCM Error", "Fix Mercurial SCM errors in Jenkins pipeline. Resolve Hg repository checkout and polling failures.", textwrap.dedent("""Mercurial (Hg) SCM errors occur when Jenkins cannot communicate with or checkout from a Mercurial repository.

## Common Causes

- Mercurial plugin not installed or outdated
- `hg` command not available on the agent
- Repository URL is incorrect

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Mercurial"
which hg || apt-get install mercurial
```

```groovy
checkout([
    $class: 'MercurialSCM',
    source: 'ssh://hg@hg.example.com/repo',
    credentialsId: 'hg-ssh-key',
    branches: [[name: 'default']]
])
```"""))

a("svn-error", "Jenkins Subversion (SVN) Error", "Fix Subversion SCM errors in Jenkins pipeline. Resolve SVN checkout, update, and authentication failures.", textwrap.dedent("""SVN errors in Jenkins occur when the pipeline cannot checkout or update from a Subversion repository.

## Common Causes

- SVN credentials not configured or expired
- Repository URL changed
- Subversion plugin not installed
- SSL certificate issues

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Subversion"
```

```groovy
checkout([
    $class: 'SubversionSCM',
    locations: [[url: 'https://svn.example.com/repo/trunk', credentialsId: 'svn-creds']],
    workspaceUpdater: [$class: 'UpdateUpdater']
])
```"""))

a("github-webhook-not-received", "GitHub Webhook Not Received by Jenkins", "Fix GitHub webhook not triggering Jenkins builds. Resolve webhook configuration and connectivity issues.", textwrap.dedent("""GitHub webhooks fail to trigger Jenkins builds when the webhook cannot reach the Jenkins server.

## Common Causes

- Jenkins URL not accessible from GitHub
- Webhook URL misconfigured
- Jenkins behind a reverse proxy without proper forwarding
- Webhook secret mismatch

## How to Fix

```groovy
pipeline {
    triggers { githubPush() }
    stages {
        stage('Build') {
            steps { checkout scm }
        }
    }
}
```

```bash
# GitHub > Repository > Settings > Webhooks > Add webhook
# Payload URL: https://jenkins.example.com/github-webhook/
```"""))

a("bitbucket-integration-error", "Jenkins Bitbucket Integration Error", "Fix Jenkins Bitbucket integration errors. Resolve Bitbucket webhook and SCM connection issues.", textwrap.dedent("""Bitbucket integration errors occur when Jenkins cannot properly connect to Bitbucket for SCM operations or receive webhooks.

## Common Causes

- Bitbucket plugin not installed or misconfigured
- Webhook URL not accessible from Bitbucket
- Credentials mismatch

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Bitbucket"
```

```groovy
pipeline {
    agent any
    triggers { bitbucketPush() }
    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']],
                    userRemoteConfigs: [[url: 'https://bitbucket.org/myorg/myrepo.git', credentialsId: 'bitbucket-app-password']]
                ])
            }
        }
    }
}
```"""))

a("gitlab-mr-trigger-error", "Jenkins GitLab Merge Request Trigger Error", "Fix Jenkins GitLab merge request trigger errors. Resolve GitLab webhook and MR build configuration issues.", textwrap.dedent("""GitLab merge request triggers fail when Jenkins cannot receive or process webhook events from GitLab.

## Common Causes

- GitLab plugin not installed or misconfigured
- Jenkins URL not accessible from GitLab
- Secret token mismatch

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "GitLab"
```

```groovy
properties([
    gitLabConnection('gitlab.example.com'),
    [pipelineTriggers: [[$class: 'GitLabTrigger', triggerOnPush: true, triggerOnMergeRequest: true, branchFilterType: 'AllBranches']]]
])
```"""))

a("checkout-submodule-error", "Jenkins Git Submodule Checkout Error", "Fix Git submodule checkout errors in Jenkins pipeline. Resolve submodule initialization and update failures.", textwrap.dedent("""Git submodule errors occur when Jenkins fails to initialize or update submodules during checkout.

## Common Causes

- `.gitmodules` references wrong URLs
- Submodule repository is private
- Submodule commit does not exist

## How to Fix

```groovy
checkout([
    $class: 'GitSCM',
    branches: [[name: 'main']],
    userRemoteConfigs: [[url: env.GIT_URL]],
    extensions: [
        [$class: 'SubmoduleOption', disableSubmodules: false, recursiveSubmodules: true]
    ]
])
```"""))

a("shallow-clone-error", "Jenkins Shallow Clone Error", "Fix shallow clone errors in Jenkins pipeline. Resolve depth-related checkout failures and missing commits.", textwrap.dedent("""Shallow clone errors occur when the clone depth is insufficient to reach the required commit.

## Common Causes

- Clone depth too shallow
- Force push moved commits beyond the shallow window
- Build requires a commit from earlier than the depth

## How to Fix

```groovy
extensions: [[$class: 'CloneOption', depth: 50]]
```

### Use Full Clone

```groovy
extensions: [[$class: 'CloneOption', depth: 0]]
```"""))

a("git-lfs-error", "Jenkins Git LFS Error", "Fix Git LFS errors in Jenkins pipeline. Resolve Large File Storage checkout and pull failures.", textwrap.dedent("""Git LFS errors occur when Jenkins cannot properly checkout or pull large files tracked by Git LFS.

## Common Causes

- Git LFS not installed on the agent
- LFS credentials not configured
- LFS storage quota exceeded

## How to Fix

```bash
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
git lfs install
```

```groovy
checkout([
    $class: 'GitSCM',
    branches: [[name: 'main']],
    userRemoteConfigs: [[url: env.GIT_URL, credentialsId: 'git-lfs-creds']],
    extensions: [[$class: 'LfsCheckout']]
])
```"""))

a("scm-changelog-error", "Jenkins SCM Changelog Error", "Fix Jenkins SCM changelog generation errors. Resolve changelog parsing and display issues.", textwrap.dedent("""SCM changelog errors occur when Jenkins cannot generate a valid changelog from the repository.

## Common Causes

- Repository history is corrupted or shallow
- Changelog includes commits from multiple branches
- Large number of commits

## How to Fix

```groovy
checkout([
    $class: 'GitSCM',
    branches: [[name: 'main']],
    userRemoteConfigs: [[url: env.GIT_URL]],
    extensions: [
        [$class: 'ChangelogToBranch', options: [compareRemote: 'origin', compareTarget: 'main']]
    ]
])
```"""))

# 3. Build errors (16)
a("maven-build-failed", "Maven Build Failed in Jenkins Pipeline", "Fix Maven build failures in Jenkins pipeline. Resolve dependency, compilation, and test failures.", textwrap.dedent("""Maven build failures occur when `mvn` commands exit with a non-zero status.

## Common Causes

- Dependency download failure
- Compilation errors
- Test failures
- Out of memory during compilation

## How to Fix

```groovy
pipeline {
    agent any
    tools { maven 'Maven-3.9'; jdk 'JDK-17' }
    stages {
        stage('Build') {
            steps { sh 'mvn clean compile -B' }
        }
    }
}
```

```bash
export MAVEN_OPTS="-Xmx2g -XX:MaxMetaspaceSize=512m"
mvn clean package -B
```"""))

a("gradle-build-failed", "Gradle Build Failed in Jenkins Pipeline", "Fix Gradle build failures in Jenkins pipeline. Resolve dependency, task, and memory issues.", textwrap.dedent("""Gradle build failures occur when the `gradle` or `./gradlew` command exits with a non-zero status.

## Common Causes

- Dependency resolution failure
- Gradle daemon OOM
- Wrapper version mismatch
- Corrupted cached dependencies

## How to Fix

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps { sh './gradlew clean build -x test --no-daemon' }
        }
    }
}
```

```groovy
environment { GRADLE_OPTS = '-Xmx2g -Dorg.gradle.daemon=false' }
```"""))

a("npm-install-failed", "NPM Install Failed in Jenkins Pipeline", "Fix npm install failures in Jenkins pipeline. Resolve Node.js dependency installation issues.", textwrap.dedent("""NPM install failures occur when `npm install` or `npm ci` cannot install dependencies.

## Common Causes

- npm registry unreachable or rate limited
- `package-lock.json` out of sync
- Native module compilation fails
- Disk space exhausted

## How to Fix

```groovy
pipeline {
    agent any
    tools { nodejs 'Node-18' }
    stages {
        stage('Install') { steps { sh 'npm ci --prefer-offline' } }
    }
}
```"""))

a("docker-build-failed", "Docker Build Failed in Jenkins Pipeline", "Fix Docker build failures in Jenkins pipeline. Resolve Dockerfile errors and image build issues.", textwrap.dedent("""Docker build failures occur when `docker build` cannot create the image from the Dockerfile.

## Common Causes

- Dockerfile syntax errors
- Base image not found
- Docker daemon not running
- Out of disk space

## How to Fix

```groovy
pipeline {
    agent { label 'docker' }
    stages {
        stage('Build Image') {
            steps { sh 'docker build -t myapp:${BUILD_NUMBER} .' }
        }
    }
}
```

```bash
docker system prune -f
```"""))

a("compiler-error", "Compiler Error in Jenkins Build", "Fix compiler errors in Jenkins builds. Resolve Java, C++, and other compilation failures.", textwrap.dedent("""Compiler errors occur when the source code cannot be compiled.

## Common Causes

- Syntax errors in source code
- Missing imports
- Incompatible compiler version

## How to Fix

```groovy
tools { jdk 'JDK-17'; maven 'Maven-3.9' }
```

```groovy
pipeline {
    agent any
    tools { jdk 'JDK-17' }
    stages {
        stage('Compile') { steps { sh 'mvn compile -B' } }
        stage('Package') { steps { sh 'mvn package -B -DskipTests' } }
    }
}
```"""))

a("test-failure-exit-code", "Test Failure Exit Code in Jenkins Build", "Fix test failure exit codes in Jenkins builds. Resolve failing tests and build abort issues.", textwrap.dedent("""Test failures cause the build to fail with a non-zero exit code.

## Common Causes

- Legitimate test failures
- Flaky tests
- Test environment issues
- Test timeout exceeded

## How to Fix

```groovy
stage('Test') {
    steps {
        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
            sh 'mvn test -B'
        }
    }
}
```

```groovy
post { always { junit '**/surefire-reports/*.xml' } }
```"""))

a("archive-artifacts-not-found", "Archive Artifacts Not Found in Jenkins Build", "Fix archive artifacts not found errors in Jenkins. Resolve missing artifact archiving issues.", textwrap.dedent("""The `archiveArtifacts` step fails when the specified artifact patterns do not match any files.

## Common Causes

- Build step did not produce expected output
- Artifact pattern does not match actual paths
- Build failed before producing artifacts

## How to Fix

```groovy
archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
archiveArtifacts artifacts: 'dist/**/*', fingerprint: true
archiveArtifacts artifacts: 'build/reports/**/*', allowEmptyArchive: true
```"""))

a("junit-report-not-found", "JUnit Report Not Found in Jenkins Build", "Fix JUnit report not found errors in Jenkins. Resolve test report archiving and display issues.", textwrap.dedent("""The `junit` step fails when no test result XML files match the specified pattern.

## Common Causes

- Test step did not run
- Report path pattern is wrong
- Build was aborted before tests completed

## How to Fix

```groovy
post {
    always {
        junit allowEmptyResults: true, testResults: '**/surefire-reports/*.xml'
    }
}
```

### Common Test Report Locations

```groovy
junit '**/surefire-reports/*.xml'    // Maven
junit '**/build/test-results/**/*.xml' // Gradle
junit 'test-results/*.xml'            // Jest
```"""))

a("build-unstable-vs-failed", "Jenkins Build Unstable vs Failed Status", "Fix Jenkins build unstable vs failed status. Resolve unstable build causes and reporting.", textwrap.dedent("""An unstable build is a middle state between success and failure. Jenkins marks builds as unstable when quality thresholds are not met.

## Common Causes

- Test failures marked as non-fatal
- Code coverage below threshold
- Warning thresholds exceeded

## How to Fix

```groovy
stage('Quality Check') {
    steps {
        script {
            def result = sh(script: 'checkstyle', returnStatus: true)
            if (result != 0) { unstable('Checkstyle warnings found') }
        }
    }
}
```"""))

a("build-timeout", "Jenkins Build Timeout", "Fix Jenkins build timeout errors. Resolve build duration exceeding configured limits.", textwrap.dedent("""Build timeouts occur when a Jenkins build exceeds the configured maximum duration.

## Common Causes

- Long-running tests without timeout
- Infinite loops in build scripts
- Waiting for external resources

## How to Fix

```groovy
pipeline {
    agent any
    options { timeout(time: 60, unit: 'MINUTES'); timestamps() }
    stages {
        stage('Build') {
            timeout(time: 10, unit: 'MINUTES') { sh 'make build' }
        }
        stage('Test') {
            timeout(time: 15, unit: 'MINUTES') { sh 'make test' }
        }
    }
}
```"""))

a("build-queue-too-long", "Jenkins Build Queue Too Long", "Fix Jenkins build queue backlog issues. Resolve long queue wait times and build scheduling.", textwrap.dedent("""Build queue issues occur when too many builds are queued and waiting for available executors.

## Common Causes

- Not enough executors
- Long-running builds holding executors
- Incorrect agent labels

## How to Fix

```groovy
properties([
    disableConcurrentBuilds(),
    buildDiscarder(logRotator(numToKeepStr: '10'))
])
```

```groovy
lock(resource: 'deploy-env', inversePrecedence: true) {
    sh './deploy.sh'
}
```"""))

a("executor-not-available", "Jenkins Executor Not Available", "Fix Jenkins executor not available errors. Resolve build scheduling and agent allocation issues.", textwrap.dedent("""The `executor not available` error means Jenkins cannot find a free executor to run the build.

## Common Causes

- All executors busy
- Agent offline
- Label mismatch

## How to Fix

```groovy
pipeline { agent any ... }
```

```bash
# Manage Jenkins > Manage Clouds > Add Kubernetes or Docker cloud
```"""))

a("node-offline", "Jenkins Node Offline Error", "Fix Jenkins node offline errors. Resolve agent connectivity and availability issues.", textwrap.dedent("""A node goes offline when Jenkins cannot communicate with the agent.

## Common Causes

- Agent machine is down
- JNLP agent lost connection
- SSH connection timed out
- Agent JVM crashed

## How to Fix

```bash
# Jenkins > Manage Jenkins > Manage Nodes > Click node > "Reconnect"
```

```bash
java -jar agent.jar -url http://jenkins:8080 -secret @secret-file -name my-agent -retry 3
```"""))

a("label-not-found", "Jenkins Agent Label Not Found", "Fix Jenkins agent label not found errors. Resolve label expression matching issues.", textwrap.dedent("""Jenkins uses labels to match builds to agents. When no agent matches, the build waits.

## Common Causes

- Label does not match any agent
- Agent offline
- Typo in label name

## How to Fix

```groovy
agent { label 'linux' }
agent { label 'linux && docker' }
agent { label 'linux || any' }
agent any
```"""))

a("agent-disconnected", "Jenkins Agent Disconnected During Build", "Fix Jenkins agent disconnection during builds. Resolve agent connectivity drops and build failures.", textwrap.dedent("""Agent disconnection occurs when the agent loses connection to Jenkins master.

## Common Causes

- Network instability
- Agent JVM crashed
- Master restarted during builds

## How to Fix

```bash
java -jar agent.jar -url http://jenkins:8080 -secret @secret-file -name my-agent -failAfter 300 -retry 5
```

### Use WebSocket Transport

```bash
# Manage Jenkins > Manage Nodes > Agent > Inbound agents > WebSocket
```"""))

a("tool-not-configured", "Jenkins Tool Not Configured Error", "Fix Jenkins tool not configured errors. Resolve missing build tool configuration in Jenkins.", textwrap.dedent("""The `tools` directive requires the tool to be configured in Global Tool Configuration.

## Common Causes

- Tool not installed
- Tool name mismatch
- Tool auto-installation failed

## How to Fix

```bash
# Manage Jenkins > Global Tool Configuration > Add JDK, Maven, etc.
```

```groovy
pipeline {
    agent any
    tools { maven 'Maven-3.9'; jdk 'JDK-17'; nodejs 'Node-18' }
    stages {
        stage('Build') {
            steps { sh 'mvn --version' }
        }
    }
}
```"""))

# 4. Credential/Secret errors (10)
a("credentials-not-found", "Jenkins Credentials Not Found", "Fix Jenkins credentials not found errors. Resolve missing credential configuration and access issues.", textwrap.dedent("""Jenkins credentials not found errors occur when the pipeline references a credential ID that does not exist.

## Common Causes

- Credential ID typo
- Credential was deleted
- Credential in different scope (folder vs global)

## How to Fix

```bash
# Manage Jenkins > Credentials > System > Global credentials
```

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ list-credentials system::system::jenkins
```"""))

a("username-password-not-found", "Jenkins Username Password Credentials Not Found", "Fix Jenkins username/password credential lookup errors. Resolve credential binding failures.", textwrap.dedent("""The `usernamePassword` credential binding fails when the credential ID does not exist or is wrong type.

## How to Fix

```groovy
withCredentials([usernamePassword(credentialsId: 'github-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
    sh 'echo "User: $USERNAME"'
}
```"""))

a("ssh-key-not-added", "Jenkins SSH Key Not Added Error", "Fix Jenkins SSH key not added errors. Resolve SSH credential configuration and access issues.", textwrap.dedent("""SSH key errors occur when Jenkins tries to use an SSH key that is not properly configured.

## How to Fix

```bash
# Manage Jenkins > Credentials > System > Global credentials
# Kind: SSH Username with private key
```

```groovy
withCredentials([sshUserPrivateKey(credentialsId: 'deploy-ssh-key', keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER')]) {
    sh 'ssh -i $SSH_KEY -o StrictHostKeyChecking=no $SSH_USER@server.example.com "ls"'
}
```"""))

a("secret-text-not-found", "Jenkins Secret Text Not Found", "Fix Jenkins secret text credential not found errors. Resolve secret text binding failures.", textwrap.dedent("""The `string` credential binding for secret text fails when the credential ID does not exist.

## How to Fix

```bash
# Manage Jenkins > Credentials > System > Global credentials
# Kind: Secret text
```

```groovy
withCredentials([string(credentialsId: 'my-secret-text', variable: 'TOKEN')]) {
    sh 'curl -H "Authorization: Bearer $TOKEN" https://api.example.com'
}
```"""))

a("decryption-failed", "Jenkins Credential Decryption Failed", "Fix Jenkins credential decryption failures. Resolve encrypted credential access and key issues.", textwrap.dedent("""Decryption failures occur when Jenkins cannot decrypt stored credentials.

## Common Causes

- Master key changed
- Credentials copied from different instance
- `credentials.xml` is corrupted

## How to Fix

```bash
ls -la $JENKINS_HOME/credentials.xml
# Delete and re-add credentials through Jenkins UI
```"""))

a("inject-passwords-error", "Jenkins Inject Passwords Error", "Fix Jenkins inject passwords step errors. Resolve password injection and credential binding failures.", textwrap.dedent("""The `injectPasswords` step fails when it cannot inject the specified credentials.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Credentials Binding"
```

```groovy
withCredentials([
    string(credentialsId: 'api-key', variable: 'API_KEY'),
    usernamePassword(credentialsId: 'db-creds', usernameVariable: 'DB_USER', passwordVariable: 'DB_PASS'),
    file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')
]) {
    sh "echo \$API_KEY"
}
```"""))

a("folder-credential-not-found", "Jenkins Folder Credential Not Found", "Fix Jenkins folder-scoped credential not found errors. Resolve credential scope and access issues.", textwrap.dedent("""Folder-scoped credentials are only accessible within the folder where they are defined.

## How to Fix

```groovy
withCredentials([string(credentialsId: 'my-folder/my-cred', variable: 'TOKEN')]) {
    sh 'echo $TOKEN'
}
```"""))

a("domain-credential-missing", "Jenkins Domain Credential Missing", "Fix Jenkins domain credential missing errors. Resolve domain-scoped credential configuration issues.", textwrap.dedent("""Jenkins organizes credentials into domains. When a credential is stored in a specific domain but referenced from a different domain, it cannot be found.

## How to Fix

```bash
# Manage Jenkins > Credentials > System > Global credentials
# Store credentials in the default (global) domain
```

```groovy
withCredentials([string(credentialsId: 'my-domain/credential-id', variable: 'SECRET')]) {
    sh 'echo $SECRET'
}
```"""))

# 5. Plugin errors (10)
a("plugin-missing", "Jenkins Plugin Missing Error", "Fix Jenkins missing plugin errors. Resolve plugin installation and dependency issues.", textwrap.dedent("""Jenkins plugins provide additional functionality. When a required plugin is missing, pipeline steps become unavailable.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install required plugin
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin workflow-aggregator
java -jar jenkins-cli.jar -s http://localhost:8080/ safe-restart
```

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ list-plugins | grep "workflow"
```"""))

a("plugin-version-conflict", "Jenkins Plugin Version Conflict", "Fix Jenkins plugin version conflict errors. Resolve incompatible plugin version and dependency issues.", textwrap.dedent("""Plugin version conflicts occur when installed plugins have incompatible version requirements.

## How to Fix

```bash
# Manage Jenkins > Plugins > Updates > Update all plugins
java -jar jenkins-cli.jar -s http://localhost:8080/ list-plugins --output txt
```"""))

a("plugin-failed-to-load", "Jenkins Plugin Failed to Load", "Fix Jenkins plugin failed to load errors. Resolve plugin initialization and startup issues.", textwrap.dedent("""Plugins fail to load during Jenkins startup when they encounter errors during initialization.

## How to Fix

```bash
# Manage Jenkins > System Log
# Or: $JENKINS_HOME/logs/
```

```bash
mkdir -p $JENKINS_HOME/plugins.disabled
mv $JENKINS_HOME/plugins/my-plugin.jpi $JENKINS_HOME/plugins.disabled/
```"""))

a("plugin-dependency-error", "Jenkins Plugin Dependency Error", "Fix Jenkins plugin dependency errors. Resolve missing or incompatible plugin dependencies.", textwrap.dedent("""Plugin dependency errors occur when a plugin cannot find required dependencies.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install the plugin (auto-installs deps)
java -jar jenkins-cli.jar -s http://localhost:8080/ list-plugins --output txt | grep "Missing"
```"""))

a("plugin-not-updated", "Jenkins Plugin Not Updated Warning", "Fix Jenkins plugin update warnings and security vulnerabilities. Resolve outdated plugin issues.", textwrap.dedent("""Outdated plugins may contain security vulnerabilities or bugs.

## How to Fix

```bash
# Manage Jenkins > Plugins > Updates
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin plugin-name:latest
java -jar jenkins-cli.jar -s http://localhost:8080/ safe-restart
```

Monitor: https://www.jenkins.io/security/advisories/"""))

a("matrix-auth-error", "Jenkins Matrix Authorization Error", "Fix Jenkins matrix authorization strategy errors. Resolve permission and access control issues.", textwrap.dedent("""Matrix authorization allows fine-grained permission control. Errors occur when configuration is incorrect.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Authorization
# Select "Matrix-based security" or "Role-based Authorization Strategy"
# Add users/groups with required permissions
```

Minimum permissions: Overall/Read, Job/Read, Job/Build, Job/Workspace"""))

a("active-directory-error", "Jenkins Active Directory Plugin Error", "Fix Jenkins Active Directory plugin errors. Resolve AD authentication and LDAP integration issues.", textwrap.dedent("""Active Directory plugin errors occur when Jenkins cannot authenticate users against AD/LDAP.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Security Realm > Active Directory
# Domain: example.com
# LDAP server: ad.example.com:636
```

```bash
ldapsearch -H ldaps://ad.example.com:636 -D "cn=jenkins,ou=service,dc=example,dc=com" -W -b "dc=example,dc=com" "(sAMAccountName=testuser)"
```"""))

a("blue-ocean-error", "Jenkins Blue Ocean Plugin Error", "Fix Jenkins Blue Ocean plugin errors. Resolve Blue Ocean installation and UI issues.", textwrap.dedent("""Blue Ocean provides a modern UI for Jenkins pipelines.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Blue Ocean"
# Required: workflow-aggregator, git, blueocean-commons
```"""))

a("credentials-plugin-error", "Jenkins Credentials Plugin Error", "Fix Jenkins credentials plugin errors. Resolve credentials plugin installation and configuration issues.", textwrap.dedent("""The credentials plugin is essential for managing secrets in Jenkins.

## How to Fix

```bash
rm $JENKINS_HOME/plugins/credentials.jpi*
# Install via Manage Jenkins > Plugins
xmllint --noout $JENKINS_HOME/credentials.xml
```"""))

a("docker-pipeline-plugin-error", "Jenkins Docker Pipeline Plugin Error", "Fix Jenkins Docker Pipeline plugin errors. Resolve docker-workflow plugin configuration issues.", textwrap.dedent("""The Docker Pipeline plugin allows using Docker agents in pipelines.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Docker Pipeline"
docker --version
sudo usermod -aG docker jenkins
```

```groovy
pipeline {
    agent { docker { image 'maven:3.9-jdk-17' } }
    stages {
        stage('Build') { steps { sh 'mvn clean package -B' } }
    }
}
```"""))

a("kubernetes-plugin-error", "Jenkins Kubernetes Plugin Error", "Fix Jenkins Kubernetes plugin errors. Resolve Kubernetes agent provisioning and pod template issues.", textwrap.dedent("""The Kubernetes plugin allows Jenkins to dynamically provision agents as pods.

## How to Fix

```bash
# Manage Jenkins > Manage Clouds > Add cloud > Kubernetes
# Kubernetes URL: https://kubernetes.default.svc
```

```groovy
pipeline {
    agent {
        kubernetes {
            yaml '''
                apiVersion: v1
                kind: Pod
                spec:
                  containers:
                  - name: maven
                    image: maven:3.9-jdk-17
                    command: ['sleep']
                    args: ['infinity']
            '''
        }
    }
    stages {
        stage('Build') {
            steps {
                container('maven') { sh 'mvn clean package -B' }
            }
        }
    }
}
```"""))

a("workflow-aggregator-missing", "Jenkins Workflow Aggregator Plugin Missing", "Fix Jenkins workflow-aggregator plugin missing error. Resolve pipeline plugin installation issues.", textwrap.dedent("""The `workflow-aggregator` plugin is the core plugin for Jenkins Pipeline.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Pipeline: Aggregator"
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin workflow-aggregator workflow-step-api workflow-cps
java -jar jenkins-cli.jar -s http://localhost:8080/ safe-restart
```"""))

# 6. Agent/node errors (12)
a("agent-not-available", "Jenkins Agent Not Available", "Fix Jenkins agent not available errors. Resolve agent allocation and scheduling failures.", textwrap.dedent("""The `agent not available` error means Jenkins cannot allocate an agent.

## Common Causes

- All matching agents offline or at capacity
- Label expression mismatch

## How to Fix

```groovy
pipeline { agent any ... }
```

```groovy
pipeline { agent { label 'linux || docker || any' } ... }
```"""))

a("node-not-found", "Jenkins Node Not Found", "Fix Jenkins node not found errors. Resolve agent node registration and availability issues.", textwrap.dedent("""Jenkins cannot find the specified node.

## How to Fix

```bash
# Jenkins > Manage Jenkins > Manage Nodes
java -jar agent.jar -url http://jenkins:8080 -secret @secret-file -name my-node
```"""))

a("label-expression-no-match", "Jenkins Label Expression No Match", "Fix Jenkins label expression no match errors. Resolve agent label expression evaluation failures.", textwrap.dedent("""Label expressions use boolean logic. When no agent satisfies the expression, the build waits.

## How to Fix

```groovy
agent { label 'linux && docker && gpu && fast' }  // complex
agent { label 'linux' }                            // simpler
agent { label 'fast-server || linux' }             // with fallback
```"""))

a("executors-busy", "Jenkins Executors All Busy", "Fix Jenkins executors all busy errors. Resolve executor capacity and build scheduling issues.", textwrap.dedent("""All executors on matching agents are busy.

## How to Fix

```groovy
properties([disableConcurrentBuilds()])
```

```groovy
lock(resource: 'build-server', inversePrecedence: true) { sh 'make build' }
```

```bash
# Manage Jenkins > Manage Nodes > Node > Configure > # of executors
```"""))

a("cloud-agent-provisioning-failed", "Jenkins Cloud Agent Provisioning Failed", "Fix Jenkins cloud agent provisioning failures. Resolve Kubernetes, Docker, and EC2 agent provisioning issues.", textwrap.dedent("""Cloud agent provisioning fails when Jenkins cannot create dynamic agents.

## How to Fix

```bash
# Manage Jenkins > Manage Clouds > Select cloud > Verify connection
kubectl get pods
aws sts get-caller-identity
```"""))

a("docker-agent-failed", "Jenkins Docker Agent Failed", "Fix Jenkins Docker agent failures. Resolve Docker agent container creation and connectivity issues.", textwrap.dedent("""Docker agent failures occur when Jenkins cannot create or connect to a Docker container agent.

## How to Fix

```bash
docker info
docker ps
sudo usermod -aG docker jenkins
```

```groovy
pipeline {
    agent { docker { image 'maven:3.9-jdk-17'; args '-v $HOME/.m2:/root/.m2 --memory 2g' } }
    stages { stage('Build') { steps { sh 'mvn clean package -B' } } }
}
```"""))

a("ssh-agent-connection-error", "Jenkins SSH Agent Connection Error", "Fix Jenkins SSH agent connection errors. Resolve SSH agent launcher and connectivity issues.", textwrap.dedent("""SSH agent connection errors occur when Jenkins cannot SSH into a remote agent.

## How to Fix

```bash
ssh -o StrictHostKeyChecking=no user@agent-host "java -version"
ssh-keyscan agent.example.com >> ~/.ssh/known_hosts
```"""))

a("jnlp-agent-disconnected", "Jenkins JNLP Agent Disconnected", "Fix Jenkins JNLP agent disconnection errors. Resolve inbound agent connectivity and stability issues.", textwrap.dedent("""JNLP agents connect to Jenkins via an outbound connection. Disconnections occur when the connection drops.

## How to Fix

```bash
java -jar agent.jar -url http://jenkins:8080 -secret @secret -name my-agent -retry 5
```

### Use WebSocket Transport

```bash
# Manage Jenkins > Manage Nodes > Agent > Enable WebSocket
```"""))

a("inbound-tcp-agent-error", "Jenkins Inbound TCP Agent Error", "Fix Jenkins inbound TCP agent connection errors. Resolve TCP agent port and firewall issues.", textwrap.dedent("""Inbound TCP agents connect on a specific TCP port. Connection errors occur when the port is blocked.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Agent protocols > Enable TCP port
sudo ufw allow 50000/tcp
# Or: sudo iptables -A INPUT -p tcp --dport 50000 -j ACCEPT
```

### Use WebSocket Instead

```bash
# Manage Jenkins > Configure Security > Enable WebSocket
```"""))

a("agent-memory-exhausted", "Jenkins Agent Memory Exhausted", "Fix Jenkins agent memory exhaustion errors. Resolve OutOfMemoryError and agent JVM crashes.", textwrap.dedent("""Agent memory exhaustion occurs when the agent JVM runs out of memory.

## How to Fix

```bash
export JAVA_OPTS="-Xmx4g -XX:MaxMetaspaceSize=512m"
java $JAVA_OPTS -jar agent.jar -url http://jenkins:8080 -secret @secret
```

```groovy
properties([disableConcurrentBuilds()])
environment { MAVEN_OPTS = '-Xmx2g'; GRADLE_OPTS = '-Xmx2g' }
```"""))

# 7. Job/Configuration errors (12)
a("job-name-invalid", "Jenkins Job Name Invalid", "Fix Jenkins invalid job name errors. Resolve job naming convention and character issues.", textwrap.dedent("""Job names must follow specific naming rules.

## Valid Characters

Letters, numbers, hyphens, underscores. No spaces, slashes, colons.

```
my-project    valid
my_project    valid
My Project    invalid (spaces)
my/project    invalid (slash)
```"""))

a("downstream-job-failed", "Jenkins Downstream Job Failed", "Fix Jenkins downstream job failure errors. Resolve build dependency and trigger chain issues.", textwrap.dedent("""Downstream jobs are triggered by upstream jobs. When downstream fails, upstream may also be affected.

## How to Fix

```groovy
stage('Trigger Downstream') {
    steps {
        build job: 'my-downstream-job', parameters: [string(name: 'VERSION', value: env.BUILD_VERSION)]
    }
}
```

```groovy
stage('Trigger Downstream') {
    steps {
        script {
            try { build job: 'my-downstream-job' }
            catch (err) {
                echo "Downstream job failed: ${err.message}"
                currentBuild.result = 'UNSTABLE'
            }
        }
    }
}
```"""))

a("upstream-job-trigger", "Jenkins Upstream Job Trigger Error", "Fix Jenkins upstream job trigger errors. Resolve build trigger and dependency chain issues.", textwrap.dedent("""Upstream triggers configure a job to start when another job completes.

## How to Fix

```bash
# Job > Configure > Build Triggers > Build after other projects > Watched items: upstream-job
```

```groovy
build job: 'upstream-job', wait: false
```"""))

a("parameterized-build-error", "Jenkins Parameterized Build Error", "Fix Jenkins parameterized build errors. Resolve parameter definition and value issues.", textwrap.dedent("""Parameterized builds allow passing values to jobs at build time.

## How to Fix

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'VERSION', defaultValue: '1.0.0', description: 'App version')
        choice(name: 'ENV', choices: ['dev', 'staging', 'prod'], description: 'Target env')
        booleanParam(name: 'SKIP_TESTS', defaultValue: false)
    }
    stages {
        stage('Build') {
            steps {
                echo "Building ${params.VERSION} for ${params.ENV}"
                sh "make VERSION=${params.VERSION} ENV=${params.ENV}"
            }
        }
    }
}
```"""))

a("choice-parameter-not-found", "Jenkins Choice Parameter Not Found", "Fix Jenkins choice parameter not found errors. Resolve choice parameter definition and access issues.", textwrap.dedent("""Choice parameters provide a dropdown list of options.

## How to Fix

```groovy
parameters {
    choice(name: 'DEPLOY_ENV', choices: ['development', 'staging', 'production'])
}
```

```groovy
def env = params.DEPLOY_ENV
echo "Deploying to: ${env}"
```"""))

a("build-trigger-cycle", "Jenkins Build Trigger Cycle Detected", "Fix Jenkins build trigger cycle errors. Resolve infinite trigger loops and circular dependencies.", textwrap.dedent("""Build trigger cycles occur when jobs trigger each other in a loop.

## How to Fix

```groovy
def isUpstreamTrigger() {
    return currentBuild.getBuildCauses('hudson.model.Cause$UpstreamCause').size() > 0
}

pipeline {
    agent any
    stages {
        stage('Build') {
            when { expression { !isUpstreamTrigger() } }
            steps { sh 'make build' }
        }
    }
}
```"""))

a("poll-scm-error", "Jenkins Poll SCM Configuration Error", "Fix Jenkins Poll SCM configuration errors. Resolve SCM polling schedule and trigger issues.", textwrap.dedent("""Poll SCM configuration errors prevent Jenkins from checking for changes.

## How to Fix

```groovy
pipeline {
    agent any
    triggers { pollSCM('H/5 * * * *') }
    stages {
        stage('Checkout') { steps { checkout scm } }
    }
}
```

### Use Webhook Instead

```groovy
pipeline { triggers { githubPush() } ... }
```"""))

a("concurrent-build-disabled", "Jenkins Concurrent Build Disabled", "Fix Jenkins concurrent build disabled errors. Resolve build queue and concurrent execution settings.", textwrap.dedent("""When concurrent builds are disabled, new builds cannot start while others are running.

## How to Fix

```groovy
options { disableConcurrentBuilds() }
```

```groovy
lock(resource: 'deploy-server', inversePrecedence: true) {
    sh './deploy.sh'
}
```"""))

a("build-discarder-error", "Jenkins Build Discarder Error", "Fix Jenkins build discarder configuration errors. Resolve build log rotation and retention issues.", textwrap.dedent("""Build discarder settings control how many builds are retained.

## How to Fix

```groovy
options {
    buildDiscarder(logRotator(daysToKeepStr: '30', numToKeepStr: '100', artifactDaysToKeepStr: '7', artifactNumToKeepStr: '10'))
}
```

```groovy
import jenkins.model.Jenkins
Jenkins.instance.getAllItems(Job.class).each { job ->
    job.builds.findAll { it.number < job.lastBuild.number - 100 }.each { it.delete() }
}
```"""))

# 8. Security/Authorization errors (11)
a("matrix-auth-permission-denied", "Jenkins Matrix Auth Permission Denied", "Fix Jenkins matrix authorization permission denied errors. Resolve user and role permission issues.", textwrap.dedent("""Permission denied errors occur when matrix authorization does not grant required permissions.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Authorization
# Add user/group with: Overall/Read, Job/Read, Job/Build, Job/Workspace
```

```groovy
def user = hudson.model.User.current()
println "Has Overall/Read: ${user?.hasPermission(hudson.model.Hudson.READ)}"
```"""))

a("anonymous-read-not-allowed", "Jenkins Anonymous Read Not Allowed", "Fix Jenkins anonymous read access denied errors. Resolve anonymous user permission issues.", textwrap.dedent("""Anonymous read not allowed means anonymous users cannot view Jenkins pages.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Authorization
# Matrix: anonymous > Overall/Read (check the box)
```"""))

a("overall-read-missing", "Jenkins Overall/Read Permission Missing", "Fix Jenkins Overall/Read permission errors. Resolve global read permission issues.", textwrap.dedent("""The `Overall/Read` permission is required to access most Jenkins pages.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Authorization
# Matrix: add user/group > Overall/Read
```"""))

a("job-build-missing", "Jenkins Job/Build Permission Missing", "Fix Jenkins Job/Build permission missing errors. Resolve build trigger permission issues.", textwrap.dedent("""The `Job/Build` permission is required to trigger builds.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Authorization
# Matrix: add user/group > Job/Build
```

Minimum permissions: Overall/Read, Job/Read, Job/Build, Job/Workspace"""))

a("role-based-strategy-error", "Jenkins Role-Based Strategy Error", "Fix Jenkins role-based authorization strategy errors. Resolve role configuration and assignment issues.", textwrap.dedent("""Role-based authorization allows defining roles with specific permissions.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Role-based Authorization Strategy"
# Manage Jenkins > Configure Security > Authorization > Role-Based Authorization Strategy
# Manage Roles > Add roles (admin, developer, viewer)
# Assign Roles > Map users/groups to roles
```"""))

a("folder-permission-denied", "Jenkins Folder Permission Denied", "Fix Jenkins folder permission denied errors. Resolve folder-level access control issues.", textwrap.dedent("""Folder permissions control access to jobs within folders.

## How to Fix

```bash
# Navigate to folder > Configure > Permissions
# Or use Role Strategy Plugin for folder-level roles
```

```groovy
withCredentials([string(credentialsId: 'my-folder/my-secret', variable: 'SECRET')]) {
    sh 'echo $SECRET'
}
```"""))

a("access-denied-for-user", "Jenkins Access Denied for User", "Fix Jenkins access denied errors for specific users. Resolve user authentication and authorization issues.", textwrap.dedent("""Access denied errors occur when a user is authenticated but not authorized.

## How to Fix

```groovy
import hudson.model.User
def user = User.get('username')
println user?.hasPermission(hudson.model.Hudson.READ)
```

```bash
# Manage Jenkins > Configure Security > Authorization > Add user with permissions
```"""))

a("csrf-protection-error", "Jenkins CSRF Protection Error", "Fix Jenkins CSRF protection errors. Resolve cross-site request forgery token issues.", textwrap.dedent("""CSRF protection requires a valid crumb token for POST requests.

## How to Fix

```bash
CRUMB=$(curl -s -u admin:token http://jenkins:8080/crumbIssuer/api/json | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['crumbRequestField']+':'+d['crumb'])")
curl -u admin:token -H "$CRUMB" -X POST http://jenkins:8080/job/my-job/build
```"""))

a("api-token-invalid", "Jenkins API Token Invalid", "Fix Jenkins API token invalid errors. Resolve API token authentication failures.", textwrap.dedent("""API tokens allow programmatic access to Jenkins.

## How to Fix

```bash
# Jenkins > User > Configure > API Token > Generate New Token
curl -u admin:abc123def456 http://jenkins:8080/api/json
```"""))

a("login-failed", "Jenkins Login Failed", "Fix Jenkins login failed errors. Resolve authentication and login issues.", textwrap.dedent("""Login failures occur when Jenkins cannot authenticate the user.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Security Realm
# Verify LDAP/AD settings
```

### Reset Admin Password

```bash
# Edit $JENKINS_HOME/users/admin/config.xml
# Remove <passwordHash> line, restart Jenkins, set new password
```"""))

a("signup-disabled", "Jenkins Signup Disabled Error", "Fix Jenkins signup disabled errors. Resolve user registration and self-signup issues.", textwrap.dedent("""Jenkins disables user self-registration by default.

## How to Fix

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ create-user --password mypass --email user@example.com newuser
```"""))

a("remember-me-error", "Jenkins Remember Me Error", "Fix Jenkins remember me login errors. Resolve persistent login and session issues.", textwrap.dedent("""Remember me allows users to stay logged in. Errors occur when sessions expire.

## How to Fix

```bash
# Manage Jenkins > Configure System > Jenkins URL
# https://jenkins.example.com/
```

Check reverse proxy cookie forwarding."""))

# 9. Artifact/Archive errors (10)
a("no-artifacts-found", "No Artifacts Found in Jenkins Build", "Fix no artifacts found errors in Jenkins. Resolve artifact generation and archiving issues.", textwrap.dedent("""No artifacts found means the build did not produce any matching files.

## How to Fix

```groovy
sh 'ls -la target/'
archiveArtifacts artifacts: 'target/*.jar', allowEmptyArchive: true, fingerprint: true
```"""))

a("artifact-file-too-large", "Jenkins Artifact File Too Large", "Fix Jenkins artifact file too large errors. Resolve artifact size limit and storage issues.", textwrap.dedent("""Artifact files that are too large consume excessive disk space.

## How to Fix

```groovy
archiveArtifacts artifacts: 'target/*.jar', excludes: '**/node_modules/**,**/target/classes/**'
```

```groovy
buildDiscarder(logRotator(numToKeepStr: '20', artifactNumToKeepStr: '5'))
```"""))

a("archive-on-master-only", "Jenkins Archive on Master Only Error", "Fix Jenkins archive on master only errors. Resolve artifact archiving restrictions.", textwrap.dedent("""The `archiveArtifacts` step only works on the master node by default.

## How to Fix

```groovy
node('remote-agent') {
    sh 'mvn package -B'
    stash includes: 'target/*.jar', name: 'artifacts'
}
node('master') {
    unstash 'artifacts'
    archiveArtifacts artifacts: 'target/*.jar'
}
```"""))

a("fingerprint-not-found", "Jenkins Fingerprint Not Found", "Fix Jenkins fingerprint not found errors. Resolve artifact fingerprint tracking issues.", textwrap.dedent("""Fingerprints track artifact usage across builds.

## How to Fix

```groovy
archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
```

```bash
# Jenkins > Fingerprint
```"""))

a("artifact-resolution-error", "Jenkins Artifact Resolution Error", "Fix Jenkins artifact resolution errors. Resolve cross-build artifact dependency issues.", textwrap.dedent("""Artifact resolution errors occur when Jenkins cannot find artifacts from a previous build.

## How to Fix

```groovy
copyArtifacts(projectName: 'upstream-job', filter: 'target/*.jar', selector: lastCompleted())
```

```groovy
buildDiscarder(logRotator(numToKeepStr: '50', artifactNumToKeepStr: '20'))
```"""))

a("copy-artifact-from-upstream", "Jenkins Copy Artifact from Upstream Error", "Fix Jenkins copy artifact from upstream errors. Resolve cross-build artifact copying issues.", textwrap.dedent("""Copy artifact errors occur when the Copy Artifact plugin cannot retrieve artifacts.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Copy Artifact"
```

```groovy
copyArtifacts(projectName: 'my-upstream-job', selector: lastSuccessful(), filter: 'target/*.jar')
```"""))

a("stash-file-not-found", "Jenkins Stash File Not Found", "Fix Jenkins stash file not found errors. Resolve stash/unstash file transfer issues.", textwrap.dedent("""Stash/unstash transfers files between nodes.

## How to Fix

```groovy
node('agent-a') {
    stash includes: 'build/**/*', name: 'my-build'
}
node('agent-b') {
    unstash 'my-build'
    archiveArtifacts artifacts: 'build/**/*'
}
```"""))

a("unstash-failed", "Jenkins Unstash Failed Error", "Fix Jenkins unstash failed errors. Resolve file restoration issues from stash.", textwrap.dedent("""Unstash fails when Jenkins cannot restore files from a previous stash.

## How to Fix

```groovy
try {
    unstash 'my-artifacts'
} catch (err) {
    echo "Failed to unstash: ${err.message}"
    sh 'make build'
}
```"""))

a("jar-cache-error", "Jenkins JAR Cache Error", "Fix Jenkins JAR cache errors. Resolve Java dependency cache and resolution issues.", textwrap.dedent("""JAR cache errors occur when Jenkins cannot cache or resolve JAR dependencies.

## How to Fix

```bash
rm -rf ~/.m2/repository
rm -rf ~/.gradle/caches
```

```groovy
environment { MAVEN_OPTS = "-Dmaven.repo.local=${WORKSPACE}/.m2/repository" }
```"""))

a("artifacts-retention-policy", "Jenkins Artifacts Retention Policy Error", "Fix Jenkins artifacts retention policy errors. Resolve artifact storage and cleanup issues.", textwrap.dedent("""Artifacts retention policy controls how long build artifacts are kept.

## How to Fix

```groovy
options {
    buildDiscarder(logRotator(numToKeepStr: '50', artifactDaysToKeepStr: '30', artifactNumToKeepStr: '10'))
}
```

```groovy
import jenkins.model.Jenkins
Jenkins.instance.getAllItems(Job.class).each { job ->
    def keep = 10
    def builds = job.builds.toList()
    if (builds.size() > keep) builds.drop(keep).each { it.delete() }
}
```"""))

# 10. REST API errors (10)
a("api-403-forbidden", "Jenkins REST API 403 Forbidden", "Fix Jenkins API 403 forbidden errors. Resolve API authentication and permission issues.", textwrap.dedent("""API calls return 403 when the authenticated user lacks permission.

## How to Fix

```bash
curl -u admin:valid-api-token http://jenkins:8080/api/json
```

```bash
CRUMB=$(curl -s -u admin:token http://jenkins:8080/crumbIssuer/api/json)
curl -u admin:token -H "$(echo $CRUMB | python3 -c 'import sys,json;d=json.load(sys.stdin);print(d["crumbRequestField"]+":"+d["crumb"])')" \
  -X POST http://jenkins:8080/job/my-job/build
```"""))

a("api-404-not-found", "Jenkins REST API 404 Not Found", "Fix Jenkins API 404 not found errors. Resolve API endpoint and job URL issues.", textwrap.dedent("""API calls return 404 when the requested resource does not exist.

## How to Fix

```bash
# Job: http://jenkins:8080/job/my-job/api/json
# Folder: http://jenkins:8080/job/my-folder/job/my-job/api/json
curl -u admin:token http://jenkins:8080/api/json?tree=jobs[name,url]
```"""))

a("api-500-error", "Jenkins REST API 500 Internal Server Error", "Fix Jenkins API 500 internal server errors. Resolve server-side API processing failures.", textwrap.dedent("""API calls return 500 when Jenkins encounters an internal server error.

## How to Fix

```bash
# Manage Jenkins > System Log
# Or: $JENKINS_HOME/logs/
```

```bash
curl -u admin:token -H "Content-Type: application/json" \
  -d '{"parameter": [{"name":"VERSION","value":"1.0"}]}' \
  http://jenkins:8080/job/my-job/buildWithParameters
```"""))

a("crumb-not-found", "Jenkins Crumb Issuer Not Found", "Fix Jenkins crumb issuer not found errors. Resolve CSRF token generation issues.", textwrap.dedent("""The crumb issuer provides CSRF tokens for API calls.

## How to Fix

```bash
# Manage Jenkins > Configure Security > CSRF Protection > Enable
curl -u admin:token http://jenkins:8080/crumbIssuer/api/json
```

```bash
CRUMB_FIELD=$(curl -s -u admin:token http://jenkins:8080/crumbIssuer/api/json | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['crumbRequestField'])")
CRUMB_VALUE=$(curl -s -u admin:token http://jenkins:8080/crumbIssuer/api/json | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['crumb'])")
curl -u admin:token -H "${CRUMB_FIELD}:${CRUMB_VALUE}" -X POST http://jenkins:8080/job/my-job/build
```"""))

a("token-authentication-failed", "Jenkins Token Authentication Failed", "Fix Jenkins token authentication failures. Resolve API token and credential authentication issues.", textwrap.dedent("""Token authentication failures occur when Jenkins rejects the API token.

## How to Fix

```bash
# Jenkins > User > Configure > API Token > Generate New Token
curl -u username:new-api-token http://jenkins:8080/api/json
```"""))

a("webhook-payload-invalid", "Jenkins Webhook Payload Invalid", "Fix Jenkins webhook payload validation errors. Resolve webhook data format and processing issues.", textwrap.dedent("""Webhook payloads fail validation when the data format does not match what Jenkins expects.

## How to Fix

```bash
# Ensure Content-Type: application/json
echo '{"ref":"refs/heads/main"}' | python3 -m json.tool
```

Ensure webhook secret matches Jenkins configuration."""))

a("json-parse-error", "Jenkins JSON Parse Error in Pipeline", "Fix Jenkins JSON parse errors in pipeline. Resolve JSON parsing and JsonSlurper issues.", textwrap.dedent("""JSON parse errors occur when pipeline scripts try to parse invalid JSON data.

## How to Fix

```groovy
@NonCPS
def parseJson(String text) {
    return new groovy.json.JsonSlurperClassic().parseText(text)
}
```

```groovy
script {
    try {
        def json = new groovy.json.JsonSlurperClassic().parseText(response)
    } catch (Exception e) {
        echo "Failed to parse JSON: ${e.message}"
    }
}
```"""))

a("xml-marshal-error", "Jenkins XML Marshal Error", "Fix Jenkins XML marshalling errors. Resolve XML serialization and parsing issues in pipeline.", textwrap.dedent("""XML marshal errors occur when Jenkins cannot convert data to or from XML format.

## How to Fix

```groovy
import groovy.xml.MarkupBuilder
def writer = new StringWriter()
def xml = new MarkupBuilder(writer)
xml.configuration {
    server('prod')
    port(8080)
}
writeFile file: 'config.xml', text: writer.toString()
```

```groovy
def xmlContent = readFile 'config.xml'
def cleanXml = xmlContent.replaceAll('[^\\x20-\\x7E\\x0A\\x0D]', '')
```"""))

a("cli-connection-error", "Jenkins CLI Connection Error", "Fix Jenkins CLI connection errors. Resolve Jenkins Command Line Interface connectivity issues.", textwrap.dedent("""Jenkins CLI connection errors occur when the CLI cannot connect to the Jenkins server.

## How to Fix

```bash
curl -s http://localhost:8080/api/json | python3 -m json.tool
java -jar jenkins-cli.jar -s http://localhost:8080/ help
java -jar jenkins-cli.jar -s ssh://admin@localhost:22/ help
```

```bash
# Manage Jenkins > Configure Security > SSH Server > Enable > Set port
```"""))

a("groovy-script-http-401", "Jenkins Groovy Script HTTP 401 Error", "Fix Jenkins Groovy script HTTP 401 unauthorized errors. Resolve script console authentication issues.", textwrap.dedent("""HTTP 401 errors occur when Groovy scripts sent via HTTP are not authenticated properly.

## How to Fix

```bash
curl -u admin:api-token -d "script=println 'Hello'" http://localhost:8080/scriptText
```

```bash
CRUMB=$(curl -s -u admin:api-token http://localhost:8080/crumbIssuer/api/json | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['crumbRequestField']+':'+d['crumb'])")
curl -u admin:api-token -H "$CRUMB" -d "script=println Jenkins.instance.version" http://localhost:8080/scriptText
```

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ groovy = <<'EOF'
println Jenkins.instance.version
EOF
```"""))

# Generate files
count = 0
for page in PAGES:
    filename = f"{page['slug']}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    content = f"""---
title: "[Solution] {page['title']}"
description: "{page['desc']}"
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# {page['title']}

{page['body']}
"""
    with open(filepath, 'w') as f:
        f.write(content)
    count += 1

print(f"Generated {count} Jenkins error pages in {OUTPUT_DIR}")
