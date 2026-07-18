---
title: "[Solution] Terraform Provisioner Execution Failed Error — How to Fix"
description: "Fix Terraform provisioner execution errors including SSH failures, script timeouts, and remote-exec connection issues with proven solutions."
comments: true
---

A Terraform provisioner execution failed error occurs when a `provisioner` block (such as `remote-exec`, `local-exec`, or `file`) cannot complete its task during resource creation or destruction. These errors typically appear after the resource itself has been successfully created.

## Why It Happens

Provisioners execute commands or transfer files on resources after they are created. They fail because:

- **SSH connection issues**: The provisioner cannot establish an SSH connection due to network restrictions, wrong key paths, or the instance not being fully booted.
- **Script failures**: The `remote-exec` script encounters errors, missing dependencies, or permission issues on the target machine.
- **Connection timeout**: The instance is not ready to accept connections when the provisioner attempts to connect, especially with boot-time delays.
- **Incorrect connection block**: The `connection` block specifies wrong user, port, or private key path.
- **Firewall or security group**: The target instance's security group blocks inbound SSH (port 22) or the provisioner's outbound traffic.
- **Provisioner not idempotent**: Running the same provisioner twice causes conflicts because it does not handle existing state gracefully.

## Common Error Messages

**Error: SSH connection refused**

```
Error: remote-exec provisioner error

connection refused: ssh: connect to host 54.123.45.67 port 22:
Connection refused

Most likely, the machine has not finished booting yet. Consider
increasing the timeout or adding a null_resource with a
remote-exec provisioner to wait for cloud-init.
```

**Error: SSH authentication failed**

```
Error: remote-exec provisioner error

ssh: handshake failed: ssh: unable to authenticate,
attempted methods [publickey none], no supported methods remain

Check the connection block user, private_key, and host.
```

**Error: Script exited with non-zero status**

```
Error: remote-exec provisioner error

Script exited with non-zero exit status: 127

Output: /bin/sh: line 3: docker: command not found

The remote-exec provisioner ran a script that failed because
the required command was not installed on the target machine.
```

**Error: File provisioner copy failed**

```
Error: file provisioner error

scp: /tmp/config.yaml: Permission denied

The file provisioner could not copy the file to the target
machine. Verify the connection user has write permission to
the destination directory.
```

## How to Fix It

### Solution 1: Add connection retries and timeouts

Increase the timeout and add retry logic for slow-booting instances:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  key_name      = "my-key"

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y nginx",
      "sudo systemctl enable nginx"
    ]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("~/.ssh/my-key.pem")
      host        = self.public_ip
      timeout     = "5m"
    }
  }
}
```

For instances that need boot time, use a `null_resource` with a delay:

```hcl
resource "null_resource" "wait_for_boot" {
  depends_on = [aws_instance.web]

  provisioner "local-exec" {
    command = "sleep 60"
  }
}

resource "null_resource" "configure_server" {
  depends_on = [null_resource.wait_for_boot]

  provisioner "remote-exec" {
    inline = ["sudo apt-get update && sudo apt-get install -y nginx"]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("~/.ssh/my-key.pem")
      host        = aws_instance.web.public_ip
      timeout     = "5m"
    }
  }
}
```

### Solution 2: Use cloud-init instead of provisioners

Terraform documentation recommends using `user_data` or cloud-init over provisioners:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  key_name      = "my-key"

  user_data = <<-EOF
              #!/bin/bash
              set -e
              apt-get update
              apt-get install -y nginx
              systemctl enable nginx
              systemctl start nginx

              cat > /etc/nginx/conf.d/app.conf << 'NGINX'
              server {
                listen 80;
                server_name _;
                location / {
                  proxy_pass http://localhost:3000;
                }
              }
              NGINX
              systemctl reload nginx
              EOF
}
```

### Solution 3: Fix connection block configuration

Verify and correct the connection parameters:

```hcl
# For AWS instances
connection {
  type        = "ssh"
  user        = "ubuntu"           # AMI-specific: ubuntu, ec2-user, admin
  private_key = file("~/.ssh/my-key.pem")
  host        = self.public_ip
  port        = 22
  timeout     = "5m"
}

# For Windows instances via WinRM
connection {
  type     = "winrm"
  user     = "Administrator"
  password = var.admin_password
  host     = self.public_ip
  port     = 5986
  https    = true
  insecure = true
  timeout  = "10m"
}
```

Verify the key permissions:

```bash
chmod 600 ~/.ssh/my-key.pem
```

### Solution 4: Add error handling in provisioner scripts

Make provisioner scripts robust with error handling:

```hcl
provisioner "remote-exec" {
  inline = [
    "set -e",
    "sudo apt-get update -qq",
    "sudo apt-get install -y -qq docker.io docker-compose",
    "sudo systemctl enable docker",
    "sudo usermod -aG docker ubuntu",
    "echo 'Docker installed successfully'",
    "docker --version"
  ]

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("~/.ssh/my-key.pem")
    host        = self.public_ip
    timeout     = "5m"
  }
}
```

For complex scripts, use `local-exec` with a proper script file:

```hcl
provisioner "local-exec" {
  command     = "bash ${path.module}/scripts/setup.sh"
  working_dir = path.module
  environment = {
    HOST     = self.public_ip
    SSH_KEY  = "~/.ssh/my-key.pem"
  }
  interpreter = ["bash", "-c"]
}
```

## Common Scenarios

**Scenario 1: Provisioner runs before instance is ready**

An EC2 instance with a small AMI boots quickly but cloud-init takes several minutes. The provisioner connects before packages are available. Use a `null_resource` with a sleep or use `cloud-init` status checks.

**Scenario 2: Provisioner succeeds on first apply but fails on destroy**

A `remote-exec` provisioner runs cleanup commands during destroy, but the instance is already in a terminated state. Use `when = destroy` with proper error handling and set the connection host dynamically.

**Scenario 3: Local-exec provisioner fails due to missing tool**

A `local-exec` provisioner calls `ansible-playbook` but Ansible is not installed on the machine running Terraform. Ensure the execution environment has all required tools or use `null_resource` with a local-exec bootstrap script.

## Prevent It

- **Prefer cloud-init over provisioners**: Use `user_data` for instance bootstrapping. It is more reliable, idempotent, and does not depend on SSH connectivity.
- **Always test provisioner scripts locally first**: Run the same commands manually on a test instance before adding them to Terraform.
- **Set explicit connection timeouts**: Never rely on the default timeout. Set `timeout = "5m"` or higher for slow-booting instances.

## Related Pages

- [Terraform Apply Error](/tools/terraform/terraform-apply-error/) — Resource creation failures
- [Terraform Cloud Error](/tools/terraform/terraform-cloud-error/) — Remote execution issues
- [Terraform Provider Error](/tools/terraform/terraform-provider-error/) — Provider connectivity
