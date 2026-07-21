---
title: "OOM Killer Adjust Score Error"
description: "OOM killer targets wrong processes due to incorrect oom_score_adj"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# OOM Killer Adjust Score Error

OOM killer targets wrong processes due to incorrect oom_score_adj

## Common Causes

- Critical service has high oom_score_adj
- oom_score_adj not reset after service restart
- Default oom_score_adj too high for important services
- cgroup OOM settings conflicting with process scores

## How to Fix

1. Check OOM scores: `for pid in /proc/[0-9]*/oom_score; do echo "$pid: $(cat $pid)"; done | sort -t: -k2 -n`
2. Set score for important service: `echo -1000 > /proc/<PID>/oom_score_adj`
3. Configure systemd: `OOMScoreAdjust=-1000` in service file
4. Review oom_score_adj in /proc/<pid>/oom_score_adj

## Examples

```bash
# Check all process OOM scores
ps -eo pid,comm,oom_score --sort=oom_score | tail -20

# Protect a process from OOM killer
echo -1000 | sudo tee /proc/$(pidof sshd)/oom_score_adj
```
