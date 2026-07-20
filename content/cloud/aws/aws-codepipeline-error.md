---
title: "[Solution] AWS CodePipeline Error — stage/action/transition failures"
description: "Fix AWS CodePipeline errors. Resolve stage, action, and transition issues."
error-types: ["api-error"]
severities: ["error"]
weight: 154
---

An AWS CodePipeline error occurs when pipelines fail to execute, actions timeout, or transitions are stuck. CodePipeline orchestrates CI/CD workflows but requires correct action configuration at each stage.

## Common Causes

- Source stage fails to pull from CodeCommit/S3
- Build stage action times out (default 60 min)
- Deploy stage has no healthy instances
- Pipeline execution role lacks cross-account permissions
- Artifact bucket access denied

## How to Fix

### List Pipelines

```bash
aws codepipeline list-pipelines \
  --query 'pipelines[*].{Name:name,Version:version}'
```

### Get Pipeline State

```bash
aws codepipeline get-pipeline-state \
  --name my-pipeline \
  --query 'stageStates[*].{Name:stageName,Status:executionState.status}'
```

### Start Pipeline

```bash
aws codepipeline start-pipeline-execution \
  --name my-pipeline
```

### Create Pipeline

```bash
aws codepipeline create-pipeline \
  --pipeline '{
    "name": "my-pipeline",
    "roleArn": "arn:aws:iam::123456789012:role/CodePipelineRole",
    "artifactStore": {"type": "S3", "location": "my-pipeline-bucket"},
    "stages": [
      {"name": "Source", "actions": [{"name": "Source", "actionTypeId": {"category": "Source", "owner": "AWS", "provider": "CodeCommit", "version": "1"}, "configuration": {"RepositoryName": "my-repo", "BranchName": "main"}, "outputArtifacts": [{"name": "SourceOutput"}]}]},
      {"name": "Build", "actions": [{"name": "Build", "actionTypeId": {"category": "Build", "owner": "AWS", "provider": "CodeBuild", "version": "1"}, "configuration": {"ProjectName": "my-project"}, "inputArtifacts": [{"name": "SourceOutput"}], "outputArtifacts": [{"name": "BuildOutput"}]}]},
      {"name": "Deploy", "actions": [{"name": "Deploy", "actionTypeId": {"category": "Deploy", "owner": "AWS", "provider": "CodeDeploy", "version": "1"}, "configuration": {"ApplicationName": "my-app", "DeploymentGroupName": "my-dg"}, "inputArtifacts": [{"name": "BuildOutput"}]}]}
    ]
  }'
```

### Disable Transition

```bash
aws codepipeline disable-stage-transition \
  --pipeline-name my-pipeline \
  --stage-name Deploy \
  --transition-type Inbound \
  --reason "Manual approval pending"
```

## Examples

```bash
# Example 1: Action failed
# Action execution failed: Deployment failed
# Fix: check CodeDeploy deployment logs

# Example 2: Source stage failed
# Unable to access the artifact bucket
# Fix: verify CodePipeline IAM role has s3 access
```

## Related Errors

- [AWS CodeBuild Error]({{< relref "/cloud/aws/aws-codebuild-error" >}}) — CodeBuild errors
- [AWS CodeDeploy Error]({{< relref "/cloud/aws/aws-codedeploy-error" >}}) — CodeDeploy errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
