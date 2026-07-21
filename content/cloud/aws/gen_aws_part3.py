"""Generate AWS cloud error pages - Part 3: ECS/EKS, API Gateway, CloudFront, Route53, CloudWatch, KMS/Security"""
import os

OUTPUT_DIR = "/home/admin1/projects/ErrorCode.excellentwiki.com/content/cloud/aws"
EXISTING = {f.rsplit(".", 1)[0] for f in os.listdir(OUTPUT_DIR) if f.endswith(".md")}

PAGES = []

def add(prefix, title, desc, causes, commands):
    base = title.lower().replace(" ", "-").replace("/", "-").replace("--", "-").replace("_", "-")
    candidate = f"{prefix}-{base}"
    slug = candidate
    if slug in EXISTING:
        i = 2
        if f"{slug}-v{i}" in EXISTING:
            i += 1
        slug = f"{slug}-v{i}"
    PAGES.append((title, desc, slug, causes, commands))

def write_pages():
    for title, desc, slug, causes, commands in PAGES:
        filename = f"aws-{slug}.md"
        fpath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(fpath):
            print(f"  SKIP: {filename}")
            continue
        lines = [
            "---",
            f"title: \"[Solution] AWS {title}\"",
            f"description: \"{desc}\"",
            "cloud: [\"aws\"]",
            "error-types: [\"cloud-error\"]",
            "severities: [\"error\"]",
            "weight: 5",
            "---",
            "",
            f"The `{title.replace('AWS ', '')}` error occurs when an AWS service cannot complete the requested operation.",
            "",
            "## Common Causes",
            "",
        ]
        for c in causes:
            lines.append(f"- {c}")
        lines.extend(["", "## How to Fix", ""])
        for label, cmd in commands:
            lines.append(f"### {label}")
            lines.append("")
            lines.append("```bash")
            lines.append(cmd)
            lines.append("```")
            lines.append("")
        lines.extend(["## Examples", ""])
        for c in causes[:4]:
            lines.append(f"- Example scenario: {c.lower()}")
        lines.extend(["", "## Related Errors", ""])
        lines.append(f"- [AWS EC2 Error]({{{{< relref \"/cloud/aws/aws-ec2-error\" >}}}}) -- General EC2 errors")
        lines.append(f"- [AWS CloudWatch Error]({{{{< relref \"/cloud/aws/aws-cloudwatch-error\" >}}}}) -- CloudWatch errors")
        with open(fpath, "w") as f:
            f.write("\n".join(lines) + "\n")
        print(f"  CREATED: {filename}")

# ===================== ECS / EKS (19 pages) =====================
add("ecs", "ECS Cluster Not Found",
    "ClusterNotFoundException when ECS cluster does not exist.",
    ["Cluster name is incorrect",
     "Cluster was deleted by another team",
     "Cluster belongs to a different AWS account",
     "Region mismatch"],
    [("List clusters", "aws ecs list-clusters"),
     ("Describe cluster", "aws ecs describe-clusters --clusters my-cluster")])

add("ecs", "ECS Service Not Stable",
    "ServiceNotActiveException/StabilityError when service is not stable.",
    "Failed to meet minimum healthy percent",
    "Task definition execution changes break tasks",
    "Service is DELETING or DRAINING",
    "Health check grace period expired"],
    [("Describe service", "aws ecs describe-services --services my-service --cluster my-cluster")])

add("ecs", "ECS Task Definition Error",
    "InvalidParameterException/ClientException for task definitions.",
    "Task definition includes non-existent container image",
    "Environment variables exceed 4KB limit",
    "Memory/hard/soft limit configuration mismatch",
    "Task role is missing permissions"],
    [("List task definitions", "aws ecs list-task-definitions"),
     ("Register new task def", "aws ecs register-task-definition --family my-task --container-definitions file://container.json")])

add("ecs", "Container Image Pull Failure",
    "CannotPullContainerError when ECS cannot pull the container image.",
    "Image not found in the registry",
    "Registry URL is incorrect",
    "Credentials for private registry missing or expired",
    "Image tag is missing or malformed"],
    [("Check image availability", "aws ecr describe-images --repository-name my-repo"),
     (force_login = "Use GetLogin API", "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com")])

