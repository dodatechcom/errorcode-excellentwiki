#!/usr/bin/env python3
import os

OUTPUT_DIR = "/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/apache"

PAGES = []

def add(slug, title, desc, causes, fixes, examples):
    PAGES.append((slug, title, desc, causes, fixes, examples))

# 1. Configuration errors
add("invalid-directive", "Apache Invalid Directive Error",
    "The configuration directive is not recognized or is invalid in the current Apache version.",
    ["Typo in directive name", "Directive requires a specific module that is not loaded", "Directive is deprecated or removed in the current Apache version", "Directive used in wrong context (server, vhost, directory)"],
    ["Check the directive name against the Apache documentation for your version", "Ensure the required module is loaded (e.g., LoadModule)", "Use the correct directive for your Apache version"],
    ["# Wrong\nDrectiveName value\n# Right\nDirectiveName value"])

add("missing-required-directive", "Apache Missing Required Directive",
    "A mandatory configuration directive is missing from the configuration file.",
    ["ServerName not defined in virtual host", "DocumentRoot directive is absent", "Missing Listen directive so no ports are bound", "Required module-specific directives not set"],
    ["Add the missing directive with a valid value", "Check module documentation for required parameters", "Use apachectl configtest to identify missing directives"],
    ["<VirtualHost *:80>\n  # ServerName is required\n  ServerName example.com\n  DocumentRoot /var/www/html\n</VirtualHost>"])

add("duplicate-listen", "Apache Duplicate Listen Address",
    "Two or more Listen directives try to bind to the same IP address and port combination.",
    ["Configuration files both define Listen on the same port", "Include'd files redundantly specify the same port", "Listen directives in both global and virtual host context conflict"],
    ["Remove duplicate Listen directives", "Use Include directives carefully to avoid duplication", "Bind different virtual hosts to different ports or IPs"],
    ["# Remove one of these duplicates\nListen 80\nListen 80"])

add("syntax-error", "Apache Configuration Syntax Error",
    "The configuration file contains a syntax error preventing Apache from starting.",
    ["Mismatched angle brackets in virtual host blocks", "Missing or extra quotes in directive values", "Unclosed quotes or parentheses", "Invalid characters in directive arguments"],
    ["Run apachectl configtest to pinpoint the error", "Review the error line number reported", "Check for matching brackets and quotes"],
    ["<VirtualHost *:80>\n  ServerName example.com\n  # Missing closing bracket\n"])

add("include-not-found", "Apache Include Not Found",
    "An Include directive references a file or directory that does not exist.",
    ["Typo in the Include file path", "The referenced file was deleted or moved", "File permissions prevent Apache from reading the file", "Glob pattern in Include matches no files"],
    ["Verify the path is correct and file exists", "Check file and directory permissions", "Use glob patterns with care; ensure at least one file matches"],
    ["# Wrong path\nInclude /etc/apache2/conf.d/mistyped.conf\n# Correct\nInclude /etc/apache2/conf.d/myconfig.conf"])

add("options-conflict", "Apache Options Directive Conflict",
    "Multiple conflicting Options directives apply to the same directory.",
    ["Options set in .htaccess conflicts with main config", "Parent and child directory have incompatible Options", "Mixing +/- with full Options replacement"],
    ["Use Options + or - syntax to selectively add or remove flags", "Ensure .htaccess options are compatible with AllowOverride", "Set Options in only one location if possible"],
    ["# Avoid conflicting full declarations\n# Instead use\nOptions +FollowSymLinks\nOptions -Indexes"])

add("allowoverride-not-allowed", "Apache AllowOverride Not Allowed",
    "The .htaccess file is trying to use directives that are not permitted by AllowOverride.",
    ["AllowOverride None is set for the directory", "AllowOverride does not include the required directive category", "Directive category (AuthConfig, FileInfo, etc.) not enabled"],
    ["Set AllowOverride All or the specific category needed", "Restart Apache after changing AllowOverride", "Place directives in the main config instead of .htaccess"],
    ["<Directory /var/www/html>\n  AllowOverride AuthConfig FileInfo\n</Directory>"])

add("order-directive-deprecated", "Apache Order Directive Deprecated",
    "The Order directive from Apache 2.2 is deprecated and may not work as expected.",
    ["Using Order allow,deny from Apache 2.2 configuration", "Mixing Order and Require directives", "Legacy configuration not updated for Apache 2.4"],
    ["Replace Order/Allow/Deny with Require directives", "Use Require all granted instead of Order allow,deny", "Consult the Apache 2.4 migration guide"],
    ["# Old (deprecated)\nOrder allow,deny\nAllow from all\n# New\nRequire all granted"])

add("requireall-syntax-error", "Apache RequireAll Syntax Error",
    "The RequireAll directive block has incorrect syntax or conflicting conditions.",
    ["Missing RequireNone or RequireAny inside RequireAll", "Conflicting RequireNone makes the entire block deny everything", "Not all directives are valid inside RequireAll block"],
    ["Review RequireAll block contents for validity", "Test combinations with apachectl configtest", "Consult Apache expressions documentation"],
    ["<RequireAll>\n  Require all granted\n  Require ip 192.168.1.0/24\n</RequireAll>"])

add("virtualhost-overlap", "Apache VirtualHost Address Overlap",
    "Two virtual hosts are configured on the same IP:port combination without name-based differentiation.",
    ["Multiple VirtualHost blocks with the same IP and port but no ServerName", "Default virtual host catches all unmatched requests", "Name-based virtual hosting not properly configured"],
    ["Add unique ServerName to each VirtualHost", "Use name-based virtual hosting", "Ensure one VirtualHost is designated as the default"],
    ["<VirtualHost *:80>\n  ServerName site1.com\n</VirtualHost>\n<VirtualHost *:80>\n  ServerName site2.com\n</VirtualHost>"])

add("namesvirtualhost-missing", "Apache NameVirtualHost Missing",
    "The NameVirtualHost directive is missing or misconfigured for name-based hosting.",
    ["Forgot to define NameVirtualHost for the port", "NameVirtualHost IP does not match Listen IP", "Apache 2.4 deprecated NameVirtualHost; removing it is correct"],
    ["On Apache 2.2: add NameVirtualHost *:80 before VirtualHosts", "On Apache 2.4: simply remove the NameVirtualHost directive", "Verify Listen and VirtualHost use matching addresses"],
    ["# Apache 2.2 only\nNameVirtualHost *:80\n# Apache 2.4: this line is no longer needed"])

add("servername-not-set", "Apache ServerName Not Set",
    "The ServerName directive is not defined, so Apache cannot determine its own hostname.",
    ["ServerName not set globally or in VirtualHost", "DNS resolution fails for the server's hostname", "Apache uses the IP address instead of a hostname"],
    ["Set ServerName in the global config or each VirtualHost", "Ensure DNS or /etc/hosts resolves the server name", "Use FQDN for ServerName"],
    ["ServerName www.example.com:80"])

add("documentroot-not-found", "Apache DocumentRoot Not Found",
    "The directory specified by DocumentRoot does not exist or is not accessible.",
    ["Typo in DocumentRoot path", "Directory was deleted or moved", "File system permissions deny Apache access"],
    ["Create the directory or correct the path", "Ensure proper ownership: chown -R www-data:www-data /var/www/html", "Check SELinux or AppArmor contexts"],
    ["DocumentRoot /var/www/html\n<Directory /var/www/html>\n  Require all granted\n</Directory>"])

add("directoryindex-missing", "Apache DirectoryIndex Missing",
    "No DirectoryIndex is configured or the default index file is not found.",
    ["index.html, index.php etc. do not exist", "DirectoryIndex directive lists no valid files", "File permissions prevent reading the index"],
    ["Create an index file or add your filename to DirectoryIndex", "Ensure the file is readable by Apache", "Check for case sensitivity in filenames"],
    ["DirectoryIndex index.html index.php"])

add("errordocument-invalid", "Apache ErrorDocument Invalid",
    "The ErrorDocument directive points to an invalid file or URL.",
    ["File path does not exist", "Relative paths not resolved correctly", "ErrorDocument points to a URL without leading slash"],
    ["Verify the ErrorDocument file exists and is readable", "Use absolute paths or paths relative to DocumentRoot", "For external URLs, use a full URL starting with http://"],
    ["ErrorDocument 404 /errors/404.html\nErrorDocument 500 http://example.com/error500.html"])

