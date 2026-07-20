---
title: "[Solution] Unexpected End of File (EOF)"
description: "Bash script ends unexpectedly with an unexpected EOF error."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# [Solution] Unexpected End of File (EOF)

This error occurs when Bash reaches the end of a file while still expecting more input, typically due to unclosed constructs.

### Common Causes
- Missing closing keyword (`done`, `fi`, `esac`, `}`) for a compound command.
- Unclosed `case` statement or `select` loop.
- Script truncated during transfer or editing.

### How to Fix
```bash
# Verify matching pairs of control structures
grep -n 'if\|then\|else\|fi' script.sh
grep -n 'for\|while\|until\|do\|done' script.sh

# Use shellcheck to detect unclosed blocks
shellcheck script.sh

# Count opening vs closing keywords
opens=$(grep -cE '^(if|for|while|until|case) ' script.sh)
closes=$(grep -cE '^(done|fi|esac)' script.sh)
echo "Opens: $opens, Closes: $closes"
```

### Example
```bash
# Broken script
#!/bin/bash
for i in 1 2 3; do
    echo "$i"
# missing: done

# Fixed script
#!/bin/bash
for i in 1 2 3; do
    echo "$i"
done
```