add("fargate", "Fargate Capacity Issue",
    "FargateCapacityExhaustion/Fargate quota reached.",
    "Regional Fargate On-Demand capacity limit hit",
    "Fargate Spot capacity temporarily exhausted",
    "Both Fargate Spot and On-Demand pools empty",
    "Specified CPU/GB combination not yet available"],
    [("Check Fargate usage", "aws service-quotas get-service-quota --service-code fargate --quota-code L-2FA1B95F")])

add("fargate", "Fargate Spot Not available",
    "FargateSpotCapacityUnavailable for Fargate spot tasks.",
    "Fargate Spot capacity in the region is exhausted",
    "Spot interruption rate is high",
    "Fargate Spot is not available on this platform version"],
    [("Use Fargate On-Demand", "aws ecs run-task --launch-type FARGATE --cluster my-cluster")])

add("ecs", "ELB Target Group Error",
    "InvalidTargetException/TargetGroupNotFound for load balancer targets.",
    "Target group does not exist",
    "The service is not in the same VPC as the target group",
    "Health check on target group fails",
    "Port mismatch between service and target group"],
    [("List target groups", "aws elbv2 describe-target-groups")])

add("ecs", "Service Auto Scaling Error",
    "ServiceAutoScalingError/ValidationException for ECS Auto Scaling.",
    "IAM role for auto scaling is misconfigured",
    "Cooldown period prevents frequent changes",
    "Min tasks greater than max tasks",
    "Service not found for auto scaling"],
    [("Describe scalable targets", "aws application-autoscaling describe-scalable-targets --service-namespace ecs")])

add("ecs", "Service Discovery Error",
    "ServiceDiscoveryDisabled/InvalidParameter for Service Discovery.",
    "Route53 private hosted zone not created",
    "Service discovery instance type mismatch",
    "Namespace does not exist",
    "Container IP address type not selected"],
    [("Describe services", "aws servicediscovery list-services")])

add("ecs", "Cluster Not Found (EKS)",
    "ResourceNotFoundException for EKS cluster.",
    "Cluster name is incorrect",
    "Cluster was deleted",
    "Cluster in other account or region",
    "IAM permissions missing"],
    [("List clusters", "aws eks list-clusters"),
     ("Describe cluster", "aws eks describe-cluster --name my-cluster")])

add("eks", "EKS Node Group Error",
    "ResourceNotFoundException/InvalidRequest for node groups.",
    "Node group not in the specified cluster",
    "Node group in DELETE or CREATE_FAILED state",
    "Instance type not supported for the AMI",
    "Node group scaling is at boundary"],
    [("List node groups", "aws eks list-nodegroups --cluster-name my-cluster")])

add("eks", "Fargate Profile Error",
    "InvalidParameterException/FargateProfileRequired for EKS Fargate.",
    "Fargate profile selector does not match pods",
    "Maximum Fargate profiles limit reached",
    "IAM role permissions missing"],
    [("List profiles", "aws eks list-fargate-profiles --cluster my-cluster")])

add("eks", "kubeconfig Error",
    "AccessDenied/InvalidStateException for kubeconfig.",
    "kubeconfig not configured for this cluster",
    "IAM role not authorized to update kubeconfig",
    "Cluster endpoint private and not accessible"],
    [("Update kubeconfig", "aws eks update-kubeconfig --region us-east-1 --name my-cluster")])

add("eks", "EKS OIDC Provide Error",
    "InvalidParameterException for OIDC Identity Provider.",
    "OIDC provider URL does not match cluster issuer",
    "OIDC provider thumbprint is incorrect",
    "Provider not associated with the cluster"],
    [("List OIDC providers", "aws eks describe-cluster --name my-cluster --query cluster.identity.oidc")])

add("eks", "IRSA Error",
    "AccessDenied/NoCredentials for IAM roles service accounts.",
    "Service account IAM role annotation missing",
    "Trust policy between OIDC and IAM misconfigured",
    "themes.oci.aws.region not set in EKS ConfigMap"],
    [("Check Service Account", "kubectl describe serviceaccount my-sa -n default")])

add("ecr", "ECR Authentication Error",
    "AccessDenied/LifecyclePolicyNotFound for registry authentication.",
    "Docker login credentials expired",
    "IAM user does not have ECR permissions",
    "ECR authorization token request fails"],
    [("Get password", "aws ecr get-login-password --region us-east-1")])

