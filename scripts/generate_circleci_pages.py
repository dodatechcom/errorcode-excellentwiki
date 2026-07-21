#!/usr/bin/env python3
import os

OUTPUT_DIR = "/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/circleci"
TOOL = "circleci"

existing = set()
for f in os.listdir(OUTPUT_DIR):
    if f.endswith(".md") and f != "_index.md":
        existing.add(f.replace(".md", ""))

pages = [
    ("circleci-config-version-error", "CircleCI Config Version Error", "Fix CircleCI config.yml version errors."),
    ("circleci-jobs-key-missing", "CircleCI Jobs Key Missing", "Resolve missing jobs key errors in CircleCI config."),
    ("circleci-steps-key-error", "CircleCI Steps Key Error", "Fix steps key configuration errors in CircleCI jobs."),
    ("circleci-docker-image-not-found", "CircleCI Docker Image Not Found", "Resolve Docker image not found errors in CircleCI."),
    ("circleci-resource-class-error", "CircleCI Resource Class Error", "Fix resource class configuration errors in CircleCI."),
    ("circleci-machine-executor-not-found", "CircleCI Machine Executor Not Found", "Resolve machine executor errors in CircleCI."),
    ("circleci-macos-executor-error", "CircleCI macOS Executor Error", "Fix macOS executor configuration errors in CircleCI."),
    ("circleci-windows-executor-error", "CircleCI Windows Executor Error", "Resolve Windows executor errors in CircleCI pipelines."),
    ("circleci-environment-variable-not-set", "CircleCI Environment Variable Not Set", "Fix missing environment variable errors in CircleCI."),
    ("circleci-context-not-found", "CircleCI Context Not Found", "Resolve context not found errors in CircleCI workflows."),
    ("circleci-workspace-not-persisted", "CircleCI Workspace Not Persisted", "Fix workspace persistence errors in CircleCI."),
    ("circleci-workflow-not-found", "CircleCI Workflow Not Found", "Resolve workflow not found errors in CircleCI."),
    ("circleci-approval-job-error", "CircleCI Approval Job Error", "Fix approval job configuration errors in CircleCI."),
    ("circleci-fan-out-workflow", "CircleCI Fan-out Workflow Error", "Resolve fan-out workflow configuration errors."),
    ("circleci-fan-in-workflow", "CircleCI Fan-in Workflow Error", "Fix fan-in workflow dependency errors in CircleCI."),
    ("circleci-scheduled-workflow-error", "CircleCI Scheduled Workflow Error", "Resolve scheduled workflow configuration errors."),
    ("circleci-filter-branch-error", "CircleCI Filter Branch Error", "Fix branch filter configuration errors in CircleCI."),
    ("circleci-filter-tag-error", "CircleCI Filter Tag Error", "Resolve tag filter errors in CircleCI workflows."),
    ("circleci-requires-dependency-error", "CircleCI Requires Dependency Error", "Fix requires dependency errors in CircleCI jobs."),
    ("circleci-parallelism-value-invalid", "CircleCI Parallelism Value Invalid", "Resolve invalid parallelism value errors in CircleCI."),
    ("circleci-caching-error", "CircleCI Caching Error", "Fix caching configuration errors in CircleCI."),
    ("circleci-restore-cache-key-not-found", "CircleCI Restore Cache Key Not Found", "Resolve restore_cache key not found errors."),
    ("circleci-save-cache-failed", "CircleCI Save Cache Failed", "Fix save_cache failure errors in CircleCI."),
    ("circleci-store-artifacts-path", "CircleCI Store Artifacts Path", "Resolve store_artifacts path errors in CircleCI."),
    ("circleci-store-test-results-path", "CircleCI Store Test Results Path", "Fix store_test_results path configuration errors."),
    ("circleci-run-command-non-zero", "CircleCI Run Command Non-Zero Exit", "Resolve non-zero exit code errors in CircleCI run steps."),
    ("circleci-checkout-error", "CircleCI Checkout Error", "Fix git checkout errors in CircleCI pipelines."),
    ("circleci-setup-remote-docker-failed", "CircleCI Setup Remote Docker Failed", "Resolve setup_remote_docker failures in CircleCI."),
    ("circleci-docker-layer-cache-error", "CircleCI Docker Layer Cache Error", "Fix Docker layer caching errors in CircleCI."),
    ("circleci-orb-not-found", "CircleCI Orb Not Found", "Resolve orb not found errors in CircleCI configuration."),
    ("circleci-orb-version-conflict", "CircleCI Orb Version Conflict", "Fix orb version conflict errors in CircleCI."),
    ("circleci-private-orb-error", "CircleCI Private Orb Error", "Resolve private orb access errors in CircleCI."),
    ("circleci-inline-orb-syntax", "CircleCI Inline Orb Syntax Error", "Fix inline orb syntax errors in CircleCI config."),
    ("circleci-command-not-found-in-orb", "CircleCI Command Not Found in Orb", "Resolve command not found errors when using orbs."),
    ("circleci-parameter-type-mismatch", "CircleCI Parameter Type Mismatch", "Fix parameter type mismatch errors in CircleCI."),
    ("circleci-job-parameter-not-set", "CircleCI Job Parameter Not Set", "Resolve job parameter not set errors in CircleCI."),
    ("circleci-continuation-orb-error", "CircleCI Continuation Orb Error", "Fix continuation orb errors in dynamic config."),
    ("circleci-pipeline-parameter-invalid", "CircleCI Pipeline Parameter Invalid", "Resolve invalid pipeline parameter errors."),
    ("circleci-setup-workflow-not-defined", "CircleCI Setup Workflow Not Defined", "Fix setup workflow not defined errors."),
    ("circleci-dynamic-config-error", "CircleCI Dynamic Config Error", "Resolve dynamic configuration errors in CircleCI."),
    ("circleci-path-filtering-error", "CircleCI Path Filtering Error", "Fix path filtering errors in dynamic config."),
    ("circleci-config-processing-error", "CircleCI Config Processing Error", "Resolve config processing errors in CircleCI."),
    ("circleci-pipeline-values-not-available", "CircleCI Pipeline Values Not Available", "Fix pipeline values not available errors."),
    ("circleci-api-error", "CircleCI API Error", "Resolve CircleCI API interaction errors."),
    ("circleci-context-environment-variable", "CircleCI Context Environment Variable", "Fix context environment variable errors."),
    ("circleci-ssh-key-add-error", "CircleCI SSH Key Add Error", "Resolve SSH key addition errors in CircleCI."),
    ("circleci-fingerprint-not-found", "CircleCI Fingerprint Not Found", "Fix SSH key fingerprint not found errors."),
    ("circleci-hostname-not-authenticated", "CircleCI Hostname Not Authenticated", "Resolve hostname authentication errors in CircleCI."),
    ("circleci-known-hosts-error", "CircleCI Known Hosts Error", "Fix known_hosts configuration errors."),
    ("circleci-workspace-attach-error", "CircleCI Workspace Attach Error", "Resolve workspace attach errors in CircleCI."),
    ("circleci-run-step-timeout", "CircleCI Run Step Timeout", "Fix run step timeout errors in CircleCI."),
    ("circleci-no-test-output-found", "CircleCI No Test Output Found", "Resolve no test output found errors."),
    ("circleci-ruby-bundle-error", "CircleCI Ruby Bundle Error", "Fix Ruby bundler errors in CircleCI pipelines."),
    ("circleci-node-version-mismatch", "CircleCI Node Version Mismatch", "Resolve Node.js version mismatch errors."),
    ("circleci-python-version-error", "CircleCI Python Version Error", "Fix Python version errors in CircleCI."),
    ("circleci-go-module-error", "CircleCI Go Module Error", "Resolve Go module errors in CircleCI pipelines."),
    ("circleci-apt-get-update-error", "CircleCI APT Get Update Error", "Fix apt-get update errors in CircleCI."),
    ("circleci-pip-install-error", "CircleCI Pip Install Error", "Resolve pip install errors in CircleCI pipelines."),
    ("circleci-npm-ci-failure", "CircleCI NPM CI Failure", "Fix npm ci failure errors in CircleCI."),
    ("circleci-docker-compose-error", "CircleCI Docker Compose Error", "Resolve Docker Compose errors in CircleCI."),
    ("circleci-docker-push-failed", "CircleCI Docker Push Failed", "Fix Docker push failures in CircleCI pipelines."),
    ("circleci-deploy-job-not-configured", "CircleCI Deploy Job Not Configured", "Resolve deploy job configuration errors."),
    ("circleci-aws-ecs-deploy-error", "CircleCI AWS ECS Deploy Error", "Fix AWS ECS deployment errors in CircleCI."),
    ("circleci-gcp-deploy-error", "CircleCI GCP Deploy Error", "Resolve GCP deployment errors in CircleCI."),
    ("circleci-azure-deploy-error", "CircleCI Azure Deploy Error", "Fix Azure deployment errors in CircleCI."),
    ("circleci-heroku-deploy-error", "CircleCI Heroku Deploy Error", "Resolve Heroku deployment errors in CircleCI."),
    ("circleci-platform-specific-error", "CircleCI Platform Specific Error", "Fix platform-specific errors in CircleCI."),
    ("circleci-resource-class-not-available", "CircleCI Resource Class Not Available", "Resolve resource class availability errors."),
    ("circleci-premium-data-residency", "CircleCI Premium Data Residency Error", "Fix premium data residency configuration errors."),
    ("circleci-performance-optimization", "CircleCI Performance Optimization Error", "Resolve performance optimization errors."),
    ("circleci-split-tests-error", "CircleCI Split Tests Error", "Fix test splitting errors in CircleCI."),
    ("circleci-test-splitting-timing", "CircleCI Test Splitting Timing", "Resolve test splitting timing issues."),
    ("circleci-flaky-test-detection", "CircleCI Flaky Test Detection Error", "Fix flaky test detection configuration errors."),
    ("circleci-store-artifacts-not-found", "CircleCI Store Artifacts Not Found", "Resolve store_artifacts not found errors."),
    ("circleci-base-revision-error", "CircleCI Base Revision Error", "Fix base_revision errors in CircleCI."),
    ("circleci-compare-revision-error", "CircleCI Compare Revision Error", "Resolve compare revision errors in CircleCI."),
    ("circleci-checkout-path", "CircleCI Checkout Path Error", "Fix checkout path errors in CircleCI."),
    ("circleci-persist-to-workspace-error", "CircleCI Persist To Workspace Error", "Resolve persist_to_workspace errors."),
    ("circleci-attach-workspace-error", "CircleCI Attach Workspace Error", "Fix attach_workspace errors in CircleCI."),
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
        + desc + ' This error occurs when CircleCI encounters configuration or execution problems.\n\n'
        '## Common Causes\n\n'
        '- Incorrect `config.yml` syntax\n'
        '- Missing or invalid configuration keys\n'
        '- Executor or resource class issues\n'
        '- Orb version conflicts\n\n'
        '## How to Fix\n\n'
        '### Solution 1: Validate Config\n\n'
        'Use the CircleCI config validation endpoint:\n\n'
        '```bash\n'
        'curl -X POST --header "Content-Type: application/json" \\\n'
        '  -d @config.yml https://circleci.com/api/v1/project/{project}/validate\n'
        '```\n\n'
        '### Solution 2: Check Configuration Structure\n\n'
        '```yaml\n'
        'version: 2.1\n\n'
        'jobs:\n'
        '  build:\n'
        '    docker:\n'
        '      - image: cimg/node:18.0\n'
        '    steps:\n'
        '      - checkout\n'
        '      - run:\n'
        '          name: Build\n'
        '          command: npm run build\n\n'
        'workflows:\n'
        '  main:\n'
        '    jobs:\n'
        '      - build\n'
        '```\n\n'
        '### Solution 3: Review Orb Versions\n\n'
        'Ensure your orbs are using compatible versions and are publicly accessible or shared with your organization.\n\n'
        '## Example\n\n'
        '```yaml\n'
        'version: 2.1\n\n'
        'orbs:\n'
        '  node: circleci/node@5.1\n\n'
        'jobs:\n'
        '  test:\n'
        '    executor: node/default\n'
        '    steps:\n'
        '      - checkout\n'
        '      - node/test\n\n'
        'workflows:\n'
        '  test:\n'
        '    jobs:\n'
        '      - node/test\n'
        '```\n\n'
        '## Related Links\n\n'
        '- [CircleCI Documentation](https://circleci.com/docs/)\n'
        '- [CircleCI Config Reference](https://circleci.com/docs/configuration-reference/)\n'
    )
    filepath = os.path.join(OUTPUT_DIR, slug + ".md")
    with open(filepath, "w") as f:
        f.write(content)
    count += 1
    existing.add(slug)

print("CircleCI: created " + str(count) + " new pages (total: " + str(count + 30) + ")")