add("logformat-undefined", "Apache LogFormat Undefined",
    "A CustomLog directive references a LogFormat nickname that has not been defined.",
    ["Typo in the LogFormat nickname", "CustomLog references format before it is defined", "LogFormat defined in an unreachable config section"],
    ["Define LogFormat before referencing it in CustomLog", "Check spelling of the nickname", "Ensure both directives are in the same config scope"],
    ["LogFormat \"%h %l %u %t \\\"%r\\\" %>s %b\" common\nCustomLog logs/access.log common"])

add("customlog-permission", "Apache CustomLog Permission Denied",
    "Apache cannot open or write to the log file specified in CustomLog.",
    ["Log file directory does not exist", "Apache user lacks write permissions", "SELinux or AppArmor blocks access", "Log file is owned by another process"],
    ["Create the log directory and set ownership to the Apache user", "Use: chown www-data:www-data /var/log/apache2/", "Check SELinux: ausearch -m avc"],
    ["# Ensure directory exists and is writable\nmkdir -p /var/log/apache2\nchown www-data:www-data /var/log/apache2"])

add("loglevel-invalid", "Apache LogLevel Invalid",
    "An invalid log level or module-specific log level is specified in LogLevel.",
    ["Misspelled log level name", "Module name in level spec is not loaded", "Level value is not one of the recognized levels"],
    ["Use valid levels: emerg, alert, crit, error, warn, notice, info, debug, trace1-trace8", "Verify module names are correct and loaded", "Consult Apache log level documentation"],
    ["LogLevel warn\nLogLevel authz_core:trace5"])

add("serverlimit-too-low", "Apache ServerLimit Too Low",
    "The ServerLimit directive is set too low to accommodate the current MaxRequestWorkers setting.",
    ["MaxRequestWorkers exceeds ServerLimit", "ServerLimit not increased before MaxRequestWorkers", "Default ServerLimit of 256 exceeded"],
    ["Set ServerLimit >= MaxRequestWorkers", "ServerLimit requires a full restart (not graceful)", "Adjust both directives together"],
    ["ServerLimit 512\nMaxRequestWorkers 512"])

add("maxclients-too-high", "Apache MaxClients Too High",
    "MaxRequestWorkers (formerly MaxClients) is set higher than the system can support.",
    ["Value exceeds available system memory", "Exceeds ServerLimit value", "System cannot fork enough child processes"],
    ["Reduce MaxRequestWorkers to match available RAM", "Set appropriate values based on: Available RAM / memory per process", "Monitor with server-status to tune"],
    ["# With 2GB RAM and ~20MB per process:\nMaxRequestWorkers 100"])

# 2. Module errors
add("module-not-found", "Apache Module Not Found",
    "Apache cannot load the specified module because the module file is missing.",
    ["Module not installed with Apache", "LoadModule path is incorrect", "Module compiled for a different Apache version", "Module name is misspelled"],
    ["Install the module package (e.g., apt install libapache2-mod-*)", "Check the module path with: apachectl -M", "Verify Apache version compatibility"],
    ["LoadModule rewrite_module modules/mod_rewrite.so"])

add("mod-rewrite-not-loaded", "Apache mod_rewrite Not Loaded",
    "The mod_rewrite module is required but has not been loaded.",
    ["LoadModule rewrite_module line is commented out or missing", "Module not installed", "RewriteEngine directives appear without loading the module"],
    ["Uncomment or add: LoadModule rewrite_module modules/mod_rewrite.so", "On Debian/Ubuntu: a2enmod rewrite", "Restart Apache after enabling the module"],
    ["# Enable mod_rewrite\nLoadModule rewrite_module modules/mod_rewrite.so\n# Or on Debian:\n# sudo a2enmod rewrite"])

add("mod-ssl-not-loaded", "Apache mod_ssl Not Loaded",
    "SSL directives are used but the mod_ssl module is not loaded.",
    ["LoadModule ssl_module is missing or commented out", "mod_ssl not installed", "SSL directives used before module is loaded"],
    ["LoadModule ssl_module modules/mod_ssl.so", "On Debian/Ubuntu: a2enmod ssl", "Ensure mod_ssl matches Apache version"],
    ["LoadModule ssl_module modules/mod_ssl.so\nSSLEngine on"])

add("mod-proxy-missing", "Apache mod_proxy Missing",
    "Proxy directives are used but mod_proxy is not loaded.",
    ["LoadModule proxy_module missing", "ProxyPass directives without loaded module", "Related proxy modules not loaded"],
    ["Load all required proxy modules:\nLoadModule proxy_module modules/mod_proxy.so\nLoadModule proxy_http_module modules/mod_proxy_http.so", "Install mod_proxy package if missing", "Restart Apache after changes"],
    ["LoadModule proxy_module modules/mod_proxy.so\nLoadModule proxy_http_module modules/mod_proxy_http.so\nProxyPass / http://backend:8080/"])

add("mod-security-error", "Apache mod_security Error",
    "The mod_security module encountered an error processing a request.",
    ["Corrupted or malformed rule file", "Rule exclusion syntax incorrect", "SecRuleEngine misconfiguration", "Memory limit exceeded by rules"],
    ["Check SecAuditLog for specific error details", "Review rule syntax in CRS configuration", "Add SecRequestBodyLimit if requests exceed default"],
    ["SecRuleEngine On\nSecRequestBodyAccess On\nSecRequestBodyLimit 13107200"])

add("mod-deflate-conflict", "Apache mod_deflate Conflict",
    "mod_deflate has a conflict, often with mod_ssl or caching modules.",
    ["DeflateFilterNote conflicts with SSL compression", "mod_deflate and mod_ssl compression both active", "Conflicting output filter chain"],
    ["Disable SSLCompression when using mod_deflate", "Order output filters correctly", "Check for duplicate Deflate directives"],
    ["# Disable SSL compression\nSSLCompression off\n# Use mod_deflate for HTTP\n<IfModule mod_deflate.c>\n  AddOutputFilterByType DEFLATE text/html\n</IfModule>"])

add("mod-cache-error", "Apache mod_cache Error",
    "The mod_cache module is misconfigured or has a storage error.",
    ["CacheRoot directory does not exist or is not writable", "CacheDefaultExpire or CacheMaxExpire not set", "Conflicting cache storage modules"],
    ["Create and set permissions on CacheRoot directory", "Set appropriate expiration times", "Choose one storage module (mod_cache_disk or mod_cache_socache)"],
    ["CacheRoot /var/cache/apache2/\nCacheDefaultExpire 3600\nCacheEnable disk http/"])

add("mod-expires-invalid", "Apache mod_expires Invalid Configuration",
    "The ExpiresActive or ExpiresByType directives have invalid syntax or values.",
    ["ExpiresByType uses invalid MIME type", "ExpiresDefault value is not a valid time expression", "ExpiresActive On set but no expiration rules defined"],
    ["Verify MIME types are correct (e.g., text/html)", "Use valid time expressions: access plus 1 month", "Ensure ExpiresActive is On before setting rules"],
    ["ExpiresActive On\nExpiresByType text/html \"access plus 1 week\"\nExpiresDefault \"access plus 1 month\""])

add("mod-headers-syntax", "Apache mod_headers Syntax Error",
    "A Header directive has incorrect syntax.",
    ["Missing header value or name", "Invalid condition syntax", "Unquoted strings with special characters", "Append vs. set vs. add used incorrectly"],
    ["Check Header directive syntax: Header [condition] set|append|add|unset|echo header value", "Quote header values with special characters", "Use always option for error pages: Header always set X-Frame-Options DENY"],
    ["Header set X-Content-Type-Options nosniff\nHeader always set X-Frame-Options DENY"])

add("mod-alias-redirect-loop", "Apache mod_alias Redirect Loop",
    "An Alias or Redirect directive creates an infinite redirect loop.",
    ["Alias overlaps with DocumentRoot in a loop", "Redirect destination matches the source pattern", "Alias points to a directory that redirects back"],
    ["Verify Alias paths do not overlap with DocumentRoot", "Ensure Redirect destination does not match the source URL", "Use RedirectMatch with careful regex to avoid loops"],
    ["# This causes a loop if /var/www/link points back to /old/\nAlias /old/ /var/www/old/\n# Avoid:\n# Alias /old/ /var/www/link/"])

add("mod-rewrite-infinite-loop", "Apache mod_rewrite Infinite Loop",
    "A RewriteRule creates an infinite loop by repeatedly matching itself.",
    ["RewriteRule pattern matches the rewritten URL", "Missing RewriteCond to prevent re-matching", "RewriteRule [L] flag not used to stop processing"],
    ["Add RewriteCond %{REQUEST_URI} to prevent re-matching", "Use [L] flag to stop rule processing", "Add [R] flag for external redirects to break loops"],
    ["RewriteEngine On\nRewriteCond %{REQUEST_URI} !^/index\\.php$\nRewriteRule ^(.*)$ /index.php [L]"])

