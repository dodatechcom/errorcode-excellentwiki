import os, json

def slug(s):
    return s.lower().replace(" ", "-").replace("/", "-").replace("--", "-")

def gen_all(provider, out_dir, pages, prefix):
    existing = {f.rsplit(".", 1)[0] for f in os.listdir(out_dir) if f.endswith(".md")}
    count = 0
    for title, desc, causes, cmds in pages:
        s = slug(f"{prefix} {title}")
        if s in existing:
            i = 2
            while f"{s}-v{i}" in existing:
                i += 1
            s = f"{s}-v{i}"
        fname = f"{s}.md"
        fpath = os.path.join(out_dir, fname)
        if os.path.exists(fpath):
            print(f"  skip: {fname}")
            continue
        short = title.replace(f"{provider.upper()} ", "")
        lines = []
        lines.append("---")
        lines.append(f"title: \"[Solution] {provider.upper()} {title}\"")
        lines.append(f"description: \"{desc}\"")
        lines.append(f"cloud: [\"{provider.lower()}\"]")
        lines.append("error-types: [\"cloud-error\"]")
        lines.append("severities: [\"error\"]")
        lines.append("weight: 5")
        lines.append("---")
        lines.append("")
        lines.append(f"The `{short}` error occurs when a {provider.upper()} service cannot complete the requested operation.")
        lines.append("")
        lines.append("## Common Causes")
        lines.append("")
        for c in causes:
            lines.append(f"- {c}")
        lines.append("")
        lines.append("## How to Fix")
        lines.append("")
        for lbl, cmd in cmds:
            lines.append(f"### {lbl}")
            lines.append("")
            lines.append("```bash")
            lines.append(cmd)
            lines.append("```")
            lines.append("")
        lines.append("## Examples")
        lines.append("")
        for c in causes[:4]:
            lines.append(f"- Example scenario: {c.lower().rstrip('.')}")
        lines.append("")
        lines.append("## Related Errors")
        lines.append("")
        lines.append(f"- [{provider.upper()} EC2 Error]({{{{< relref \"/cloud/{provider.lower()}/{prefix}-error\" >}}}}) -- General errors")
        lines.append(f"- [{provider.upper()} Logging Error]({{{{< relref \"/cloud/{provider.lower()}/{prefix}-logging-error\" >}}}}) -- Logging errors")
        with open(fpath, "w") as f:
            f.write("\n".join(lines) + "\n")
        print(f"  CREATED: {fname}")
        count += 1
    return count