add("ecr", "Docker push Error",
    "Denied/DiskFull/EcrImageDoesNotExist for Docker push to ECR.",
    "Repository does not exist",
    "Docker image size exceeds limit (40GB)",
    "Push rate exceeded for the repository",
    "Authentication token has expired"],
    [("Create repository", "aws ecr create-repository --repository my-repo")])

add("ecr", "Repository Policy Error",
    "InvalidParameterException/RepositoryNotFoundException for ECR policy.",
    "Repository policy exceeds 20 KB limit",
    "Policy syntax is invalid",
    "Policy specifies a nonexistent principal",
    "Cross-account access incorrect"],
    [("Get repository policy", "aws ecr get-repository-policy --repository my-repo")])

# ===================== API Gateway (19 pages) =====================
add("api-gateway", "REST API Not Found",
    "NotFoundException when the REST API does not exist.",
    "API ID is incorrect",
    "API was deleted",
    "API in different region or account"],
    [("List APIs", "aws apigateway get-rest-apis")])

add("api-gateway", "API Deployment Error",
    "BadRequestException/LimitExceeded for API deployment.",
    "Deployment already exists with this ID",
    "Stage does not support deployment",
    "Invalid deployment description"],
    [("Create deployment", "aws apigateway create-deployment --rest-api-id abc123 --stage prod")])

add("api-gateway", "Stage Not Found",
    "NotFoundException for API stage.",
    "Stage name does not exist",
    "Stage was deleted",
    "Stage name is case-sensitive"],
    [("List stages", "aws apigateway get-stages --rest-api-id abc123")])

add("api-gateway", "Resource Path Error",
    "BadRequestException for invalid resource path.",
    "Path does not match configured resources",
    "Path parameter name in URI not defined",
    "Resource hierarchy is incorrect"],
    [("List resources", "aws apigateway get-resources --rest-api-id abc123")])

add("api-gateway", "Method Not Defined",
    "NotFoundException for request method not enabled.",
    "HTTP method not enabled on the resource",
    "Method does not exist in API definition"],
    [("Get method", "aws apigateway get-method --rest-api-id abc123 --resource-id def456 --http-method POST")])

add("api-gateway", "Integration Failed",
    "BadRequestException/IntegrationFailure for backend integration.",
    "Integration type not set for the method",
    "Endpoint URL is invalid or unreachable",
    "Timeout waiting for backend (default 29s)"],
    [("Get integration", "aws apigateway get-integration --rest-api-id abc123 --resource-id def456 --http-method GET")])

add("api-gateway", "Lambda proxy Integration Error",
    "InternalServerError for Lambda proxy integration.",
    "Lambda function does not exist",
    "Lambda function returns invalid response format",
    "Function execution role permissions insufficient"],
    [("Check Lambda response", "aws lambda invoke --function-name my-function response.json")])

add("api-gateway", "Model/Schema Error",
    "BadRequestException for invalid request model/schema.",
    "Request body does not match the API schema",
    "Required fields missing in the request body",
    "Model not defined for the content type"],
    [("Get model", "aws apigateway get-model --rest-api-id abc123 --model-name MyModel")])

add("api-gateway", "API Key Error",
    "BadRequestException/Forbidden for API key issues.",
    "API key is required but missing in the request",
    "API key has been deactivated",
    "API usage plan and key mismatch"],
    [("List API keys", "aws apigateway get-api-keys")])

add("api-gateway", "Usage Plan Error",
    "BadRequestException/LimitExceeded for usage plans.",
    "API is not associated with any usage plan",
    "Throttle or quota limit exceeded",
    "Usage plan ID is invalid"],
    [("List usage plans", "aws apigateway get-usage-plans")])

add("api-gateway", "WAF Association Error",
    "BadRequestException for WAF web ACL association.",
    "Web ACL for regional resource does not exist",
    "WAF v1 ACL cannot be used with REST API",
    "Web ACL already associated with this resource"],
    [("List for resource", "aws wafv2 list-resources-for-web-acl --web-acl-arn arn:aws:waf...")])

add("api-gateway", "Domain Name Error",
    "NotFoundException/BadRequestException for custom domain.",
    "Domain name is not set up in API Gateway",
    "ACM certificate does not match the domain",
    "Route53 record missing for the domain"],
    [("List domain names", "aws apigateway get-domain-names")])

add("api-gateway", "Base Path Mapping Error",
    "NotFoundException/BadRequest for base path mapping.",
    "Base path does not match any API mapping",
    "Domain name not found for mapping"],
    [("Get base path mappings", "aws apigateway get-base-path-mappings --domain my-api.com")])