add("mod-proxy-balancer-error", "Apache mod_proxy_balancer Error",
    "The proxy balancer module encounters an error managing backend members.",
    ["BalancerMember not configured or unreachable", "lbmethod not specified or module not loaded", "Health check URL returning errors", "BalancerMember max_fails too low"],
    ["Ensure all BalancerMember backends are running", "Load required modules: mod_proxy_balancer, mod_lbmethod_byrequests", "Set max_fails and failtimeout appropriately"],
    ["<Proxy balancer://mycluster>\n  BalancerMember http://backend1:8080\n  BalancerMember http://backend2:8080\n  ProxySet lbmethod=byrequests\n</Proxy>"])

add("mod-status-disabled", "Apache mod_status Disabled",
    "The server-status handler is not available because mod_status is not loaded or configured.",
    ["LoadModule status_module is missing", "SetHandler server-status not configured", "Access denied by Require directive"],
    ["LoadModule status_module modules/mod_status.so", "Add Location block for /server-status", "Restrict access with Require ip"],
    ["<Location /server-status>\n  SetHandler server-status\n  Require ip 127.0.0.1\n</Location>"])

add("mod-info-disabled", "Apache mod_info Disabled",
    "The server-info handler is not available because mod_info is not loaded or configured.",
    ["LoadModule info_module missing", "SetHandler server-info not configured", "No access restrictions defined"],
    ["LoadModule info_module modules/mod_info.so", "Add Location block for /server-info", "Restrict to trusted IPs only"],
    ["<Location /server-info>\n  SetHandler server-info\n  Require ip 127.0.0.1\n</Location>"])

add("mod-userdir-error", "Apache mod_userdir Error",
    "The UserDir directive is misconfigured or user directories are not accessible.",
    ["UserDir disabled for all users", "User directory does not exist or has wrong permissions", "UserDir path does not match actual home directory layout"],
    ["Enable UserDir for specific users or *", "Ensure home directories have execute permission for Apache", "Configure UserDir to match your home directory structure"],
    ["UserDir public_html\n<Directory /home/*/public_html>\n  AllowOverride All\n  Require all granted\n</Directory>"])

# 3. SSL/TLS errors
add("sslcertificatefile-not-found", "Apache SSLCertificateFile Not Found",
    "The SSL certificate file specified does not exist or is not readable by Apache.",
    ["File path is incorrect or typo", "Certificate file was deleted or not yet generated", "File permissions prevent Apache from reading it", "SELinux context is wrong"],
    ["Verify the file path and existence", "Check permissions: ls -la /path/to/cert.pem", "Regenerate or re-download the certificate", "Fix SELinux: restorecon -Rv /etc/ssl/"],
    ["SSLCertificateFile /etc/ssl/certs/ssl-cert-snakeoil.pem\nSSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key"])

add("sslcertificatekeyfile-mismatch", "Apache SSLCertificateKeyFile Mismatch",
    "The private key file does not match the SSL certificate.",
    ["Key and certificate were generated separately", "Wrong key file referenced", "Key file is corrupted or incomplete"],
    ["Ensure key and certificate share the same key pair", "Verify with: openssl x509 -noout -modulus -in cert.pem | md5sum", "Regenerate a matching pair if needed"],
    ["# Verify match\nopenssl x509 -noout -modulus -in cert.pem | md5sum\nopenssl rsa -noout -modulus -in key.pem | md5sum"])

add("sslcertificatechainfile-missing", "Apache SSLCertificateChainFile Missing",
    "The certificate chain or intermediate certificates are not configured.",
    ["Intermediate CA certificates not included", "SSLCertificateChainFile directive missing or points to wrong file", "Browser cannot validate the certificate chain"],
    ["Combine intermediate certificates into a chain file", "Set SSLCertificateChainFile to the chain file path", "Order: server cert first, then intermediates, no root"],
    ["# Create chain file\ncat intermediate.crt > chain.pem\n# Configure\nSSLCertificateChainFile /etc/ssl/chain.pem"])

add("sslprotocol-mismatch", "Apache SSLProtocol Mismatch",
    "The SSLProtocol directive has incompatible or invalid values.",
    ["SSLProtocol set to only old, insecure protocols", "Client supports none of the specified protocols", "Mixing incompatible protocol flags"],
    ["Use: SSLProtocol all -SSLv2 -SSLv3 -TLSv1 -TLSv1.1", "Enable TLSv1.2 and TLSv1.3 only", "Test with: openssl s_client -connect host:443 -tls1_2"],
    ["SSLProtocol all -SSLv2 -SSLv3 -TLSv1 -TLSv1.1\nSSLProtocol TLSv1.2 TLSv1.3"])

add("sslciphersuite-too-strict", "Apache SSLCipherSuite Too Strict",
    "The cipher suite configuration excludes all possible ciphers or is incompatible.",
    ["Cipher suite string is invalid or empty", "No ciphers match both client and server capabilities", "CipherSuite uses deprecated cipher names"],
    ["Use a well-known cipher suite string", "Test with: openssl ciphers -v 'YOUR-CIPHER-STRING'", "Use Mozilla SSL Configuration Generator as reference"],
    ["SSLCipherSuite HIGH:!aNULL:!MD5:!3DES\nSSLHonorCipherOrder on"])

add("sslhonorcipherorder-error", "Apache SSLHonorCipherOrder Error",
    "The SSLHonorCipherOrder directive is misconfigured.",
    ["Directive used when SSLCipherSuite is not set", "Value is not On or Off", "Conflicts with client's cipher preferences"],
    ["Set SSLHonorCipherOrder On to prefer server cipher order", "Ensure SSLCipherSuite is defined", "Use server cipher order for security"],
    ["SSLHonorCipherOrder on\nSSLCipherSuite HIGH:!aNULL:!MD5"])

add("sslcompression-disabled", "Apache SSLCompression Disabled",
    "SSLCompression directive is configured but compression is not supported or is a security risk.",
    ["SSLCompression on set but OpenSSL compiled without compression", "CRIME attack vulnerability when compression is enabled", "Directive not recognized by older OpenSSL"],
    ["Set SSLCompression off (recommended)", "Do not enable TLS compression due to CRIME attack", "Remove the directive if using default (off)"],
    ["SSLCompression off"])

add("sslsessioncache-timeout", "Apache SSLSessionCache Timeout",
    "The SSL session cache is misconfigured with an invalid timeout or shared memory issue.",
    ["Timeout value is negative or unreasonably large", "Shared memory cache file already in use by another process", "Cache type incompatible with MPM module"],
    ["Set SSLSessionCacheTimeout to a reasonable value (300-86400)", "Ensure cache file path is unique per Apache instance", "Use SSLSessionCache shmcb:/path/to/cache for best performance"],
    ["SSLSessionCache shmcb:/var/run/ssl_scache(512000)\nSSLSessionCacheTimeout 300"])

add("sslverifyclient-required", "Apache SSLVerifyClient Required",
    "Client certificate verification is required but failing or misconfigured.",
    ["SSLVerifyClient set to require but no CA configured", "Client certificate not signed by configured CA", "SSLCACertificatePath or SSLCACertificateFile not set", "Certificate expired or not yet valid"],
    ["Set SSLCACertificateFile or SSLCACertificatePath", "Ensure client certificates are signed by the trusted CA", "Use SSLVerifyClient optional if client certs are not mandatory"],
    ["SSLVerifyClient require\nSSLCACertificateFile /etc/ssl/ca-bundle.crt"])

add("sslproxyengine-error", "Apache SSLProxyEngine Error",
    "SSL proxy directives are used but SSLProxyEngine is not enabled.",
    ["SSLProxyEngine Off or missing", "SSLProxy* directives used without SSLProxyEngine On", "Module mod_proxy_http not loaded"],
    ["Add SSLProxyEngine On in the relevant VirtualHost", "Ensure mod_proxy and mod_proxy_http are loaded", "Configure SSLProxyCACertificateFile for backend verification"],
    ["SSLProxyEngine On\nSSLProxyCACertificateFile /etc/ssl/ca.crt\nProxyPass / https://backend:443/"])

