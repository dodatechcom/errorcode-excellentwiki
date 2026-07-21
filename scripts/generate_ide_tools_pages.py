#!/usr/bin/env python3
"""Generate error page markdown files for 6 IDE/tool sections to 100+ pages each."""

import os
import re

BASE = "/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools"

def slugify(name):
    s = name.lower().strip().replace(" ", "-").replace("/", "-").replace("'", "")
    s = re.sub(r"[^a-z0-9\-]", "", s)
    while "--" in s:
        s = s.replace("--", "-")
    return s

def titlecase(name):
    return " ".join(w.capitalize() if w not in ("of", "in", "on", "to", "for", "a", "an", "the", "and", "or", "not", "is") else w for w in name.split())

def capitalize_desc(name):
    return name[0].upper() + name[1:]

TOOLS = {
    "vscode": {
        "display": "VS Code",
        "error_type": "tool-error",
        "existing": {
            "debug-attach-error", "debug-breakpoint-error", "debug-launch-error",
            "emmet-error", "extension-activation-failed", "extension-api-error",
            "extension-host-crash", "file-association-error", "format-error",
            "git-integration-error", "high-cpu-error", "intellisense-error",
            "keybinding-error", "lint-error", "lsp-crash", "marketplace-error",
            "memory-error", "multi-root-error", "profiler-error", "python-error",
            "remote-container-error", "remote-development-error", "remote-ssh-error",
            "remote-wsl-error", "settings-sync-error", "snippets-error",
            "terminal-error", "typescript-error", "walkthrough-error", "workspace-error",
        },
        "pages": [
            "extension not found", "extension failed", "extension host terminated",
            "language server crashed", "IntelliSense not working",
            "code completion", "go to definition", "find references",
            "hover info", "format document", "format selection",
            "organize imports", "code actions", "quick fix", "refactor error",
            "rename symbol", "workspace trust", "restricted mode",
            "settings sync", "settings not applied", "keybinding conflict",
            "command not found", "palette not showing", "terminal error",
            "integrated terminal", "shell path not found", "launch.json",
            "debug config", "attach to process", "no debug adapter",
            "breakpoint not binding", "source map", "step over", "step into",
            "step out", "variable not available", "watch expression",
            "call stack", "debug console", "task runner", "tasks.json",
            "shell command", "problem matcher", "output panel", "problems panel",
            "markers", "git integration", "source control", "commit failed",
            "push rejected", "pull merge conflict", "staged changes",
            "stash error", "diff editor", "merge editor", "inline merge",
            "notebooks", "Jupyter kernel", "interactive window",
            "remote development", "SSH host not found", "SSH connection",
            "remote server", "container not found", "devcontainer",
            "WSL integration", "SSH config", "port forwarding", "code-server",
            "Web UI", "live share", "join session", "share terminal",
            "share debug", "file encoding", "line endings", "EOL sequence",
            "BOM", "language mode", "indentation", "tab size",
            "detect indentation", "trim whitespace", "snippet error",
            "user snippet", "global snippet", "project snippet",
            "emmet error", "emmet abbreviation", "emmet expansion",
            "markdown preview", "math in markdown", "Mermaid diagram",
            "search exclude", "files exclude", "watch exclusion",
            "file nesting", "file name not found", "dirty write",
            "will not save", "save error", "autosave", "file watcher",
            "process on Mac", "process on Linux", "process on Windows",
            "memory usage", "high CPU", "crash report", "telemetry",
            "disable telemetry", "update error", "install error",
            "corrupt installation", "extension marketplace", "gallery error",
            "offline mode", "proxy setting", "auth token",
        ],
    },
    "intellij": {
        "display": "IntelliJ IDEA",
        "error_type": "tool-error",
        "existing": {
            "change-signature-error", "code-analysis-error", "code-completion-error",
            "compilation-error", "database-error", "debug-error",
            "external-tools-error", "extract-error", "format-error",
            "generate-error", "gradle-integration-error", "indexing-error",
            "inline-error", "inspection-error", "inspections-error",
            "maven-integration-error", "memory-heap-error", "move-error",
            "navigation-error", "optimize-imports-error", "plugin-conflict-error",
            "profiler-error", "refactoring-error", "rename-error",
            "run-configuration-error", "spring-boot-error", "surround-error",
            "terminal-error", "test-error", "version-control-error",
        },
        "pages": [
            "project not found", "project import", "project structure",
            "module not found", "module dependency", "SDK not set",
            "JDK not found", "JDK version", "SDK configuration",
            "language level", "bytecode version", "compiler error",
            "build error", "make project", "rebuild project",
            "compile module", "annotation processing", "incremental compilation",
            "build output", "artifact configuration", "JAR artifact",
            "WAR artifact", "exploded artifact", "run configuration",
            "application configuration", "JUnit config", "TestNG config",
            "remote config", "tomcat config", "jetty config",
            "JBoss config", "VM options", "program arguments",
            "environment vars", "working directory", "classpath error",
            "module classpath", "library classpath", "SDK classpath",
            "cannot resolve symbol", "import not resolved",
            "dependency not indexed", "index error", "caches error",
            "invalidate caches", "file index", "module index",
            "Maven projects", "sync error", "reimport failed",
            "dependency graph", "artifact not found", "repository error",
            "Gradle projects", "Gradle sync", "Gradle JVM",
            "Gradle distribution", "wrapper error", "Kotlin plugin",
            "Kotlin JVM", "Kotlin JS", "Kotlin native", "Kotlin compiler",
            "Android plugin", "Android SDK", "AVD manager", "ADB error",
            "layout editor", "resource manager", "database tool",
            "data source", "SQL console", "query error",
            "schema not selected", "connection failed", "version control",
            "VCS root", "git branch", "git log", "git stash",
            "git merge", "git rebase", "conflict resolver", "changelist",
            "commit dialog", "push dialog", "code review",
            "inspection error", "inspection profile", "inspection severity",
            "on-the-fly inspection", "code cleanup", "optimize imports",
            "code coverage", "coverage suite", "test runner",
            "test report", "debugger error", "breakpoint properties",
            "method breakpoint", "field breakpoint", "exception breakpoint",
            "evaluate expression", "conditional breakpoint", "log breakpoint",
            "frame drop", "smart step", "force return", "throw exception",
            "profiler error", "CPU profiler", "memory profiler",
            "snapshot analysis", "flame graph", "call tree", "method list",
            "plugin error", "plugin conflict", "plugin disable",
            "plugin repository", "custom plugin", "IDE settings",
            "export settings", "import settings", "settings repository",
            "sync settings", "HTTP proxy", "SOCKS proxy", "no proxy",
            "firewall error", "certificate error", "license server",
            "activation error", "evaluation expired", "floating license",
        ],
    },
    "eclipse": {
        "display": "Eclipse",
        "error_type": "tool-error",
        "existing": {
            "build-path-error", "checkstyle-error", "code-completion-error",
            "compilation-error", "console-error", "content-assist-error",
            "database-error", "debug-error", "formatter-error",
            "git-integration-error", "gradle-integration-error", "jdt-error",
            "jpa-error", "maven-integration-error", "outline-error",
            "package-explorer-error", "plugin-error", "pmd-error",
            "problems-view-error", "properties-error", "quick-fix-error",
            "refactoring-error", "run-configuration-error",
            "svn-integration-error", "terminal-error", "test-error",
            "tomcat-error", "web-tools-error", "workspace-corruption", "xml-error",
        },
        "pages": [
            "workspace in use", "workspace locked", "cannot create workspace",
            "workspace path", "JVM terminated", "exit code",
            "Java was started", "JNI error", "-vm argument",
            "eclipse.ini", "launcher error", "configuration error",
            "config area", "feature not found", "plugin not loaded",
            "bundle not resolved", "missing dependency",
            "unsatisfied dependency", "constraint violation",
            "class not found", "NoClassDefFoundError",
            "ClassNotFoundException", "method not found",
            "NoSuchMethodError", "field not found", "NoSuchFieldError",
            "access restriction", "discouraged access", "forbidden reference",
            "project nature error", "project not configured",
            "build path error", "build path entry", "classpath variable",
            "JRE system library", "JRE not defined", "execution environment",
            "compiler compliance", "JDT error", "Java editor",
            "content assist", "source attachment", "javadoc location",
            "aspectJ error", "AJDT", "aspect missing", "pointcut error",
            "advice error", "inter-type declaration", "Maven Eclipse",
            "m2e plugin", "maven integration", "dependency resolution",
            "archetype error", "M2 repo", "settings.xml", "POM error",
            "PDE error", "plugin development", "target platform",
            "OSGi framework", "bundle manifest", "MANIFEST.MF",
            "build.properties", "product configuration", "feature project",
            "update site", "p2 repository", "metadata error",
            "artifact pool", "p2 director", "install error",
            "update error", "uninstall error", "dropins folder",
            "repository not found", "authentication failed", "mirror URL",
            "EMF error", "generated code", "model resource",
            "Xtext error", "Xtext grammar", "language generator",
            "DSL editor", "Mylyn error", "task repository",
            "bug tracker", "connector error", "local task",
            "RCP error", "RCP application", "Workbench advisor",
            "application model", "part descriptor", "perspective extension",
            "view extension", "editor extension", "handler extension",
            "menu contribution", "toolbar contribution", "command definition",
            "key binding", "context menu", "object contribution",
            "declarative services", "DS annotation", "component error",
            "reference error", "service binding", "settings error",
            "preference page", "preference store", "instance scope",
            "configuration scope", "project scope", "workspace preference",
            "export/import preference", "server runtime", "Tomcat server",
            "JEE server", "deploy error", "publish module",
            "server adapter", "debug server", "remote debug",
            "APT error", "annotation processing", "factory path",
            "processor option",
        ],
    },
    "neovim": {
        "display": "Neovim",
        "error_type": "tool-error",
        "existing": {
            "autocmd-error", "buffer-error", "clipboard-error",
            "completion-error", "config-error", "dap-error",
            "float-error", "git-integration-error", "healthcheck-error",
            "highlight-error", "init-lua-error", "keymap-error",
            "lazy-error", "lsp-crash", "lsp-diagnostics-error",
            "lsp-initialize-error", "lsp-timeout", "mason-error",
            "mason-lsp-error", "migration-error", "packer-error",
            "plugin-load-error", "plugin-manager-error", "statusline-error",
            "tab-error", "telescope-error", "terminal-error",
            "theme-error", "treesitter-error", "window-error",
        },
        "pages": [
            "Lua error", "Lua require", "module not found",
            "package.path", "package.cpath", "LuaRocks",
            "lua54.dll", "lua54.so", "VimL error",
            "E117 unknown function", "E118 no matching", "E119 no match",
            "E120 cannot use", "E121 key not found", "E122 invalid expression",
            "E123 internal error", "E124 missing", "E125 illegal",
            "E126 missing end", "E127 cannot define", "E128 function name",
            "E129 function", "E130 undefined variable",
            "E131 trailing characters", "E132 illegal character",
            "E133 string", "E134 list", "E135 dictionary",
            "E136 blob", "E137 floating point", "E138 line number",
            "E139 internal error", "E140 argument", "E141 invalid range",
            "E142 no marks", "E143 autocommand", "E144 non-numeric",
            "E145 line number", "plugin not loading", "packadd error",
            "packpath", "lazy loading", "plugin manager",
            "packer.nvim", "lazy.nvim", "vim-plug", "dein.vim",
            "minpac", "color scheme", "colorscheme not found",
            "terminfo error", "GUI font", "font not found",
            "GUI options", "gvimrc", "terminal emulator",
            ":terminal", "job control", "jobstart", "jobwait",
            "jobstop", "channel error", "chansend", "chanclose",
            "RPC error", "msgpack", "msgpackparse", "msgpackdump",
            "vim.inspect", "vim.pretty_print", "vim.print",
            "vim.notify", "vim.notify_once", "vim.cmd", "vim.api",
            "vim.fn", "vim.bo", "vim.wo", "vim.go", "vim.o",
            "vim.opt", "vim.opt_local", "vim.opt_global", "vim.g",
            "vim.v", "vim.env", "vim.b", "vim.w", "vim.t",
            "namespaced highlight", "vim.highlight", "treesitter",
            "parser not installed", "language parser", "query error",
            "captures error", "highlights error", "folds error",
            "indents error", "injections error", "LSP error",
            "language server", "lspconfig", "capabilities",
            "initialize error", "textDocument/hover",
            "textDocument/definition", "textDocument/references",
            "textDocument/completion", "textDocument/formatting",
            "textDocument/codeAction", "textDocument/diagnostic",
            "diagnostic error", "diagnostic signs", "virtual text",
            "float window", "diagnostic list", "telescope error",
            "finder error", "fzf error", "fzf-lua", "grep error",
            "live grep", "file picker", "buffer picker",
            "help tags", "helptags", "tagbar", "ctags",
            "goto definition", "tag jump", "tags file", "cscope",
            "quickfix list", "location list", "vimgrep", "cexpr",
            "make error", "compiler set", "errorformat",
            "autocommand", "autocmd", "augroup", "BufRead",
            "BufWrite", "FileType", "InsertEnter", "InsertLeave",
            "TextChanged", "VimEnter", "VimLeave", "OptionSet",
            "User command", "command! bang range nargs",
            "complete custom", "command completion",
            "argument completion", "mapping error", "noremap",
            "nnoremap", "inoremap", "vnoremap", "xnoremap",
            "snoremap", "map leader", "localleader", "timeoutlen",
            "ttimeoutlen", "keycode", "term codes",
            "bracketed paste", "register error", "clipboard",
            "clipboard provider", "xclip", "wl-copy", "pbcopy",
            "visual selection", "system clipboard", "'* register",
            "'+ register", ":reg", "expression register",
            "= expression", "black hole", "named register",
            "numbered register", "small delete", "yank register",
        ],
    },
    "vite": {
        "display": "Vite",
        "error_type": "tool-error",
        "existing": {
            "asset-error", "build-error7", "config-error6", "css-error",
            "dev-server-error", "import-error8", "pre-transform-error",
            "ssr-error", "vite-asset-error", "vite-asset-error-v2",
            "vite-build-error", "vite-build-error-v2", "vite-config-error",
            "vite-config-error-v2", "vite-css-error", "vite-css-error-v2",
            "vite-deps-error", "vite-deps-error-v2", "vite-dev-server-error",
            "vite-dev-server-error-v2", "vite-hmr-error", "vite-hmr-error-v2",
            "vite-plugin-error", "vite-plugin-error-v2", "vite-react-error",
            "vite-ssr-error", "vite-ssr-error-v2", "vite-svelte-error",
            "vite-tailwind-error", "vite-typescript-error", "vite-vue-error",
            "vite-wasm-error",
        },
        "pages": [
            "plugin not found", "plugin error", "vite.config",
            "config file not found", "config validation", "root path",
            "base URL", "mode not set", "env variable", "env prefix",
            "define not working", "server port", "strict port",
            "host binding", "HTTPS config", "proxy error",
            "proxy target", "proxy rewrite", "WebSocket proxy",
            "CORS error", "HMR error", "hot reload",
            "HMR connection", "WebSocket connection", "module graph",
            "dependency pre-bundling", "optimize deps", "dep scan",
            "dep cache", "esbuild error", "transform error",
            "build error", "rollup error", "output dir",
            "assets dir", "assets inline", "chunk split",
            "manual chunks", "entry chunk", "CSS code split",
            "CSS modules", "CSS import", "PostCSS error",
            "PostCSS config", "autoprefixer error", "tailwind CSS",
            "tailwind config", "@apply error", "SCSS/SASS error",
            "less error", "stylus error", "CSS url",
            "asset reference", "public dir", "static assets",
            "image import", "SVG import", "JSON import",
            "WASM import", "worker import", "web worker",
            "shared worker", "SSR error", "ssrLoadModule",
            "ssrFetchModule", "ssr external", "ssr noExternal",
            "library mode", "library entry", "library formats",
            "ESM format", "UMD format", "global name",
            "TypeScript error", "tsconfig path", "alias resolve",
            "path alias", "resolve alias", "node resolve",
            "browser field", "module field", "main field",
            "exports field", "conditions", "external globals",
            "glob import", "dynamic import", "import.meta.glob",
            "import.meta.url", "new URL import", "asset URL",
            "WASM helper", "webworker constructor", "preload error",
            "preload helper", "legacy plugin", "polyfill",
            "browser target", "browserslist", "build target",
            "minify error", "terser error", "manual chunks function",
            "chunk info", "emit assets", "emit file", "close bundle",
            "watch mode", "chokidar error", "file watcher",
            "notify plugin", "HTML plugin", "SPA fallback",
            "history fallback", "404 page",
        ],
    },
    "webpack": {
        "display": "Webpack",
        "error_type": "tool-error",
        "existing": {
            "chunk-loading", "config-error5", "hmr-error",
            "loaders-error", "module-not-found", "optimization-error",
            "syntax-error9", "typescript-error", "webpack-asset-error",
            "webpack-asset-error-v2", "webpack-build-error",
            "webpack-build-error-v2", "webpack-chunk-error",
            "webpack-chunk-error-v2", "webpack-config-error",
            "webpack-config-error-v2", "webpack-dev-server-error",
            "webpack-dev-server-error-v2", "webpack-hot-reload-error",
            "webpack-hot-reload-error-v2", "webpack-loader-error",
            "webpack-loader-error-v2", "webpack-module-not-found",
            "webpack-module-not-found-v2", "webpack-plugin-error",
            "webpack-plugin-error-v2", "webpack-tree-shaking-error",
            "webpack-treeshaking-error",
        },
        "pages": [
            "configuration error", "config not found", "config validation",
            "mode not set", "entry not found", "entry point",
            "output path", "public path", "filename not set",
            "chunk filename", "hash contenthash", "module rules",
            "rule test", "rule use", "loader not found",
            "loader order", "loader chain", "babel-loader",
            "babel config", "preset env", "@babel/preset-react",
            "@babel/preset-typescript", "ts-loader", "TypeScript config",
            "css-loader", "style-loader", "sass-loader",
            "less-loader", "postcss-loader", "file-loader",
            "url-loader", "asset module", "asset/resource",
            "asset/inline", "asset/source", "issuer condition",
            "resolve alias", "resolve extensions", "resolve modules",
            "symlinks", "fallback", "resolve fullySpecified",
            "plugins not found", "HtmlWebpackPlugin",
            "template not found", "MiniCssExtractPlugin",
            "split chunks", "cache groups", "chunks all",
            "minSize", "maxSize", "automaticNameDelimiter",
            "reuseExistingChunk", "optimization split",
            "runtime chunk", "module ids", "chunk ids",
            "named modules", "deterministic modules", "minimize error",
            "TerserPlugin", "CSS minimizer", "devtool",
            "source map", "eval", "cheap-source-map",
            "hidden-source-map", "nosources-source-map",
            "dev server", "devServer config", "hot reload",
            "live reload", "proxy dev", "historyApiFallback",
            "hmr hot", "webpack-serve", "webpack-dev-middleware",
            "webpack-hot-middleware", "Watch mode", "watchOptions",
            "poll ignored", "aggregateTimeout", "stats preset",
            "errors-only", "minimal", "normal", "verbose",
            "performance hints", "asset size limit",
            "entrypoint size", "maxAssetSize", "maxEntrypointSize",
            "assetFilter", "externals not found", "node global",
            "__dirname", "__filename", "global", "process.env",
            "ProvidePlugin", "DefinePlugin", "EnvironmentPlugin",
            "IgnorePlugin", "BannerPlugin",
            "ContextReplacementPlugin", "NormalModuleReplacementPlugin",
            "DllPlugin", "DllReferencePlugin",
            "ModuleFederationPlugin", "shared modules", "exposes",
            "remotes", "federation config", "container reference",
            "shared version", "eager loading", "singleton shared",
            "requiredVersion",
        ],
    },
}