add("api-gateway", "Canary deployment Error",
    "BadRequestException/NotFoundException for canary settings.",
    "Canary not enabled on the stage",
    "Invalid canary traffic percentage",
    "Stage name does not have canary"],
    [("Get canary settings", "aws apigateway get-stage --rest-api abc123 --stage prod")])

add("api-gateway", "Throttling quota exceeded",
    "LimitExceededException/TooManyRequests for throttling.",
    "Per-account throttling limit hit (10,000 RPS)",
    "Regional rate limit exceeded",
    "Usage plan throttling exceeded"],
    [("Check usage plan", "aws apigateway get-usage-plan --usage-plan-id plan123")])

# ===================== CloudFront (19 pages) =====================
add("cloudfront", "Distribution Not Found",
    "NoSuchDistribution when the CloudFront distribution does not exist.",
    "Distribution ID is wrong",
    "Distribution has been deleted",
    "Distribution belongs to different account"],
    [("List distributions", "aws cloudfront list-distributions")])

add("cloudfront", "Origin not accessible",
    "OriginAccessDenied/OriginNotFound for CloudFront origin.",
    "Origin bucket policy does not allow CloudFront",
    "Origin is not in same account",
    "Origin endpoint unreachable",
    "Origin OAI/OAC credentials incorrect"],
    [("Check origin domain", "aws cloudfront get-distribution --id E123EXAMPLE")])

add("cloudfront", "CNAME already exists",
    "CNAMEAlreadyExists for an alternative domain.",
    "CNAME already associated with another distribution",
    "CNAME belongs to another AWS account",
    "Domain used on another CloudFront distribution"],
    [("List aliases", "aws cloudfront get-distribution --id E123EXAMPLE --query Distribution.DistributionConfig.Aliases")])

add("cloudfront", "SSL cert not found",
    "InvalidViewerCertificate/BadRequest for SSL issues.",
    "ACM cert not in us-east-1 region",
    "Cert does not match the CNAME domain",
    "Cert is expired or not valid"],
    [("List ACM certs", "aws acm list-certificates --region us-east-1")])

add("cloudfront", "Viewer protocol error",
    "InvalidProtocolException/InvalidViewerCertificate.",
    "HTTPS only selected but no SSL cert associated",
    "Viewer protocol set incorrectly in cache behavior",
    "Protocol policy mismatch between patterns"],
    [("Update cache behavior", "aws cloudfront update-distribution --id E123EXAMPLE --default-cache-behavior file://cache.json")])

add("cloudfront", "Cache behavior error",
    "InvalidArgumentException for cache behavior routing.",
    "Path pattern conflicts with another behavior",
    "Priority order of cache behaviors is ambiguous",
    "Default cache behavior must be set"],
    [("Get distribution config", "aws cloudfront get-distribution-config --id E123EXAMPLE")])

add("cloudfront", "TTL config error",
    "InvalidArgumentException for TTL settings.",
    "Minimum TTL cannot be greater than maximum TTL",
    "Default TTL must be less than maximum TTL",
    "TTL values must be >= 0"],
    [("Update distribution", "aws cloudfront update-distribution --id E123EXAMPLE --distribution-config file://config.json")])

add("cloudfront", "Invalidation error",
    "InvalidArgumentException/BatchToLarge for invalidations.",
    "Invalidation path does not match CloudFront format",
    "Too many items in a single invalidation (limit 3000 per batch)"],
    [("Create invalidation", "aws cloudfront create-invalidation --distribution-id E123EXAMPLE --paths /images/*")])

add("cloudfront", "Field level encryption",
    "NotFound/InvalidArgument for field-level encryption.",
    "Field level encryption config not found",
    "Profile ID does not exist",
    "Encryption key not configured"],
    [("List field level encryption", "aws cloudfront list-field-level-encryption-configs")])

add("cloudfront", "WAF web ACL error",
    "InvalidWebACLId/NoSuchWebAcl for CloudFront WAF.",
    "Web ACL ID is not for CloudFront",
    "Web ACL region is set incorrectly (must be us-east-1)",
    "Web ACL does not exist"],
    [("List web ACLs", "aws wafv2 list-web-acls --scope CLOUDFRONT")])