add("sslcacertificatepath-invalid", "Apache SSLCACertificatePath Invalid",
    "The directory specified for CA certificates does not exist or has incorrect format.",
    ["Directory does not exist", "CA certificate files are not in hashed format", "File permissions prevent Apache from reading"],
    ["Create the directory and run: c_rehash /path/to/ca/", "Use SSLCACertificateFile for a single bundle instead", "Verify with: ls -la /path/to/ca/"],
    ["mkdir -p /etc/ssl/cacerts\nc_rehash /etc/ssl/cacerts\nSSLCACertificatePath /etc/ssl/cacerts"])

add("sslcrlfile-missing", "Apache SSLCRLFile Missing",
    "The Certificate Revocation List file is missing or invalid.",
    ["CRL file path is incorrect", "CRL file not generated or updated", "CRL has expired"],
    ["Download or generate a fresh CRL", "Set the correct path in SSLCRLFile", "Automate CRL updates with a cron job"],
    ["SSLCRLFile /etc/ssl/crl/ca-crl.pem"])

add("sslpassphrasedialog-error", "Apache SSLPassPhraseDialog Error",
    "The SSLPassPhraseDialog command fails to provide the passphrase for encrypted private keys.",
    ["External program path is wrong or not executable", "Program does not output the passphrase correctly", "Program requires interactive input not possible in server context"],
    ["Verify the external program exists and is executable", "Ensure the program outputs the passphrase to stdout", "Use builtin: for testing or unencrypted keys for production"],
    ["SSLPassPhraseDialog builtin:\n# Or external:\nSSLPassPhraseDialog exec:/usr/local/bin/ssl-passphrase.sh"])

add("sslrandomseed-error", "Apache SSLRandomSeed Error",
    "The SSLRandomSeed directive is misconfigured and cannot seed the PRNG.",
    ["File path does not exist", "Wrong syntax for the seed source", "Entropy source exhausted or unavailable"],
    ["Use a valid entropy source: /dev/urandom or /dev/random", "Check syntax: SSLRandomSeed startup|connect builtin|/dev/urandom", "Ensure /dev/urandom is available"],
    ["SSLRandomSeed startup builtin\nSSLRandomSeed connect builtin"])

# 4. Rewrite/Redirect errors
add("rewriteengine-not-enabled", "Apache RewriteEngine Not Enabled",
    "RewriteRule directives are present but RewriteEngine is not turned on.",
    ["RewriteEngine directive is missing or set to Off", "Rewrite rules in .htaccess but AllowOverride does not include FileInfo", "Module loaded but not activated for the context"],
    ["Add RewriteEngine On before any RewriteRule", "Ensure AllowOverride FileInfo or All is set", "Verify mod_rewrite is loaded"],
    ["RewriteEngine On\nRewriteRule ^old-page$ new-page [R=301,L]"])

add("rewrite-rule-too-complex", "Apache RewriteRule Too Complex",
    "The RewriteRule pattern is too complex, causing performance issues or errors.",
    ["Excessive backreferences or lookaheads", "Pattern matching is too broad and matches everything", "Rule tries to do too much in a single step"],
    ["Simplify the regex pattern", "Break complex rules into multiple simpler rules", "Use RewriteCond to narrow matches"],
    ["# Instead of one complex rule:\nRewriteCond %{HTTP_HOST} ^www\\.(.*)$\nRewriteCond %{REQUEST_URI} !^/old/\nRewriteRule ^(.*)$ /%1$1 [R=301,L]"])

add("rewritecond-not-matching", "Apache RewriteCond Not Matching",
    "The RewriteCond test expression is not matching as expected.",
    ["Incorrect test variable (e.g., %{REQUEST_URI} vs %{THE_REQUEST})", "Regex pattern does not match the intended input", "Condition flags like [NC] (case-insensitive) missing"],
    ["Use %{THE_REQUEST} to match the original request line", "Test regex with online tools or command line", "Add [NC] for case-insensitive matching"],
    ["RewriteCond %{THE_REQUEST} \\s/old-page\\s [NC]\nRewriteRule ^ /new-page [R=301,L]"])

add("rewritebase-missing", "Apache RewriteBase Missing",
    "RewriteRule requires RewriteBase but it is not defined.",
    ["RewriteRule in .htaccess without RewriteBase", "Alias causes DocumentRoot mismatch", "Subdirectory rewrites need explicit base"],
    ["Add RewriteBase / before RewriteRule", "Set RewriteBase to the directory path", "Use absolute paths in RewriteRule target"],
    ["RewriteEngine On\nRewriteBase /\nRewriteRule ^old$ new [L]"])

add("rewritemap-error", "Apache RewriteMap Error",
    "The RewriteMap directive references an invalid map or map type.",
    ["Map file does not exist or is not readable", "Invalid map type (int, rnd, dbm, txt, int)", "Map name is misspelled in RewriteRule"],
    ["Verify the map file exists and is readable", "Use correct map type: txt, rnd, int, dbm, or prg", "Ensure map name matches in RewriteRule"],
    ["RewriteMap lc int:tolower\nRewriteRule ^(.*)$ ${lc:$1} [L]"])

add("redirect-permanent-loop", "Apache Redirect Permanent Loop",
    "A Redirect permanent (301) creates an infinite redirect loop.",
    ["Redirect destination matches the source URL", "Redirect on the same path with a different hostname but both point to same server", "Missing conditions to prevent recursive redirect"],
    ["Use RedirectMatch with conditions", "Ensure destination differs from source", "Test redirect chains with curl -v"],
    ["# Causes loop:\n# RedirectMatch ^/$ /home\n# Fix - be specific:\nRedirect 301 /old-path /new-path"])

add("redirectmatch-regex-error", "Apache RedirectMatch Regex Error",
    "The RedirectMatch directive has an invalid regular expression.",
    ["Unescaped special characters", "Unmatched parentheses or brackets", "Invalid capture group syntax"],
    ["Escape special regex characters with backslash", "Test regex pattern independently", "Use simple patterns where possible"],
    ["RedirectMatch 301 ^/blog/(.*)$ /articles/$1"])

add("proxyreverse-mismatch", "Apache ProxyPassReverse Mismatch",
    "ProxyPassReverse does not match the corresponding ProxyPass configuration.",
    ["ProxyPassReverse missing for a proxied path", "ProxyPassReverse URL does not match backend response", "Multiple ProxyPass without corresponding ProxyPassReverse"],
    ["Add matching ProxyPassReverse for each ProxyPass", "Ensure the reverse URL matches the backend's redirect location", "Test with curl -I to check response headers"],
    ["ProxyPass /app http://backend:8080/app\nProxyPassReverse /app http://backend:8080/app"])

add("rewritelog-deprecated", "Apache RewriteLog Deprecated",
    "The RewriteLog directive is used but has been deprecated.",
    ["Using RewriteLog instead of LogLevel for rewrite debugging", "Apache 2.4+ removed RewriteLog", "Logging level not set high enough for rewrite traces"],
    ["Use LogLevel rewrite:trace3 or higher instead of RewriteLog", "Set LogLevel in the relevant VirtualHost or Directory", "Use trace levels 1-8 for varying detail"],
    ["LogLevel rewrite:trace3\n# Trace levels:\n# trace1 - minimal\n# trace8 - most verbose"])

add("rewriteoptions-inherit-conflict", "Apache RewriteOptions Inherit Conflict",
    "The RewriteOptions Inherit directive causes unexpected behavior in subdirectories.",
    ["Subdirectory .htaccess overrides parent rewrite rules", "InheritDownBefore or InheritDown not used correctly", "Subdirectory rules conflict with parent rules"],
    ["Use RewriteOptions InheritDown to explicitly control inheritance", "Use InheritDownBefore to run parent rules first", "Be explicit about rule scope"],
    ["# In parent config:\nRewriteOptions InheritDown\n# In subdirectory .htaccess:\nRewriteEngine On"])

# 5. Performance/Resource errors
add("maxrequestworkers-reached", "Apache Server Reached MaxRequestWorkers",
    "The server has reached the maximum number of simultaneous request workers.",
    ["Traffic spike exceeds configured MaxRequestWorkers", "Slow backend responses tying up workers", "KeepAliveTimeout too high holding idle connections", "MaxRequestWorkers set too low for workload"],
    ["Increase MaxRequestWorkers with adequate memory", "Reduce KeepAliveTimeout", "Consider using a reverse proxy or load balancer", "Enable mod_status to monitor worker usage"],
    ["# Monitor\n<Location /server-status>\n  SetHandler server-status\n  Require ip 127.0.0.1\n</Location>\n# Tune\nMaxRequestWorkers 256\nKeepAliveTimeout 5"])

