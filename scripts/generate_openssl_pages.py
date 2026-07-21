#!/usr/bin/env python3
"""Generate new OpenSSL error pages to expand to 100+ total."""
import os

TOOL_DIR = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/openssl/'
EXISTING = {f.replace('.md', '') for f in os.listdir(TOOL_DIR) if f.endswith('.md')}

PAGES = [
    # Certificate errors
    ("openssl-unable-to-load-certificate", "OpenSSL Unable to Load Certificate Error",
     "Fix OpenSSL unable to load certificate error. Resolve certificate loading failures.",
     "OpenSSL cannot load the certificate file. The file path is wrong, the file is corrupted, or the format is unsupported.",
     ["Certificate file path is wrong", "File is corrupted or empty", "Format is not PEM or DER"],
     ["openssl x509 -in cert.pem -noout -text",
      "file /path/to/cert.pem"]),

    ("openssl-pem-read-certificate", "OpenSSL PEM Read Certificate Error",
     "Fix OpenSSL PEM read certificate error. Resolve PEM parsing failures.",
     "OpenSSL fails to read the certificate in PEM format. The PEM encoding is corrupted or incomplete.",
     ["PEM headers are missing or wrong", "Base64 content is corrupted", "File is truncated"],
     ["openssl x509 -in cert.pem -noout",
      "head -5 cert.pem"]),

    ("openssl-certificate-expired", "OpenSSL Certificate Expired Error",
     "Fix OpenSSL certificate expired error. Resolve certificate expiration issues.",
     "The certificate has expired and is no longer valid. TLS connections using this certificate will fail.",
     ["Certificate validity period has ended", "Certificate was not renewed", "System clock is wrong"],
     ["openssl x509 -in cert.pem -noout -dates",
      "openssl x509 -in cert.pem -noout -enddate"]),

    ("openssl-certificate-not-yet-valid", "OpenSSL Certificate Not Yet Valid Error",
     "Fix OpenSSL certificate not yet valid error. Resolve certificate validity start time issues.",
     "The certificate is not yet valid. The validity period has not started.",
     ["Certificate start date is in the future", "System clock is wrong", "Certificate was issued with wrong dates"],
     ["openssl x509 -in cert.pem -noout -dates",
      "date"]),

    ("openssl-certificate-revoked", "OpenSSL Certificate Revoked Error",
     "Fix OpenSSL certificate revoked error. Resolve certificate revocation issues.",
     "The certificate has been revoked by the CA. It should no longer be trusted.",
     ["Certificate was revoked by CA", "Certificate is in CRL", "OCSP reports revoked status"],
     ["openssl x509 -in cert.pem -noout -serial"]),

    ("openssl-certificate-chain-incomplete", "OpenSSL Certificate Chain Incomplete Error",
     "Fix OpenSSL certificate chain incomplete error. Resolve missing intermediate certificates.",
     "The certificate chain is incomplete. Intermediate or root certificates are missing.",
     ["Intermediate certificate is missing", "Root certificate is not in the chain", "Chain is not properly ordered"],
     ["openssl verify -CAfile ca.pem cert.pem",
      "openssl s_client -connect host:443 -showcerts"]),

    ("openssl-self-signed-cert", "OpenSSL Self-Signed Certificate Error",
     "Fix OpenSSL self-signed certificate error. Resolve self-signed certificate trust issues.",
     "The certificate is self-signed and not trusted by clients. Browsers and clients reject the connection.",
     ["Certificate was signed by its own key", "CA certificate is not in trust store", "Self-signed cert used in production"],
     ["openssl x509 -in cert.pem -noout -issuer -subject"]),

    ("openssl-untrusted-root", "OpenSSL Untrusted Root Error",
     "Fix OpenSSL untrusted root error. Resolve root certificate trust issues.",
     "The root CA certificate is not in the trust store. The certificate chain cannot be verified.",
     ["Root CA is not installed in trust store", "Custom CA was used but not trusted", "Trust store is outdated"],
     ["openssl verify -CAfile ca.pem cert.pem",
      "update-ca-certificates"]),

    ("openssl-issuer-not-found", "OpenSSL Issuer Not Found Error",
     "Fix OpenSSL issuer not found error. Resolve certificate issuer reference issues.",
     "The issuer of the certificate cannot be found. The issuer certificate is not available.",
     ["Issuer certificate is not in the chain", "Issuer CA is not installed", "Certificate chain is broken"],
     ["openssl x509 -in cert.pem -noout -issuer"]),

    ("openssl-subject-mismatch", "OpenSSL Subject Mismatch Error",
     "Fix OpenSSL subject mismatch error. Resolve certificate subject verification issues.",
     "The certificate subject does not match the expected name. Hostname verification fails.",
     ["Certificate CN does not match hostname", "SAN does not include the hostname", "Wrong certificate for the domain"],
     ["openssl x509 -in cert.pem -noout -subject",
      "openssl x509 -in cert.pem -noout -text | grep 'Subject Alternative Name'"]),

    ("openssl-san-missing", "OpenSSL SAN Missing Error",
     "Fix OpenSSL SAN missing error. Resolve Subject Alternative Name issues.",
     "The certificate does not have a Subject Alternative Name (SAN) extension. Modern TLS requires SAN.",
     ["SAN extension was not included when generating cert", "Only CN is set without SAN", "SAN is empty"],
     ["openssl x509 -in cert.pem -noout -text | grep -A1 'Subject Alternative Name'"]),

    ("openssl-key-usage-invalid", "OpenSSL Key Usage Invalid Error",
     "Fix OpenSSL key usage invalid error. Resolve key usage extension issues.",
     "The certificate key usage does not include the required usage. TLS or code signing usage is missing.",
     ["Key usage does not include digitalSignature", "Key usage does not include keyEncipherment", "Extended key usage is wrong"],
     ["openssl x509 -in cert.pem -noout -text | grep -A1 'Key Usage'"]),

    ("openssl-extended-key-usage", "OpenSSL Extended Key Usage Error",
     "Fix OpenSSL extended key usage error. Resolve EKU extension issues.",
     "The extended key usage does not include the required purpose. TLS server auth EKU is missing.",
     ["EKU does not include serverAuth", "EKU does not include clientAuth", "EKU OID is not recognized"],
     ["openssl x509 -in cert.pem -noout -text | grep -A1 'Extended Key Usage'"]),

    ("openssl-basic-constraints", "OpenSSL Basic Constraints Error",
     "Fix OpenSSL basic constraints error. Resolve basic constraints extension issues.",
     "The basic constraints are missing or wrong. A CA certificate does not have CA:true, or a leaf cert has CA:true.",
     ["CA certificate missing CA:TRUE", "Leaf certificate has CA:TRUE", "Path length constraint is exceeded"],
     ["openssl x509 -in cert.pem -noout -text | grep -A1 'Basic Constraints'"]),

    ("openssl-certificate-format-error", "OpenSSL Certificate Format Error",
     "Fix OpenSSL certificate format error. Resolve certificate encoding issues.",
     "The certificate file format is not recognized. The file is not in PEM or DER format.",
     ["File is not in a recognized format", "File is corrupted", "Wrong file extension for the format"],
     ["openssl x509 -in cert.pem -noout",
      "file /path/to/certificate"]),

    ("openssl-der-vs-pem", "OpenSSL DER vs PEM Error",
     "Fix OpenSSL DER vs PEM error. Resolve certificate encoding format issues.",
     "OpenSSL expects PEM format but receives DER, or vice versa. The format flags are wrong.",
     ["PEM file read with DER flag", "DER file read with PEM flag", "File format does not match expected"],
     ["openssl x509 -in cert.der -inform DER -noout",
      "openssl x509 -in cert.pem -inform PEM -noout"]),

    ("openssl-cert-file-not-found", "OpenSSL Certificate File Not Found Error",
     "Fix OpenSSL certificate file not found error. Resolve certificate path issues.",
     "The certificate file does not exist at the specified path.",
     ["File path is wrong", "File was deleted", "File permissions prevent access"],
     ["ls -la /path/to/cert.pem",
      "find /etc -name '*.pem' -type f"]),

    # Key errors
    ("openssl-unable-to-load-private-key", "OpenSSL Unable to Load Private Key Error",
     "Fix OpenSSL unable to load private key error. Resolve private key loading failures.",
     "OpenSSL cannot load the private key file. The file path is wrong, the password is missing, or the format is wrong.",
     ["Key file path is wrong", "Encrypted key needs password", "Key format is unsupported"],
     ["openssl rsa -in key.pem -check",
      "openssl pkey -in key.pem -check"]),

    ("openssl-key-file-not-found", "OpenSSL Private Key File Not Found Error",
     "Fix OpenSSL private key file not found error. Resolve key path issues.",
     "The private key file does not exist at the specified path.",
     ["File path is wrong", "File was deleted", "File permissions prevent access"],
     ["ls -la /path/to/key.pem",
      "find /etc -name '*.key' -type f"]),

    ("openssl-pem-read-private-key", "OpenSSL PEM Read Private Key Error",
     "Fix OpenSSL PEM read private key error. Resolve PEM key parsing failures.",
     "OpenSSL fails to read the private key in PEM format. The PEM encoding is corrupted.",
     ["PEM headers are wrong", "Base64 content is corrupted", "Key is encrypted and no password provided"],
     ["openssl pkey -in key.pem -noout"]),

    ("openssl-key-format-error", "OpenSSL Key Format Error",
     "Fix OpenSSL key format error. Resolve private key encoding issues.",
     "The private key format is not recognized. The file is not in PEM, DER, or PKCS8 format.",
     ["File is not in recognized format", "Format flags are wrong", "File is corrupted"],
     ["openssl pkey -in key.pem -noout -text",
      "openssl rsa -in key.pem -noout -text"]),

    ("openssl-key-size-too-small", "OpenSSL Key Size Too Small Error",
     "Fix OpenSSL key size too small error. Resolve minimum key length requirements.",
     "The private key size is too small. Modern security requirements mandate minimum key sizes.",
     ["RSA key is less than 2048 bits", "EC key uses weak curve", "Key was generated with old defaults"],
     ["openssl rsa -in key.pem -noout -text | head -5",
      "openssl ecparam -list_curves"]),

    ("openssl-key-size-too-large", "OpenSSL Key Size Too Large Error",
     "Fix OpenSSL key size too large error. Resolve key size compatibility issues.",
     "The private key size is too large for the hardware or software to handle efficiently.",
     ["RSA key exceeds 4096 bits", "Key size causes performance issues", "Hardware security module has size limits"],
     ["openssl rsa -in key.pem -noout -text | head -5"]),

    ("openssl-key-not-match-certificate", "OpenSSL Key Not Match Certificate Error",
     "Fix OpenSSL key not match certificate error. Resolve key-certificate pairing issues.",
     "The private key does not match the certificate. The public key in the certificate does not correspond to the private key.",
     ["Key was regenerated after certificate was issued", "Wrong key file for the certificate", "Multiple keys exist"],
     ["openssl x509 -noout -modulus -in cert.pem | openssl md5",
      "openssl rsa -noout -modulus -in key.pem | openssl md5"]),

    ("openssl-encrypted-key-no-password", "OpenSSL Encrypted Key No Password Error",
     "Fix OpenSSL encrypted key no password error. Resolve encrypted key passphrase issues.",
     "The private key is encrypted and requires a passphrase to decrypt.",
     ["Key is encrypted with a passphrase", "No password was provided", "Passphrase is wrong"],
     ["openssl rsa -in key.pem -passin pass:mypass"]),

    ("openssl-bad-decrypt", "OpenSSL Bad Decrypt Error",
     "Fix OpenSSL bad decrypt error. Resolve decryption failure issues.",
     "OpenSSL fails to decrypt the data. The password is wrong or the encryption algorithm is wrong.",
     ["Wrong password for encrypted key", "Encryption algorithm does not match", "Data is corrupted"],
     ["openssl rsa -in key.pem -passin pass:mypass -check"]),

    ("openssl-key-file-permission", "OpenSSL Key File Permission Error",
     "Fix OpenSSL key file permission error. Resolve file access permission issues.",
     "The private key file permissions are too open. OpenSSL refuses to read a key with wrong permissions.",
     ["Key file has group or world read permissions", "Key file is owned by wrong user", "SELinux or AppArmor blocks access"],
     ["ls -la /path/to/key.pem",
      "chmod 600 /path/to/key.pem"]),

    ("openssl-rsa-key-error", "OpenSSL RSA Key Error",
     "Fix OpenSSL RSA key error. Resolve RSA key generation or usage issues.",
     "The RSA key operation fails. The key is corrupted, too small, or not RSA format.",
     ["RSA key is corrupted", "RSA key exponent is wrong", "Key is not RSA format"],
     ["openssl rsa -in key.pem -check"]),

    ("openssl-ec-key-error", "OpenSSL EC Key Error",
     "Fix OpenSSL EC key error. Resolve elliptic curve key issues.",
     "The EC key operation fails. The curve is not supported or the key is corrupted.",
     ["Curve is not supported", "EC key is corrupted", "Curve parameters are wrong"],
     ["openssl ec -in ec_key.pem -check",
      "openssl ecparam -list_curves"]),

    ("openssl-dsa-key-error", "OpenSSL DSA Key Error",
     "Fix OpenSSL DSA key error. Resolve DSA key issues.",
     "The DSA key operation fails. DSA is deprecated for TLS use.",
     ["DSA key is corrupted", "DSA is not supported for this operation", "Key parameters are wrong"],
     ["openssl dsa -in dsa_key.pem -check"]),

    ("openssl-dh-key-error", "OpenSSL DH Key Error",
     "Fix OpenSSL DH key error. Resolve Diffie-Hellman key issues.",
     "The DH key operation fails. The DH parameters are weak or the key is corrupted.",
     ["DH parameters are too small", "DH key is corrupted", "DH group is not supported"],
     ["openssl dhparam -in dhparam.pem -check"]),

    ("openssl-ed25519-key-error", "OpenSSL Ed25519 Key Error",
     "Fix OpenSSL Ed25519 key error. Resolve EdDSA key issues.",
     "The Ed25519 key operation fails. The key is corrupted or the operation is not supported.",
     ["Ed25519 key is corrupted", "OpenSSL version does not support Ed25519", "Key format is wrong"],
     ["openssl pkey -in ed25519_key.pem -check"]),

    ("openssl-key-generation-failed", "OpenSSL Key Generation Failed Error",
     "Fix OpenSSL key generation failed error. Resolve key pair generation issues.",
     "OpenSSL fails to generate a new key pair. The entropy source is exhausted or parameters are invalid.",
     ["Entropy source is exhausted", "Key parameters are invalid", "System has insufficient randomness"],
     ["openssl rand -hex 32",
      "openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out key.pem"]),

    ("openssl-key-validation-failed", "OpenSSL Key Validation Failed Error",
     "Fix OpenSSL key validation failed error. Resolve key integrity check issues.",
     "The private key fails validation. The key is corrupted or has invalid parameters.",
     ["Key data is corrupted", "Key has invalid parameters", "Key was truncated during copy"],
     ["openssl rsa -in key.pem -check",
      "openssl pkey -in key.pem -check"]),

    # TLS/SSL connection errors
    ("openssl-ssl-handshake-failure", "OpenSSL SSL Handshake Failure Error",
     "Fix OpenSSL SSL handshake failure error. Resolve TLS handshake issues.",
     "The TLS handshake fails. The client and server cannot agree on protocol version, cipher suite, or certificate.",
     ["Protocol version mismatch", "Cipher suite not supported", "Certificate verification failed"],
     ["openssl s_client -connect host:443 -brief",
      "openssl s_client -connect host:443 -tls1_2"]),

    ("openssl-certificate-verify-failed", "OpenSSL Certificate Verify Failed Error",
     "Fix OpenSSL certificate verify failed error. Resolve certificate chain verification issues.",
     "The certificate chain verification fails. The certificate is not trusted or the chain is broken.",
     ["Certificate is not signed by trusted CA", "Chain is incomplete", "Certificate is expired"],
     ["openssl verify -CAfile ca.pem cert.pem",
      "openssl verify -untrusted intermediate.pem -CAfile root.pem cert.pem"]),

    ("openssl-tls-version-mismatch", "OpenSSL TLS Version Mismatch Error",
     "Fix OpenSSL TLS version mismatch error. Resolve protocol version compatibility issues.",
     "The client and server cannot agree on a TLS protocol version. One side requires a version the other does not support.",
     ["Client only supports old TLS version", "Server requires TLS 1.3", "Protocol negotiation failed"],
     ["openssl s_client -connect host:443 -tls1_2",
      "openssl s_client -connect host:443 -tls1_3"]),

    ("openssl-cipher-suite-not-available", "OpenSSL Cipher Suite Not Available Error",
     "Fix OpenSSL cipher suite not available error. Resolve cipher negotiation issues.",
     "The requested cipher suite is not available. The OpenSSL build does not include the cipher.",
     ["Cipher is not compiled into OpenSSL", "Cipher is disabled by security policy", "FIPS mode restricts ciphers"],
     ["openssl ciphers -v 'ALL' | head -20",
      "openssl ciphers -v 'HIGH:!aNULL:!MD5'"]),

    ("openssl-no-shared-cipher", "OpenSSL No Shared Cipher Error",
     "Fix OpenSSL no shared cipher error. Resolve cipher suite negotiation failure.",
     "The client and server have no cipher suites in common. Neither side can agree on a cipher.",
     ["Client cipher list does not overlap with server", "Server requires specific ciphers client lacks", "FIPS restrictions"],
     ["openssl s_client -connect host:443 -cipher 'ALL'"]),

    ("openssl-ssl-alert", "OpenSSL SSL Alert Error",
     "Fix OpenSSL SSL alert error. Resolve TLS alert message issues.",
     "The TLS connection returns an alert message. The peer is signaling an error condition.",
     ["Peer detected a protocol error", "Certificate is rejected by peer", "Decryption failure on peer"],
     ["openssl s_client -connect host:443 -state"]),

    ("openssl-unexpected-eof", "OpenSSL Unexpected EOF Error",
     "Fix OpenSSL unexpected EOF error. Resolve premature connection closure issues.",
     "The TLS connection is closed unexpectedly. The peer closed the connection without proper shutdown.",
     ["Peer crashed or was killed", "Network issue caused connection drop", "Peer did not send close_notify"],
     ["openssl s_client -connect host:443"]),

    ("openssl-broken-pipe", "OpenSSL Broken Pipe Error",
     "Fix OpenSSL broken pipe error. Resolve connection write failure issues.",
     "Writing to the TLS connection fails because the peer has closed the connection.",
     ["Peer closed connection", "Network issue interrupted write", "Connection was reset by peer"],
     ["openssl s_client -connect host:443"]),

    ("openssl-connection-reset", "OpenSSL Connection Reset Error",
     "Fix OpenSSL connection reset error. Resolve TCP connection reset issues.",
     "The connection is reset by the peer. The TCP connection is forcibly closed.",
     ["Peer reset the connection", "Firewall dropped the connection", "Server crashed during TLS handshake"],
     ["openssl s_client -connect host:443",
      "tcpdump -i any port 443"]),

    ("openssl-sslv3-alert", "OpenSSL SSLv3 Alert Error",
     "Fix OpenSSL SSLv3 alert error. Resolve SSLv3 protocol alert issues.",
     "The connection uses SSLv3 and receives an alert. SSLv3 is deprecated and has known vulnerabilities.",
     ["SSLv3 is enabled but should be disabled", "SSLv3 POODLE vulnerability", "Peer rejects SSLv3"],
     ["openssl s_client -connect host:443 -no_ssl3"]),

    ("openssl-tls-alert-unknown-ca", "OpenSSL TLS Alert Unknown CA Error",
     "Fix OpenSSL TLS alert unknown CA error. Resolve unknown CA certificate issues.",
     "The peer rejects the certificate because the issuing CA is not in its trust store.",
     ["Client does not trust the server CA", "Intermediate CA is not installed", "Self-signed CA is not trusted"],
     ["openssl s_client -connect host:443 -CAfile ca.pem"]),

    ("openssl-self-signed-in-chain", "OpenSSL Self-Signed Cert in Chain Error",
     "Fix OpenSSL self-signed cert in chain error. Resolve self-signed certificate in chain issues.",
     "A self-signed certificate is found in the certificate chain. The chain cannot be verified to a trusted root.",
     ["Self-signed CA is in the chain", "Root certificate is self-signed and not in trust store", "Chain includes untrusted cert"],
     ["openssl verify -CAfile ca.pem cert.pem",
      "openssl s_client -connect host:443 -showcerts"]),

    ("openssl-hostname-mismatch", "OpenSSL Hostname Mismatch Error",
     "Fix OpenSSL hostname mismatch error. Resolve certificate hostname verification issues.",
     "The hostname in the certificate does not match the connected hostname. TLS verification fails.",
     ["Certificate CN does not match hostname", "SAN does not include the hostname", "Wrong certificate installed on server"],
     ["openssl x509 -in cert.pem -noout -text | grep -A1 'Subject Alternative Name'"]),

    ("openssl-ssl-error-syscall", "OpenSSL SSL_ERROR_SYSCALL Error",
     "Fix OpenSSL SSL_ERROR_SYSCALL error. Resolve system call error during TLS operations.",
     "A system call error occurs during TLS operations. The underlying I/O operation failed.",
     ["Network connection was lost", "I/O error on the socket", "Peer reset connection during handshake"],
     ["openssl s_client -connect host:443"]),

    ("openssl-ssl-error-zero-return", "OpenSSL SSL_ERROR_ZERO_RETURN Error",
     "Fix OpenSSL SSL_ERROR_ZERO_RETURN error. Resolve TLS connection closure issues.",
     "The peer has sent a close_notify alert. The TLS connection is being cleanly shut down.",
     ["Peer initiated graceful shutdown", "TLS session is ending normally", "Application should handle closure"],
     ["openssl s_client -connect host:443"]),

    ("openssl-ssl-error-want-read", "OpenSSL SSL_ERROR_WANT_READ Error",
     "Fix OpenSSL SSL_ERROR_WANT_READ error. Resolve non-blocking TLS read issues.",
     "The TLS operation needs to read more data but the socket would block. The operation is non-blocking.",
     ["Non-blocking socket has no data available", "TLS record is incomplete", "Need to retry after data arrives"],
     ["openssl s_client -connect host:443"]),

    ("openssl-ssl-error-want-write", "OpenSSL SSL_ERROR_WANT_WRITE Error",
     "Fix OpenSSL SSL_ERROR_WANT_WRITE error. Resolve non-blocking TLS write issues.",
     "The TLS operation needs to write data but the socket would block. The operation is non-blocking.",
     ["Non-blocking socket send buffer is full", "TLS record cannot be sent", "Need to retry after buffer frees"],
     ["openssl s_client -connect host:443"]),

    ("openssl-sni-mismatch", "OpenSSL SNI Mismatch Error",
     "Fix OpenSSL SNI mismatch error. Resolve Server Name Indication issues.",
     "The SNI hostname does not match the server certificate. The server returns the wrong certificate.",
     ["SNI hostname does not match any certificate on server", "Server does not support SNI", "Default certificate is returned"],
     ["openssl s_client -connect host:443 -servername hostname"]),

    ("openssl-alpn-negotiation", "OpenSSL ALPN Negotiation Error",
     "Fix OpenSSL ALPN negotiation error. Resolve Application-Layer Protocol Negotiation issues.",
     "ALPN negotiation fails. The client and server cannot agree on an application protocol.",
     ["Client ALPN list does not overlap with server", "HTTP/2 is required but not negotiated", "ALPN extension is missing"],
     ["openssl s_client -connect host:443 -alpn h2"]),

    ("openssl-npn-not-supported", "OpenSSL NPN Not Supported Error",
     "Fix OpenSSL NPN not supported error. Resolve Next Protocol Negotiation deprecation issues.",
     "NPN is not supported. NPN has been replaced by ALPN in modern TLS.",
     ["NPN is deprecated and removed", "OpenSSL version does not support NPN", "Server does not support NPN"],
     ["openssl s_client -connect host:443 -alpn h2"]),

    # CSR errors
    ("openssl-unable-to-load-csr", "OpenSSL Unable to Load CSR Error",
     "Fix OpenSSL unable to load CSR error. Resolve CSR loading failures.",
     "OpenSSL cannot load the CSR file. The file path is wrong or the format is unsupported.",
     ["CSR file path is wrong", "File is corrupted", "Format is not PEM or DER"],
     ["openssl req -in csr.pem -noout -text"]),

    ("openssl-csr-request-not-match", "OpenSSL CSR Request Not Match Error",
     "Fix OpenSSL CSR request not match error. Resolve CSR and key matching issues.",
     "The CSR does not match the provided private key. The public key in the CSR does not correspond to the key.",
     ["CSR was generated with a different key", "Wrong key file provided", "CSR was corrupted"],
     ["openssl req -in csr.pem -noout -verify -key key.pem"]),

    ("openssl-csr-subject-missing", "OpenSSL CSR Subject Missing Error",
     "Fix OpenSSL CSR subject missing error. Resolve CSR subject DN issues.",
     "The CSR does not contain a subject distinguished name. The subject is required for certificate issuance.",
     ["Subject was not specified during CSR creation", "CSR subject is empty", "Subject field was malformed"],
     ["openssl req -in csr.pem -noout -subject"]),

    ("openssl-csr-extensions-missing", "OpenSSL CSR Extensions Missing Error",
     "Fix OpenSSL CSR extensions missing error. Resolve CSR extension issues.",
     "The CSR does not contain the required extensions (SAN, key usage, etc.).",
     ["Extensions were not included in CSR config", "SAN was not specified", "Key usage extension is missing"],
     ["openssl req -in csr.pem -noout -text | grep -A1 'Subject Alternative Name'"]),

    ("openssl-csr-attribute-error", "OpenSSL CSR Attribute Error",
     "Fix OpenSSL CSR attribute error. Resolve CSR attribute configuration issues.",
     "The CSR contains invalid or malformed attributes. The attribute format is wrong.",
     ["Attribute format is invalid", "Challenge password attribute is wrong", "Unstructured name is malformed"],
     ["openssl req -in csr.pem -noout -text"]),

    ("openssl-csr-challenge-password", "OpenSSL CSR Challenge Password Error",
     "Fix OpenSSL CSR challenge password error. Resolve CSR challenge password issues.",
     "The CSR challenge password attribute is missing or invalid.",
     ["Challenge password was not set in CSR", "Challenge password is wrong", "CA requires challenge password"],
     ["openssl req -in csr.pem -noout -text"]),

    ("openssl-csr-format-error", "OpenSSL CSR Format Error",
     "Fix OpenSSL CSR format error. Resolve CSR encoding issues.",
     "The CSR file format is not recognized. The file is not in PEM or DER format.",
     ["File is not in recognized format", "File is corrupted", "Wrong format flag"],
     ["openssl req -in csr.pem -noout -text"]),

    ("openssl-csr-signature-invalid", "OpenSSL CSR Signature Invalid Error",
     "Fix OpenSSL CSR signature invalid error. Resolve CSR signature verification issues.",
     "The CSR signature is invalid. The CSR was modified after signing or the key does not match.",
     ["CSR was tampered with after signing", "Key does not match CSR", "CSR is corrupted"],
     ["openssl req -in csr.pem -noout -verify -key key.pem"]),

    ("openssl-csr-public-key", "OpenSSL CSR Public Key Error",
     "Fix OpenSSL CSR public key error. Resolve CSR public key issues.",
     "The public key in the CSR is invalid or has wrong parameters.",
     ["Public key is corrupted", "Key parameters are wrong", "Public key algorithm is unsupported"],
     ["openssl req -in csr.pem -noout -pubkey"]),

    ("openssl-csr-not-signed", "OpenSSL CSR Not Signed Error",
     "Fix OpenSSL CSR not signed error. Resolve unsigned CSR issues.",
     "The CSR is not signed. It was created without a private key or the signing step was skipped.",
     ["CSR was created without -newkey", "CSR signing was skipped", "CSR was generated as unsigned"],
     ["openssl req -in csr.pem -noout -verify"]),

    ("openssl-csr-already-signed", "OpenSSL CSR Already Signed Error",
     "Fix OpenSSL CSR already signed error. Resolve already-signed CSR issues.",
     "The CSR has already been signed. A CSR should only be signed once by the requestor.",
     ["CSR was signed twice", "CSR has a self-signature that is invalid", "CSR was modified after signing"],
     ["openssl req -in csr.pem -noout -verify"]),

    # Hash/encryption errors
    ("openssl-evp-decrypt-final-bad-decrypt", "OpenSSL Bad Decrypt Error",
     "Fix OpenSSL EVP_DecryptFinal_ex bad decrypt error. Resolve decryption failure issues.",
     "The decryption operation fails at the final step. The password is wrong or the data is corrupted.",
     ["Wrong password or key for decryption", "Encrypted data is corrupted", "Cipher or padding is wrong"],
     ["openssl enc -d -aes-256-cbc -in encrypted.bin -out decrypted.bin -pass pass:mypass"]),

    ("openssl-digest-initialization-failed", "OpenSSL Digest Initialization Failed Error",
     "Fix OpenSSL digest initialization failed error. Resolve hash function initialization issues.",
     "The message digest fails to initialize. The digest algorithm is not supported or configured.",
     ["Digest algorithm is not supported", "Digest is not compiled into OpenSSL", "FIPS mode restricts digest"],
     ["openssl dgst -sha256 file.txt"]),

    ("openssl-evp-cipher-error", "OpenSSL EVP_CIPHER Error",
     "Fix OpenSSL EVP_CIPHER error. Resolve cipher operation issues.",
     "The EVP cipher operation fails. The cipher algorithm is not supported or the parameters are wrong.",
     ["Cipher is not supported", "Key length is wrong for the cipher", "IV length is wrong"],
     ["openssl enc -aes-256-cbc -salt -in plain.txt -out encrypted.bin"]),

    ("openssl-unknown-cipher", "OpenSSL Unknown Cipher Error",
     "Fix OpenSSL unknown cipher error. Resolve unrecognized cipher algorithm issues.",
     "The specified cipher algorithm is not recognized. The cipher name is wrong or not compiled in.",
     ["Cipher name is misspelled", "Cipher is not compiled into OpenSSL", "Cipher was removed in newer version"],
     ["openssl ciphers -v 'ALL'"]),

    ("openssl-unsupported-encryption", "OpenSSL Unsupported Encryption Error",
     "Fix OpenSSL unsupported encryption error. Resolve encryption algorithm compatibility issues.",
     "The encryption algorithm is not supported. The algorithm may be deprecated or removed.",
     ["Algorithm is deprecated", "Algorithm requires special build flags", "FIPS mode does not allow algorithm"],
     ["openssl version",
      "openssl list-cipher-algorithms"]),

    ("openssl-key-derivation-fail", "OpenSSL Key Derivation Fail Error",
     "Fix OpenSSL key derivation fail error. Resolve key derivation function issues.",
     "The key derivation function fails. The KDF parameters are wrong or the input is invalid.",
     ["KDF algorithm is not supported", "Salt is missing or wrong", "Iteration count is too low"],
     ["openssl kdf -keylen 32 -out key.bin HKDF -hash SHA256 -salt salt -ikm secret"]),

    ("openssl-pbkdf2-error", "OpenSSL PBKDF2 Error",
     "Fix OpenSSL PBKDF2 error. Resolve PBKDF2 key derivation issues.",
     "The PBKDF2 operation fails. The parameters are invalid or the algorithm is not available.",
     ["Iteration count is too low", "Hash algorithm is not available", "Key length is invalid"],
     ["openssl kdf -keylen 32 -out key.bin PBKDF2 -hash SHA256 -iter 100000 -salt salt -secret password"]),

    ("openssl-bcrypt-error", "OpenSSL Bcrypt Error",
     "Fix OpenSSL bcrypt error. Resolve bcrypt hashing issues.",
     "The bcrypt operation fails. The cost factor is wrong or the input is invalid.",
     ["Cost factor is out of range", "Input is too long", "Bcrypt is not compiled in"],
     ["openssl passwd -6 -salt salt -in password.txt"]),

    ("openssl-scrypt-error", "OpenSSL Scrypt Error",
     "Fix OpenSSL scrypt error. Resolve scrypt key derivation issues.",
     "The scrypt operation fails. The parameters exceed memory or CPU limits.",
     ["N parameter is too large", "r or p parameter is invalid", "Memory requirements exceed available RAM"],
     ["openssl kdf -keylen 64 -out key.bin SCRYPT -N 16384 -r 8 -p 1 -salt salt -secret password"]),

    ("openssl-hmac-error", "OpenSSL HMAC Error",
     "Fix OpenSSL HMAC error. Resolve HMAC computation issues.",
     "The HMAC computation fails. The key or digest algorithm is invalid.",
     ["HMAC key is empty or wrong", "Digest algorithm is not available", "Input is invalid"],
     ["openssl dgst -sha256 -hmac 'key' file.txt"]),

    ("openssl-sha-error", "OpenSSL SHA Error",
     "Fix OpenSSL SHA error. Resolve SHA hash function issues.",
     "The SHA hash operation fails. The digest algorithm is not supported or configured.",
     ["SHA algorithm is not available", "FIPS mode restricts SHA variant", "Input data is invalid"],
     ["openssl dgst -sha256 file.txt"]),

    ("openssl-md5-weak", "OpenSSL MD5 Weak Error",
     "Fix OpenSSL MD5 weak warning. Resolve MD5 deprecation issues.",
     "MD5 is considered weak and may be rejected. MD5 should not be used for security purposes.",
     ["MD5 is cryptographically broken", "MD5 is not allowed by security policy", "MD5 should be replaced with SHA-256"],
     ["openssl dgst -sha256 file.txt"]),

    ("openssl-signature-verification", "OpenSSL Signature Verification Error",
     "Fix OpenSSL signature verification error. Resolve signature check failures.",
     "The signature verification fails. The signature does not match the data or the wrong public key is used.",
     ["Signature does not match the data", "Wrong public key for verification", "Signature algorithm mismatch"],
     ["openssl dgst -sha256 -verify pub.pem -signature sig.bin data.txt"]),

    ("openssl-signing-failed", "OpenSSL Signing Failed Error",
     "Fix OpenSSL signing failed error. Resolve digital signature creation issues.",
     "The signing operation fails. The private key is wrong or the data cannot be signed.",
     ["Private key does not exist", "Key type does not match signing algorithm", "Data is too large to sign"],
     ["openssl dgst -sha256 -sign key.pem -out sig.bin data.txt"]),

    ("openssl-verification-failed", "OpenSSL Verification Failed Error",
     "Fix OpenSSL verification failed error. Resolve signature or certificate verification issues.",
     "The verification operation fails. The data, signature, or certificate is invalid.",
     ["Data has been modified since signing", "Certificate is expired or revoked", "Verification key is wrong"],
     ["openssl verify -CAfile ca.pem cert.pem"]),

    # Random/entropy errors
    ("openssl-unable-to-write-random-state", "OpenSSL Unable to Write Random State Error",
     "Fix OpenSSL unable to write random state error. Resolve random state file issues.",
     "OpenSSL cannot write the random seed file. The file is not writable or the disk is full.",
     ["Random state file is not writable", "Disk is full", "File permissions prevent write"],
     ["openssl rand -hex 32"]),

    ("openssl-prng-not-seeded", "OpenSSL PRNG Not Seeded Error",
     "Fix OpenSSL PRNG not seeded error. Resolve random number generator seeding issues.",
     "The PRNG is not seeded. OpenSSL cannot generate random numbers.",
     ["Entropy source is not available", "/dev/urandom is not accessible", "RAND_seed was not called"],
     ["openssl rand -hex 32",
      "ls -la /dev/urandom"]),

    ("openssl-entropy-exhausted", "OpenSSL Entropy Exhausted Error",
     "Fix OpenSSL entropy exhausted error. Resolve entropy pool exhaustion issues.",
     "The entropy pool is exhausted. OpenSSL cannot gather enough randomness.",
     ["System entropy pool is depleted", "Too many concurrent random operations", "Virtual machine has low entropy"],
     ["cat /proc/sys/kernel/random/entropy_avail",
      "haveged -n 1000 -o /dev/null"]),

    ("openssl-dev-urandom-not-available", "OpenSSL /dev/urandom Not Available Error",
     "Fix OpenSSL /dev/urandom not available error. Resolve random device issues.",
     "/dev/urandom is not available on the system. OpenSSL cannot read random data.",
     ["/dev/urandom does not exist", "Device permissions are wrong", "Kernel does not provide /dev/urandom"],
     ["ls -la /dev/urandom",
      "mknod /dev/urandom c 1 9"]),

    ("openssl-random-number-generation", "OpenSSL Random Number Generation Error",
     "Fix OpenSSL random number generation error. Resolve RNG issues.",
     "Random number generation fails. The RNG cannot produce random output.",
     ["RNG is not properly seeded", "Entropy source is not available", "RNG algorithm is not supported"],
     ["openssl rand -hex 32",
      "openssl rand -engine /dev/urandom 32"]),

    ("openssl-rand-bytes-failed", "OpenSSL RAND_bytes Failed Error",
     "Fix OpenSSL RAND_bytes failed error. Resolve random byte generation issues.",
     "The RAND_bytes function fails. OpenSSL cannot generate random bytes.",
     ["Entropy source is unavailable", "FIPS mode restrictions", "System has no entropy"],
     ["openssl rand 32 -out random.bin"]),

    ("openssl-seeding-file-error", "OpenSSL Seeding File Error",
     "Fix OpenSSL seeding file error. Resolve seed file issues.",
     "The seed file cannot be read or is corrupted. OpenSSL cannot reseed from the file.",
     ["Seed file is corrupted", "Seed file path is wrong", "Seed file is not readable"],
     ["openssl rand -hex 32 -out seed.bin"]),

    ("openssl-random-pool-error", "OpenSSL Random Pool Error",
     "Fix OpenSSL random pool error. Resolve random pool configuration issues.",
     "The random pool is not properly configured. The pool size or method is wrong.",
     ["Pool method is not available", "Pool size is too small", "Pool is not initialized"],
     ["openssl rand -hex 32"]),

    # S/MIME errors
    ("openssl-smime-read-failed", "OpenSSL S/MIME Read Failed Error",
     "Fix OpenSSL S/MIME read failed error. Resolve S/MIME parsing issues.",
     "OpenSSL cannot read the S/MIME message. The message format is wrong or corrupted.",
     ["S/MIME message is corrupted", "MIME headers are wrong", "Message is truncated"],
     ["openssl smime -verify -in smime.pem -CAfile ca.pem"]),

    ("openssl-pkcs7-parse-error", "OpenSSL PKCS7 Parse Error",
     "Fix OpenSSL PKCS7 parse error. Resolve PKCS7 data parsing issues.",
     "OpenSSL cannot parse the PKCS7 data. The data is corrupted or the format is wrong.",
     ["PKCS7 data is corrupted", "Format is not PKCS7", "DER encoding is wrong"],
     ["openssl pkcs7 -in pkcs7.pem -print_certs -text"]),

    ("openssl-pkcs12-parse-error", "OpenSSL PKCS12 Parse Error",
     "Fix OpenSSL PKCS12 parse error. Resolve PKCS12/PFX parsing issues.",
     "OpenSSL cannot parse the PKCS12 file. The file is corrupted or the password is wrong.",
     ["PKCS12 file is corrupted", "Password is wrong", "PKCS12 version is unsupported"],
     ["openssl pkcs12 -in bundle.pfx -noout -info"]),

    ("openssl-pkcs12-key-not-match", "OpenSSL PKCS12 Key Not Match Error",
     "Fix OpenSSL PKCS12 key not match error. Resolve PKCS12 bundle key issues.",
     "The private key inside the PKCS12 bundle does not match the certificate.",
     ["Key and cert were different when bundled", "PKCS12 was created with wrong key", "Bundle is corrupted"],
     ["openssl pkcs12 -in bundle.pfx -noout -info"]),

    ("openssl-cms-error", "OpenSSL CMS Error",
     "Fix OpenSSL CMS error. Resolve Cryptographic Message Syntax issues.",
     "The CMS operation fails. The data is corrupted or the algorithm is not supported.",
     ["CMS data is corrupted", "Signing algorithm is not supported", "Certificate is not in CMS bundle"],
     ["openssl cms -verify -in cms.pem -CAfile ca.pem -out content.txt"]),

    ("openssl-der-decode-smime", "OpenSSL DER Decode S/MIME Error",
     "Fix OpenSSL DER decode S/MIME error. Resolve DER encoding issues in S/MIME.",
     "The DER decoding of the S/MIME message fails. The encoding is wrong.",
     ["DER encoding is corrupted", "Format is not DER", "Data is truncated"],
     ["openssl asn1parse -in smime.der -inform DER"]),

    ("openssl-pem-to-pkcs7", "OpenSSL PEM to PKCS7 Error",
     "Fix OpenSSL PEM to PKCS7 conversion error. Resolve format conversion issues.",
     "Converting a PEM certificate to PKCS7 format fails.",
     ["PEM file is corrupted", "Certificate chain is incomplete", "Output format is wrong"],
     ["openssl pkcs7 -inform PEM -in cert.pem -outform DER -out cert.p7b"]),

    ("openssl-encrypted-email-error", "OpenSSL Encrypted Email Error",
     "Fix OpenSSL encrypted email error. Resolve S/MIME email encryption issues.",
     "The encrypted email cannot be decrypted. The recipient key is wrong or the message is corrupted.",
     ["Wrong private key for decryption", "Email message is corrupted", "Encryption certificate is expired"],
     ["openssl smime -decrypt -in encrypted.pem -inkey key.pem -recip cert.pem"]),

    ("openssl-digital-signature-email", "OpenSSL Digital Signature in Email Error",
     "Fix OpenSSL digital signature in email error. Resolve S/MIME email signature issues.",
     "The digital signature on the email cannot be verified. The signer certificate is not trusted.",
     ["Signer certificate is not trusted", "Signature is corrupted", "Signer certificate is expired"],
     ["openssl smime -verify -in signed.pem -CAfile ca.pem"]),

    ("openssl-certificate-attachment", "OpenSSL Certificate Attachment Error",
     "Fix OpenSSL certificate attachment error. Resolve certificate in email attachment issues.",
     "The certificate attachment in the S/MIME message is invalid or missing.",
     ["Certificate attachment is missing", "Certificate is corrupted", "Attachment format is wrong"],
     ["openssl smime -verify -in smime.pem -CAfile ca.pem"]),

    # CRL/OCSP errors
    ("openssl-unable-to-load-crl", "OpenSSL Unable to Load CRL Error",
     "Fix OpenSSL unable to load CRL error. Resolve CRL loading issues.",
     "OpenSSL cannot load the Certificate Revocation List. The file is wrong or corrupted.",
     ["CRL file path is wrong", "CRL file is corrupted", "Format is not PEM or DER"],
     ["openssl crl -in ca.crl -noout -text"]),

    ("openssl-crl-expired", "OpenSSL CRL Expired Error",
     "Fix OpenSSL CRL expired error. Resolve CRL expiration issues.",
     "The Certificate Revocation List has expired. Revocation checking is unreliable.",
     ["CRL nextUpdate has passed", "CRL was not refreshed by CA", "CA is not publishing new CRLs"],
     ["openssl crl -in ca.crl -noout -lastupdate -nextupdate"]),

    ("openssl-crl-next-update", "OpenSSL CRL Next Update Error",
     "Fix OpenSSL CRL next update error. Resolve CRL refresh issues.",
     "The CRL nextUpdate field indicates a new CRL should have been published but was not.",
     ["CA is not publishing new CRLs on schedule", "CRL distribution point is down", "CRL refresh job failed"],
     ["openssl crl -in ca.crl -noout -nextupdate"]),

    ("openssl-ocsp-response-verify", "OpenSSL OCSP Response Verify Error",
     "Fix OpenSSL OCSP response verify error. Resolve OCSP response verification issues.",
     "The OCSP response verification fails. The response is signed by an unknown or untrusted signer.",
     ["OCSP response signer is not trusted", "Response signature is invalid", "Response is corrupted"],
     ["openssl ocsp -issuer ca.pem -cert cert.pem -url http://ocsp.example.com -resp_text"]),

    ("openssl-ocsp-status-unknown", "OpenSSL OCSP Status Unknown Error",
     "Fix OpenSSL OCSP status unknown error. Resolve OCSP responder issues.",
     "The OCSP responder returns an unknown status. The certificate serial number is not in the response.",
     ["Certificate is not in OCSP database", "OCSP responder is misconfigured", "Serial number format is wrong"],
     ["openssl ocsp -issuer ca.pem -cert cert.pem -url http://ocsp.example.com"]),

    ("openssl-ocsp-nonce-mismatch", "OpenSSL OCSP Nonce Mismatch Error",
     "Fix OpenSSL OCSP nonce mismatch error. Resolve OCSP nonce verification issues.",
     "The OCSP response nonce does not match the request nonce. Replay attack protection triggered.",
     ["Nonce in response does not match request", "OCSP proxy modified nonce", "Replay attack detected"],
     ["openssl ocsp -issuer ca.pem -cert cert.pem -url http://ocsp.example.com -nonce"]),

    ("openssl-ocsp-must-staple", "OpenSSL OCSP Must-Staple Error",
     "Fix OpenSSL OCSP must-staple error. Resolve OCSP stapling requirement issues.",
     "The certificate requires OCSP stapling but the server does not provide it.",
     ["Certificate has must-staple extension", "Server does not staple OCSP response", "OCSP stapling is not configured"],
     ["openssl s_client -connect host:443 -status"]),

    ("openssl-ocsp-response-expired", "OpenSSL OCSP Response Expired Error",
     "Fix OpenSSL OCSP response expired error. Resolve OCSP response freshness issues.",
     "The OCSP response has expired. The response thisUpdate is too old.",
     ["OCSP response was cached too long", "OCSP responder produces infrequent updates", "Response validity period is short"],
     ["openssl ocsp -issuer ca.pem -cert cert.pem -url http://ocsp.example.com"]),

    ("openssl-ocsp-responder-uri", "OpenSSL OCSP Responder URI Error",
     "Fix OpenSSL OCSP responder URI error. Resolve OCSP responder configuration issues.",
     "The OCSP responder URI is not accessible or is wrong.",
     ["OCSP responder URL is wrong", "OCSP responder is down", "Network issue accessing responder"],
     ["openssl x509 -in cert.pem -noout -ocsp_uri"]),

    ("openssl-ocsp-signing-cert", "OpenSSL OCSP Signing Cert Error",
     "Fix OpenSSL OCSP signing cert error. Resolve OCSP signer certificate issues.",
     "The OCSP signing certificate is invalid or not authorized to sign OCSP responses.",
     ["OCSP signing cert is expired", "Signing cert is not authorized", "Signing cert chain is broken"],
     ["openssl x509 -in ocsp_signer.pem -noout -purpose"]),

    # CA/configuration errors
    ("openssl-ca-config-not-found", "OpenSSL CA Config Not Found Error",
     "Fix OpenSSL CA config not found error. Resolve CA configuration file issues.",
     "The CA configuration file does not exist at the specified path.",
     ["Config file path is wrong", "Config file was deleted", "Config file was never created"],
     ["ls -la /path/to/openssl.cnf",
      "find /etc -name 'openssl.cnf'"]),

    ("openssl-ca-section-missing", "OpenSSL CA Section Missing Error",
     "Fix OpenSSL CA section missing error. Resolve CA section configuration issues.",
     "The [CA_default] or [CA] section is missing from the OpenSSL configuration file.",
     ["[CA_default] section is missing", "Section name is misspelled", "Config file is incomplete"],
     ["grep '\\[CA_default\\]' /etc/ssl/openssl.cnf"]),

    ("openssl-ca-database-error", "OpenSSL CA Database Error",
     "Fix OpenSSL CA database error. Resolve CA serial and index issues.",
     "The CA database (index.txt) is corrupted or missing. The CA cannot track issued certificates.",
     ["index.txt is missing or corrupted", "serial file is missing", "new_certs_dir does not exist"],
     ["ls -la /etc/ssl/ca/",
      "cat /etc/ssl/ca/index.txt"]),

    ("openssl-ca-serial-file", "OpenSSL CA Serial File Error",
     "Fix OpenSSL CA serial file error. Resolve CA serial number issues.",
     "The CA serial number file is missing or empty. New certificates cannot be issued.",
     ["serial file is missing", "serial file is empty", "serial counter is wrong"],
     ["cat /etc/ssl/ca/serial"]),

    ("openssl-ca-new-certs-dir", "OpenSSL CA New Certs Dir Error",
     "Fix OpenSSL CA new certs dir error. Resolve CA output directory issues.",
     "The new_certs_dir does not exist or is not writable. Issued certificates cannot be stored.",
     ["new_certs_dir does not exist", "Directory is not writable", "Directory is full"],
     ["ls -la /etc/ssl/ca/newcerts/"]),

    ("openssl-ca-index-txt-corrupt", "OpenSSL CA Index.txt Corrupt Error",
     "Fix OpenSSL CA index.txt corrupt error. Resolve CA database corruption issues.",
     "The CA index.txt file is corrupted. The database entries are malformed.",
     ["Index.txt has malformed entries", "File was edited incorrectly", "File encoding is wrong"],
     ["cat /etc/ssl/ca/index.txt"]),

    ("openssl-ca-policy-mismatch", "OpenSSL CA Policy Mismatch Error",
     "Fix OpenSSL CA policy mismatch error. Resolve CA policy configuration issues.",
     "The CA policy does not match the certificate request. The policy requires fields not in the CSR.",
     ["CSR does not include required fields", "Policy requires specific O or OU", "Policy is too restrictive"],
     ["grep -A5 'policy' /etc/ssl/openssl.cnf"]),

    ("openssl-ca-extensions-not-found", "OpenSSL CA Extensions Not Found Error",
     "Fix OpenSSL CA extensions not found error. Resolve CA extension configuration issues.",
     "The x509 extensions section referenced by the CA is missing from the config.",
     ["x509_extensions section is missing", "Section name is misspelled", "Config file is incomplete"],
     ["grep 'x509_extensions' /etc/ssl/openssl.cnf"]),

    ("openssl-ca-name-mismatch", "OpenSSL CA Name Mismatch Error",
     "Fix OpenSSL CA name mismatch error. Resolve CA distinguished name issues.",
     "The CA name does not match the expected CA distinguished name.",
     ["CA subject DN does not match", "CA certificate subject is wrong", "Multiple CAs in config"],
     ["openssl x509 -in ca.pem -noout -subject"]),

    ("openssl-ca-default-file", "OpenSSL CA Default File Error",
     "Fix OpenSSL CA default file error. Resolve CA default configuration issues.",
     "The CA default configuration file is missing or has wrong settings.",
     ["Default config file is missing", "Default settings are wrong", "Config file path is wrong"],
     ["ls -la /etc/ssl/openssl.cnf"]),

    ("openssl-ca-unique-subject", "OpenSSL CA Unique Subject Error",
     "Fix OpenSSL CA unique subject error. Resolve duplicate certificate subject issues.",
     "The CA rejects the certificate because the subject already exists and unique_subject is set.",
     ["Subject already exists in CA database", "unique_subject = yes in config", "Certificate was already issued"],
     ["cat /etc/ssl/ca/index.txt | grep '/CN=myhost'"]),

    # Engine/pkcs11 errors
    ("openssl-engine-not-loaded", "OpenSSL Engine Not Loaded Error",
     "Fix OpenSSL engine not loaded error. Resolve engine loading issues.",
     "The OpenSSL engine cannot be loaded. The engine shared library is missing or incompatible.",
     ["Engine .so file is not found", "Engine version is incompatible", "Engine has dependency issues"],
     ["openssl engine -t",
      "ls /usr/lib/ssl/engines/"]),

    ("openssl-pkcs11-engine-error", "OpenSSL PKCS11 Engine Error",
     "Fix OpenSSL PKCS11 engine error. Resolve PKCS#11 engine issues.",
     "The PKCS11 engine fails to initialize or operate. The engine or PKCS#11 module is not working.",
     ["PKCS11 engine is not loaded", "PKCS#11 module path is wrong", "Engine configuration is wrong"],
     ["openssl engine -t pkcs11"]),

    ("openssl-smart-card-not-found", "OpenSSL Smart Card Not Found Error",
     "Fix OpenSSL smart card not found error. Resolve smart card reader issues.",
     "The smart card or token is not detected. The reader is not connected or the token is not inserted.",
     ["Smart card reader is not connected", "Token is not inserted", "pcscd service is not running"],
     ["pcsc_scan",
      "pkcs11-tool --list-slots"]),

    ("openssl-hsm-connection", "OpenSSL HSM Connection Error",
     "Fix OpenSSL HSM connection error. Resolve Hardware Security Module issues.",
     "The connection to the HSM fails. The HSM is not accessible or the credentials are wrong.",
     ["HSM is not accessible over network", "PKCS#11 library path is wrong", "HSM login credentials are wrong"],
     ["pkcs11-tool --list-slots --module /path/to/pkcs11.so"]),

    ("openssl-token-not-present", "OpenSSL Token Not Present Error",
     "Fix OpenSSL token not present error. Resolve PKCS#11 token detection issues.",
     "The PKCS#11 token is not present. The token was removed or the slot is not available.",
     ["Token was removed from reader", "Slot does not contain a token", "Token is locked"],
     ["pkcs11-tool --list-slots --module /path/to/pkcs11.so"]),

    ("openssl-slot-not-available", "OpenSSL Slot Not Available Error",
     "Fix OpenSSL slot not available error. Resolve PKCS#11 slot issues.",
     "The PKCS#11 slot is not available. The reader or slot index is wrong.",
     ["Slot index is out of range", "Reader is not connected", "No slots are available"],
     ["pkcs11-tool --list-slots --module /path/to/pkcs11.so"]),

    ("openssl-pkcs11-login", "OpenSSL PKCS11 Login Error",
     "Fix OpenSSL PKCS11 login error. Resolve PKCS#11 authentication issues.",
     "The PKCS#11 login fails. The PIN is wrong or the token is locked.",
     ["PIN is wrong", "Token is locked after too many attempts", "Login type is wrong"],
     ["pkcs11-tool --login --module /path/to/pkcs11.so --list-slots"]),

    ("openssl-pkcs11-sign", "OpenSSL PKCS11 Sign Error",
     "Fix OpenSSL PKCS11 sign error. Resolve PKCS#11 signing issues.",
     "The PKCS#11 signing operation fails. The key is not on the token or the mechanism is unsupported.",
     ["Key is not on the token", "Mechanism is not supported", "Token is not logged in"],
     ["pkcs11-tool --module /path/to/pkcs11.so --list-objects --type privkey"]),

    ("openssl-key-not-on-token", "OpenSSL Key Not On Token Error",
     "Fix OpenSSL key not on token error. Resolve PKCS#11 key storage issues.",
     "The private key is not found on the PKCS#11 token.",
     ["Key was never generated on token", "Key was deleted", "Wrong slot is being used"],
     ["pkcs11-tool --module /path/to/pkcs11.so --list-objects --type privkey"]),

    ("openssl-cert-not-on-token", "OpenSSL Cert Not On Token Error",
     "Fix OpenSSL cert not on token error. Resolve PKCS#11 certificate storage issues.",
     "The certificate is not found on the PKCS#11 token.",
     ["Certificate was never stored on token", "Certificate was deleted", "Wrong slot is being used"],
     ["pkcs11-tool --module /path/to/pkcs11.so --list-objects --type cert"]),
]

