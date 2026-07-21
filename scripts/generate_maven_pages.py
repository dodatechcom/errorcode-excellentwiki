#!/usr/bin/env python3
import os

OUTPUT_DIR = "/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/maven"
TOOL = "maven"

existing = set()
for f in os.listdir(OUTPUT_DIR):
    if f.endswith(".md") and f != "_index.md":
        existing.add(f.replace(".md", ""))

pages = [
    ("maven-compilation-error", "Maven Compilation Error", "Fix Maven compilation errors during build."),
    ("maven-package-does-not-exist", "Maven Package Does Not Exist", "Resolve package not found errors in Maven."),
    ("maven-cannot-find-symbol", "Maven Cannot Find Symbol", "Fix cannot find symbol errors in Maven builds."),
    ("maven-compiler-plugin-version", "Maven Compiler Plugin Version Error", "Resolve maven-compiler-plugin version errors."),
    ("maven-source-target-release", "Maven Source Target Release Error", "Fix source and target release configuration errors."),
    ("maven-java-version-mismatch", "Maven Java Version Mismatch", "Resolve Java version mismatch errors in Maven."),
    ("maven-dependency-resolution-failed", "Maven Dependency Resolution Failed", "Fix dependency resolution failure errors."),
    ("maven-artifact-not-found-repo", "Maven Artifact Not Found in Repository", "Resolve artifact not found in remote repository errors."),
    ("maven-repository-not-accessible", "Maven Repository Not Accessible", "Fix repository access and connectivity errors."),
    ("maven-plugin-not-found", "Maven Plugin Not Found", "Resolve plugin not found errors in Maven builds."),
    ("maven-plugin-execution-failed", "Maven Plugin Execution Failed", "Fix plugin execution failure errors."),
    ("maven-plugin-version-not-specified", "Maven Plugin Version Not Specified", "Resolve plugin version specification warnings."),
    ("maven-surefire-test-failure", "Maven Surefire Test Failure", "Fix maven-surefire-plugin test failure errors."),
    ("maven-test-not-run", "Maven Test Not Run", "Resolve tests not being executed by Maven."),
    ("maven-failsafe-plugin-error", "Maven Failsafe Plugin Error", "Fix maven-failsafe-plugin configuration errors."),
    ("maven-integration-test-failure", "Maven Integration Test Failure", "Resolve integration test failure errors."),
    ("maven-missing-test-class", "Maven Missing Test Class", "Fix missing test class errors in Maven."),
    ("maven-goal-not-found-in-plugin", "Maven Goal Not Found in Plugin", "Resolve goal not found errors in Maven plugins."),
    ("maven-lifecycle-phase-not-found", "Maven Lifecycle Phase Not Found", "Fix lifecycle phase not found errors."),
    ("maven-packaging-type-invalid", "Maven Packaging Type Invalid", "Resolve invalid packaging type errors."),
    ("maven-classifier-not-allowed", "Maven Classifier Not Allowed", "Fix classifier not allowed errors in Maven."),
    ("maven-type-not-recognized", "Maven Type Not Recognized", "Resolve type not recognized errors in Maven."),
    ("maven-install-plugin-failed", "Maven Install Plugin Failed", "Fix maven-install-plugin failure errors."),
    ("maven-deploy-plugin-failed", "Maven Deploy Plugin Failed", "Resolve maven-deploy-plugin failure errors."),
    ("maven-deploy-repo-not-configured", "Maven Deploy Repository Not Configured", "Fix deploy repository configuration errors."),
    ("maven-distribution-management-error", "Maven Distribution Management Error", "Resolve distribution management configuration errors."),
    ("maven-site-generation-error", "Maven Site Generation Error", "Fix maven-site-plugin generation errors."),
    ("maven-reporting-plugin-not-found", "Maven Reporting Plugin Not Found", "Resolve reporting plugin not found errors."),
    ("maven-javadoc-plugin-error", "Maven Javadoc Plugin Error", "Fix maven-javadoc-plugin configuration errors."),
    ("maven-javadoc-generation-failed", "Maven Javadoc Generation Failed", "Resolve Javadoc generation failure errors."),
    ("maven-source-plugin-error", "Maven Source Plugin Error", "Fix maven-source-plugin configuration errors."),
    ("maven-jar-plugin-error", "Maven JAR Plugin Error", "Resolve maven-jar-plugin configuration errors."),
    ("maven-no-main-manifest-attribute", "Maven No Main Manifest Attribute", "Fix missing Main-Class manifest attribute errors."),
    ("maven-war-plugin-error", "Maven WAR Plugin Error", "Resolve maven-war-plugin configuration errors."),
    ("maven-web-xml-missing", "Maven web.xml Missing", "Fix web.xml missing errors in WAR packaging."),
    ("maven-shade-plugin-error", "Maven Shade Plugin Error", "Resolve maven-shade-plugin uber-jar errors."),
    ("maven-uber-jar-conflict", "Maven Uber JAR Conflict", "Fix class conflicts in shaded uber-jar artifacts."),
    ("maven-assembly-plugin-error", "Maven Assembly Plugin Error", "Resolve maven-assembly-plugin configuration errors."),
    ("maven-descriptor-not-found", "Maven Descriptor Not Found", "Fix assembly descriptor not found errors."),
    ("maven-release-plugin-error", "Maven Release Plugin Error", "Resolve maven-release-plugin configuration errors."),
    ("maven-release-prepare-failed", "Maven Release Prepare Failed", "Fix release:prepare failure errors."),
    ("maven-release-perform-failed", "Maven Release Perform Failed", "Resolve release:perform failure errors."),
    ("maven-scm-connection-not-set", "Maven SCM Connection Not Set", "Fix SCM connection configuration errors."),
    ("maven-tag-already-exists", "Maven Tag Already Exists", "Resolve tag already exists errors in release."),
    ("maven-gpg-plugin-error", "Maven GPG Plugin Error", "Fix maven-gpg-plugin signing errors."),
    ("maven-signature-verification-failed", "Maven Signature Verification Failed", "Resolve signature verification failure errors."),
    ("maven-checkstyle-plugin-error", "Maven Checkstyle Plugin Error", "Fix maven-checkstyle-plugin configuration errors."),
    ("maven-checkstyle-violation", "Maven Checkstyle Violation", "Resolve checkstyle violation errors in Maven."),
    ("maven-pmd-plugin-error", "Maven PMD Plugin Error", "Fix maven-pmd-plugin configuration errors."),
    ("maven-pmd-violation-found", "Maven PMD Violation Found", "Resolve PMD violation errors in Maven builds."),
    ("maven-spotbugs-plugin-error", "Maven SpotBugs Plugin Error", "Fix maven-spotbugs-plugin configuration errors."),
    ("maven-spotbugs-analysis-failed", "Maven SpotBugs Analysis Failed", "Resolve SpotBugs analysis failure errors."),
    ("maven-jacoco-plugin-error", "Maven JaCoCo Plugin Error", "Fix maven-jacoco-plugin configuration errors."),
    ("maven-coverage-check-failed", "Maven Coverage Check Failed", "Resolve code coverage threshold check failures."),
    ("maven-sonar-plugin-error", "Maven Sonar Plugin Error", "Fix sonar-maven-plugin configuration errors."),
    ("maven-sonar-analysis-failed", "Maven Sonar Analysis Failed", "Resolve SonarQube analysis failure errors."),
    ("maven-profile-not-activated", "Maven Profile Not Activated", "Fix profile activation and not activated errors."),
    ("maven-profile-activation-error", "Maven Profile Activation Error", "Resolve profile activation condition errors."),
    ("maven-parent-pom-not-found", "Maven Parent POM Not Found", "Fix parent POM not found dependency errors."),
    ("maven-relativepath-not-resolved", "Maven RelativePath Not Resolved", "Resolve relativePath not resolved errors."),
    ("maven-effective-pom-error", "Maven Effective POM Error", "Fix effective POM generation errors."),
    ("maven-dependency-management-version", "Maven Dependency Management Version", "Resolve dependency management version conflicts."),
    ("maven-plugin-management-version", "Maven Plugin Management Version", "Fix plugin management version specification errors."),
    ("maven-properties-interpolation-error", "Maven Properties Interpolation Error", "Resolve property interpolation errors in POM."),
    ("maven-filtering-resource-error", "Maven Filtering Resource Error", "Fix resource filtering configuration errors."),
    ("maven-resource-encoding-error", "Maven Resource Encoding Error", "Resolve resource encoding configuration errors."),
    ("maven-proxy-configuration-error", "Maven Proxy Configuration Error", "Fix proxy configuration errors in Maven settings."),
    ("maven-mirrors-misconfiguration", "Maven Mirrors Misconfiguration", "Resolve mirror configuration errors in Maven."),
    ("maven-server-credentials-missing", "Maven Server Credentials Missing", "Fix missing server credentials in settings.xml."),
    ("maven-settings-security-error", "Maven Settings Security Error", "Resolve settings-security.xml configuration errors."),
    ("maven-toolchains-not-configured", "Maven Toolchains Not Configured", "Fix toolchains configuration errors in Maven."),
    ("maven-jdk-toolchain-error", "Maven JDK Toolchain Error", "Resolve JDK toolchain selection errors."),
    ("maven-wrapper-error-new", "Maven Wrapper Error", "Fix maven-wrapper.jar and mvnw errors."),
    ("mvnw-not-executable", "Maven Wrapper mvnw Not Executable", "Resolve mvnw not executable permission errors."),
    ("maven-multi-module-reactor", "Maven Multi-Module Reactor Error", "Fix multi-module reactor build order errors."),
    ("maven-module-not-found", "Maven Module Not Found", "Resolve module not found errors in multi-module builds."),
    ("maven-reactor-build-order", "Maven Reactor Build Order Error", "Fix reactor build order and dependency errors."),
    ("maven-make-like-dependency", "Maven Make-Like Dependency Error", "Resolve make-like dependency errors in reactor builds."),
    ("maven-advanced-reactor-options", "Maven Advanced Reactor Options Error", "Fix advanced reactor options configuration errors."),
]