add("server-seems-busy", "Apache Server Seems Busy",
    "Apache is responding slowly and workers are all occupied.",
    ["High concurrent connections", "Slow CGI or application responses", "Insufficient worker threads or processes", "Denial-of-service traffic"],
    ["Increase ServerLimit and MaxRequestWorkers", "Move slow applications to separate servers", "Enable rate limiting with mod_ratelimit", "Use mod_evasive for DoS protection"],
    ["# Use event MPM for better performance\nLoadModule mpm_event_module modules/mod_mpm_event.so"])

add("could-not-bind-to-address", "Apache Could Not Bind to Address",
    "Apache cannot bind to the specified IP address and port.",
    ["Port already in use by another process", "Insufficient privileges for ports below 1024", "IP address is not configured on this machine", "IPv6 address format incorrect"],
    ["Check what is using the port: ss -tlnp | grep :80", "Use setcap or authbind for low ports", "Ensure the IP address exists on the system"],
    ["# Find conflicting process\nss -tlnp | grep :80\n# Use a different port\nListen 8080"])

add("address-already-in-use", "Apache Address Already in Use",
    "Another Apache instance or process is already bound to the requested address.",
    ["Previous Apache process did not shut down cleanly", "Duplicate Listen directive in configuration", "Apache was restarted without stopping the old process first"],
    ["Kill stale Apache processes: pkill httpd", "Ensure only one Apache instance runs", "Check for zombie processes"],
    ["# Check for running processes\nps aux | grep apache\n# Kill if needed\npkill -9 httpd"])

add("unable-to-create-shared-memory", "Apache Unable to Create Shared Memory",
    "Apache cannot create shared memory segments for caches or session data.",
    ["Shared memory file directory does not exist", "Disk quota exceeded", "shmcb cache file permissions wrong", "Kernel limits on shared memory exceeded"],
    ["Create and set permissions on the shared memory directory", "Check disk quota with: df -h", "Tune kernel parameters: sysctl kern.ipc.shmmax"],
    ["# Create cache directory\nmkdir -p /var/run/apache2\nchown www-data:www-data /var/run/apache2"])

add("scoreboard-full", "Apache Scoreboard Full",
    "The scoreboard that tracks worker status is full, indicating all workers are busy.",
    ["All MaxRequestWorkers are active", "Scoreboard file is too small", "Workers stuck in reading or sending states"],
    ["Increase MaxRequestWorkers and ServerLimit", "Investigate slow requests tying up workers", "Check for application-level bottlenecks"],
    ["# Increase workers (requires restart, not graceful)\nServerLimit 512\nMaxRequestWorkers 512"])

add("acceptmutex-error", "Apache AcceptMutex Error",
    "Apache cannot acquire the accept mutex, preventing new connections from being accepted.",
    ["Mutex implementation incompatible with MPM", "Another process holds the mutex", "Lock file permissions wrong"],
    ["Check AcceptMutex directive for your MPM", "Ensure lock file directory is writable", "Use a different mutex mechanism"],
    ["# For event MPM, accept mutex is typically not needed\n# If needed:\nMutex default:/var/lock/apache2"])

add("listenbacklog-too-high", "Apache ListenBacklog Too High",
    "The ListenBacklog value exceeds the system's maximum connection queue size.",
    ["Value exceeds sysctl somaxconn limit", "Value is negative or extremely large", "Value not supported by the operating system kernel"],
    ["Set ListenBacklog to match or be below somaxconn", "Increase somaxconn: sysctl -w net.core.somaxconn=1024", "Use a reasonable value like 200-511"],
    ["ListenBacklog 511\n# Or increase system limit:\n# sysctl -w net.core.somaxconn=1024"])

add("keepalivetimeout-too-high", "Apache KeepAliveTimeout Too High",
    "The KeepAliveTimeout is set too high, consuming worker resources.",
    ["Timeout set to many seconds or minutes", "Idle connections occupying workers", "Combined with high MaxKeepAliveRequests"],
    ["Reduce KeepAliveTimeout to 2-5 seconds", "Set MaxKeepAliveRequests to 100", "Monitor with server-status for idle connections"],
    ["KeepAlive On\nKeepAliveTimeout 5\nMaxKeepAliveRequests 100"])

add("maxrequestsperchild-too-low", "Apache MaxRequestsPerChild Too Low",
    "MaxRequestsPerChild is set so low that child processes recycle too frequently.",
    ["Value is very small (e.g., 10-50)", "Frequent process restarts wasting resources", "Child processes do not live long enough to benefit from caching"],
    ["Set MaxRequestsPerChild to 1000 or higher", "Set to 0 for unlimited (caution with memory leaks)", "Monitor process lifecycle with server-status"],
    ["# Recycle processes after 10000 requests\nMaxRequestsPerChild 10000"])

add("worker-thread-limit", "Apache Worker Thread Limit",
    "The thread limit for the MPM worker or event module is reached.",
    ["ThreadsPerChild exceeds ThreadLimit", "ThreadLimit not increased before ThreadsPerChild", "Default ThreadLimit of 64 or 19200 exceeded"],
    ["Set ThreadLimit >= ThreadsPerChild", "Both require a full restart", "Tune based on system resources"],
    ["ThreadLimit 256\nThreadsPerChild 256\nServerLimit 64"])

add("child-process-exited", "Apache Child Process Exited Unexpectedly",
    "An Apache child process terminated abnormally.",
    ["Segfault in a module (e.g., mod_php bug)", "Memory corruption or exhaustion", "Killed by OOM killer", "Module bug or incompatibility"],
    ["Check error log for segfault details", "Update all modules to match Apache version", "Monitor memory usage and increase if needed", "Check dmesg for OOM killer messages"],
    ["# Check error log\ntail -f /var/log/apache2/error.log\n# Check for OOM\ndmesg | grep -i oom"])

add("graceful-restart-failed", "Apache Graceful Restart Failed",
    "A graceful restart (graceful or reload) did not complete successfully.",
    ["Configuration syntax error detected during restart", "Old child processes not terminating", "Module fails to reinitialize"],
    ["Run apachectl configtest before reloading", "Check for syntax errors in configuration", "Force kill stuck processes if needed"],
    ["apachectl configtest && apachectl graceful"])

add("graceful-restart-completed", "Apache Graceful Restart Completed",
    "Informational message indicating a graceful restart completed successfully.",
    ["This is typically informational, not an error", "May appear in logs during routine restarts", "Verify all modules reloaded correctly"],
    ["No fix needed - this is a normal log entry", "Monitor error logs for any issues during the restart", "Verify site functionality after restart"],
    ["# Verify Apache is running\napachectl status\n# Or\ncurl -I http://localhost/"])

# 6. Access control errors
add("client-denied-by-server-config", "Apache Client Denied by Server Configuration",
    "Apache denied access to the client based on server configuration.",
    ["Deny from all directive blocking the request", "Require directive does not match client IP or credentials", "Order allow,deny with missing Allow rule", "GeoIP or environment-based blocking"],
    ["Check Allow/Deny or Require directives", "Verify client IP is permitted", "Review access logs for denial details"],
    ["<Directory /var/www/protected>\n  Require ip 192.168.1.0/24\n</Directory>"])

add("htaccess-not-allowed", "Apache .htaccess Not Allowed",
    "The .htaccess file is present but AllowOverride is set to None.",
    ["AllowOverride None set for the directory tree", "Directive in .htaccess requires AllowOverride All", "Per-directory overrides not permitted in main config"],
    ["Set AllowOverride All or the specific directive class", "Move directives to the main config instead", "Use <Directory> blocks in the main config"],
    ["<Directory /var/www/html>\n  AllowOverride All\n</Directory>"])

add("authtype-not-set", "Apache AuthType Not Set",
    "Authentication directives are used without setting AuthType.",
    ["AuthType Basic or Digest missing", "AuthUserFile or AuthGroupFile set without AuthType", "Require valid-user used without authentication setup"],
    ["Add AuthType Basic (or Digest) before other auth directives", "Set AuthName along with AuthType", "Complete authentication configuration before Require"],
    ["AuthType Basic\nAuthName \"Restricted Area\"\nAuthUserFile /etc/apache2/.htpasswd\nRequire valid-user"])

add("authuserfile-not-found", "Apache AuthUserFile Not Found",
    "The htpasswd file specified in AuthUserFile does not exist or is not readable.",
    ["File path is incorrect", "File not created with htpasswd utility", "File permissions prevent Apache from reading it"],
    ["Create the file: htpasswd -c /etc/apache2/.htpasswd username", "Verify file exists and is readable by Apache user", "Check file permissions: chmod 640 .htpasswd"],
    ["# Create password file\nhtpasswd -c /etc/apache2/.htpasswd admin\n# In Apache config\nAuthUserFile /etc/apache2/.htpasswd"])

