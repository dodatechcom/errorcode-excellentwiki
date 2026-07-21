#!/usr/bin/env python3
"""Generate 100+ pages for each of 11 dev tool/framework sections."""

import os
import random
import textwrap

ROOT = "/home/admin1/projects/ErrorCode.excellentwiki.com/content"

TARGET = 105  # aim slightly above 100

# ---------------------------------------------------------------------------
# Tool definitions
# ---------------------------------------------------------------------------

TOOLS = {
    # ── Tools ──────────────────────────────────────────────────────────────
    "poetry": {
        "base": os.path.join(ROOT, "tools", "poetry"),
        "prefix": "poetry",
        "frontmatter_kind": 'tools: ["poetry"]',
        "frontmatter_et": 'error-types: ["tool-error"]',
        "cmd": "poetry",
        "slugs": [
            "pyproject-toml-not-found", "pyproject-toml-parse", "toml-syntax",
            "invalid-toml", "poetry-lock-not-found", "poetry-lock-outdated",
            "lock-file-stale", "lock-regenerate", "install-failed",
            "package-not-found", "package-version", "no-matching-version",
            "version-constraint", "requires-python", "python-version",
            "python-compatibility", "dependency-conflict", "diamond-dependency",
            "resolution-failed", "resolver-error", "solver-error",
            "environment-not-found", "virtualenv-not-found", "virtualenv-create",
            "venv-path", "system-python", "poetry-shell", "shell-activation",
            "add-command", "add-package", "add-dependency", "add-dev-dependency",
            "remove-dependency", "update-package", "update-all", "update-dry-run",
            "build-error", "wheel-build", "sdist-build", "build-format",
            "publish-error", "repository-auth", "pypi-upload", "pypi-token",
            "config-error", "config-key", "config-value", "local-config",
            "global-config", "source-priority", "supplemental-source",
            "private-repository", "repository-url", "install-from-source",
            "cache-error", "cache-clear", "cache-dir", "artifacts-cache",
            "warn-about-lock", "warn-about-update", "script-entry-point",
            "console-script", "plugin-error", "plugin-enable", "plugin-disable",
            "export-requirements", "requirements-txt", "export-format",
            "groups", "main-group", "dev-group", "group-install", "group-sync",
            "optional-group", "extras", "extras-install", "markers-error",
            "python-marker", "platform-marker", "os-marker", "sys-platform",
            "extra-marker", "environment-marker", "scripts-section",
            "build-script", "build-hook", "pre-commit", "post-install",
            "source-url", "legacy-url", "experimental-new-installer",
            "installer-parallel", "wheel-install", "source-install",
            "preference-installed", "priority-package", "minimal-install",
            "poetry-init", "poetry-new", "project-name", "project-version",
            "project-description", "project-authors", "license-field",
            "readme-field", "repository-field", "homepage-field",
            "documentation", "keywords", "classifiers", "package-mode",
            "poetry-run", "run-script", "run-command", "env-info", "env-list",
            "env-remove", "self-update", "check-command", "about-command",
            "help-command",
        ],
    },
    "conda": {
        "base": os.path.join(ROOT, "tools", "conda"),
        "prefix": "conda",
        "frontmatter_kind": 'tools: ["conda"]',
        "frontmatter_et": 'error-types: ["tool-error"]',
        "cmd": "conda",
        "slugs": [
            "conda-not-found", "command-not-found", "activate-error",
            "deactivate-error", "base-environment", "environment-not-found",
            "env-create", "env-remove", "env-export", "env-update",
            "env-list", "env-config", "prefix-path", "environment-name",
            "package-not-found", "package-version", "package-install",
            "package-update", "package-remove", "package-search", "package-list",
            "channel-not-found", "conda-forge", "defaults-channel",
            "custom-channel", "channel-priority", "strict-priority",
            "flexible-priority", "disabled-channel", "channel-alias",
            "offline-channel", "proxy-channel", "ssl-verify", "condarc-error",
            "condarc-read", "condarc-parse", "channels-config",
            "default-channels", "create-config", "solver-error",
            "libmamba-solver", "classic-solver", "experimental-solver",
            "solver-ignore", "dependency-conflict", "unsatisfiable",
            "too-many-conflicts", "pip-interop", "pip-in-conda",
            "mixed-packages", "conda-pip", "pip-only", "pip-not-installed",
            "menu-package", "console-shortcut", "repodata-error",
            "repodata-fetch", "repodata-cache", "repodata-parsing",
            "metadata-error", "index-error", "package-cache", "cache-clear",
            "tarball-cache", "extract-cache", "pkgs-dir", "envs-dir",
            "dot-conda-directory", "disk-full", "disk-space", "no-space",
            "permission-denied", "write-access", "read-only", "proxy-error",
            "http-error", "ssl-error", "connection-timeout", "read-timeout",
            "404-channel", "403-forbidden", "conda-update", "conda-upgrade",
            "conda-downgrade", "conda-version", "python-version",
            "incompatible-python", "library-loading", "dll-error",
            "lib-not-found", "conda-init", "shell-init", "bash-init",
            "zsh-init", "fish-init", "powershell-init", "conda-run",
            "run-in-env", "no-cap", "prefix-error", "environment-variable",
            "conda-prefix", "conda-default-env", "conda-exe", "conda-shlvl",
            "clean-command", "clean-tarballs", "clean-packages", "clean-index",
            "clean-all", "dry-run", "dry-run-install", "dry-run-update",
            "yes-flag", "force-install", "force-reinstall", "no-deps",
            "only-deps", "no-channel", "channel-map", "offline-mode",
            "quiet-mode", "verbose-mode", "json-output", "json-format",
            "repodata-fnm", "repodata-jlap", "parallel-download",
            "fetch-threads", "extract-threads", "conda-doctor",
            "health-check", "health-tests", "conda-compare",
            "environment-comparison", "spec-list", "explicit-spec",
            "free-channel-removed", "remove-channel",
        ],
    },
    "pip": {
        "base": os.path.join(ROOT, "tools", "pip"),
        "prefix": "pip",
        "frontmatter_kind": 'tools: ["pip"]',
        "frontmatter_et": 'error-types: ["tool-error"]',
        "cmd": "pip",
        "slugs": [
            "command-not-found", "no-such-option", "no-such-command",
            "install-failed", "package-not-found", "could-not-find-version",
            "no-matching-distribution", "index-not-found", "simple-index",
            "package-url", "requirement-parse", "requirements-file",
            "dash-r-file-not-found", "constraints-file",
            "dash-c-file-not-found", "editable-install", "dash-e-flag",
            "develop-mode", "git-repo", "git-clone", "git-checkout",
            "git-error", "mercurial-error", "svn-error", "bazaar-error",
            "vcs-url", "egg-fragment", "subdirectory", "hash-egg",
            "vcs-branch", "vcs-tag", "vcs-commit",
            "dependency-link-deprecated", "find-links", "extra-index",
            "trusted-host", "trusted-source", "no-index", "only-binary",
            "no-binary", "platform-wheel", "manylinux", "musllinux",
            "linux-platform", "macosx-platform", "win-platform", "abi-tag",
            "python-tag", "py2-only", "py3-only", "py2-py3",
            "universal-wheel", "source-distribution", "sdist-install",
            "wheel-install", "wheel-build", "bdist-wheel", "wheel-cache",
            "no-cache", "cache-dir", "pip-cache", "cache-list", "cache-purge",
            "cache-remove", "download-cache", "no-download-cache",
            "build-isolation", "no-build-isolation", "pep517",
            "build-backend", "setuptools", "setuptools-error",
            "setup-py-install", "setup-py-develop", "setup-cfg",
            "pyproject-toml-setup", "build-meta", "isolated-build",
            "deps-not-satisfied", "missing-dependency", "dependency-conflict",
            "cyclic-dependency", "dependency-resolution", "resolver-change",
            "backtracking", "legacy-resolver", "2020-resolver",
            "conflict-resolution", "incompatible-package", "override-package",
            "force-reinstall", "upgrade-strategy", "eager-upgrade",
            "only-if-needed", "upgrade-package", "uninstall-error",
            "uninstall-package", "uninstall-deps", "auto-uninstall",
            "no-input", "confirmation-prompt", "dry-run-uninstall",
            "list-installed", "outdated-list", "pip-list", "pip-show",
            "pip-check", "pip-freeze", "pipdeptree", "requirement-specifier",
            "exact-version", "version-comparison", "local-version",
            "pre-release", "dev-version", "post-release", "dot-dev", "dot-post",
            "wheel-file", "egg-info", "metadata-parsing", "dist-info",
            "record-file", "installed-files", "scripts-directory",
            "bin-directory", "shebang-error", "script-wrapper",
            "easy-install", "pip3-vs-pip", "python-m-dash-m-pip",
            "virtual-environment", "venv-create", "no-activate", "path-error",
            "python-path", "site-packages", "user-site", "dash-dash-user-install",
            "system-site", "dist-packages", "debian-python", "python-config",
            "sysconfig", "platlib", "purelib", "scheme-error", "compile-error",
            "c-extension", "build-ext", "no-compiler", "msvc-error",
            "gcc-error", "missing-header", "python-dot-h", "library-not-found",
            "link-error", "cython", "c-extension-build", "setuptools-scm",
            "version-from-git", "metadata-version", "egg-info-generate",
            "requirements-parsing", "options-error", "pip-conf", "config-file",
            "global-config", "user-config", "site-config", "pip-env-var",
            "proxy-env", "http-proxy", "https-proxy", "no-proxy",
            "timeout-env", "retries-env", "cert-env",
        ],
    },
    "cargo": {
        "base": os.path.join(ROOT, "tools", "cargo"),
        "prefix": "cargo",
        "frontmatter_kind": 'tools: ["cargo"]',
        "frontmatter_et": 'error-types: ["tool-error"]',
        "cmd": "cargo",
        "slugs": [
            "project-not-found", "cargo-init", "cargo-new", "project-name",
            "binary-crate", "library-crate", "edition-2015", "edition-2018",
            "edition-2021", "edition-2024", "crate-type", "dependencies-not-found",
            "crate-not-found", "version-not-found", "crate-registry",
            "crates-dot-io", "alternative-registry", "private-registry",
            "registry-auth", "registry-token", "git-dependency", "branch-dep",
            "tag-dep", "rev-dep", "path-dependency", "workspace-member",
            "patch-dependency", "replace-dependency", "patch-section",
            "replace-deprecated", "dev-dependency", "build-dependency",
            "optional-dependency", "feature-flag", "default-features",
            "no-default-features", "features-toggle", "cfg-attribute",
            "feature-resolver", "resolver-v1", "resolver-v2",
            "target-specific-dep", "cfg-target", "target-os", "target-arch",
            "build-script", "build-rs", "link-to-native", "cc-crate",
            "cmake-crate", "pkg-config", "library-link", "native-lib",
            "dll-load", "soname", "rpath", "cargo-build", "build-failed",
            "error-e02", "error-e04", "type-mismatch", "cannot-find-type",
            "cannot-find-module", "module-not-found", "module-file", "mod-rs",
            "lib-rs", "main-rs", "mod-declaration", "file-path",
            "module-tree", "use-declaration", "extern-crate-deprecated",
            "2018-edition-import", "nested-import", "self-import",
            "super-import", "crate-import", "absolute-path", "relative-path",
            "cargo-check", "cargo-test", "test-failed", "test-function",
            "test-attribute", "test-name", "test-filter", "test-thread",
            "test-panic", "test-result", "cargo-run", "run-binary",
            "run-example", "run-test", "run-bench", "cargo-doc",
            "doc-generation", "doc-test", "doc-attribute", "doc-comment",
            "doc-comment-bang", "doc-comment-triple", "pub-use",
            "doc-re-export", "cargo-publish", "publish-dry-run",
            "publish-token", "publish-verify", "cargo-install",
            "install-from-path", "install-binary", "uninstall-crate",
            "cargo-update", "update-dep", "update-dry-run", "cargo-outdated",
            "cargo-tree", "tree-format", "tree-no-dedup", "tree-invert",
            "cargo-clean", "clean-target", "clean-package", "cargo-metadata",
            "metadata-output", "cargo-vendor", "vendor-dir", "cargo-fetch",
            "fetch-offline", "offline-mode", "cargo-package", "package-verify",
            "package-list", "include-exclude", "license-file", "readme-file",
            "package-keys", "authors", "description-field", "repository-field",
            "cargo-fmt", "rustfmt", "format-check", "format-config",
            "cargo-clippy", "clippy-lint", "lint-level", "allow-lint",
            "deny-lint", "warn-lint", "clippy-fix", "cargo-fix",
            "fix-suggestion", "edition-migration", "cargo-audit", "audit-db",
            "vulnerability", "advisory", "rustsec", "cargo-deny",
            "deny-policy", "license-check", "cargo-outdated-check",
            "build-script-error", "rerun-if-changed",
            "rerun-if-env-changed", "cargo-location", "cargo-home",
            "target-dir", "cargo-config", "dot-cargo-config-toml",
            "config-env", "target-config", "linker-config",
            "rustflags-config", "rustdocflags", "profile-error", "opt-level",
            "debug-info", "debug-symbol", "incremental", "codegen-units",
            "lto", "panic-abort", "panic-unwind", "strip", "profile-dev",
            "profile-release", "profile-test", "profile-bench",
            "workspace-error", "workspace-root", "member-path",
            "workspace-dep", "exclude-path",
        ],
    },
    "brew": {
        "base": os.path.join(ROOT, "tools", "brew"),
        "prefix": "brew",
        "frontmatter_kind": 'tools: ["brew"]',
        "frontmatter_et": 'error-types: ["tool-error"]',
        "cmd": "brew",
        "slugs": [
            "command-not-found", "formula-not-found", "cask-not-found",
            "tap-not-found", "formula-already-installed", "cask-already-installed",
            "no-available-formula", "no-available-cask", "formula-outdated",
            "cask-outdated", "install-failed", "download-failed",
            "checksum-mismatch", "sha256-mismatch", "verification-failed",
            "bottle-not-available", "build-from-source", "source-code-download",
            "source-compile", "make-error", "cmake-error", "autotools-error",
            "configure-error", "compiler-not-found", "xcode-not-installed",
            "clt-not-installed", "clt-path", "sdk-not-found", "macos-version",
            "architecture-mismatch", "intel-vs-arm", "rosetta",
            "apple-silicon", "universal-binary", "keg-only-formula",
            "conflicting-formula", "link-error", "symlink-conflict",
            "file-exists", "overwrite-error", "forced-link", "unlink-error",
            "permission-denied", "usr-local", "writable-error",
            "ownership-error", "user-permission", "sudo-required", "no-sudo",
            "homebrew-prefix", "homewbrew-prefix", "custom-prefix",
            "relocate-error", "cellar-path", "cellar-not-writable",
            "opt-path", "bin-path", "man-path", "brew-doctor", "doctor-warning",
            "doctor-error", "system-check", "config-check", "env-check",
            "brew-update", "update-failed", "git-error", "origin-fetch",
            "upstream-tag", "brew-outdated", "brew-upgrade", "upgrade-all",
            "upgrade-formula", "cleanup-error", "cleanup-old",
            "prune-symlink", "prune-error", "autoremove",
            "unused-dependency", "brew-search", "search-remote",
            "search-desc", "brew-info", "info-json", "bottle-info",
            "dependencies-list", "tree-view", "brew-deps", "deps-tree",
            "brew-uses", "reverse-deps", "brew-config", "homewbrew-bundle",
            "bundle-brewfile", "brewfile-not-found", "tap-cask",
            "mas-plugin", "bundle-install", "bundle-dump", "bundle-cleanup",
            "brew-services", "services-list", "service-start", "service-stop",
            "service-restart", "service-run", "service-error",
            "plist-launchd", "launchd-plist", "background-service",
            "brew-cask", "cask-install", "cask-reinstall", "cask-upgrade",
            "cask-zap", "cask-uninstall", "cask-outdated",
            "quarantine-attribute", "security-quarantine", "gatekeeper",
            "unsigned-binary", "brew-developer", "developer-mode",
            "homewbrew-developer", "brew-tests", "test-bot", "ci-testing",
            "brew-create", "create-formula", "new-formula", "ruby-template",
            "formula-dsl", "bottle-dsl", "livecheck", "livecheck-formula",
            "brew-bump", "bump-formula", "bump-cask", "pr-creator",
            "brew-autobump", "analytics", "homewbrew-no-analytics",
            "homewbrew-no-auto-update", "homewbrew-no-github-api",
            "homewbrew-install-cleanup", "environment-variable",
            "proxy-setting", "homebrew-proxy", "ssl-error", "tls-error",
            "certificate-verify", "curl-error", "git-protocol",
            "homewbrew-no-insecure-redirect",
        ],
    },
    "helm": {
        "base": os.path.join(ROOT, "tools", "helm"),
        "prefix": "helm",
        "frontmatter_kind": 'tools: ["helm"]',
        "frontmatter_et": 'error-types: ["tool-error"]',
        "cmd": "helm",
        "slugs": [
            "chart-not-found", "chart-download", "chart-fetch",
            "repo-not-found", "repo-add", "repo-remove", "repo-update",
            "repo-list", "repo-index", "repo-url", "chartmuseum",
            "oci-registry", "oci-pull", "oci-push", "oci-tag",
            "registry-login", "registry-logout", "registry-auth",
            "helm-install", "install-dry-run", "install-name",
            "install-namespace", "install-wait", "install-timeout",
            "install-atomic", "install-cleanup", "install-replace",
            "install-no-hooks", "install-skip", "upgrade-error",
            "upgrade-install", "upgrade-force", "upgrade-recreate",
            "upgrade-reset", "upgrade-cleanup", "upgrade-timeout",
            "upgrade-atomic", "upgrade-wait", "rollback-error",
            "rollback-version", "rollback-wait", "rollback-timeout",
            "uninstall-error", "uninstall-keep", "uninstall-dry-run",
            "template-error", "helm-template", "template-name",
            "template-output", "template-validate", "lint-error",
            "chart-lint", "lint-values", "lint-strict", "lint-namespace",
            "test-error", "helm-test", "test-run", "test-timeout",
            "test-cleanup", "test-logs", "package-error", "chart-package",
            "package-sign", "package-key", "package-passphrase",
            "signing-key", "gpg-error", "pgp-signature",
            "provenance-error", "provenance-verify", "provenance-check",
            "dependency-build", "dependency-update", "dependency-list",
            "dep-up", "dep-build", "repository-alias", "condition-tag",
            "subchart-error", "global-value", "parent-chart", "child-chart",
            "hook-error", "hook-weight", "hook-delete", "hook-policy",
            "pre-install", "post-install", "pre-upgrade", "post-upgrade",
            "pre-rollback", "post-rollback", "pre-delete", "post-delete",
            "crd-install", "crd-error", "custom-resource", "crd-version",
            "created-crd", "installed-crd", "namespace-not-found",
            "invalid-namespace", "template-rendering", "built-in-object",
            "dot-values", "dot-chart", "dot-release", "dot-template",
            "dot-capabilities", "dot-files", "dot-subcharts", "scope-error",
            "values-file", "values-schema", "json-schema",
            "validate-schema", "override-values", "set-values",
            "string-value", "int-value", "bool-value", "object-value",
            "yaml-parse", "yaml-indent", "multi-doc-yaml",
            "separator-doc", "tpl-function", "include-function",
            "required-function", "lookup-function", "fail-function",
            "to-yaml", "from-yaml", "indent-function", "nindent",
            "default-function", "coalesce", "ternary", "empty-function",
            "kind-is", "semver-compare", "regex-match", "contains",
            "has-key", "has", "keys", "values-func", "uniq", "without",
            "dict", "set", "unset", "must-deep-copy", "type-is", "type-of",
            "url-parse", "split-list", "join", "sort-alpha", "kube-version",
            "api-version", "capabilities-api-versions", "upgrade-compat",
            "api-deprecation", "kubernetes-version", "helm-version",
            "tiller-removed", "helm-2-vs-3", "helm-2-migration",
            "tillerless",
        ],
    },
    "kubectl": {
        "base": os.path.join(ROOT, "tools", "kubectl"),
        "prefix": "kubectl",
        "frontmatter_kind": 'tools: ["kubectl"]',
        "frontmatter_et": 'error-types: ["tool-error"]',
        "cmd": "kubectl",
        "slugs": [
            "command-not-found", "no-such-command", "kubeconfig-not-found",
            "config-not-found", "context-not-set", "current-context",
            "cluster-not-found", "user-not-found", "namespace-not-found",
            "context-namespace", "server-not-found", "connection-refused",
            "api-server", "endpoint-timeout", "load-balancer",
            "certificate-error", "client-cert", "client-key", "ca-cert",
            "tls-verify", "insecure-skip", "token-auth", "bearer-token",
            "basic-auth", "username-password", "service-account",
            "rbac-error", "forbidden", "unauthorized", "access-denied",
            "cannot-list-resource", "cannot-get-resource", "cannot-create",
            "cannot-update", "cannot-delete", "cannot-patch", "cannot-watch",
            "clusterrole-not-found", "role-not-found",
            "clusterrolebinding", "rolebinding", "subject-not-found",
            "pod-not-found", "pod-running", "pod-pending", "pod-crashloop",
            "pod-oom", "pod-error", "pod-evicted", "node-not-found",
            "node-ready", "node-not-ready", "node-cordon", "node-drain",
            "node-taint", "node-unschedulable", "namespace-active",
            "namespace-terminating", "service-not-found", "service-endpoint",
            "endpoint-not-found", "endpoint-slice", "ingress-not-found",
            "configmap-not-found", "secret-not-found", "pvc-not-found",
            "pv-not-found", "pvc-pending", "pv-available", "storage-class",
            "persistent-volume", "pod-volume", "deployment-not-found",
            "deployment-replicas", "deployment-rollout", "deployment-strategy",
            "recreate-strategy", "rolling-update", "deployment-paused",
            "deployment-progress", "deployment-revision", "rollout-history",
            "rollout-undo", "rollout-status", "rollout-restart",
            "scale-deployment", "replica-set", "daemonset-not-found",
            "daemonset-rollout", "daemonset-schedule", "statefulset-not-found",
            "statefulset-replicas", "statefulset-rolling",
            "statefulset-partition", "job-not-found", "job-complete",
            "job-failed", "job-backoff", "cronjob-not-found",
            "cronjob-schedule", "cronjob-suspend", "resource-quota",
            "quota-exceeded", "limit-range", "container-limit",
            "container-request", "pod-limit", "pod-resource", "hpa-not-found",
            "horizontal-pod-autoscaler", "vpa-not-found",
            "vertical-pod-autoscaler", "pdb-not-found", "pod-disruption",
            "min-available", "max-unavailable", "network-policy",
            "egress-rule", "ingress-rule", "pod-selector",
            "network-policy-deny", "apply-error", "apply-dry-run",
            "apply-force", "apply-prune", "apply-prune-whitelist",
            "delete-error", "delete-all", "delete-force", "delete-grace",
            "delete-now", "get-error", "get-output", "get-json", "get-yaml",
            "get-wide", "get-watch", "describe-error", "logs-error",
            "logs-tail", "logs-follow", "logs-previous", "logs-container",
            "exec-error", "exec-command", "exec-stdin", "exec-tty",
            "exec-container", "port-forward", "port-forward-error",
            "local-port", "pod-port", "debug-pod", "ephemeral-container",
            "copy-error", "cp-local", "cp-pod", "diff-error", "diff-local",
            "diff-live", "explain-error", "explain-resource",
            "api-resources", "api-versions", "version-error",
            "cluster-info", "top-node", "top-pod", "drain-node",
            "cordon-node", "uncordon-node", "taint-node", "label-node",
            "annotate-node",
        ],
    },
    "stripe": {
        "base": os.path.join(ROOT, "tools", "stripe"),
        "prefix": "stripe",
        "frontmatter_kind": 'tools: ["stripe"]',
        "frontmatter_et": 'error-types: ["tool-error"]',
        "cmd": "stripe",
        "slugs": [
            "api-key-not-set", "secret-key-invalid", "publishable-key",
            "restricted-key", "key-prefix-sk-live", "key-prefix-pk-live",
            "test-mode-key", "live-mode-key", "account-not-found",
            "account-link", "account-reject", "account-verification",
            "balance-not-available", "balance-transaction",
            "charge-not-found", "charge-declined", "charge-failed",
            "charge-refunded", "capture-charge", "authorize-charge",
            "card-declined", "generic-decline", "insufficient-funds",
            "stolen-card", "lost-card", "expired-card", "invalid-cvc",
            "invalid-expiry", "invalid-number", "processing-error",
            "rate-limit", "too-many-requests", "api-timeout",
            "connection-timeout", "idempotency-key", "duplicate-request",
            "idempotency-replay", "webhook-error", "webhook-signature",
            "webhook-secret", "webhook-event", "event-not-found",
            "event-type", "event-data", "customer-not-found",
            "customer-create", "customer-update", "customer-delete",
            "customer-email", "customer-source", "payment-method",
            "payment-method-not-found", "payment-method-attach",
            "payment-method-detach", "payment-intents",
            "intent-not-found", "intent-cancel", "intent-confirm",
            "intent-capture", "next-action", "requires-action",
            "requires-payment", "requires-confirmation",
            "requires-capture", "sca-required", "3d-secure",
            "authentication-required", "setup-intent", "setup-future",
            "off-session", "on-session", "pipe-read",
            "subscription-not-found", "subscription-create",
            "subscription-update", "subscription-cancel",
            "subscription-pause", "subscription-resume",
            "subscription-trial", "trial-end", "billing-cycle",
            "invoice-not-found", "invoice-finalize", "invoice-pay",
            "invoice-send", "invoice-void", "invoice-upcoming",
            "invoice-item", "price-not-found", "price-currency",
            "price-interval", "price-tier", "product-not-found",
            "product-active", "product-shippable", "sku-not-found",
            "coupon-not-found", "coupon-percent", "coupon-amount",
            "promotion-code", "discount-error", "tax-rate", "tax-id",
            "vat-number", "eu-vat", "gst", "tax-calculation",
            "refund-error", "refund-reason", "refund-amount",
            "dispute-not-found", "dispute-evidence", "dispute-submit",
            "dispute-outcome", "dispute-closed", "chargeback",
            "connect-not-enabled", "connected-account", "platform-account",
            "destination-charge", "separate-charge", "transfer-not-found",
            "transfer-group", "application-fee", "connect-onboarding",
            "express-account", "custom-account", "account-capabilities",
            "requirement-error", "document-upload", "file-not-found",
            "file-upload", "file-purpose", "file-link", "file-type",
            "report-not-found", "report-run", "report-type", "report-column",
            "sigma-query", "sql-query", "query-timeout", "query-result",
            "query-error",
        ],
    },
    # ── Frameworks ─────────────────────────────────────────────────────────
    "gin": {
        "base": os.path.join(ROOT, "frameworks", "gin"),
        "prefix": "gin",
        "frontmatter_kind": 'frameworks: ["gin"]',
        "frontmatter_et": 'error-types: ["framework-error"]',
        "cmd": "gin",
        "slugs": [
            "router-not-found", "route-conflict", "handler-not-defined",
            "handle-func", "context-not-found", "context-get", "context-set",
            "context-param", "query-param", "post-form", "bind-json",
            "bind-xml", "bind-query", "bind-form", "validation-error",
            "binding-required", "binding-struct", "binding-tag",
            "binding-default", "custom-validator", "engine-not-found",
            "default-engine", "engine-secure", "engine-trust",
            "middleware-not-applied", "middleware-order", "middleware-abort",
            "middleware-next", "logger-middleware", "recovery-middleware",
            "custom-middleware", "cors-middleware", "gin-cors",
            "allow-origin", "allow-methods", "allow-headers", "group-routes",
            "route-group", "group-relative", "group-handler",
            "version-group", "api-version", "path-parameter",
            "parameter-type", "wildcard-route", "catch-all-route",
            "redirect-trailing-slash", "redirect-fixed-path", "handle-method",
            "get-method", "post-method", "put-method", "delete-method",
            "patch-method", "any-method", "static-file", "static-fs",
            "static-dir", "file-server", "template-render", "html-template",
            "template-cache", "template-reload", "multipart-form",
            "file-upload", "file-size", "max-multipart", "form-parse",
            "query-escape", "url-encode", "response-json", "json-pretty",
            "jsonp", "xml-response", "yaml-response", "protobuf",
            "protobuf-marshal", "protobuf-unmarshal", "string-response",
            "data-response", "redirect-response", "redirect-code",
            "render-interface", "writer-header", "writer-status",
            "writer-body", "response-flush", "abort-error",
            "abort-with-status", "abort-with-json", "abort-with-error",
            "error-type", "error-meta", "error-string", "panic-recovery",
            "panic-error", "stack-trace", "recovery-handler",
            "trusted-proxies", "proxy-header", "client-ip",
            "forward-header", "x-forwarded-for", "x-real-ip",
            "x-forwarded-proto", "tls-config", "https-server",
            "http2-support", "server-timeouts", "read-timeout",
            "write-timeout", "idle-timeout", "graceful-shutdown",
            "graceful-restart", "signal-notify", "os-signal",
            "prefix-route", "route-not-match", "404-handler", "405-handler",
            "not-allowed-method", "binding-error", "form-validation",
            "struct-validation", "binding-nested", "binding-map",
            "binding-slice", "binding-array", "binding-default-value",
        ],
    },
    "fiber": {
        "base": os.path.join(ROOT, "frameworks", "fiber"),
        "prefix": "fiber",
        "frontmatter_kind": 'frameworks: ["fiber"]',
        "frontmatter_et": 'error-types: ["framework-error"]',
        "cmd": "fiber",
        "slugs": [
            "app-not-found", "fiber-app", "new-app", "config-error",
            "config-prefork", "server-header", "body-limit", "concurrency",
            "read-timeout", "write-timeout", "idle-timeout", "error-handler",
            "recover-handler", "not-found-handler", "method-not-allowed",
            "stack-trace", "disable-startup", "startup-message",
            "route-not-found", "route-conflict", "route-handler",
            "route-func", "route-method", "get-method", "post-method",
            "put-method", "delete-method", "patch-method",
            "connect-options-trace", "group-route", "use-middleware",
            "middleware-order", "static-file", "static-dir", "static-index",
            "static-browse", "static-download", "filesystem-embed",
            "embed-fs", "http11", "http2", "prefork-mode",
            "child-process", "master-process", "listener-error",
            "listener-network", "tcp-listener", "tls-listener",
            "cert-file", "key-file", "acme-auto", "lets-encrypt",
            "autocert-manager", "domain-cache", "port-not-available",
            "address-in-use", "context-not-found", "c-body", "c-params",
            "c-query", "c-form", "c-json", "c-jsonp", "c-xml",
            "c-yaml", "c-string", "c-send", "c-send-string",
            "c-send-file", "c-download", "c-redirect", "c-render",
            "c-next", "c-abort", "c-abort-with-status", "c-status",
            "c-set", "c-get", "c-cookie", "c-cookies",
            "c-clear-cookie", "c-bind", "c-bind-query", "c-bind-form",
            "c-bind-json", "c-bind-params", "validation-error",
            "validate-struct", "validate-field", "custom-validator",
            "go-playground-validator", "error-handler",
            "error-handler-default", "error-handler-custom",
            "recover-panic", "panic-handler", "stack-log", "ctx-logger",
            "log-level", "log-format", "middleware-limiter",
            "rate-limiter", "max-requests", "expiration",
            "skip-middleware", "when-func", "ip-middleware", "ip-whitelist",
            "ip-blacklist", "proxy-header", "x-forwarded-for",
            "compress-middleware", "level", "brotli", "gzip", "deflate",
            "cache-middleware", "storage-backend",
            "cache-control", "etag", "cors-middleware",
            "allow-origins", "allow-methods-allow", "allow-headers-allow",
            "expose-headers", "allow-credentials", "max-age",
            "csrf-middleware", "token-lookup", "cookie-name",
            "cookie-http-only", "expiration-csrf", "key-lookup",
            "context-key", "csrf-error", "session-middleware",
            "session-store", "session-get", "session-set", "session-delete",
            "session-save", "session-destroy", "session-id",
            "cookie-storage", "file-storage", "redis-storage",
            "database-storage", "websocket-upgrade", "ws-upgrader",
            "ws-conn", "ws-read", "ws-write", "client-close",
        ],
    },
    "actix": {
        "base": os.path.join(ROOT, "frameworks", "actix"),
        "prefix": "actix",
        "frontmatter_kind": 'frameworks: ["actix"]',
        "frontmatter_et": 'error-types: ["framework-error"]',
        "cmd": "actix",
        "slugs": [
            "app-not-found", "app-create", "app-new",
            "service-config", "configure-route", "route-pattern",
            "resource-route", "scope-route", "guard-route", "guard-method",
            "guard-header", "guard-host", "guard-param", "guard-not",
            "guard-any", "guard-all", "middleware-wrap", "middleware-order",
            "middleware-compose", "logger-middleware", "compress-middleware",
            "identity-middleware", "default-headers", "cors-middleware",
            "cors-allowed", "cors-max-age", "cors-allowed-origin",
            "cors-allowed-methods", "cors-allowed-headers",
            "cors-expose-headers", "cors-blocking", "data-not-found",
            "app-data", "data-factory", "insert-data", "extract-data",
            "json-config", "limit-config", "error-handling",
            "actix-error", "error-response", "internal-error",
            "bad-request", "not-found-actix", "method-not-allowed-actix",
            "custom-error", "error-impl", "response-error",
            "http-response", "http-request", "request-head",
            "request-uri", "request-method", "request-headers",
            "query-string", "url-encoded", "path-info", "matched-path",
            "json-body", "form-body", "bytes-body", "string-body",
            "param-extract", "path-extractor", "query-extractor",
            "json-extractor", "form-extractor", "data-extractor",
            "state-extractor", "config-extractor", "connection-extractor",
            "peer-addr", "socket-addr", "http-server", "server-bind",
            "server-run", "server-addr", "server-workers",
            "worker-count", "max-connections", "backlog",
            "keep-alive", "client-disconnect", "server-shutdown",
            "graceful-shutdown", "signal-stop", "ctrl-c", "sigint",
            "sigterm", "tls-config", "rustls-error", "openssl-error",
            "cert-file-actix", "key-file-actix", "tls-acceptor",
            "http1-only", "http2-upgrade", "upgrade-header",
            "upgrade-error", "websocket-error", "ws-protocol",
            "ws-upgrade", "ws-session", "ws-text", "ws-binary",
            "ws-ping", "ws-pong", "ws-close", "ws-codec", "ws-message",
            "ws-start", "ws-actor", "ws-handler", "stream-handler",
            "actor", "mailbox-error", "actor-spawn", "addr-error",
            "do-send", "try-send", "recipient-error", "context-run",
            "context-wait", "context-notify", "arbiter-error",
            "system-error", "system-new", "system-run", "runtime-error",
            "tokio-runtime", "async-runtime", "block-on",
            "spawn-block", "thread-pool", "local-set", "actix-rt",
            "actix-web-version", "actix-rt-architecture",
            "actor-context", "context-future-spawner",
            "not-supported-actor", "actor-state",
            "running-stopping", "address-not-connected",
        ],
    },
}

