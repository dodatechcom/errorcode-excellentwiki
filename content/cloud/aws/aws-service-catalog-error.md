---
title: "[Solution] AWS Service Catalog Error — portfolio/product/provision failures"
description: "Fix AWS Service Catalog errors. Resolve portfolio, product, and provisioned product issues."
error-types: ["api-error"]
severities: ["error"]
weight: 158
---

An AWS Service Catalog error occurs when portfolios are not shared, products fail to provision, or CloudFormation templates have errors. Service Catalog provides curated product portfolios for self-service provisioning.

## Common Causes

- CloudFormation template has syntax errors
- IAM role lacks CloudFormation execute permissions
- Portfolio not shared with end user account
- Product version constraints not satisfied
- Provisioned product name already exists

## How to Fix

### List Portfolios

```bash
aws servicecatalog list-portfolios \
  --query 'PortfolioDetails[*].{ID:Id,Name:DisplayName}'
```

### List Products

```bash
aws servicecatalog list-products \
  --query 'ProductSummaries[*].{ID:Id,Name:Name,Type:ProductType}'
```

### Create Portfolio

```bash
aws servicecatalog create-portfolio \
  --display-name "My DevOps Stack" \
  --description "Curated infrastructure products"
```

### Share Portfolio

```bash
aws servicecatalog create-portfolio-share \
  --portfolio-id port-xxx \
  --account-id 098765432109
```

### Provision Product

```bash
aws servicecatalog provision-product \
  --product-id prod-xxx \
  --provisioning-artifact-id pa-xxx \
  --provisioned-product-name my-stack \
  --provisioning-parameters Key=Environment,Value=production
```

## Examples

```bash
# Example 1: Provisioning failed
# ProvisionedProductPlanException: CloudFormation stack failed
# Fix: validate CloudFormation template in staging account

# Example 2: Access denied
# AccessDeniedException: Portfolio not shared with account
# Fix: share portfolio with target account
```

## Related Errors

- [AWS CloudFormation Error]({{< relref "/cloud/aws/aws-cloudformation-error" >}}) — CloudFormation errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS Organizations Error]({{< relref "/cloud/aws/aws-organizations-error" >}}) — Organizations errors