add("authgroupfile-missing", "Apache AuthGroupFile Missing",
    "The group file specified in AuthGroupFile does not exist.",
    ["File path incorrect or file not created", "File format is wrong (groupname: user1 user2)", "File permissions prevent reading"],
    ["Create the group file with correct format", "Verify file path and permissions", "Ensure group file is readable by Apache"],
    ["# /etc/apache2/groupfile format:\n# admins: alice bob\nAuthGroupFile /etc/apache2/groupfile\nRequire group admins"])

add("require-valid-user-failed", "Apache Require valid-user Failed",
    "The Require valid-user directive fails because no valid user authenticated.",
    ["User provided wrong credentials", "AuthUserFile does not contain the user", "Password file is empty or corrupted"],
    ["Verify username exists in AuthUserFile", "Reset password: htpasswd /etc/apache2/.htpasswd username", "Check AuthUserFile path is correct"],
    ["# Add or reset user\nhtpasswd /etc/apache2/.htpasswd username\n# Verify file content\ncat /etc/apache2/.htpasswd"])

add("satisfy-any-all-error", "Apache Satisfy Any/All Error",
    "The Satisfy directive has conflicting or invalid configuration.",
    ["Satisfy Any combined with Require causing unexpected access", "Satisfy All but one condition always fails", "Satisfy used in contexts where it is not applicable"],
    ["Use Require directives instead of Satisfy (Apache 2.4+)", "Test access with both IP and authentication", "Clarify whether Any or All is needed"],
    ["# Apache 2.4 approach - use Require with environment:\nRequire ip 192.168.1.0/24\nRequire valid-user\n# Or use RequireAny:\n<RequireAny>\n  Require ip 192.168.1.0/24\n  Require valid-user\n</RequireAny>"])

add("access-forbidden", "Apache Access to Path Forbidden",
    "Access to a specific path or resource is forbidden by Apache configuration.",
    ["Options -Indexes set and no index file exists", "Require all denied for the directory", "File permissions prevent access", "SELinux or AppArmor blocking access"],
    ["Add an index file or enable Options +Indexes", "Set Require all granted for the directory", "Check file ownership and permissions"],
    ["<Directory /var/www/html>\n  Options +FollowSymLinks +Indexes\n  Require all granted\n</Directory>"])

add("options-indexes-security", "Apache Options Indexes Security Risk",
    "Directory listing is enabled, exposing file structure to visitors.",
    ["Options +Indexes allows directory browsing", "No index.html or DirectoryIndex file present", "Sensitive files visible in directory listing"],
    ["Add an index file or set Options -Indexes", "Remove sensitive files from web-accessible directories", "Use Apache autoindex module with careful configuration"],
    ["# Disable directory listing\n<Directory /var/www/html>\n  Options -Indexes +FollowSymLinks\n</Directory>"])

add("followsymlinks-not-enabled", "Apache FollowSymLinks Not Enabled",
    "A symbolic link is being followed but FollowSymLinks is not enabled.",
    ["Options +FollowSymLinks not set", "Options +SymLinksIfOwnerMatch not set", "Symlink points outside DocumentRoot"],
    ["Enable Options +FollowSymLinks or +SymLinksIfOwnerMatch", "Use SymlinksIfOwnerMatch for better security", "Verify symlink targets are accessible"],
    ["<Directory /var/www/html>\n  Options +FollowSymLinks\n</Directory>"])

# 7. CGI/FastCGI errors
add("premature-end-of-script", "Apache Premature End of Script Headers",
    "The CGI script closed its output before sending complete HTTP headers.",
    ["Script crashes or exits before printing headers", "Script outputs binary data before headers", "Script takes too long and is killed", "Interpreter error in script"],
    ["Ensure script prints Content-Type header first", "Check script for errors: perl -c script.pl", "Increase ScriptTimeout if script needs more time", "Add error logging to the script"],
    ["#!/usr/bin/perl\nprint \"Content-type: text/html\\n\\n\";\nprint \"Hello World\\n\";"])

add("script-not-found", "Apache CGI Script Not Found",
    "The requested CGI script does not exist at the specified path.",
    ["Script file not uploaded or deployed", "Script path in URL does not match actual file location", "Script permissions are wrong (not executable)", "ScriptHandler or AddHandler not configured"],
    ["Verify script exists at the CGI directory path", "Ensure script has execute permission: chmod +x script.cgi", "Check ScriptAlias or AddHandler configuration"],
    ["# Ensure script is executable\nchmod +x /usr/lib/cgi-bin/script.cgi\n# Check ScriptAlias\nScriptAlias /cgi-bin/ /usr/lib/cgi-bin/"])

add("fastcgi-timeout", "Apache FastCGI Timeout",
    "The FastCGI application did not respond within the configured timeout.",
    ["Backend application is too slow", "FcgiIpcTimeout set too low", "Backend process is deadlocked or crashed", "Network latency between Apache and FastCGI backend"],
    ["Increase FcgidIOTimeout or FcgidProcessLifeTime", "Optimize backend application response time", "Check if backend process is still running"],
    ["FcgidIOTimeout 300\nFcgidConnectTimeout 60\nFcgidProcessLifeTime 3600"])

add("fastcgi-exhausted", "Apache FastCGI Process Exhausted",
    "All FastCGI processes are busy and no more can be spawned.",
    ["FcgidMaxProcesses reached", "Backend processes not releasing resources", "FcgidProcessLifeTime too long keeping dead processes"],
    ["Increase FcgidMaxProcesses", "Reduce FcgidProcessLifeTime to recycle stale processes", "Check for resource leaks in the application"],
    ["FcgidMaxProcesses 100\nFcgidProcessLifeTime 600\nFcgidMinProcesses 5"])

add("mod-cgi-not-allowed", "Apache mod_cgi Not Allowed",
    "CGI execution is not permitted in the specified directory.",
    ["ScriptAlias not set for the directory", "Options +ExecCGI not enabled", "AddHandler cgi-script not configured", "AllowOverride prevents CGI in .htaccess"],
    ["Set Options +ExecCGI for the CGI directory", "Use ScriptAlias for the CGI directory", "Ensure AllowOverride allows the directives"],
    ["<Directory /usr/lib/cgi-bin>\n  Options +ExecCGI\n  AddHandler cgi-script .cgi .pl\n  Require all granted\n</Directory>"])

add("suexec-error", "Apache suEXEC Error",
    "The suEXEC wrapper encountered an error running CGI as a different user.",
    ["suEXEC binary not installed or not in correct location", "User/group not permitted to run CGI", "suEXEC binary permissions are wrong", "DocumentRoot is not owned by the user"],
    ["Verify suEXEC is installed: which suexec", "Ensure user/group exist and are valid", "Check suEXEC permissions: ls -la /usr/sbin/suexec"],
    ["# Check suEXEC configuration\n/usr/sbin/suexec -V\n# Verify ownership\nls -la /home/user/public_html/"])

add("script-header-too-long", "Apache Script Header Too Long",
    "The CGI script output headers that exceed Apache's maximum header length.",
    ["Script generates extremely long headers", "Infinite header output due to script bug", "Header buffer size exceeded"],
    ["Reduce header length in the script", "Check for infinite loops in header generation", "Increase header buffer if legitimately needed"],
    ["# In Apache config\nLimitRequestFields 100\nLimitRequestFieldSize 8190"])

add("script-output-too-large", "Apache Script Output Too Large",
    "The CGI script produced output that exceeds the configured size limit.",
    ["Script generates more output than LimitRequestBody allows", "Script error causes massive output", "Default output limit exceeded"],
    ["Increase LimitRequestBody if large output is expected", "Fix script to produce output within limits", "Stream output instead of buffering"],
    ["# Allow up to 10MB\nLimitRequestBody 10485760"])

add("script-failed-to-start", "Apache Script Failed to Start",
    "The CGI script could not be started by Apache.",
    ["Script interpreter not found (bad shebang line)", "Script lacks execute permission", "Required libraries not available to the script", "Script file is corrupted"],
    ["Check the shebang line: head -1 script.cgi", "chmod +x the script file", "Verify the interpreter exists at the specified path"],
    ["#!/usr/bin/perl\n# Verify perl exists\nwhich perl"])