add("cloudfront", "Geo restriction error",
    "IllegalUpdate/CannotDelete for geo restriction.",

    "Location code is invalid",
    "Both whitelist and blocklist specified",
    "Cannot have 0 locations",


    [("Update geo restriction", "aws cloudfront update-distribution --id E123EXAMPLE --distribution-config file://config.json")])

add("cloudfront", "Signed URL error",
    "AccessDenied/InvalidArgument for CloudFront signed URLs.",
    "Signed URL policy or condition is invalid",
    "Signature expired or timestamp skewed",
    "Canonicalized resource does not match"],
    [("Generate signed URL", "aws cloudfront sign --url https://xxx.cloudfront.net/file.txt --key-pair-id K12XYZ")])

add("cloudfront", "OAI/OAC error",
    "IllegalUpdate/OriginAccessControlNotFound for OAI/OAC.",
    "OAC not enabled for the origin",
    "OAI ID does not exist",
    "S3 bucket policy missing authorization"],
    [("Create OAC", "aws cloudfront create-origin-access-control --origin-access-control file://oac.json")])

add("cloudfront", "Origin access dened",
    "OriginAccessIdentityAccessDenied/OIConfigurationError.",
    "S3 bucket ACL lacking CloudFront OAI perms",
    "Origin protocol mismatch (HTTPS vs HTTP)",
    "Bucket is in a different region"],
    [("Check bucket policy", "aws s3api get-bucket-policy --bucket my-bucket")])

# ===================== Route53 (19 pages) =====================
add("route53", "Hosted zone not found",
    "NoSuchHostedZone when the zone does not exist.",
    "Zone ID is incorrect",
    "Zone deleted by administrator",
    "Zone belongs to different account"],
    [("List zones", "aws route53 list-hosted-zones")])

add("route53", "Record set conflict",
    "InvalidChangeBatch/ConflictingDomainExists for record sets.",
    "Record with the same name and type already exists",
    "Alias record target conflicts with existing record",
    "CNAME record cannot be at the zone apex"],
    [("List records", "aws route53 list-resource-record-sets --hosted-zone-id ZONE123")])

add("route53", "Alias target error",
    "InvalidChangeBatch/VPCAssociationNotFound for alias targets.",
    "Alias target does not exist in Route53",
    "Elastic LB or CF distribution target DNS mismatch",
    "Alias target in different account"],
    [("Get alias target", "aws route53 list-resource-record-sets --hosted-zone-id ZONE123 --query ResourceRecordSets[?Type==`A`].AliasTarget")])

add("route53", "Health check error",
    "NoSuchHealthCheck/HealthCheckInUse for health checks.",
    "Health check ID does not exist",
    "Health check configuration invalid",
    "Health check endpoint unreachable"],
    [("List health checks", "aws route53 list-health-checks")])

add("route53", "Failover routing error",
    "InvalidChangeBatch for failover records.",
    "Failover routing must have both PRIMARY and SECONDARY",
    "Same record cannot have two PRIMARY entries",
    "Failover record not in the same hosted zone"],
    [("Get failover records", "aws route53 list-resource-record-sets --hosted-zone-id ZONE123")])

add("route53", "Latency routing error",
    "InvalidChangeBatch for latency records.",
    "Latency alias record must include a region",
    "Record label outside of valid region ID",
    "Duplicate resource name in latency set"],
    [("List routing records", "aws route53 list-resource-record-sets --hosted-zone ZONE123")])

add("route53", "Geolocation routing error",
    "InvalidChangeBatch/NoSuchGeoLocation for geolocation.",
    "Geolocation code is invalid",
    "Two records with overlapping geo scopes",
    "Default geolocation record missing"],
    [("List geo records", "aws route53 list-resource-record-sets --hosted-zone ZONE123")])

add("route53", "Weighted routing error",
    "InvalidChangeBatch for weighted records.",
    "Weight values sum to 0 or negative",
    "Record identifier missing for weighted set",
    "Weight set member record exists with invalid weight"],
    [("List weighted records", "aws route53 list-resource-record-sets --hosted-zone ZONE123")])

add("route53", "Latency record error",
    "InvalidVPCId/BadRequest for latency records.",
    "Region must be specified for a latency record",
    "Latency record across non-unique region"],
    [("Describe geo parameters", "aws route53 list-geo-locations")])

