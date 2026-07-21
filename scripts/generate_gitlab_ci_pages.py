#!/usr/bin/env python3
import os

OUTPUT_DIR = "/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/gitlab-ci"
TOOL = "gitlab-ci"

existing = set()
for f in os.listdir(OUTPUT_DIR):
    if f.endswith(".md") and f != "_index.md":
        existing.add(f.replace(".md", ""))

pages = [
    ("gitlab-ci-pipeline-syntax-error", "GitLab CI Pipeline Syntax Error", "Fix GitLab CI pipeline syntax errors in .gitlab-ci.yml files."),
    ("gitlab-ci-variable-not-found", "GitLab CI Variable Not Found", "Resolve CI/CD variable not found errors in GitLab pipelines."),
    ("gitlab-ci-runner-not-found", "GitLab CI Runner Not Found", "Fix runner not found errors when running GitLab CI jobs."),
    ("gitlab-ci-job-failed-exit-code", "GitLab CI Job Failed Exit Code", "Debug job failures with non-zero exit codes in GitLab CI."),
    ("gitlab-ci-artifacts-too-large", "GitLab CI Artifacts Too Large", "Fix artifacts too large errors in GitLab CI pipelines."),
    ("gitlab-ci-cache-not-found", "GitLab CI Cache Not Found", "Resolve cache not found errors in GitLab CI builds."),
    ("gitlab-ci-environment-not-found", "GitLab CI Environment Not Found", "Fix environment not found errors in GitLab CI deployment."),
    ("gitlab-ci-dind-error", "GitLab CI Docker-in-Docker Error", "Troubleshoot Docker-in-Docker errors in GitLab CI."),
    ("gitlab-ci-registry-auth-failed", "GitLab CI Registry Auth Failed", "Fix Docker registry authentication failures in GitLab CI."),
    ("gitlab-ci-git-clone-failed", "GitLab CI Git Clone Failed", "Resolve git clone failures in GitLab CI runner jobs."),
    ("gitlab-ci-merge-request-pipeline", "GitLab CI Merge Request Pipeline", "Fix merge request pipeline configuration errors."),
    ("gitlab-ci-tags-not-matching", "GitLab CI Tags Not Matching", "Resolve tag matching issues when GitLab CI jobs cannot find runners."),
    ("gitlab-ci-rules-only-except-syntax", "GitLab CI Rules Only Except Syntax", "Fix rules, only, and except syntax errors in .gitlab-ci.yml."),
    ("gitlab-ci-needs-dependency-cycle", "GitLab CI Needs Dependency Cycle", "Resolve dependency cycles in GitLab CI needs keyword."),
    ("gitlab-ci-include-file-not-found", "GitLab CI Include File Not Found", "Fix include file not found errors in GitLab CI configuration."),
    ("gitlab-ci-stage-not-found", "GitLab CI Stage Not Found", "Resolve stage not found errors in GitLab CI pipelines."),
    ("gitlab-ci-timeout-triggered", "GitLab CI Timeout Triggered", "Fix job timeout errors in GitLab CI pipelines."),
    ("gitlab-ci-job-stuck-pending", "GitLab CI Job Stuck Pending", "Resolve jobs stuck in pending state in GitLab CI."),
    ("gitlab-ci-runner-not-online", "GitLab CI Runner Not Online", "Fix offline runner errors in GitLab CI."),
    ("gitlab-ci-concurrency-limit", "GitLab CI Concurrency Limit", "Resolve concurrency limit issues in GitLab CI pipelines."),
    ("gitlab-ci-api-rate-limit", "GitLab CI API Rate Limit", "Fix API rate limit errors when using GitLab CI."),
    ("gitlab-ci-pages-expired", "GitLab CI Pages Expired", "Resolve GitLab Pages deployment expiration errors."),
    ("gitlab-ci-pages-deploy-failed", "GitLab CI Pages Deploy Failed", "Fix GitLab Pages deployment failures."),
    ("gitlab-ci-security-scanner-failed", "GitLab CI Security Scanner Failed", "Troubleshoot security scanner failures in GitLab CI."),
    ("gitlab-ci-dast-error", "GitLab CI DAST Error", "Fix DAST scanning errors in GitLab CI security pipelines."),
    ("gitlab-ci-sast-error", "GitLab CI SAST Error", "Resolve SAST scanning errors in GitLab CI."),
    ("gitlab-ci-terraform-ci-error", "GitLab CI Terraform Error", "Fix Terraform errors in GitLab CI/CD pipelines."),
    ("gitlab-ci-kaniko-build-error", "GitLab CI Kaniko Build Error", "Troubleshoot Kaniko container build errors in GitLab CI."),
    ("gitlab-ci-multi-project-pipeline", "GitLab CI Multi-Project Pipeline", "Fix multi-project pipeline trigger errors in GitLab CI."),
    ("gitlab-ci-trigger-api-error", "GitLab CI Trigger API Error", "Resolve trigger API errors when creating pipelines programmatically."),
    ("gitlab-ci-upstream-pipeline-failed", "GitLab CI Upstream Pipeline Failed", "Fix upstream pipeline failure propagation in GitLab CI."),
    ("gitlab-ci-downstream-pipeline-error", "GitLab CI Downstream Pipeline Error", "Resolve downstream pipeline errors in multi-project CI."),
    ("gitlab-ci-schedule-not-working", "GitLab CI Schedule Not Working", "Fix scheduled pipeline configuration errors in GitLab CI."),
    ("gitlab-ci-variables-precedence", "GitLab CI Variables Precedence", "Resolve variable precedence conflicts in GitLab CI."),
    ("gitlab-ci-resource-group-error", "GitLab CI Resource Group Error", "Fix resource group locking errors in GitLab CI pipelines."),
    ("gitlab-ci-interruptible-not-set", "GitLab CI Interruptible Not Set", "Resolve interruptible keyword issues in GitLab CI."),
    ("gitlab-ci-retry-failed", "GitLab CI Retry Failed", "Fix retry configuration failures in GitLab CI jobs."),
    ("gitlab-ci-manual-job-timeout", "GitLab CI Manual Job Timeout", "Resolve manual job timeout issues in GitLab CI."),
    ("gitlab-ci-when-manual-delayed", "GitLab CI When Manual Delayed", "Fix when:manual and when:delayed configuration errors."),
    ("gitlab-ci-extends-keyword-error", "GitLab CI Extends Keyword Error", "Resolve extends keyword errors in GitLab CI configuration."),
    ("gitlab-ci-image-pull-failed", "GitLab CI Image Pull Failed", "Fix Docker image pull failures in GitLab CI jobs."),
    ("gitlab-ci-services-not-available", "GitLab CI Services Not Available", "Resolve service availability errors in GitLab CI."),
    ("gitlab-ci-before-script-failed", "GitLab CI Before Script Failed", "Fix before_script execution failures in GitLab CI."),
    ("gitlab-ci-after-script-failed", "GitLab CI After Script Failed", "Resolve after_script execution errors in GitLab CI."),
    ("gitlab-ci-coverage-report-not-found", "GitLab CI Coverage Report Not Found", "Fix coverage report not found errors in GitLab CI."),
    ("gitlab-ci-dag-visualization", "GitLab CI DAG Visualization Error", "Resolve DAG visualization issues in GitLab CI needs keyword."),
    ("gitlab-ci-parallel-matrix", "GitLab CI Parallel Matrix Error", "Fix parallel:matrix configuration errors in GitLab CI."),
    ("gitlab-ci-child-pipeline", "GitLab CI Child Pipeline Error", "Resolve child pipeline creation and trigger errors."),
    ("gitlab-ci-ci-job-token-scopes", "GitLab CI CI_JOB_TOKEN Scopes", "Fix CI_JOB_TOKEN scope and permission errors."),
    ("gitlab-ci-group-access-token", "GitLab CI Group Access Token", "Resolve group access token authentication errors."),
    ("gitlab-ci-job-token-scope", "GitLab CI Job Token Scope", "Fix job token scope configuration errors in GitLab CI."),
    ("gitlab-ci-pages-domain-error", "GitLab CI Pages Domain Error", "Resolve custom domain errors for GitLab Pages."),
    ("gitlab-ci-terraform-state-error", "GitLab CI Terraform State Error", "Fix Terraform state backend errors in GitLab CI."),
    ("gitlab-ci-artifact-expiration", "GitLab CI Artifact Expiration", "Resolve artifact expiration policy configuration errors."),
    ("gitlab-ci-yaml-lint-error", "GitLab CI YAML Lint Error", "Fix YAML linting errors in .gitlab-ci.yml files."),
    ("gitlab-ci-yaml-syntax-error-new", "GitLab CI YAML Syntax Error", "Resolve YAML syntax parsing errors in GitLab CI config."),
    ("gitlab-ci-invalid-ci-config", "GitLab CI Invalid Config", "Fix invalid CI configuration errors in GitLab."),
    ("gitlab-ci-needs-pipeline-cycle", "GitLab CI Needs Pipeline Cycle", "Resolve pipeline dependency cycle errors in GitLab CI."),
    ("gitlab-ci-workflow-rules", "GitLab CI Workflow Rules Error", "Fix workflow:rules configuration errors in GitLab CI."),
    ("gitlab-ci-identity-provider-error", "GitLab CI Identity Provider Error", "Resolve identity provider and SSO errors in GitLab CI."),
    ("gitlab-ci-feature-flag-error", "GitLab CI Feature Flag Error", "Fix feature flag related errors in GitLab CI pipelines."),
    ("gitlab-ci-release-cli-error", "GitLab CI Release CLI Error", "Resolve release-cli command errors in GitLab CI."),
    ("gitlab-ci-cluster-agent-error", "GitLab CI Cluster Agent Error", "Fix Kubernetes cluster agent connection errors in GitLab CI."),
    ("gitlab-ci-gitops-error", "GitLab CI GitOps Error", "Resolve GitOps workflow errors in GitLab CI/CD."),
    ("gitlab-ci-deploy-token-error", "GitLab CI Deploy Token Error", "Fix deploy token authentication errors in GitLab CI."),
    ("gitlab-ci-project-access-token", "GitLab CI Project Access Token", "Resolve project access token errors in GitLab CI pipelines."),
    ("gitlab-ci-artifact-metadata-error", "GitLab CI Artifact Metadata Error", "Fix artifact metadata reporting errors in GitLab CI."),
    ("gitlab-ci-dependency-proxy-error", "GitLab CI Dependency Proxy Error", "Resolve dependency proxy pull errors in GitLab CI."),
    ("gitlab-ci-auto-devops-error", "GitLab CI Auto DevOps Error", "Fix Auto DevOps pipeline configuration errors."),
    ("gitlab-ci-inherited-ci-config", "GitLab CI Inherited Config Error", "Resolve inherited CI configuration errors across projects."),
    ("gitlab-ci-config-lint-error", "GitLab CI Config Lint Error", "Fix CI configuration linting errors with CI Lint API."),
    ("gitlab-ci-yaml-anchor-error", "GitLab CI YAML Anchor Error", "Resolve YAML anchor and alias errors in GitLab CI."),
    ("gitlab-ci-yaml-merge-error", "GitLab CI YAML Merge Error", "Fix YAML merge key errors in GitLab CI configuration."),
    ("gitlab-ci-yaml-reference-error", "GitLab CI YAML Reference Error", "Resolve YAML reference errors in .gitlab-ci.yml files."),
    ("gitlab-ci-yaml-extends-error", "GitLab CI YAML Extends Error", "Fix YAML extends keyword errors in GitLab CI."),
    ("gitlab-ci-yaml-default-error", "GitLab CI YAML Default Error", "Resolve YAML default keyword errors in GitLab CI."),
    ("gitlab-ci-yaml-global-error", "GitLab CI YAML Global Error", "Fix YAML global keyword errors in GitLab CI configuration."),
]