add("cgi-directory-not-configured", "Apache CGI Directory Not Configured",
    "No CGI directory is configured, so CGI scripts cannot be executed.",
    ["No ScriptAlias directive in configuration", "No directory with Options +ExecCGI", "CGI module not loaded"],
    ["Add a ScriptAlias directive for the CGI directory", "Set Options +ExecCGI for the appropriate directory", "Load mod_cgi or mod_cgid"],
    ["ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/\n<Directory /usr/lib/cgi-bin>\n  Options +ExecCGI\n  Require all granted\n</Directory>"])

# 8. Proxy errors
add("proxy-error-502", "Apache Proxy Error 502 Bad Gateway",
    "The backend server returned an invalid response or is unreachable.",
    ["Backend server is down or not responding", "Backend returned malformed HTTP response", "Connection to backend was reset mid-transfer", "Backend overloaded or out of resources"],
    ["Verify backend server is running", "Check ProxyPass and backend URL configuration", "Increase ProxyTimeout", "Check firewall rules between Apache and backend"],
    ["ProxyPass /app http://backend:8080/\nProxyTimeout 300"])

add("proxypass-invalid", "Apache ProxyPass Invalid",
    "The ProxyPass directive has invalid syntax or configuration.",
    ["Missing URL or backend URL", "Invalid path syntax", "ProxyPass used in wrong context", "Trailing slash mismatch between source and target"],
    ["Verify ProxyPass syntax: ProxyPass /path http://backend:port/path", "Ensure source and target paths have consistent trailing slashes", "Check that mod_proxy is loaded"],
    ["# Correct - trailing slash matters\nProxyPass /app/ http://backend:8080/app/\nProxyPass /app http://backend:8080/app/"])

add("proxypassreverse-not-set", "Apache ProxyPassReverse Not Set",
    "Backend server responses contain internal redirects or links that are not rewritten.",
    ["Missing ProxyPassReverse directive", "ProxyPassReverse URL does not match backend's redirect location", "Application generates absolute URLs pointing to backend"],
    ["Add ProxyPassReverse for each ProxyPass", "Match ProxyPassReverse URL to backend's actual redirect URL", "Test with curl -I to verify Location headers"],
    ["ProxyPass /app http://backend:8080/\nProxyPassReverse /app http://backend:8080/"])

add("balancermember-not-configured", "Apache BalancerMember Not Configured",
    "The proxy balancer has no valid backend members defined.",
    ["No BalancerMember directives in Proxy block", "All BalancerMember backends are down", "BalancerMember URLs are invalid", "Missing mod_proxy_balancer module"],
    ["Add BalancerMember directives with valid backend URLs", "Ensure backend servers are running", "Load mod_proxy_balancer module"],
    ["<Proxy balancer://cluster>\n  BalancerMember http://backend1:8080\n  BalancerMember http://backend2:8080\n</Proxy>"])

add("proxytimeout-too-low", "Apache ProxyTimeout Too Low",
    "The ProxyTimeout is set too low, causing premature connection closure.",
    ["Default ProxyTimeout of 60 seconds too short", "Backend takes longer than configured timeout", "Large file transfers need more time"],
    ["Increase ProxyTimeout to match backend response time", "Set per-connection timeouts if needed", "Consider async processing for long operations"],
    ["ProxyTimeout 300\n# Or per-location:\n<Location /api/>\n  ProxyTimeout 600\n</Location>"])

add("proxybadheader", "Apache ProxyBadHeader",
    "The backend server returned HTTP headers that are malformed or invalid.",
    ["Backend sends non-standard header format", "Header contains invalid characters", "Backend response encoding is wrong", "Network corruption of response"],
    ["Fix the backend application to send valid HTTP headers", "Check for encoding issues in backend response", "Use proxy-error overrides if backend cannot be fixed"],
    ["# Check backend response\ncurl -v http://backend:8080/\n# Ensure clean HTTP/1.1 headers"])

add("noprotocol-handler-valid", "Apache No Protocol Handler Was Valid",
    "No proxy protocol handler is available for the requested URL scheme.",
    ["mod_proxy_http not loaded for HTTP backends", "mod_proxy_fcgi not loaded for FastCGI", "mod_proxy_ajp not loaded for AJP", "Wrong URL scheme in ProxyPass"],
    ["Load the appropriate proxy protocol module", "Verify module matches the backend protocol", "Check ProxyPass URL scheme"],
    ["LoadModule proxy_http_module modules/mod_proxy_http.so\nLoadModule proxy_fcgi_module modules/mod_proxy_fcgi.so\nLoadModule proxy_ajp_module modules/mod_proxy_ajp.so"])

add("proxy-reading-status-line", "Apache Proxy Error Reading Status Line",
    "Apache could not read the HTTP status line from the backend server response.",
    ["Backend closed connection before sending status line", "Backend is using an incompatible protocol", "Network issue between Apache and backend", "Backend is down or not listening"],
    ["Verify backend is running and accepting connections", "Check network connectivity between Apache and backend", "Increase ProxyTimeout", "Check backend logs for errors"],
    ["# Test backend connectivity\ncurl -v http://backend:8080/\n# Check if backend is listening\nss -tlnp | grep 8080"])

add("proxy-connection-timeout", "Apache Proxy Connection Timeout",
    "The proxy connection to the backend timed out.",
    ["Backend server is unreachable", "Network latency too high", "Firewall blocking the connection", "Backend overloaded"],
    ["Increase ProxyTimeout or ProxyIOTimeout", "Check network path between Apache and backend", "Verify firewall rules", "Consider connection pooling"],
    ["ProxyTimeout 120\nProxyIOTimeout 120"])

add("proxy-ssl-handshake-failed", "Apache Proxy SSL Handshake Failed",
    "The SSL/TLS handshake between Apache and the backend proxy target failed.",
    ["Backend SSL certificate not trusted by Apache", "SSL protocol mismatch between Apache and backend", "SSLProxyCACertificateFile not configured", "Backend uses self-signed certificate"],
    ["Configure SSLProxyCACertificateFile to trust the backend certificate", "Set SSLProxyVerify and SSLProxyCheckPeerCN", "Use SSLProxyNone if testing with self-signed certs"],
    ["SSLProxyEngine On\nSSLProxyVerify none\nSSLProxyCheckPeerCN off\nSSLProxyCheckPeerName off"])

# 9. MIME/content errors
add("addtype-invalid", "Apache AddType Invalid",
    "The AddType directive has invalid syntax or an unrecognized MIME type.",
    ["MIME type string is incorrect", "File extension does not include the dot", "MIME type not registered in the system"],
    ["Use correct MIME type format: application/javascript", "Ensure extension starts with a dot: .js", "Consult IANA MIME type list"],
    ["AddType application/javascript .js\nAddType text/css .css"])

add("addhandler-conflict", "Apache AddHandler Conflict",
    "Multiple AddHandler or SetHandler directives conflict for the same file extension.",
    ["Two handlers registered for the same extension", "AddHandler and SetHandler contradict each other", "Handler for extension defined in multiple config files"],
    ["Use only one handler per extension", "Remove conflicting handler definitions", "Use a single AddHandler for each extension"],
    ["# Choose one:\nAddHandler cgi-script .cgi\n# Remove any conflicting:\n# SetHandler cgi-script .cgi"])

add("forcetype-not-allowed", "Apache ForceType Not Allowed",
    "The ForceType directive is used in a context where it is not permitted.",
    ["ForceType in .htaccess but AllowOverride does not include FileInfo", "ForceType used in VirtualHost context instead of Directory", "Directive not supported in the current configuration"],
    ["Ensure AllowOverride includes FileInfo", "Use ForceType within <Directory> or .htaccess blocks", "Use AddType or SetHandler instead if appropriate"],
    ["<Directory /var/www/html>\n  ForceType text/plain\n</Directory>"])

add("removetype-error", "Apache RemoveType Error",
    "The RemoveType directive has incorrect syntax or does not remove the expected type.",
    ["Extension argument does not include the dot", "Extension does not match any previously added type", "RemoveType used in wrong context"],
    ["Use the full extension with dot: RemoveType .cgi", "Ensure the type was previously added with AddType", "Check config file load order"],
    ["RemoveType .php\nRemoveType .cgi"])

add("defaulttype-missing", "Apache DefaultType Missing",
    "The DefaultType directive is not set, so Apache uses application/octet-stream for unknown types.",
    ["Unknown MIME types served with wrong Content-Type", "DefaultType not configured in main config", "Files without extensions served incorrectly"],
    ["Set DefaultType to the most common type in your site", "Use text/html for HTML-heavy sites", "Set specific types with AddType for better accuracy"],
    ["DefaultType text/html"])

