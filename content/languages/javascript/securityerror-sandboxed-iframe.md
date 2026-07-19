---
title: "[Solution] SecurityError Sandbox — Blocked Script Execution in iframe Fix"
description: "Fix SecurityError when iframe sandbox prevents script execution or form submission."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Sandbox SecurityError

```html
<!-- Scripts blocked -->
<iframe sandbox src="page.html"></iframe>

<!-- Allow scripts -->
<iframe sandbox="allow-scripts" src="page.html"></iframe>

<!-- Allow scripts and same-origin -->
<iframe sandbox="allow-scripts allow-same-origin" src="page.html"></iframe>
```