def generate_page(tool_key, page_title):
    info = TOOLS[tool_key]
    display = info["display"]
    slug = slugify(page_title)
    title = f"{display} {page_title}"
    desc = f"Fix {display} {page_title.lower()} errors. Resolve issues when {page_title.lower()} functionality fails or produces unexpected behavior."

    solutions = f"""## Solutions

### Solution 1: Verify Configuration

Check your {display} configuration for the {page_title.lower()} setting. Ensure all required fields are properly specified and there are no syntax errors in your configuration file.

```
{{
  // Example configuration for {page_title.lower()}
  "setting": "value",
  "enabled": true
}}
```

### Solution 2: Restart {display}

Restart {display} to reset the affected subsystem. This clears temporary state and reloads configuration files.

```
# Close all {display} windows and restart
code --new-window
```

### Solution 3: Check Logs for Details

Open the {display} developer console or log files to find detailed error messages related to this issue.

1. Open the command palette
2. Run the "Developer: Toggle Developer Tools" command
3. Look for error messages in the Console tab

### Solution 4: Update {display}

Ensure you are running the latest version of {display}, as this issue may have been fixed in a recent release.

1. Check for updates in the Help menu
2. Install any available updates
3. Restart {display} after updating"""

    if slug.startswith("@") or slug.startswith(".") or slug.startswith("-"):
        # Escape or adjust slug for special characters
        pass

    # Ensure slug is safe - handle @babel, __dirname, etc.
    if slug.startswith("@babel"):
        slug = slug.replace("@", "at-").replace("/", "-")
    elif slug.startswith("__"):
        slug = "double-underscore-" + slug[2:]
    elif slug.startswith("@"):
        slug = "at-" + slug[1:]

    # Handle relref - no em dashes
    # The page_title may contain chars unsuitable for slug in certain places

    return f"""---
title: "[Solution] {display} {titlecase(page_title)}"
description: "{desc}"
date: 2026-07-21T00:00:00+08:00
draft: false
tool: "{tool_key}"
tags: ["{tool_key}", "ide", "{slug}"]
severity: "error"
---

# {display} {titlecase(page_title)}

## Error Message

```
{display} {titlecase(page_title)} error: The requested operation could not be completed. Check configuration and try again.
```

## Common Causes

- Configuration is missing or invalid for the {page_title.lower()} feature
- A required dependency or plugin is not installed or outdated
- Temporary state corruption caused by an unexpected shutdown
- Version incompatibility between {display} and related components

{solutions}

## Prevention Tips

- Keep {display} and all related plugins updated to the latest versions
- Review configuration files for syntax errors after making changes
- Regularly clear caches and temporary data to avoid state corruption

## Related Errors

- [{display} workspace error]({{{{< relref "/tools/{tool_key}/{slugify(page_title)}" >}}}})
"""