count = 0
for slug, title, desc in pages:
    if slug in existing:
        continue
    content = (
        '---\n'
        'title: "[Solution] ' + title + '"\n'
        'description: "' + desc + '"\n'
        'tools: ["' + TOOL + '"]\n'
        'error-types: ["tool-error"]\n'
        'severities: ["error"]\n'
        '---\n\n'
        '# ' + title + '\n\n'
        + desc + ' This error occurs when GitLab CI encounters configuration or execution problems.\n\n'
        '## Common Causes\n\n'
        '- Incorrect `.gitlab-ci.yml` configuration\n'
        '- Missing or invalid variables\n'
        '- Runner not available or offline\n'
        '- Permission or access issues\n\n'
        '## How to Fix\n\n'
        '### Solution 1: Validate Configuration\n\n'
        'Check your `.gitlab-ci.yml` syntax using the GitLab CI Lint tool:\n\n'
        '```yaml\n'
        '# .gitlab-ci.yml example\n'
        'stages:\n'
        '  - build\n'
        '  - test\n'
        '  - deploy\n\n'
        'build_job:\n'
        '  stage: build\n'
        '  script:\n'
        '    - echo "Building..."\n'
        '```\n\n'
        '### Solution 2: Check Runner Status\n\n'
        '```bash\n'
        '# List registered runners\n'
        'gitlab-runner list\n\n'
        '# Verify runner is online\n'
        'gitlab-runner verify\n'
        '```\n\n'
        '### Solution 3: Review Pipeline Logs\n\n'
        'Navigate to your pipeline in GitLab and review the job logs for specific error messages.\n\n'
        '## Example\n\n'
        '```yaml\n'
        '# Correct configuration example\n'
        'stages:\n'
        '  - build\n\n'
        'build_job:\n'
        '  stage: build\n'
        '  image: node:18\n'
        '  script:\n'
        '    - npm install\n'
        '    - npm run build\n'
        '```\n\n'
        '## Related Links\n\n'
        '- [GitLab CI Documentation](https://docs.gitlab.com/ee/ci/)\n'
        '- [GitLab CI Troubleshooting](https://docs.gitlab.com/ee/ci/troubleshooting.html)\n'
    )
    filepath = os.path.join(OUTPUT_DIR, slug + ".md")
    with open(filepath, "w") as f:
        f.write(content)
    count += 1
    existing.add(slug)

print("GitLab CI: created " + str(count) + " new pages (total: " + str(count + 30) + ")")
