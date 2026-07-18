---
title: "[Solution] Go CDK Error — How to Fix"
description: "Fix Go CDK errors. Handle construct configuration, synthesis, stack output, and resource creation."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go CDK Error

Fix Go CDK errors. Handle construct configuration, synthesis, stack output, and resource creation.

## Why It Happens

- CDK construct is not properly configured causing synthesis failures
- Stack synthesis fails because of missing AWS account configuration
- Resource properties are incorrect causing CloudFormation deployment failures
- CDK app does not synthesize because of missing dependencies

## Common Error Messages

```
cdk: construct not found
```
```
cdk: synthesis failed
```
```
cdk: invalid resource properties
```
```
cdk: stack output not found
```

## How to Fix It

### Solution 1: Configure CDK stack

```go
import (
    "github.com/aws/aws-cdk-go/awscdk/v2"
    "github.com/aws/aws-cdk-go/awscdk/v2/awslambda"
    "github.com/aws/constructs-go/constructs/v10"
)
type MyStack struct {
    awscdk.Stack
}
```

### Solution 2: Create resources

```go
func NewMyStack(scope constructs.Construct, id string, props *MyStackProps) awscdk.Stack {
    stack := awscdk.NewStack(scope, &id, &props.StackProps)
    awslambda.NewFunction(stack, jsii.String("MyFunction"), &awslambda.FunctionProps{
        Runtime: awslambda.Runtime_GO_1_X(),
        Handler: jsii.String("main"),
        Code:    awslambda.Code_FromAsset(jsii.String("./lambda")),
    })
    return stack
}
```

### Solution 3: Synthesize and deploy

```bash
cdk bootstrap
cdk synth
cdk deploy
```

### Solution 4: Add outputs

```go
awscdk.NewCfnOutput(stack, jsii.String("FunctionName"), &awscdk.CfnOutputProps{
    Value: function.FunctionName(),
})
```

## Common Scenarios

- CDK synthesis fails because of wrong resource properties
- Stack deployment fails because of missing IAM permissions
- CDK app does not find the right AWS account

## Prevent It

- Use CDK documentation for correct resource property names
- Ensure AWS credentials are configured correctly
- Run cdk synth to validate before deploying