def main():
    total_new = {}
    for tool_key, info in TOOLS.items():
        existing = info["existing"]
        pages = info["pages"]
        dir_path = os.path.join(BASE, tool_key)
        os.makedirs(dir_path, exist_ok=True)

        # Also check files on disk
        on_disk = set()
        for f in os.listdir(dir_path):
            if f.endswith(".md"):
                on_disk.add(f[:-3])

        created = 0
        for page_title in pages:
            slug = slugify(page_title)

            # Handle special slugs
            if slug.startswith("@babel"):
                slug = slug.replace("@", "at-").replace("/", "-")
            elif slug.startswith("__"):
                slug = "double-underscore-" + slug[2:]
            elif slug.startswith("@"):
                slug = "at-" + slug[1:]

            if slug in existing or slug in on_disk:
                continue

            content = generate_page(tool_key, page_title)
            filepath = os.path.join(dir_path, f"{slug}.md")
            with open(filepath, "w") as f:
                f.write(content)
            created += 1

        total_new[tool_key] = created
        print(f"{info['display']}: {created} new pages (total now {len(on_disk) + created}/100+)")

    print("\n--- Summary ---")
    for tool_key, count in total_new.items():
        info = TOOLS[tool_key]
        print(f"{info['display']}: +{count} pages")


if __name__ == "__main__":
    main()