# ---------------------------------------------------------------------------
# Body templates per tool / framework
# ---------------------------------------------------------------------------

def make_body(tool_name, cmd, slug, is_framework):
    """Return markdown body for a generated page."""
    title_human = slug.replace("-", " ").title()
    code_block_lang = "go" if is_framework else "bash"

    if is_framework:
        err_desc = (
            f"Occurs when using {tool_name} to build a web application. "
            f"The {title_human} problem prevents requests from being handled "
            f"correctly and typically surfaces as a runtime or build error."
        )
        fix_intro = (
            f"To resolve this {tool_name} error, verify the following configuration "
            f"and code patterns."
        )
    else:
        err_desc = (
            f"The `{cmd}` command encountered a {title_human} issue. "
            f"This error stops normal operation and must be resolved before "
            f"continuing with your workflow."
        )
        fix_intro = (
            f"Fix the {title_human} by following the steps below."
        )

    # Build a plausible error message
    error_snippet = f"Error: {title_human}"

    body = f"""## Error Description

{err_desc}

## Common Causes

- Misconfigured settings or missing configuration
- Incompatible version of {tool_name} or one of its dependencies
- File or directory permissions issue
- Network or connectivity problem during operation
- Platform-specific incompatibility
- Incorrect command syntax or API usage

## Typical Error Output

```
{error_snippet}
```

## How to Fix

### 1. Verify Installation

```bash
{cmd} --version
```

Ensure the installed version is up to date and compatible with your project.

### 2. Check Configuration

```{code_block_lang}
# Verify your configuration file exists and is valid
cat {tool_name}.yaml 2>/dev/null || echo "Config file not found"
```

### 3. Clear Cache and Retry

```bash
{cmd} clean 2>/dev/null; {cmd} install
```

### 4. Reinstall Dependencies

```bash
{cmd} remove --purge affected-package
{cmd} install affected-package
```

### 5. Verify File Permissions

```bash
ls -la $(which {cmd} 2>/dev/null || echo "/usr/local/bin/{cmd}")
chmod +x $(which {cmd} 2>/dev/null || echo "/usr/local/bin/{cmd}")
```

### 6. Test in Isolation

Create a minimal reproduction to isolate the issue:

```bash
mkdir /tmp/{tool_name}-test && cd /tmp/{tool_name}-test
{cmd} init 2>/dev/null || true
```

## Common Scenarios

**After upgrading {tool_name}.**
A recent upgrade may have changed defaults or removed deprecated options. Check the
release notes for breaking changes and update your configuration accordingly.

**CI/CD pipeline failure.**
Ensure the CI environment has the correct {tool_name} version installed and that
all required environment variables are set.

## Prevention

1. Pin {tool_name} versions in CI configuration to avoid surprise upgrades
2. Run `{cmd} doctor` or equivalent health check before making changes
3. Keep a backup of your configuration before modifying it
4. Test changes in a staging environment before applying to production
"""
    return body