add("adddefaultcharset-error", "Apache AddDefaultCharset Error",
    "The AddDefaultCharset directive specifies an invalid or unrecognized character set.",
    ["Charset name is misspelled", "Charset is not supported by Apache", "AddDefaultCharset conflicts with AddDefaultCharsetOff"],
    ["Use a valid charset name: UTF-8, ISO-8859-1", "Check Apache documentation for supported charsets", "Remove AddDefaultCharsetOff if you want default charset"],
    ["AddDefaultCharset UTF-8"])

add("mod-mime-error", "Apache mod_mime Error",
    "The mod_mime module encountered an error mapping file extensions to content types.",
    ["Multiple extensions on a file (e.g., file.php.txt)", "AddType and RemoveType conflict", "Module not loaded but directives reference it"],
    ["LoadModule mime_module modules/mod_mime.so", "Avoid multiple extensions on files", "Check AddType/RemoveType/DefaultType for conflicts"],
    ["LoadModule mime_module modules/mod_mime.so\n# Ensure /etc/mime.types is accessible"])

add("mime-type-not-recognized", "Apache MIME Type Not Recognized",
    "The MIME type specified in AddType or Content-Type is not recognized.",
    ["Typo in the MIME type string", "MIME type is not in the system's mime.types", "Custom MIME type not registered"],
    ["Check the MIME type spelling against IANA list", "Add custom types with AddType", "Verify /etc/mime.types is up to date"],
    ["AddType application/wasm .wasm\nAddType font/woff2 .woff2"])

add("sethandler-not-allowed", "Apache SetHandler Not Allowed",
    "The SetHandler directive is used in an invalid context.",
    ["SetHandler in .htaccess without AllowOverride FileInfo", "SetHandler used where AddHandler should be", "SetHandler in wrong configuration block"],
    ["Ensure AllowOverride includes FileInfo for .htaccess usage", "Use SetHandler within <Location>, <Files>, or Directory", "Use AddHandler for file extension-based processing"],
    ["<Location /server-status>\n  SetHandler server-status\n</Location>"])

add("action-not-configured", "Apache Action Not Configured",
    "The Action directive references a handler or CGI script that is not properly configured.",
    ["Handler name in Action does not match a defined handler", "CGI script path is incorrect", "Action used without the required module"],
    ["Verify the handler name matches an existing handler", "Ensure the CGI script exists and is executable", "Load the module that defines the handler"],
    ["Action image/jpeg /cgi-bin/images.cgi\n<FilesMatch \"\\.jpg$\">\n  SetHandler image/jpeg\n</FilesMatch>"])

# 10. Logging/Status
add("customlog-pipe-broken", "Apache CustomLog Pipe Broken",
    "The CustomLog pipe command is not running or has crashed.",
    ["Piped logging process has exited", "Command in CustomLog pipe is not executable", "Pipe command path is incorrect"],
    ["Restart the piped logging process", "Verify the command exists and is executable", "Check error log for pipe process exit status"],
    ["# Verify pipe command exists\nwhich rotatelogs\n# Use full path\nCustomLog \"|/usr/bin/rotatelogs /var/log/apache2/access.log 86400\" combined"])

add("errorlog-rotation-failed", "Apache ErrorLog Rotation Failed",
    "The error log rotation mechanism has failed.",
    ["Log rotation command is not executable", "Rotated log file permissions wrong", "Disk full preventing log rotation", "Log file locked by another process"],
    ["Check logrotate configuration", "Ensure the rotation script has proper permissions", "Verify sufficient disk space", "Use: lsof +D /var/log/apache2/"],
    ["# Check disk space\ndf -h /var/log/apache2/\n# Check for locked files\nlsof /var/log/apache2/error.log"])

add("logformat-parse-error", "Apache LogFormat Parse Error",
    "The LogFormat string contains invalid or unrecognized format specifiers.",
    ["Invalid percent directive (e.g., %Z which is not supported)", "Mismatched quotes in the format string", "Unknown format specifier used"],
    ["Check format string against Apache log format documentation", "Remove or replace invalid specifiers", "Escape literal percent signs with %%"],
    ["LogFormat \"%h %l %u %t \\\"%r\\\" %>s %b \\\"%{Referer}i\\\" \\\"%{User-Agent}i\\\"\" combined"])

add("mod-status-restricted", "Apache mod_status Restricted",
    "Access to server-status is restricted and returning errors.",
    ["Require directive does not match the requesting client", "No Location block defined for /server-status", "mod_status not loaded"],
    ["Add proper Require directives for trusted IPs", "Load mod_status module", "Restrict access to localhost or admin subnet"],
    ["<Location /server-status>\n  SetHandler server-status\n  Require ip 127.0.0.1 10.0.0.0/8\n</Location>"])

add("server-status-403", "Apache server-status 403 Forbidden",
    "Access to /server-status returns 403 Forbidden.",
    ["No Require directive allows the client IP", "All Require denied the request", "Location block missing for server-status handler"],
    ["Add Require ip for the accessing client", "Allow from localhost: Require ip 127.0.0.1", "Check access logs for denial reason"],
    ["<Location /server-status>\n  SetHandler server-status\n  Require ip 127.0.0.1\n</Location>"])

add("server-info-403", "Apache server-info 403 Forbidden",
    "Access to /server-info returns 403 Forbidden.",
    ["No Require directive allows the client", "mod_info not loaded", "Location block for server-info missing or has wrong Require"],
    ["Add Require ip for trusted clients only", "Load mod_info module", "Restrict to admin IPs for security"],
    ["<Location /server-info>\n  SetHandler server-info\n  Require ip 127.0.0.1\n</Location>"])

add("scoreboard-file-error", "Apache ScoreBoardFile Error",
    "The ScoreBoardFile cannot be created or accessed.",
    ["File path does not exist", "File permissions prevent creation", "Another Apache instance uses the same scoreboard", "Disk full"],
    ["Create the directory for the scoreboard file", "Set proper ownership: chown www-data:www-data /var/run/apache2/", "Ensure unique scoreboard for each Apache instance", "Check disk space"],
    ["ScoreBoardFile /var/run/apache2/apache_runtime_main"])

add("lockfile-deprecated", "Apache LockFile Deprecated",
    "The LockFile directive is deprecated and should not be used.",
    ["Using LockFile in Apache 2.4+ configuration", "Legacy configuration from Apache 2.2 not updated", "LockFile conflicts with Mutex directive"],
    ["Remove the LockFile directive", "Use Mutex default:/path instead", "Apache 2.4 manages lock files automatically"],
    ["# Remove this:\n# LockFile /var/lock/apache2/accept.lock\n# Apache 2.4 manages this automatically"])

add("pidfile-not-writable", "Apache PidFile Not Writable",
    "Apache cannot write the PID file to the specified location.",
    ["Directory does not exist", "Apache user lacks write permissions", "File already exists and is locked by another process", "SELinux context is wrong"],
    ["Create the PID directory with proper ownership", "Set permissions: chown www-data:www-data /var/run/apache2/", "Check SELinux: restorecon -Rv /var/run/apache2/"],
    ["mkdir -p /var/run/apache2\nchown www-data:www-data /var/run/apache2\nchmod 755 /var/run/apache2"])

add("mutex-error", "Apache Mutex Error",
    "Apache cannot create or acquire a mutex for inter-process synchronization.",
    ["Mutex directory does not exist or is not writable", "Another Apache instance uses the same mutex file", "Mutex implementation incompatible with the OS", "Lock file permissions are wrong"],
    ["Create the mutex directory and set ownership", "Use unique mutex paths for each Apache instance", "Check disk space in the mutex directory", "Use default mutex mechanism"],
    ["Mutex default:/var/lock/apache2\n# Or for specific needs:\nMutex ssl-cache /var/run/apache2/ssl_mutex"])


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0
    for slug, title, desc, causes, fixes, examples in PAGES:
        causes_md = "\n".join(f"- {c}" for c in causes)
        fixes_md = "\n".join(f"- {f}" for f in fixes)
        body = f"""## Error Description

{desc}

## Common Causes

{causes_md}

## How to Fix

{fixes_md}

## Examples

```
{examples}
```
"""
        frontmatter = f"""---
title: "[Solution] {title}"
description: "{desc}"
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---
"""
        content = frontmatter + "\n" + body
        filepath = os.path.join(OUTPUT_DIR, f"{slug}.md")
        with open(filepath, "w") as f:
            f.write(content)
        count += 1
    print(f"Created {count} Apache error pages in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
