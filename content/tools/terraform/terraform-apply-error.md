---
title: "[Solution] Terraform Apply Error — Fix Plan Application"
description: "Fix Terraform apply errors including resource creation failures, dependency issues, and timeout problems with actionable solutions."
---

## What This Error Means

A Terraform apply error occurs when Terraform cannot successfully create, update, or destroy resources during the `terraform apply` phase. Unlike plan errors, apply errors happen after Terraform has committed to making changes, leaving infrastructure in a partially modified state.

A typical error:

```
Error: Error creating instance: UnauthorizedOperation

You are not authorized to perform this operation. User:
arn:aws:iam::123456789012:user/deploy is not authorized to perform:
ec2:RunInstances on resource: arn:aws:ec2:us-east-1::instance/*
```

Or:

```
Error: Error applying plan

3 resources to apply, 1 error(s):
Error: aws_lambda_function.handler: InvalidParameterValueException:
The role defined for the function cannot be assumed by Lambda.
```

## Why It Happens

Apply errors surface due to:

- **Permission issues**: The IAM role or user lacks necessary permissions for the resource being created.
- **Dependency failures**: A required resource failed to create, cascading failures to dependent resources.
- **API throttling**: Cloud provider rate limits exceeded during bulk resource creation.
- **Timeout issues**: Resources taking longer than expected to provision.
- **Quota limits**: Account or region resource quotas exhausted.
- **Input validation**: Incorrect resource configuration values caught during creation.

## How to Fix It

**Step 1: Review the specific error message**

Identify the exact resource and error code from the output. Terraform marks failed resources clearly.

**Step 2: Fix permissions and retry only the failed resource**

```bash
# Check current identity
aws sts get-caller-identity

# Apply only the failed resource
terraform apply -target=aws_lambda_function.handler
```

**Step 3: Increase timeouts for slow resources**

```hcl
resource "aws_instance" "web" {
  instance_type = "t3.micro"

  timeouts {
    create = "10m"
    update = "10m"
    delete = "10m"
  }
}
```

**Step 4: Handle partial apply state**

After a failed apply, Terraform records which resources were successfully created. Review state:

```bash
terraform state list
terraform state show aws_instance.web
```

**Step 5: Retry the full apply**

Once the root cause is fixed, apply remaining changes:

```bash
terraform apply
```

## Common Mistakes

- **Running full apply repeatedly without fixing the root cause**: Use `-target` to isolate and fix the failing resource first.
- **Ignoring partial state after failures**: Always check `terraform state list` after a failed apply to understand what was created.
- **Not setting timeouts**: Long-running resources like databases and load balancers often need explicit timeouts.
- **Forgetting dependency ordering**: Use `depends_on` explicitly when implicit dependencies are not detected.

## Related Pages

- [Terraform Plan Changed](/tools/terraform/terraform-plan-changed/) — Plan drift before apply
- [Terraform Apply Error](/tools/terraform/terraform-apply-error/) — Resource creation failures
- [Ansible Task Failed](/tools/ansible/ansible-task-failed/) — Task execution errors
