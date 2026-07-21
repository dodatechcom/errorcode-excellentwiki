---
title: "[Solution] Bash Here Document Indentation Error"
description: "Fix Bash here document errors caused by incorrect indentation or delimiter handling."
tools: ["bash"]
error-types: ["tool-error"]
severities: ["error"]
---

# Bash Here Document Indentation Error

Bash here documents fail due to improper indentation or delimiter issues.

```
here-document at line 5 delimited by end-of-file
```

## Common Causes

- Delimiter word is indented (must be at column 0 unless using <<-)
- Tab vs space mismatch with <<- syntax
- Quoted delimiter prevents variable expansion
- Empty line before closing delimiter
- Heredoc inside function with local variables

## How to Fix

### Use <<- for Indented Delimiters

```bash
if true; then
    cat <<-EOF
    This line is indented with tabs
    The delimiter can be indented with tabs
	EOF
fi
```

### Quote Delimiter to Prevent Expansion

```bash
# Variables are expanded
cat <<EOF
Hello $USER, today is $(date)
EOF

# Variables are NOT expanded
cat <<'EOF'
Hello $USER, today is $(date)
EOF
```

### Heredoc with Variable Content

```bash
#!/bin/bash
TEMPLATE="user_conf"
HOSTNAME="webserver01"

cat <<EOF > "$TEMPLATE"
server {
    listen 80;
    server_name ${HOSTNAME};
    root /var/www/${HOSTNAME};
}
EOF
```

### Indented Heredoc in Functions

```bash
generate_config() {
    local port=$1
    cat <<-CONF
	listen ${port};
	server_name example.com;
	CONF
}
```

## Examples

```bash
#!/bin/bash
# Proper heredoc usage patterns

# 1. Generate config file
cat > /etc/nginx/sites-available/app.conf <<'NGINX'
server {
    listen 80;
    server_name app.example.com;
    location / {
        proxy_pass http://127.0.0.1:3000;
    }
}
NGINX

# 2. Multi-line string variable
read -r -d '' SQL <<'SQL'
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
SQL

echo "$SQL"
```