count = 0
for slug, title, desc in pages:
    if slug in existing:
        continue
    content = (
        '---\n'
        'title: "[Solution] ' + title + '"\n'
        'description: "' + desc + '"\n'
        'tools: ["' + TOOL + '"]\n'
        'error-types: ["tool-error"]\n'
        'severities: ["error"]\n'
        '---\n\n'
        '# ' + title + '\n\n'
        + desc + ' This error occurs when Maven encounters build, dependency, or plugin problems.\n\n'
        '## Common Causes\n\n'
        '- Incorrect POM configuration\n'
        '- Missing or incompatible dependencies\n'
        '- Plugin execution failures\n'
        '- Repository access issues\n\n'
        '## How to Fix\n\n'
        '### Solution 1: Check POM Configuration\n\n'
        'Review your `pom.xml` for syntax errors:\n\n'
        '```xml\n'
        '<project>\n'
        '  <modelVersion>4.0.0</modelVersion>\n'
        '  <groupId>com.example</groupId>\n'
        '  <artifactId>my-app</artifactId>\n'
        '  <version>1.0-SNAPSHOT</version>\n'
        '</project>\n'
        '```\n\n'
        '### Solution 2: Clean and Rebuild\n\n'
        '```bash\n'
        'mvn clean install -U\n'
        '```\n\n'
        '### Solution 3: Debug Build\n\n'
        '```bash\n'
        'mvn clean install -X\n'
        '```\n\n'
        'The `-X` flag enables debug output for detailed troubleshooting.\n\n'
        '## Example\n\n'
        '```bash\n'
        '# Check dependency tree\n'
        'mvn dependency:tree\n\n'
        '# Validate POM\n'
        'mvn validate\n\n'
        '# Skip tests temporarily for debugging\n'
        'mvn install -DskipTests\n'
        '```\n\n'
        '## Related Links\n\n'
        '- [Maven Documentation](https://maven.apache.org/guides/)\n'
        '- [Maven Troubleshooting](https://maven.apache.org/guides/troubleshooting/)\n'
    )
    filepath = os.path.join(OUTPUT_DIR, slug + ".md")
    with open(filepath, "w") as f:
        f.write(content)
    count += 1
    existing.add(slug)

print("Maven: created " + str(count) + " new pages (total: " + str(count + 33) + ")")
