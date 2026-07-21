#!/usr/bin/env python3
import os

OUTPUT_DIR = "/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/gradle"
TOOL = "gradle"

existing = set()
for f in os.listdir(OUTPUT_DIR):
    if f.endswith(".md") and f != "_index.md":
        existing.add(f.replace(".md", ""))

pages = [
    ("gradle-build-script-error", "Gradle Build Script Error", "Fix Gradle build script errors in build.gradle files."),
    ("gradle-plugins-block-syntax", "Gradle Plugins Block Syntax Error", "Resolve plugins block syntax errors in Gradle."),
    ("gradle-plugin-not-found-repository", "Gradle Plugin Not Found in Repository", "Fix plugin not found errors in Gradle plugin repositories."),
    ("gradle-id-vs-apply-false", "Gradle ID vs Apply False Error", "Resolve id vs apply false plugin configuration errors."),
    ("gradle-version-catalog-not-found", "Gradle Version Catalog Not Found", "Fix version catalog not found errors in Gradle."),
    ("gradle-toml-file-syntax", "Gradle TOML File Syntax Error", "Resolve TOML file syntax errors in version catalogs."),
    ("gradle-libs-version-toml-parse", "Gradle libs.versions.toml Parse Error", "Fix libs.versions.toml parsing errors."),
    ("gradle-alias-not-found-catalog", "Gradle Alias Not Found in Catalog", "Resolve alias not found errors in version catalogs."),
    ("gradle-dependency-constraint-conflict", "Gradle Dependency Constraint Conflict", "Fix dependency constraint conflict errors."),
    ("gradle-module-metadata-error", "Gradle Module Metadata Error", "Resolve module metadata parsing errors."),
    ("gradle-variant-selection-error", "Gradle Variant Selection Error", "Fix variant selection errors in Gradle builds."),
    ("gradle-capability-conflict", "Gradle Capability Conflict", "Resolve capability conflict errors in dependencies."),
    ("gradle-forced-dependency-conflict", "Gradle Forced Dependency Conflict", "Fix forced dependency conflict resolution errors."),
    ("gradle-exclude-dependency-error", "Gradle Exclude Dependency Error", "Resolve dependency exclusion configuration errors."),
    ("gradle-transitive-dependency-error", "Gradle Transitive Dependency Error", "Fix transitive dependency resolution errors."),
    ("gradle-api-vs-implementation", "Gradle API vs Implementation Error", "Resolve api vs implementation dependency scope errors."),
    ("gradle-compileonly-vs-runtimeonly", "Gradle CompileOnly vs RuntimeOnly Error", "Fix compileOnly vs runtimeOnly scope errors."),
    ("gradle-annotation-processor-error", "Gradle Annotation Processor Error", "Resolve annotation processor configuration errors."),
    ("gradle-test-implementation-not-resolved", "Gradle TestImplementation Not Resolved", "Fix testImplementation dependency resolution errors."),
    ("gradle-android-test-error", "Gradle Android Test Error", "Resolve Android test configuration errors."),
    ("gradle-lint-check-failed", "Gradle Lint Check Failed", "Fix Android lint check failure errors."),
    ("gradle-test-task-not-found", "Gradle Test Task Not Found", "Resolve test task not found errors in Gradle."),
    ("gradle-junit-platform-error", "Gradle JUnit Platform Error", "Fix JUnit platform configuration errors in Gradle."),
    ("gradle-test-execution-failed", "Gradle Test Execution Failed", "Resolve test execution failure errors in Gradle."),
    ("gradle-test-report-generation", "Gradle Test Report Generation Error", "Fix test report generation errors."),
    ("gradle-jacoco-plugin-error", "Gradle JaCoCo Plugin Error", "Resolve JaCoCo plugin configuration errors."),
    ("gradle-code-coverage-below-threshold", "Gradle Code Coverage Below Threshold", "Fix code coverage threshold check failures."),
    ("gradle-checkstyle-error", "Gradle Checkstyle Error", "Resolve Checkstyle configuration errors in Gradle."),
    ("gradle-pmd-error", "Gradle PMD Error", "Fix PMD plugin configuration errors in Gradle."),
    ("gradle-spotbugs-error", "Gradle SpotBugs Error", "Resolve SpotBugs plugin errors in Gradle."),
    ("gradle-java-compilation-failed", "Gradle Java Compilation Failed", "Fix Java compilation errors in Gradle builds."),
    ("gradle-kotlin-compilation-error", "Gradle Kotlin Compilation Error", "Resolve Kotlin compilation errors in Gradle."),
    ("gradle-source-set-not-found", "Gradle Source Set Not Found", "Fix source set not found errors in Gradle."),
    ("gradle-kotlin-dsl-error", "Gradle Kotlin DSL Error", "Resolve Kotlin DSL syntax and configuration errors."),
    ("gradle-groovy-dsl-syntax", "Gradle Groovy DSL Syntax Error", "Fix Groovy DSL syntax errors in build.gradle."),
    ("gradle-settings-gradle-missing", "Gradle settings.gradle Missing", "Resolve missing settings.gradle file errors."),
    ("gradle-rootproject-name-not-set", "Gradle rootProject.name Not Set", "Fix rootProject.name not set errors in settings."),
    ("gradle-include-module-not-found", "Gradle Include Module Not Found", "Resolve include module not found errors."),
    ("gradle-multi-project-build", "Gradle Multi-Project Build Error", "Fix multi-project build configuration errors."),
    ("gradle-project-dependency-not-resolved", "Gradle Project Dependency Not Resolved", "Resolve project dependency resolution errors."),
    ("gradle-task-not-found", "Gradle Task Not Found", "Fix task not found errors in Gradle."),
    ("gradle-task-dependency-cycle", "Gradle Task Dependency Cycle", "Resolve task dependency cycle errors."),
    ("gradle-up-to-date-check", "Gradle Up-to-Date Check Error", "Fix up-to-date check errors in Gradle."),
    ("gradle-incremental-build-failed", "Gradle Incremental Build Failed", "Resolve incremental build failure errors."),
    ("gradle-build-cache-error", "Gradle Build Cache Error", "Fix build cache configuration errors."),
    ("gradle-remote-cache-push-rejected", "Gradle Remote Cache Push Rejected", "Resolve remote cache push rejection errors."),
    ("gradle-configuration-cache-error", "Gradle Configuration Cache Error", "Fix configuration cache serialization errors."),
    ("gradle-configuration-cache-serialization", "Gradle Configuration Cache Serialization", "Resolve configuration cache serialization errors."),
    ("gradle-build-scan-not-created", "Gradle Build Scan Not Created", "Fix build scan creation errors."),
    ("gradle-develocity-plugin-error", "Gradle Develocity Plugin Error", "Resolve Develocity plugin configuration errors."),
    ("gradle-maven-publish-plugin-error", "Gradle Maven Publish Plugin Error", "Fix maven-publish plugin errors."),
    ("gradle-publication-not-found", "Gradle Publication Not Found", "Resolve publication not found errors."),
    ("gradle-repository-not-defined", "Gradle Repository Not Defined", "Fix repository not defined errors for publishing."),
    ("gradle-signing-key-not-found", "Gradle Signing Key Not Found", "Resolve signing key not found errors."),
    ("gradle-signing-plugin-error", "Gradle Signing Plugin Error", "Fix signing plugin configuration errors."),
    ("gradle-artifact-not-published", "Gradle Artifact Not Published", "Resolve artifact not published errors."),
    ("gradle-bintray-jcenter-deprecated", "Gradle Bintray JCenter Deprecated Error", "Fix Bintray/JCenter deprecation migration errors."),
    ("gradle-mavencentral-credentials", "Gradle MavenCentral Credentials Error", "Resolve MavenCentral credentials configuration errors."),
    ("gradle-docker-plugin-error", "Gradle Docker Plugin Error", "Fix Docker plugin configuration errors."),
    ("gradle-docker-image-build-error", "Gradle Docker Image Build Error", "Resolve Docker image build errors in Gradle."),
    ("gradle-spring-boot-plugin", "Gradle Spring Boot Plugin Error", "Fix Spring Boot plugin configuration errors."),
    ("gradle-bootjar-task-error", "Gradle bootJar Task Error", "Resolve bootJar task failure errors."),
    ("gradle-bootrun-failed", "Gradle bootRun Failed", "Fix bootRun task failure errors."),
    ("gradle-application-plugin-error", "Gradle Application Plugin Error", "Resolve application plugin configuration errors."),
    ("gradle-distribution-plugin-error", "Gradle Distribution Plugin Error", "Fix distribution plugin configuration errors."),
    ("gradle-application-default-jvm-args", "Gradle Application Default JVM Args", "Resolve application default JVM arguments errors."),
    ("gradle-wrapper-task-error", "Gradle Wrapper Task Error", "Fix wrapper task configuration errors."),
    ("gradle-gradlew-not-executable", "Gradle gradlew Not Executable", "Resolve gradlew not executable permission errors."),
    ("gradle-wrapper-properties-download", "Gradle Wrapper Properties Download Error", "Fix wrapper properties download errors."),
    ("gradle-distribution-url-not-found", "Gradle Distribution URL Not Found", "Resolve distribution URL not found errors."),
    ("gradle-daemon-error", "Gradle Daemon Error", "Fix Gradle daemon startup and runtime errors."),
    ("gradle-daemon-jvm-args", "Gradle Daemon JVM Args Error", "Resolve daemon JVM arguments configuration errors."),
    ("gradle-daemon-memory-exhausted", "Gradle Daemon Memory Exhausted", "Fix daemon memory exhaustion errors."),
    ("gradle-parallel-execution-error", "Gradle Parallel Execution Error", "Resolve parallel execution configuration errors."),
    ("gradle-worker-api-error", "Gradle Worker API Error", "Fix Worker API usage errors in Gradle."),
    ("gradle-file-operations-error", "Gradle File Operations Error", "Resolve file operations errors in Gradle tasks."),
    ("gradle-process-forking-error", "Gradle Process Forking Error", "Fix process forking errors in Gradle."),
    ("gradle-lazy-configuration-error", "Gradle Lazy Configuration Error", "Resolve lazy configuration API errors."),
    ("gradle-provider-not-realized", "Gradle Provider Not Realized", "Fix provider not realized errors in Gradle."),
    ("gradle-property-not-set", "Gradle Property Not Set", "Resolve property not set errors in Gradle."),
    ("gradle-extension-not-found", "Gradle Extension Not Found", "Fix extension not found errors in Gradle."),
    ("gradle-convention-deprecated", "Gradle Convention Deprecated Error", "Resolve convention deprecation errors in Gradle."),
    ("gradle-build-script-compile", "Gradle Build Script Compile Error", "Fix build script compilation errors."),
    ("gradle-classpath-not-resolved", "Gradle Classpath Not Resolved", "Resolve classpath resolution errors in Gradle."),
    ("gradle-settings-plugin-management", "Gradle Settings Plugin Management Error", "Fix settings plugin management errors."),
    ("gradle-init-script-error", "Gradle Init Script Error", "Resolve init script configuration errors."),
    ("gradle-init-script-classpath", "Gradle Init Script Classpath Error", "Fix init script classpath errors."),
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
        + desc + ' This error occurs when Gradle encounters build, plugin, or dependency problems.\n\n'
        '## Common Causes\n\n'
        '- Incorrect build.gradle configuration\n'
        '- Plugin compatibility issues\n'
        '- Dependency resolution failures\n'
        '- Gradle version incompatibility\n\n'
        '## How to Fix\n\n'
        '### Solution 1: Check Build Configuration\n\n'
        'Review your `build.gradle` or `build.gradle.kts` for errors:\n\n'
        '```groovy\n'
        'plugins {\n'
        "    id 'java'\n"
        '}\n\n'
        'repositories {\n'
        '    mavenCentral()\n'
        '}\n\n'
        'dependencies {\n'
        "    implementation 'com.google.guava:guava:31.1-jre'\n"
        '}\n'
        '```\n\n'
        '### Solution 2: Clean and Rebuild\n\n'
        '```bash\n'
        './gradlew clean build\n'
        '```\n\n'
        '### Solution 3: Debug Build\n\n'
        '```bash\n'
        './gradlew build --stacktrace --info\n'
        '```\n\n'
        'The `--stacktrace` flag provides detailed error traces and `--info` gives verbose logging.\n\n'
        '## Example\n\n'
        '```kotlin\n'
        '// build.gradle.kts example\n'
        'plugins {\n'
        '    java\n'
        '}\n\n'
        'repositories {\n'
        '    mavenCentral()\n'
        '}\n\n'
        'dependencies {\n'
        '    testImplementation("org.junit.jupiter:junit-jupiter:5.9.0")\n'
        '}\n\n'
        'tasks.test {\n'
        '    useJUnitPlatform()\n'
        '}\n'
        '```\n\n'
        '## Related Links\n\n'
        '- [Gradle Documentation](https://docs.gradle.org/)\n'
        '- [Gradle Troubleshooting](https://docs.gradle.org/current/userguide/troubleshooting.html)\n'
    )
    filepath = os.path.join(OUTPUT_DIR, slug + ".md")
    with open(filepath, "w") as f:
        f.write(content)
    count += 1
    existing.add(slug)

print("Gradle: created " + str(count) + " new pages (total: " + str(count + 33) + ")")