add("route53", "Multivalue answer error",
    "InvalidChangeBatch for multivalue records.",
    "Multivalue requires multiple records with same name",
    "Cannot mix multivalue and other routing policies"],
    [("Check multivalue records", "aws route53 list-resource-record-sets --hosted-zone ZONE123")])

add("route53", "DNSSEC error",
    "InvalidSigningStatus/DNSSECKeySigningKeyNotFound.",

    "Key signing key (KSK) has not been created",
    "DNSSEC not enabled on the hosted zone",
    "Signing key is not ACTIVE",
    "DNSSEC configuration incomplete",


    [("Check DNSSEC status", "aws route53 get-dnssec --hosted-zone ZONE123")])

add("route53", "Domain registration error",
    "InvalidDomainSummary/DuplicateRequest for domains.",

    "Domain name exists for another account",
    "Domain not available for registration",
    "Registrar contact information validation failed",


    [("List domains", "aws route53domains list-domains")])

add("route53", "NS delegation error",
    "InvalidChangeBatch for NS records.",
    "NS record count must be at least 2",
    "NS record TTL must be consistent",
    "Delegation set missing or not signed"],
    [("Get NS records", "aws route53 list-resource-record-sets --hosted-zone ZONE123 --query ResourceRecordSets[?Type==`NS`]")])

add("route53", "SOA record error",
    "InvalidChangeBatch/NoSuchHostedZone for SOA.",
    "SOA TTL cannot be modified directly",
    "SOA record belongs to a different zone"],
    [("Get SOA record", "aws route53 list-resource-record-sets --hosted-zone ZONE123 --query ResourceRecordSets[?Type==`SOA`]")])

add("route53", "Private hosted zone error",
    "InvalidVPCId/Conflicting types for private hosted zones.",
    "No VPC associated with the private zone",
    "Private zone not created for VPC",
    "VPC IAM permissions missing"],
    [("List hosted zones with VPCs", "aws route53 list-hosted-zones-by-vpc --vpc-id vpc-abc")])

add("route53", "Resolver rule error",
    "ResourceNotFoundException/InvalidParameter for resolver rules.",
    "Resolver rule ID does not exist",
    "Rule type mismatch for the target",
    "Outbound rule needs a target IP"],
    [("List resolver rules", "route53resolver list-resolver-rules")])

# ===================== CloudWatch (19 pages) =====================
add("cloudwatch", "Log group error",
    "ResourceNotFoundException/InvalidParameter for log groups.",
    "Log group name is incorrect",
    "Log group does not exist",
    "Log group in a different region"],
    [("List log groups", "aws logs describe-log-groups")])

add("cloudwatch", "Log stream error",
    "ResourceNotFoundException/InvalidParameter for log streams.",
    "Log stream name does not exist",
    "Log stream was deleted",
    "Stream in wrong log group"],
    [("Describe log streams", "aws logs describe-log-streams --log-group-name /aws/lambda/myFunc")])

add("cloudwatch", "Metric filter error",
    "InvalidParameterException for metric filters.",
    "Filter pattern syntax is invalid",
    "Metric name or namespace invalid",
    "Filter must match something"],
    [("List metric filters", "aws logs describe-metric-filters --log-group /aws/lambda/myFunc")])

add("cloudwatch", "Alarm evaluation error",
    "BadRequest/ResourceNotFound for alarm evaluation.",

    "Metrics being evaluated do not match alarm period",
    "Period is not a divisor of 60 (e.g., 60, 120)",
    "Evaluation periods exhausted",
    "Alarm had insufficient data",
    "Mismatched threshold and metric unit",
    [("Describe alarm", "aws cloudwatch describe-alarms --alarm-names my-alarm")])

add("cloudwatch", "Insufficient data error",
    "InsufficientData/MissingMetricData for CloudWatch alarm.",

    "No metric datapoints in the specified period",
    "Metric generation stopped or delayed",
    "Alarm was recently created",
    "Namespace or metric name is wrong",


    [("Get metric data", "aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric CPUUtilization")])

add("cloudwatch", "SNS action error",
    "InvalidParameter combination for alarm SNS actions.",

    "SNS topic does not exist",
    "IAM permissions for CloudWatch to publish missing",
    "Cross-region.oa SNS topic not supported",
    "SNS topic used by another alarm",

    [("Check alarm actions", "aws cloudwatch describe-alarms --alarm-name my-alarm")])