def slugify_for_filename(prefix, slug):
    return f"{prefix}-{slug}.md"


def existing_slugs(base_dir):
    """Return set of base names (without .md) already present."""
    if not os.path.isdir(base_dir):
        return set()
    return {
        f.replace(".md", "")
        for f in os.listdir(base_dir)
        if f.endswith(".md")
    }


def title_for_slug(tool_name, slug):
    """Human-readable title from slug."""
    words = slug.replace("-", " ").title()
    return f"{tool_name.title()} {words}"


def desc_for_slug(tool_name, slug):
    """Short description for front matter."""
    words = slug.replace("-", " ")
    return (
        f"Understand and fix {tool_name} {words} errors. "
        f"Troubleshooting guide with common causes, solutions, and code examples."
    )


def write_page(base_dir, prefix, slug, tool_cfg):
    """Write a single .md page. Returns True if written."""
    existing = existing_slugs(base_dir)
    filename = slugify_for_filename(prefix, slug)
    basename = filename.replace(".md", "")

    if basename in existing:
        return False

    is_framework = "frameworks" in tool_cfg["frontmatter_kind"]
    title = title_for_slug(tool_cfg["cmd"], slug)
    desc = desc_for_slug(tool_cfg["cmd"], slug)
    body = make_body(tool_cfg["cmd"], tool_cfg["cmd"], slug, is_framework)

    fm = f"""---
title: "[Solution] {title}"
description: "{desc}"
{tool_cfg['frontmatter_kind']}
{tool_cfg['frontmatter_et']}
severities: ["error"]
weight: 5
comments: true
---

"""

    path = os.path.join(base_dir, filename)
    with open(path, "w") as f:
        f.write(fm)
        f.write(body)
    return True


def main():
    total_written = 0
    summary = {}

    for tool_name, cfg in TOOLS.items():
        base_dir = cfg["base"]
        prefix = cfg["prefix"]
        os.makedirs(base_dir, exist_ok=True)

        before = len(existing_slugs(base_dir))
        written = 0

        for slug in cfg["slugs"]:
            if written >= (TARGET - before):
                break
            if write_page(base_dir, prefix, slug, cfg):
                written += 1

        after = len(existing_slugs(base_dir))
        total_written += written
        summary[tool_name] = {"before": before, "after": after, "new": written}
        print(f"{tool_name:>10}: {before:>3} existing -> {after:>3} total ({written} new)")

    print(f"\nTotal new pages: {total_written}")
    print(f"All sections target: {TARGET}+")


if __name__ == "__main__":
    main()
