---
title: "[Solution] AWS Step Functions Error — state/execution/definition failures"
description: "Fix AWS Step Functions errors. Resolve state machine, execution, and definition issues."
error-types: ["api-error"]
severities: ["error"]
weight: 147
---

An AWS Step Functions error occurs when executions fail, state machine definitions have syntax errors, or task states encounter integration failures. Step Functions orchestrates workflows but requires correct state machine definitions.

## Common Causes

- State machine definition JSON syntax invalid
- Lambda task function ARN does not exist
- Execution input/output size exceeds 256 KB limit
- Map state parallelism limit exceeded (40)
- Wait state timestamp in the past

## How to Fix

### List State Machines

```bash
aws stepfunctions list-state-machines \
  --query 'stateMachines[*].{Name:name,ARN:stateMachineArn,Status:status}'
```

### Describe State Machine

```bash
aws stepfunctions describe-state-machine \
  --state-machine-arn arn:aws:states:us-east-1:123456789012:stateMachine:my-workflow
```

### List Executions

```bash
aws stepfunctions list-executions \
  --state-machine-arn arn:aws:states:us-east-1:123456789012:stateMachine:my-workflow \
  --max-items 10
```

### Start Execution

```bash
aws stepfunctions start-execution \
  --state-machine-arn arn:aws:states:us-east-1:123456789012:stateMachine:my-workflow \
  --input '{"key": "value"}'
```

### Create State Machine

```bash
aws stepfunctions create-state-machine \
  --name my-workflow \
  --definition '{"StartAt":"FirstState","States":{"FirstState":{"Type":"Task","Resource":"arn:aws:lambda:us-east-1:123456789012:function:my-function","End":true}}}' \
  --role-arn arn:aws:iam::123456789012:role/StepFunctionsRole
```

## Examples

```bash
# Example 1: Definition invalid
# InvalidDefinition: State machine definition is not valid JSON
# Fix: validate JSON with a linter

# Example 2: Execution failed
# ExecutionFailed: Lambda function returned error
# Fix: check Lambda function logs and retry policy
```

## Related Errors

- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS CloudFormation Error]({{< relref "/cloud/aws/aws-cloudformation-error" >}}) — CloudFormation errors