def make_page(slug, title, desc, body, causes, fixes, examples):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["openssl"]',
        'error-types: ["tool-error"]',
        'severities: ["error"]',
        '---',
        '',
        f'# {title}',
        '',
        body,
        '',
        '## Common Causes',
        '',
    ]
    for c in causes:
        lines.append(f'- {c}')
    lines.append('')
    lines.append('## How to Fix')
    lines.append('')
    for i, fix in enumerate(fixes, 1):
        lines.append(f'### Solution {i}')
        lines.append('')
        lines.append('```bash')
        lines.append(fix)
        lines.append('```')
        lines.append('')
    if examples:
        lines.append('## Examples')
        lines.append('')
        for ex in examples:
            lines.append('```bash')
            lines.append(ex)
            lines.append('```')
            lines.append('')
    related = [
        '- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})',
        '- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})',
        '- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})',
    ]
    lines.append('## Related Pages')
    lines.append('')
    lines.extend(related)
    lines.append('')
    return '\n'.join(lines)


count = 0
skipped = 0
for page in PAGES:
    slug, title, desc, body, causes, fixes = page[:6]
    examples = page[6] if len(page) > 6 else []
    if slug in EXISTING:
        print(f"SKIP (exists): {slug}")
        skipped += 1
        continue
    content = make_page(slug, title, desc, body, causes, fixes, examples)
    path = os.path.join(TOOL_DIR, f'{slug}.md')
    with open(path, 'w') as f:
        f.write(content)
    count += 1
    print(f"CREATED: {slug}")

print(f"\nTotal created: {count}")
print(f"Total skipped (existing): {skipped}")
total = len([f for f in os.listdir(TOOL_DIR) if f.endswith('.md')])
print(f"Total .md files in openssl/: {total}")