add("cloudwatch", "Dashboard error",
    "InvalidParameter/ResourceNotFound for CloudWatch Dashboards.",
    "Dashboard body JSON is invalid",
    "Dashboard name length exceeds 255 characters",
    "Widget type is unsupported",
    "Metrics for widgets are in a different region",
    [("List dashboards", "aws cloudwatch list-dashboards")])

add("cloudwatch", "Metric math error",
    "InvalidStatistic/ParameterInvalid/InvalidExpression.",
    "Metric math expression contains syntax error",
    "Time period mismatch between function arguments",
    "Statistic is invalid for the given metric",
    "Returned timestamp format mismatch",
    [("Get metric math", "aws cloudwatch get-metric-data --metric-data-queries file://queries.json")])

add("cloudwatch", "Logs insight error",
    "InvalidQueryException/MalformedQuery for Logs Insights.",
    "Syntax errors in the Logs Insights query",
    "Log group not found",
    "Query timeout exceeded",
    "Too many log groups in a single query",
    [("List log groups", "aws logs describe-log-groups")])

add("cloudwatch", "Contributor Insights error",
    "AccessDenied/ResourceNotFoundException for Contributor Insights.",
    "Contributor Insights rule not found",
    "Permissions for logs not set up",
    "S3 bucket for reports not configured",
    [("List rules", "logs untag-log-group --log-group my-group")])

# region contributed insights
add("cloudwatch", "Anomaly detection error",
    "InvalidParameter/ResourceNotFoundException for anomaly detection.",

    "Anomaly detection band does not exist",
    "Time series not long enough for anomaly detection",
    "Metric has too many zero or empty values",
    "Anomaly model training incomplete",

    [("Check anomaly detection", "aws cloudwatch describe-anomaly-detectors")])

add("cloudwatch", "Composite alarm error",
    "BadRequest/MissingRequiredParameter for composite alarms.",
    "Composite alarm rule expression is empty",
    "Alarm rule references non-existent alarm",
    "Alarm rule uses unsupported operator",
    "Composite alarm rule circular dependency",
    [("List composite alarms", "aws cloudwatch describe-alarms --alarm-type CompositeAlarm")])

add("cloudwatch", "Service quota error",
    "LimitExceeded/ServiceQuotaError for CloudWatch services.",
    "Maximum number of alarms reached (5000 per region)",
    "Dashboards limit per account (500) exceeded",
    "Metric filters limit (1000) exceeded",
    "Cross-account observability limit hit",
    [("Check service quotas", "aws service-quotas get-service-quota --service-code cloudwatch --quota-code L-00CMI9Q0")])

cloudwatch_agent_pages = [
    ("CloudWatch agent error",
     "CloudWatchAgentConfigurationError/cwl-command-error.",
     ["Agent configuration file is invalid",
      "Agent not installed or not running",
      "iptables/Operating system firewall blocking",
      "Agent CloudWatch endpoint unreachable"],
     [("Check agent status", "sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status")]),
]

add("cloudwatch", "CloudWatch agent error",
    "CloudWatchAgentConfigurationError for the CW agent.",
    ["Agent configuration file is invalid",
     "Agent not installed or not running",
     "Operating system firewall blocking",
     "CloudWatch endpoint unreachable"],
    [("Check agent status", "sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status")])

add("cloudwatch", "Unified agent error",
    "CWAgentConfigurationError for CloudWatch unified agent.",
    ["Agent version mismatch across multiple hosts",
     "CollectD/procstat plugin configs are invalid",
     "CPU/mem metrics not enabled",
     "Agent not reporting telemetry"],
    [("Restart agent", "sudo systemctl restart amazon-cloudwatch-agent")])

add("cloudwatch", "Logs subscription error",
    "BadRequest/InvalidParameter for logs subscription.",
    "Subscription destination (Kinesis/Lambda) not in the same account",
    "Destination access policy missing",
    "Cross-region subscription not supported"],
    [("List subscriptions", "aws logs describe-subscription-filters --log-group my-group")])

# ===================== KMS/Security (19 pages) =====================
add("kms", "Key not found",
    "NotFoundException/KeyUnavailableException for KMS keys.",
    "Key ID does not exist",
    "Key was deleted or pending deletion",
    "Key in a different account or region"],
    [("List keys", "aws kms list-keys")])

add("kms", "Key disabled",
    "DisabledException/KMSInvalidStateException for disabled keys.",
    "Key was disabled by admin",
    "Access key reached deactive state",
    "Scheduled for deletion"],
    [("List keys", "aws kms list-key-rotation-policies --key-id alias/MyKey")])

add("kms", "key pending deletion",
    "KMSInvalidStateException for pending deletion keys.",
    "Key scheduled for deletion (pending state)",
    "Operations are not allowed while pending deletion"],
    [("Cancel key deletion", "aws kms cancel-key-deletion --key-id 1234abcd-12ab-34cd-56ef-1234567890ab")])

add("kms", "Key usage error",
    "ValidationException/BadRequest for Key usage.",
    "Key usage mismatch (ENCRYPT_DECRYPT vs. SIGN_VERIFY)",
    "Operation forbidden for key type"),
    [("Describe key", "aws kms describe-key --key-id alias/my-key")])

add("kms", "Custom key store error",
    "InvalidState/CustomKeyStoreNotFoundException for cloud HSM.",
    "CloudHSM cluster is not active",
    "Custom key store ID is invalid",
    "HSM proxy authentication failed",
    ["List custom stores", "aws kms list-custom-key-stores"])

add("cloudhsm", "CloudHSM error",
    "CloudHsmAccessDenied/CloudHsmResourceNotFound.",
    "HSM cluster not provisioned",
    "HSM client IP not authorized",
    "HSM partition password incorrect"],
    [("List HSM clusters", "cloudhsm list-clusters")])

add("secrets-manager", "secret not found",
    "ResourceNotFoundException for Secrets Manager.",
    "Secret name or ARN is incorrect",
    "Secret was deleted or scheduled for deletion",
    "Secret in a different account or region"],
    [("List secrets", "aws secretsmanager list-secrets")])

add("secrets-manager", "secret rotation error",
    "InvalidRequestException/ValidationException for rotation.",
    "Lambda function for rotation does not exist",
    "Rotation period is invalid (must be 0-1091 days)",
    "Cross-region rotation not supported",
    "Secret type is not supported"],
    [("Describe secret", "aws secretsmanager describe-secret --secret-id my-secret")])

add("acm", "Certificate not found",
    "ResourceNotFoundException/InvalidDomainValidationOptions.",
    "Certificate does not exist",
    "Certificate was deleted",
    "Domain mismatch"],
    [("List certificates", "aws acm list-certificates")])

add("acm", "Certificate renewal error",
    "ValidationException/ResourceNotFoundException for renewal.",
    "Email validation pending from domain owner",
    "DNS validation records missing",
    "CAA records at domain are blocking verification"],
    [("Check cert details", "aws acm describe-certificate --certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/xxx")])

add("acm", "ACM private renewal",
    "ResourceNotFound/InvalidState for private CA cert renewal.",
    "Private CA does not exist",
    "CA has been deleted or suspended"],
    [("List CAs", "aws acm-pca list-certificate-authorities")])

add("guardduty", "GuardDuty error",
    "ResourceNotFoundException/InvalidState for GuardDuty.",
    "GuardDuty not enabled in your account",
    "Detector ID does not exist"],
    [("List detectors", "guardduty list-detectors")])

add("security-hub", "Security Hub error",
    "AccessDeniedException/ResourceNotFoundException.",
    "Security Hub not enabled",
    "Member account not invited",
    "Standards association is invalid"],
    [("Enable Security Hub", "aws securityhub enable-security-hub")])

add("config", "Config rule error",
    "ResourceNotFoundException/InvalidSNSTopicARN.",
    "Config rule does not exist",
    "Recording is not enabled",
    "SNS topic not configured"],
    [("List rules", "aws configservice describe-config-rules")])

add("waf", "WAF rule error",
    "WAFNonexistentRuleException/WAFInvalidParameter.",
    "Rule name is incorrect",
    "Rule deleted but still used",
    "Action types are invalid"],
    [("List waf rules", "aws wafv2 list-rules --scope REGIONAL --visibility-config file://vis.json")])

add("shield", "Shield Advanced error",
    "AccessDenied/ResourceNotFoundException for Shield.",
    "Shield Advanced subscription not active",
    "Resource ID for Shield is invalid",
    "Protection does not exist"],
    [("List Shield protections", "shield list-protections")])

if __name__ == "__main__":
    write_pages()
    print(f"\nTotal new AWS pages from part3: {len(PAGES)}")
