#!/usr/bin/env python3
"""Generate Ansible error pages programmatically."""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/ansible'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}


def make_page(title, desc, body):
    return '\n'.join([
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["ansible"]',
        'error-types: ["tool-error"]',
        'severities: ["error"]',
        '---',
        '',
        body,
    ])


def body_template(error_name, error_desc, example_error, causes, fix_code, extra_sections=""):
    causes_md = '\n'.join(f'- {c}' for c in causes)
    parts = [
        f'## Error Description\n\n{error_desc}\n\n```\n{example_error}\n```\n',
        f'## Common Causes\n\n{causes_md}\n',
        f'## How to Fix\n\n{fix_code}\n',
    ]
    if extra_sections:
        parts.append(extra_sections)
    return '\n'.join(parts)


# Define all pages: (slug, title, desc, body)
PAGES = []

# ====== 1. CONNECTION ERRORS ======

PAGES.append(('ansible-connection-timeout', 'Ansible Connection Timeout',
    'Diagnose and fix Ansible SSH connection timeout errors',
    body_template('Ansible Connection Timeout',
        'Ansible connection timeout occurs when the controller cannot establish a connection to the managed host within the configured time limit.',
        'UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh: Connection timed out"}',
        ['Host is down or not reachable on the network',
         'Firewall blocking SSH port (default 22)',
         'Incorrect host IP address or DNS name',
         'SSH service not running on remote host',
         'Network latency too high'],
        """```yaml\n# In inventory\n[all]\nwebserver ansible_host=192.168.1.100 ansible_timeout=30\n\n# In ansible.cfg\n[defaults]\ntimeout = 30\n\n# In playbook\n- hosts: all\n  gather_facts: false\n  vars:\n    ansible_timeout: 60\n  tasks:\n    - name: Ping test\n      ansible.builtin.ping:\n```""")))

PAGES.append(('ansible-authentication-failed', 'Ansible SSH Authentication Failed',
    'Fix Ansible SSH authentication failures when connecting to managed nodes',
    body_template('Ansible SSH Authentication Failed',
        'Ansible cannot authenticate to the remote host using the provided credentials or SSH key.',
        'UNREACHABLE! => {"msg": "Permission denied (publickey,password)"}',
        ['Incorrect SSH username',
         'Password mismatch or not provided',
         'SSH key not added to remote host',
         'Key file permissions too open',
         'Remote host password authentication disabled'],
        """```yaml\n# Inventory with explicit credentials\n[webservers]\nweb1 ansible_host=192.168.1.100 ansible_user=admin ansible_ssh_private_key_file=~/.ssh/id_rsa\n\n- hosts: webservers\n  gather_facts: false\n  tasks:\n    - name: Test connection\n      ansible.builtin.ping:\n      vars:\n        ansible_user: admin\n        ansible_password: "{{ vault_ssh_password }}"\n```""")))

PAGES.append(('ansible-ssh-protocol-error', 'Ansible SSH Protocol Error',
    'Resolve SSH protocol version mismatch errors in Ansible connections',
    body_template('Ansible SSH Protocol Error',
        'Ansible encounters an SSH protocol error during connection negotiation.',
        'UNREACHABLE! => {"msg": "ssh_dispatch_runssh: SSH protocol error"}',
        ['Remote host SSH daemon using incompatible protocol version',
         'SSH client and server algorithm mismatch',
         'Corrupted SSH session',
         'Network middlebox interference'],
        """```ini\n# ansible.cfg\n[ssh_connection]\nssh_args = -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no\npipelining = True\n```""")))

PAGES.append(('ansible-invalid-ssh-key', 'Ansible Invalid SSH Key',
    'Fix Ansible errors caused by invalid or corrupted SSH private keys',
    body_template('Ansible Invalid SSH Key',
        'Ansible cannot use the provided SSH key for authentication.',
        'Permissions 0644 for /home/admin/.ssh/id_rsa are too open.',
        ['SSH key file permissions too open',
         'Corrupted private key file',
         'Wrong key format',
         'Key passphrase not provided'],
        """```bash\n# Fix key permissions\nchmod 600 ~/.ssh/id_rsa\nchmod 644 ~/.ssh/id_rsa.pub\n\n# Verify key integrity\nssh-keygen -l -f ~/.ssh/id_rsa\n\n# Generate a new key pair\nssh-keygen -t ed25519 -C \\"ansible-deploy\\" -f ~/.ssh/ansible_deploy -N \\"\\"\nssh-copy-id -i ~/.ssh/ansible_deploy.pub admin@192.168.1.100\n```""")))

PAGES.append(('ansible-winrm-connection-failed', 'Ansible WinRM Connection Failed',
    'Troubleshoot and fix WinRM connection failures for Windows hosts',
    body_template('Ansible WinRM Connection Failed',
        'Ansible cannot establish a WinRM connection to a Windows managed host.',
        'UNREACHABLE! => {"msg": "winrm connection error: An existing connection was forcibly closed"}',
        ['WinRM not enabled on Windows host',
         'WinRM listener not configured for HTTPS',
         'Certificate issues',
         'Firewall blocking WinRM ports (5985/5986)',
         'Authentication method mismatch'],
        """```powershell\n# Run on Windows host as Administrator\nEnable-PSRemoting -Force\nSet-Item WSMan:\\\\localhost\\\\Service\\\\Auth\\\\Basic -Value $true\nwinrm set winrm/config/service '@{MaxConcurrentOperationsPerUser="5000"}'\n```\n\n```yaml\n# Inventory for Windows\n[win]\nwinserver ansible_host=10.0.0.50 ansible_port=5986 ansible_connection=winrm ansible_winrm_transport=basic\n```""")))

PAGES.append(('ansible-winrm-timeout', 'Ansible WinRM Connection Timeout',
    'Fix WinRM timeout issues when managing Windows hosts with Ansible',
    body_template('Ansible WinRM Connection Timeout',
        'WinRM connection times out when Ansible tries to execute commands on Windows hosts.',
        'FAILED! => {"msg": "winrm connection error: timed out"}',
        ['WinRM operation timeout too low',
         'Large data transfer over WinRM',
         'Windows host overloaded',
         'Network latency between controller and Windows host'],
        """```ini\n# ansible.cfg\n[winrm]\noperation_timeout_sec = 60\nread_timeout_sec = 60\n```\n\n```yaml\n# Per-host timeout settings\n[win]\nwinserver ansible_host=10.0.0.50 ansible_winrm_operation_timeout_sec=120\n```""")))

PAGES.append(('ansible-winrm-certificate-error', 'Ansible WinRM Certificate Error',
    'Resolve WinRM SSL certificate validation errors in Ansible',
    body_template('Ansible WinRM Certificate Error',
        'Ansible fails to connect via WinRM due to SSL certificate validation issues.',
        'UNREACHABLE! => SSLError: certificate verify failed',
        ['Self-signed certificate on Windows host',
         'Certificate not trusted by Ansible controller',
         'Certificate hostname mismatch',
         'WinRM HTTPS listener misconfigured'],
        """```ini\n# ansible.cfg (testing only)\n[winrm]\nserver_cert_validation = ignore\n```\n\n```yaml\n# Production with proper certificates\n- hosts: win\n  vars:\n    ansible_winrm_transport: certificate\n    ansible_winrm_cert_pem: /etc/ansible/certs/client.pem\n    ansible_winrm_cert_key_pem: /etc/ansible/certs/client-key.pem\n    ansible_winrm_server_cert_validation: validate\n    ansible_winrm_ca_trust_path: /etc/ansible/certs/ca.pem\n```""")))

PAGES.append(('ansible-winrm-basic-auth-disabled', 'Ansible WinRM Basic Auth Disabled',
    'Enable basic authentication for WinRM in Ansible Windows management',
    body_template('Ansible WinRM Basic Auth Disabled',
        'WinRM connection fails because basic authentication is not enabled on the Windows host.',
        'UNREACHABLE! => "Basic auth is not enabled or supported by the server"',
        ['Basic authentication disabled in WinRM configuration',
         'Group policy restricting auth methods',
         'WinRM service configuration does not allow basic auth'],
        """```powershell\n# On Windows host (run as Administrator)\nwinrm set winrm/config/service/auth '@{Basic="true"}'\nwinrm set winrm/config/service '@{AllowUnencrypted="true"}'\nwinrm get winrm/config/service/auth\n```""")))

PAGES.append(('ansible-winrm-negotiate-error', 'Ansible WinRM Negotiate Auth Error',
    'Fix WinRM negotiate authentication errors in Ansible Windows playbooks',
    body_template('Ansible WinRM Negotiate Auth Error',
        'Ansible WinRM connection fails with negotiate authentication errors.',
        'UNREACHABLE! => "winrm connection error: negotiate auth failed"',
        ['Kerberos not configured on Ansible controller',
         'SPN (Service Principal Name) not set',
         'Time synchronization issues',
         'NTLM authentication not enabled'],
        """```yaml\n# Use NTLM instead of Kerberos\n[win]\nwinserver ansible_connection=winrm ansible_winrm_transport=ntlm ansible_user=administrator\n```\n\n```bash\n# Or install Kerberos\nsudo apt-get install python3-winrm python3-requests-kerberos krb5-user\n```""")))

PAGES.append(('ansible-local-connection-error', 'Ansible Local Connection Error',
    'Fix Ansible local connection plugin errors and issues',
    body_template('Ansible Local Connection Error',
        'Ansible fails to execute tasks using the local connection plugin.',
        "ERROR! [Exception]: AnsibleError('Unexpected failure during module execution.')",
        ['Missing local connection plugin',
         'Incorrect connection type specification',
         'Python interpreter mismatch',
         'Module not available on Ansible controller'],
        """```yaml\n- hosts: localhost\n  connection: local\n  gather_facts: false\n  tasks:\n    - name: Run local command\n      ansible.builtin.command: echo \\"hello\\"\n      delegate_to: localhost\n```\n\n```ini\n# ansible.cfg\n[defaults]\nconnection = local\n```""")))

PAGES.append(('ansible-docker-connection-error', 'Ansible Docker Connection Error',
    'Resolve Ansible Docker connection plugin errors when managing containers',
    body_template('Ansible Docker Connection Error',
        'Ansible cannot connect to Docker daemon or containers using the Docker connection plugin.',
        'FAILED! => "docker connection plugin failed to connect: Cannot connect to Docker daemon"',
        ['Docker daemon not running',
         'Current user not in docker group',
         'Docker socket permissions wrong',
         'Docker connection plugin not installed'],
        """```bash\nsudo systemctl start docker\nsudo usermod -aG docker $USER\nnewgrp docker\nls -la /var/run/docker.sock\n```\n\n```yaml\n[containers]\ncontainer1 ansible_connection=docker\n```""")))

PAGES.append(('ansible-network-unreachable', 'Ansible Network Unreachable Error',
    'Fix Ansible network unreachable errors when target hosts are not accessible',
    body_template('Ansible Network Unreachable Error',
        'Ansible cannot reach the target host due to network-level issues.',
        'UNREACHABLE! => "ssh: connect to host 10.0.50.10 port 22: Network is unreachable"',
        ['No route to target network',
         'VPN not connected',
         'Network interface down',
         'Routing table misconfigured',
         'Gateway unreachable'],
        """```yaml\n# Use jump host\n[proxy]\nbastion ansible_host=203.0.113.50\n\n[targets]\ntarget1 ansible_host=10.0.50.10 ansible_ssh_common_args='-o ProxyJump=admin@203.0.113.50'\n```\n\n```bash\nping -c 3 10.0.50.10\nip route show\n```""")))

PAGES.append(('ansible-proxy-connection-failed', 'Ansible Proxy Connection Failed',
    'Fix Ansible connection failures when using HTTP or SOCKS proxies',
    body_template('Ansible Proxy Connection Failed',
        'Ansible cannot establish connections through a proxy server.',
        'FAILED! => "Connection timed out through proxy"',
        ['Proxy settings not configured',
         'Proxy authentication required',
         'Proxy does not support SSH tunneling',
         'NO_PROXY not set for internal hosts'],
        """```bash\nexport http_proxy=http://proxy.example.com:8080\nexport https_proxy=http://proxy.example.com:8080\nexport no_proxy=localhost,127.0.0.1,192.168.1.0/24\n```\n\n```yaml\n[all:vars]\nansible_ssh_common_args='-o ProxyJump=admin@bastion.example.com'\n```""")))

PAGES.append(('ansible-become-password-required', 'Ansible Become Password Required',
    'Fix Ansible privilege escalation password prompts during playbook execution',
    body_template('Ansible Become Password Required',
        'Ansible prompts for a become (sudo) password during execution, causing the playbook to hang or fail.',
        'BECOME-password:\\nfatal: [web1]: FAILED! => {"msg": "Incorrect become password"}',
         ['Become password not configured in inventory',
          'sudo requires TTY but none allocated',
          'sudo NOPASSWD not configured',
          'vault password not provided'],
        """```yaml\n[all:vars]\nansible_become=true\nansible_become_method=sudo\nansible_become_user=root\nansible_become_password="{{ vault_sudo_password }}"\n```\n\n```bash\necho \\"ansible ALL=(ALL) NOPASSWD: ALL\\" | sudo tee /etc/sudoers.d/ansible\n```""")))

# ====== 2. PLAYBOOK ERRORS ======

PAGES.append(('ansible-missing-hosts-directive', 'Ansible Missing Hosts Directive',
    'Fix Ansible playbooks that are missing the required hosts directive',
    body_template('Ansible Missing Hosts Directive',
        'Ansible playbook fails because the hosts directive is missing from a play.',
        'ERROR! playbooks must include a list of hosts',
        ['Typo in play structure',
         'hosts key omitted entirely',
         'Empty hosts value'],
        """```yaml\n# CORRECT\n- name: Install web server\n  hosts: webservers\n  become: true\n  tasks:\n    - name: Install nginx\n      ansible.builtin.apt:\n        name: nginx\n        state: present\n```""")))

PAGES.append(('ansible-missing-tasks-directive', 'Ansible Missing Tasks Directive',
    'Fix Ansible plays that are missing the tasks directive',
    body_template('Ansible Missing Tasks Directive',
        'Ansible playbook fails because no tasks are defined in a play.',
        "ERROR! 'tasks' is not a valid attribute for a Play",
        ['Tasks keyword misspelled',
         'Roles-only play without tasks key',
         'Empty play definition'],
        """```yaml\n# CORRECT: Include tasks\n- name: Setup web server\n  hosts: webservers\n  tasks:\n    - name: Ensure nginx is installed\n      ansible.builtin.apt:\n        name: nginx\n        state: present\n\n# Roles-only play (valid without tasks)\n- name: Setup web server\n  hosts: webservers\n  roles:\n    - nginx\n```""")))

PAGES.append(('ansible-invalid-yaml-syntax', 'Ansible Invalid YAML Syntax',
    'Fix YAML syntax errors that prevent Ansible playbooks from parsing',
    body_template('Ansible Invalid YAML Syntax',
        'Ansible cannot parse the playbook due to YAML syntax errors.',
        'ERROR! We could not match supplied with a key on hosts',
        ['Incorrect indentation',
         'Missing colons after keys',
         'Unbalanced quotes',
         'Mixed tabs and spaces'],
        """```yaml\n# CORRECT YAML structure\n---\n- name: Example playbook\n  hosts: all\n  become: true\n  tasks:\n    - name: Install package\n      ansible.builtin.apt:\n        name: nginx\n        state: present\n```\n\n```bash\npython3 -c \\"import yaml; yaml.safe_load(open('playbook.yml'))\\\"\nansible-lint playbook.yml\n```""")))

PAGES.append(('ansible-recursive-loop-detected', 'Ansible Recursive Loop Detected',
    'Fix Ansible recursive variable references and loops',
    body_template('Ansible Recursive Loop Detected',
        'Ansible detects an infinite loop or recursive reference during playbook execution.',
        'ERROR! A recursive loop was detected: var_a -> var_b -> var_a',
        ['Variable A references Variable B which references Variable A',
         'include loop (playbook A includes B which includes A)',
         'When/loop creating infinite recursion'],
        """```yaml\n# WRONG - circular reference\nvars:\n  var_a: "{{ var_b }}"\n  var_b: "{{ var_a }}"\n\n# CORRECT - break the cycle\nvars:\n  var_a: "fixed_value"\n  var_b: "{{ var_a }}"\n```""")))

PAGES.append(('ansible-duplicate-task-name', 'Ansible Duplicate Task Name',
    'Fix Ansible playbooks with duplicate task names that cause ambiguity',
    body_template('Ansible Duplicate Task Name',
        'Ansible warns or fails when multiple tasks share the same name within a play.',
        'WARNING: A duplicate named task was found. The task "Install package" is defined more than once.',
        ['Copy-paste errors',
         'Multiple includes defining same task names',
         'Role tasks conflicting with play tasks'],
        """```yaml\n# WRONG - duplicate task names\n- name: Install package\n  ansible.builtin.apt:\n    name: nginx\n- name: Install package\n  ansible.builtin.apt:\n    name: apache2\n\n# CORRECT - unique names\n- name: Install nginx\n  ansible.builtin.apt:\n    name: nginx\n- name: Install apache2\n  ansible.builtin.apt:\n    name: apache2\n```""")))

PAGES.append(('ansible-include-file-not-found', 'Ansible Include File Not Found',
    'Fix Ansible errors when included task files do not exist',
    body_template('Ansible Include File Not Found',
        'Ansible cannot find the file specified in an include_tasks or import_tasks directive.',
        'ERROR! could not find file /path/to/tasks/missing_tasks.yml',
        ['File path typo',
         'Relative path resolution issues',
         'File not committed to version control',
         'Role path not configured correctly'],
        """```yaml\n- name: Include tasks\n  ansible.builtin.include_tasks: "{{ role_path }}/tasks/main.yml"\n\n- name: Conditional include with file check\n  ansible.builtin.stat:\n    path: "{{ playbook_dir }}/files/optional.conf"\n  register: config_check\n- name: Include optional configuration\n  ansible.builtin.include_tasks: optional_config.yml\n  when: config_check.stat.exists\n```""")))

PAGES.append(('ansible-import-role-not-found', 'Ansible Import Role Not Found',
    'Fix Ansible errors when imported roles are not found in the search path',
    body_template('Ansible Import Role Not Found',
        'Ansible cannot locate the specified role during playbook execution.',
        "ERROR! the role 'nginx' was not found in /path/to/roles:/etc/ansible/roles",
        ['Role not installed via ansible-galaxy',
         'Incorrect role name',
         'roles_path not configured',
         'Role directory structure incorrect'],
        """```bash\nansible-galaxy install nginx\nansible-config dump | grep roles_path\n```\n\n```ini\n[defaults]\nroles_path = ./roles:/etc/ansible/roles:/usr/share/ansible/roles\n```\n\n```yaml\n# requirements.yml\n---\nroles:\n  - name: nginx\n    version: "3.1.0"\n```""")))

PAGES.append(('ansible-vars-prompt-not-allowed', 'Ansible Vars Prompt Not Allowed',
    'Fix Ansible vars_prompt restrictions in certain contexts',
    body_template('Ansible Vars Prompt Not Allowed',
        'Ansible vars_prompt is used in an invalid context.',
        'ERROR! vars_prompt is not allowed in a pre_tasks or role context',
        ['vars_prompt used in pre_tasks instead of play level',
         'vars_prompt used inside a role',
         'vars_prompt in imported play'],
        """```yaml\n# CORRECT: vars_prompt at play level\n- name: Deploy with confirmation\n  hosts: all\n  vars_prompt:\n    - name: deploy_env\n      prompt: "Enter target environment"\n      default: dev\n      private: false\n  tasks:\n    - name: Deploy\n      ansible.builtin.debug:\n        msg: "Deploying to {{ deploy_env }}"\n```\n\n# Use --extra-vars instead:\n# ansible-playbook deploy.yml --extra-vars \\"deploy_env=prod\\"" """)))

PAGES.append(('ansible-tags-not-recognized', 'Ansible Tags Not Recognized',
    'Fix Ansible tag configuration errors in playbooks and roles',
    body_template('Ansible Tags Not Recognized',
        'Ansible cannot recognize or match the specified tags.',
        "ERROR! No matches found for the tag 'deploy' in the playbook",
        ['Tag name typo',
         'Tag applied to wrong element',
         'Using tags with import (not supported)',
         'Tag name with invalid characters'],
        """```yaml\n- name: Deploy application\n  hosts: all\n  tasks:\n    - name: Install dependencies\n      ansible.builtin.apt:\n        name: "{{ item }}"\n      tags:\n        - install\n    - name: Deploy code\n      ansible.builtin.git:\n        repo: https://github.com/example/app.git\n        dest: /opt/app\n      tags:\n        - deploy\n\n# Run: ansible-playbook site.yml --tags "deploy"\n```""")))

PAGES.append(('ansible-strategy-not-found', 'Ansible Strategy Plugin Not Found',
    'Fix Ansible strategy plugin configuration errors',
    body_template('Ansible Strategy Plugin Not Found',
        'Ansible cannot find the specified strategy plugin.',
        "ERROR! the strategy 'free' could not be loaded",
        ['Strategy plugin not installed',
         'Typo in strategy name',
         'Strategy plugin incompatible with Ansible version',
         'Custom plugin not in plugin path'],
        """```yaml\n- name: Use linear strategy (default)\n  hosts: all\n  strategy: linear\n  tasks:\n    - name: Task 1\n      ansible.builtin.debug:\n        msg: "Running on {{ inventory_hostname }}"\n\n- name: Use debug strategy\n  hosts: all\n  strategy: debug\n```\n\n```ini\n[defaults]\nstrategy = linear\n```""")))

PAGES.append(('ansible-serial-count-invalid', 'Ansible Serial Count Invalid',
    'Fix Ansible serial batch configuration errors in rolling updates',
    body_template('Ansible Serial Count Invalid',
        'Ansible serial parameter has an invalid value.',
        "ERROR! the serial value specified is not valid: 'abc'",
        ['Non-numeric serial value',
         'Percentage value malformed',
         'Serial greater than host count'],
        """```yaml\n# Valid serial values\n- name: Rolling update\n  hosts: webservers\n  serial: 2\n  tasks:\n    - name: Update\n      ansible.builtin.apt:\n        name: nginx\n        state: latest\n\n# Percentage-based\n- name: 25% at a time\n  hosts: webservers\n  serial: "25%"\n  max_fail_percentage: 10\n```\n\n```yaml\n# Complex serial\n- name: Multi-stage deployment\n  hosts: webservers\n  serial:\n    - 1\n    - "25%"\n    - "100%"\n```""")))

PAGES.append(('ansible-throttle-limit-reached', 'Ansible Throttle Limit Reached',
    'Fix Ansible throttle limit configuration errors in task definitions',
    body_template('Ansible Throttle Limit Reached',
        'Ansible throttle limit has been exceeded or is invalid.',
        "ERROR! the throttle value must be a positive integer, got 'abc'",
        ['Non-integer throttle value',
         'Throttle set to zero or negative',
         'Throttle exceeding available forks'],
        """```yaml\n- name: API calls with rate limiting\n  hosts: all\n  tasks:\n    - name: Call external API\n      ansible.builtin.uri:\n        url: "https://api.example.com/data"\n      throttle: 5\n```""")))

PAGES.append(('ansible-order-directive-invalid', 'Ansible Order Directive Invalid',
    'Fix Ansible role include order configuration errors',
    body_template('Ansible Order Directive Invalid',
        'Ansible encounters an invalid order directive in role includes.',
        "ERROR! Invalid order value for role include: 'xyz'",
        ['Non-numeric order value',
         'Duplicate order values',
         'order used with the wrong include type'],
        """```yaml\n- name: Setup servers\n  hosts: all\n  roles:\n    - role: base\n      order: 1\n    - role: common\n      order: 2\n    - role: nginx\n      order: 3\n```""")))

PAGES.append(('ansible-recursive-import', 'Ansible Recursive Import Error',
    'Fix Ansible recursive import and include errors in playbooks',
    body_template('Ansible Recursive Import Error',
        'Ansible detects a recursive import or include pattern.',
        'ERROR! Recursive include detected: playbook.yml -> tasks/main.yml -> playbook.yml',
         ['Playbook A imports Playbook B which imports Playbook A',
          'Role A depends on Role B which depends on Role A',
          'include_tasks creating circular reference'],
        """```yaml\n# Safe import structure\n- import_playbook: site-common.yml\n- import_playbook: site-web.yml\n- import_playbook: site-db.yml\n\n# site-web.yml\n- hosts: webservers\n  tasks:\n    - import_tasks: tasks/install.yml\n    - import_tasks: tasks/configure.yml\n```""")))

# ====== 3. MODULE ERRORS ======

PAGES.append(('ansible-module-not-found', 'Ansible Module Not Found',
    'Fix Ansible module not found errors during playbook execution',
    body_template('Ansible Module Not Found',
        'Ansible cannot locate the specified module.',
        "ERROR! no action detected in task, Ansible could not identify this 'module'",
        ['Module name typo',
         'Module requires additional collection',
         'Module from deprecated namespace',
         'Ansible version mismatch'],
        """```yaml\n# Use FQCN\n- name: Install package\n  ansible.builtin.apt:\n    name: nginx\n    state: present\n```\n\n```bash\nansible-galaxy collection install community.general\nansible-galaxy collection install community.docker\n```""")))

PAGES.append(('ansible-missing-required-arguments', 'Ansible Missing Required Arguments',
    'Fix Ansible module errors due to missing required parameters',
    body_template('Ansible Missing Required Arguments',
        'Ansible module fails because required arguments are not provided.',
        "ERROR! this task 'ansible.builtin.apt' requires one of 'name', 'deb'",
        ['Required parameter not specified',
         'Variable used but undefined',
         'Incorrect parameter name'],
        """```yaml\n# WRONG\n- name: Install package\n  ansible.builtin.apt:\n    state: present\n\n# CORRECT\n- name: Install package\n  ansible.builtin.apt:\n    name: nginx\n    state: present\n```""")))

PAGES.append(('ansible-parameter-type-mismatch', 'Ansible Parameter Type Mismatch',
    'Fix Ansible module errors when parameter types do not match expected values',
    body_template('Ansible Parameter Type Mismatch',
        'Ansible module receives a parameter of the wrong type.',
        "ERROR! 'port' must be a string, got '<class int>'",
        ['Integer passed where string expected',
         'String passed where boolean expected',
         'List passed where string expected'],
        """```yaml\n- name: Configure service\n  ansible.builtin.template:\n    src: config.j2\n    dest: /etc/app/config\n    mode: '0644'  # string not integer\n\n- name: Install package\n  ansible.builtin.apt:\n    name: nginx\n    update_cache: true  # boolean not string\n```""")))

PAGES.append(('ansible-unsupported-parameter', 'Ansible Unsupported Parameter',
    'Fix Ansible errors when using parameters not supported by a module',
    body_template('Ansible Unsupported Parameter',
        'Ansible module receives an unrecognized parameter.',
        "ERROR! unsupported parameter for module: 'enable_ssl'",
        ['Parameter name typo',
         'Parameter from wrong module version',
         'Module version mismatch with documentation'],
        """```yaml\n# Check docs first: ansible-doc ansible.builtin.apt\n\n# WRONG\n- name: Install package\n  ansible.builtin.apt:\n    name: nginx\n    enable_ssl: true  # Not valid\n\n# CORRECT\n- name: Install package\n  ansible.builtin.apt:\n    name: nginx\n    state: present\n```""")))

PAGES.append(('ansible-check-mode-not-supported', 'Ansible Check Mode Not Supported',
    'Handle Ansible modules that do not support check mode (dry run)',
    body_template('Ansible Check Mode Not Supported',
        'Ansible module does not support check mode (dry run).',
        'FAILED! => {"msg": "check mode is not supported for this task"}',
        ['Module implemented without check_mode support',
         'Custom module lacking check mode logic',
         'Certain operations cannot be previewed'],
        """```yaml\n- name: Run destructive task\n  ansible.builtin.command: /opt/scripts/migrate_db.sh\n  check_mode: false\n\n# Or use when condition\n- name: Apply changes\n  ansible.builtin.command: /opt/scripts/migrate_db.sh\n  when: not ansible_check_mode\n```""")))

PAGES.append(('ansible-diff-not-supported', 'Ansible Diff Mode Not Supported',
    'Handle Ansible modules that do not support diff mode output',
    body_template('Ansible Diff Mode Not Supported',
        'Ansible module does not support diff mode output.',
        'FAILED! => {"msg": "diff mode is not supported for this task"}',
        ['Module does not implement diff support',
         'Complex operations without diff representation',
         'Custom module without diff output'],
        """```yaml\n- name: Apply configuration\n  ansible.builtin.command: /opt/scripts/configure.sh\n  diff: false\n\n# Enable diff for templates\n- name: Update nginx config\n  ansible.builtin.template:\n    src: nginx.conf.j2\n    dest: /etc/nginx/nginx.conf\n  diff: true\n```""")))

PAGES.append(('ansible-module-timeout', 'Ansible Module Execution Timeout',
    'Fix Ansible module timeout errors during long-running operations',
    body_template('Ansible Module Execution Timeout',
        'Ansible module exceeds the configured timeout during execution.',
        'ERROR! Timeout waiting for module result',
        ['Task taking longer than expected',
         'Default timeout too short',
         'Resource contention on remote host',
         'Network issues causing slow responses'],
        """```yaml\n- name: Long-running task\n  ansible.builtin.command: /opt/scripts/heavy_computation.sh\n  async: 3600\n  poll: 0\n  register: job_result\n\n- name: Wait for completion\n  ansible.builtin.async_status:\n    jid: "{{ job_result.ansible_job_id }}"\n  register: job_status\n  until: job_status.finished\n  retries: 60\n  delay: 60\n```""")))

PAGES.append(('ansible-failed-import-module', 'Ansible Failed to Import Module Library',
    'Fix Ansible Python module import failures on managed nodes',
    body_template('Ansible Failed to Import Module Library',
        'Ansible cannot import a required Python module on the remote host.',
        'FAILED! => "Failed to import the required Python library (paramiko)"',
        ['Missing Python library on remote host',
         'Wrong Python interpreter selected',
         'pip not installed',
         'Virtual environment issues'],
        """```bash\nsudo apt-get install python3-pip python3-paramiko\n```\n\n```yaml\n[all:vars]\nansible_python_interpreter=/usr/bin/python3\n```\n\n```yaml\n- name: Install missing libraries\n  ansible.builtin.pip:\n    name:\n      - paramiko\n      - pyyaml\n    executable: pip3\n```""")))

PAGES.append(('ansible-module-non-empty-warning', 'Ansible Module Non-Empty Warning',
    'Address Ansible module warnings that may indicate configuration issues',
    body_template('Ansible Module Non-Empty Warning',
        'Ansible module returns a non-empty warning message.',
        'WARNING: Module returned non-empty warning',
        ['Module completed but with caveats',
         'Service installed but not started',
         'Configuration partially applied',
         'Deprecated feature usage'],
        """```yaml\n- name: Install and start nginx\n  ansible.builtin.apt:\n    name: nginx\n    state: present\n  register: nginx_install\n\n- name: Display warnings\n  ansible.builtin.debug:\n    var: nginx_install.warnings\n  when: nginx_install.warnings is defined\n\n- name: Start nginx service\n  ansible.builtin.service:\n    name: nginx\n    state: started\n```""")))

PAGES.append(('ansible-aws-module-auth-error', 'Ansible AWS Module Authentication Error',
    'Fix Ansible AWS module authentication failures for EC2, S3, and other services',
    body_template('Ansible AWS Module Authentication Error',
        'Ansible AWS modules fail due to authentication issues.',
        'FAILED! => AuthFailure: AWS was not able to validate the provided access credentials',
        ['AWS credentials not configured',
         'Expired access keys',
         'Incorrect region',
         'IAM permissions insufficient'],
        """```bash\naws configure\nexport AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE\nexport AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY\nexport AWS_DEFAULT_REGION=us-east-1\n```\n\n```yaml\n- name: Create EC2 instance\n  amazon.aws.ec2_instance:\n    name: my-server\n    instance_type: t3.micro\n    image_id: ami-12345678\n    region: us-east-1\n    aws_access_key: "{{ vault_aws_access_key }}"\n    aws_secret_key: "{{ vault_aws_secret_key }}"\n```""")))

PAGES.append(('ansible-docker-module-not-found', 'Ansible Docker Module Not Found',
    'Fix Ansible Docker module errors when Docker modules are not available',
    body_template('Ansible Docker Module Not Found',
        'Ansible cannot find Docker-related modules.',
        "ERROR! no action detected in task. The 'docker_container' module is not available.",
        ['Docker collection not installed',
         'Using old module names',
         'Missing Python Docker library'],
        """```bash\nansible-galaxy collection install community.docker\npip install docker\n```\n\n```yaml\n- name: Create container\n  community.docker.docker_container:\n    name: my-app\n    image: nginx:latest\n    state: started\n    ports:\n      - "8080:80"\n```""")))

PAGES.append(('ansible-kubernetes-module-error', 'Ansible Kubernetes Module Error',
    'Fix Ansible Kubernetes module errors when managing K8s resources',
    body_template('Ansible Kubernetes Module Error',
        'Ansible Kubernetes module fails to manage cluster resources.',
        'FAILED! => "kubernetes.config.load_kube_config failed"',
        ['kubeconfig not found or invalid',
         'Missing kubernetes collection',
         'Cluster not accessible',
         'Insufficient RBAC permissions'],
        """```bash\nansible-galaxy collection install kubernetes.core\npip install kubernetes\n```\n\n```yaml\n- name: Deploy to Kubernetes\n  kubernetes.core.k8s:\n    state: present\n    definition:\n      apiVersion: apps/v1\n      kind: Deployment\n      metadata:\n        name: nginx-deployment\n      spec:\n        replicas: 3\n        selector:\n          matchLabels:\n            app: nginx\n        template:\n          metadata:\n            labels:\n              app: nginx\n          spec:\n            containers:\n              - name: nginx\n                image: nginx:1.19\n    kubeconfig: ~/.kube/config\n```""")))

PAGES.append(('ansible-pip-module-failed', 'Ansible pip Module Failed',
    'Fix Ansible pip module errors when installing Python packages',
    body_template('Ansible pip Module Failed',
        'Ansible pip module fails to install Python packages.',
        'FAILED! => "Could not find a version that satisfies the requirement"',
        ['Package name incorrect',
         'pip version mismatch',
         'Network issues (PyPI unreachable)',
         'Dependency conflicts'],
        """```yaml\n- name: Install Python packages\n  ansible.builtin.pip:\n    name:\n      - django>=3.2\n      - celery>=5.0\n    state: present\n    executable: pip3\n\n- name: Install from requirements\n  ansible.builtin.pip:\n    requirements: /opt/app/requirements.txt\n    virtualenv: /opt/app/venv\n```""")))

PAGES.append(('ansible-apt-module-failed', 'Ansible apt Module Failed',
    'Fix Ansible apt module errors on Debian/Ubuntu systems',
    body_template('Ansible apt Module Failed',
        'Ansible apt module fails to manage packages on Debian/Ubuntu.',
        'FAILED! => "Failed to update apt cache: E: Could not get lock"',
        ['Another process holding apt lock',
         'Package repository issues',
         'GPG key problems',
         'Disk space full'],
        """```yaml\n- name: Wait for apt lock\n  ansible.builtin.wait_for:\n    path: /var/lib/dpkg/lock-frontend\n    timeout: 300\n\n- name: Install package\n  ansible.builtin.apt:\n    name: nginx\n    state: present\n    update_cache: true\n    cache_valid_time: 3600\n```""")))

PAGES.append(('ansible-yum-module-error', 'Ansible yum Module Error',
    'Fix Ansible yum module errors on RHEL/CentOS systems',
    body_template('Ansible yum Module Error',
        'Ansible yum module fails to manage packages on RHEL/CentOS systems.',
        'FAILED! => "Error: Unable to find a match: nginx"',
        ['Package not in enabled repositories',
         'EPEL not installed',
         'Repository metadata stale',
         'DNF/yum version mismatch'],
        """```yaml\n- name: Install EPEL\n  ansible.builtin.yum:\n    name: epel-release\n    state: present\n\n- name: Install nginx\n  ansible.builtin.yum:\n    name: nginx\n    state: present\n\n# Or use dnf on newer systems\n- name: Install package\n  ansible.builtin.dnf:\n    name: nginx\n    state: present\n```""")))

# ====== 4. VARIABLE ERRORS ======

PAGES.append(('ansible-undefined-variable', 'Ansible Undefined Variable Error',
    'Fix Ansible undefined variable errors during playbook execution',
    body_template('Ansible Undefined Variable Error',
        'Ansible encounters a variable that has not been defined.',
        "ERROR! 'my_variable' is undefined",
         ['Variable name typo',
          'Variable not set in inventory, vars, or extra-vars',
          'Variable scope issue',
          'Variable set conditionally but condition was false'],
        """```yaml\n# Use default values\n- name: Safe variable usage\n  ansible.builtin.debug:\n    msg: "Value: {{ my_variable | default('fallback') }}"\n\n# Define variable in inventory\n[all:vars]\nmy_variable=production_value\n\n# Or use extra-vars\n# ansible-playbook site.yml --extra-vars "my_variable=value"\n```""")))

PAGES.append(('ansible-recursive-variable-reference', 'Ansible Recursive Variable Reference',
    'Fix Ansible circular variable references that cause infinite recursion',
    body_template('Ansible Recursive Variable Reference',
        'Ansible detects a recursive variable reference during template evaluation.',
        'ERROR! A recursive loop was detected: var_a -> var_b -> var_a',
         ['Variable A references Variable B which references Variable A',
          'set_fact creating circular references',
          'Variable inheritance chain broken'],
        """```yaml\n# WRONG - circular reference\nvars:\n  app_name: "{{ project_name }}"\n  project_name: "{{ app_name }}"\n\n# CORRECT - break the cycle\nvars:\n  app_name: "my-application"\n  project_name: "{{ app_name }}"\n```""")))

PAGES.append(('ansible-template-evaluation-error', 'Ansible Template Evaluation Error',
    'Fix Ansible Jinja2 template evaluation errors during variable resolution',
    body_template('Ansible Template Evaluation Error',
        'Ansible fails to evaluate a Jinja2 template expression.',
        "ERROR! Template syntax error: unexpected '/'",
        ['Invalid Jinja2 syntax',
         'Division by zero in template',
         'Undefined variable in template',
         'Missing closing brackets'],
        """```yaml\n- name: Display message\n  ansible.builtin.debug:\n    msg: "Count is {{ item_count | default(0) }}"\n\n# Escape special characters\n- name: Use literal braces\n  ansible.builtin.debug:\n    msg: "Literal brace: {{ '{{' }} and {{ '}}' }}"\n```""")))

PAGES.append(('ansible-jinja2-filter-not-found', 'Ansible Jinja2 Filter Not Found',
    'Fix Ansible errors when using unavailable Jinja2 filters',
    body_template('Ansible Jinja2 Filter Not Found',
        'Ansible encounters an unknown Jinja2 filter.',
        "ERROR! 'json_query' is not a filter",
        ['Filter from uninstalled collection',
         'Filter name typo',
         'Filter requires additional Python library'],
        """```bash\nansible-galaxy collection install community.general\nansible-doc -t filter -l\n```\n\n```yaml\n- name: Query JSON\n  ansible.builtin.debug:\n    msg: "{{ data | community.general.json_query('servers[*].name') }}"\n```\n\n# Alternative: use built-in filters\n- name: Filter list\n  ansible.builtin.debug:\n    msg: "{{ my_list | select('match', '^web') | list }}"\n```""")))

PAGES.append(('ansible-lookup-plugin-error', 'Ansible Lookup Plugin Error',
    'Fix Ansible lookup plugin errors when fetching external data',
    body_template('Ansible Lookup Plugin Error',
        'Ansible lookup plugin fails to retrieve data.',
        "LookupError: [Errno 2] No such file or directory: '/path/to/file'",
        ['File path incorrect',
         'Network resource unavailable',
         'Authentication required for lookup',
         'Lookup plugin not installed'],
        """```yaml\n- name: Read file content\n  ansible.builtin.debug:\n    msg: "{{ lookup('ansible.builtin.file', '/path/to/file', errors='ignore') }}"\n\n- name: Password lookup\n  ansible.builtin.debug:\n    msg: "{{ lookup('ansible.builtin.password', '/tmp/password.txt', length=20) }}"\n```\n\n```yaml\n# Safe lookup with fallback\n- name: Read optional config\n  ansible.builtin.set_fact:\n    config: "{{ lookup('ansible.builtin.file', '/etc/app/config', errors='ignore') | default('{}') }}"\n```""")))

PAGES.append(('ansible-undefined-dict-key', 'Ansible Undefined Dictionary Key',
    'Fix Ansible errors when accessing non-existent dictionary keys',
    body_template('Ansible Undefined Dictionary Key',
        'Ansible tries to access a dictionary key that does not exist.',
        "'dict object' has no attribute 'nonexistent'",
        ['Variable not populated',
         'Key name typo',
         'Nested key access without null check',
         'Variable scope issue'],
        """```yaml\n- name: Access key safely\n  ansible.builtin.debug:\n    msg: "Value: {{ my_dict.get('key', 'default_value') }}"\n\n- name: Safe access with default\n  ansible.builtin.debug:\n    msg: "Value: {{ my_dict.key | default('fallback') }}"\n\n- name: Check key existence\n  ansible.builtin.debug:\n    msg: "Has key: {{ 'key' in my_dict }}"\n```""")))

PAGES.append(('ansible-list-index-out-of-range', 'Ansible List Index Out of Range',
    'Fix Ansible errors when accessing list elements beyond bounds',
    body_template('Ansible List Index Out of Range',
        'Ansible tries to access a list index that does not exist.',
        'ERROR! list index out of range',
        ['List shorter than expected',
         'Index calculated incorrectly',
         'Loop variable exceeds bounds',
         'Variable not populated'],
        """```yaml\n- name: Get first element\n  ansible.builtin.debug:\n    msg: "{{ myList[0] | default('empty list') }}"\n\n- name: Safe access\n  ansible.builtin.debug:\n    msg: "{{ myList[0] if myList | length > 0 else 'empty' }}"\n```\n\n```yaml\n- name: Iterate safely\n  ansible.builtin.debug:\n    msg: "Item {{ idx }}: {{ item }}"\n  loop: "{{ myList | default([]) }}"\n```""")))

PAGES.append(('ansible-string-to-int-conversion', 'Ansible String to Integer Conversion Error',
    'Fix Ansible type conversion errors between strings and integers',
    body_template('Ansible String to Integer Conversion Error',
        'Ansible fails to convert between string and integer types.',
        "'string' object cannot be interpreted as an integer",
        ['Numeric value stored as string',
         'Jinja2 filter applied to wrong type',
         'Arithmetic on string values'],
        """```yaml\n- name: Convert string to int\n  ansible.builtin.debug:\n    msg: "{{ '42' | int }}"\n\n- name: Add numbers\n  ansible.builtin.debug:\n    msg: "{{ (count_a | int) + (count_b | int) }}"\n\n- name: Float conversion\n  ansible.builtin.debug:\n    msg: "{{ '3.14' | float }}"\n```""")))

PAGES.append(('ansible-fact-not-set', 'Ansible Fact Not Set Error',
    'Fix Ansible errors when expected facts are not available on managed hosts',
    body_template('Ansible Fact Not Set Error',
        'Ansible playbook fails because expected facts are not set on the target host.',
        "ERROR! 'ansible_distribution' is undefined",
        ['gather_facts disabled',
         'Fact caching issues',
         'Custom module not returning expected facts',
         'Connection type does not support fact gathering'],
        """```yaml\n- name: Deploy with facts\n  hosts: all\n  gather_facts: true\n  tasks:\n    - name: Install package\n      ansible.builtin.apt:\n        name: nginx\n      when: ansible_os_family == "Debian"\n\n# Or set fallback\n- name: Use facts with defaults\n  ansible.builtin.debug:\n    msg: "OS: {{ ansible_distribution | default('unknown') }}"\n```""")))

PAGES.append(('ansible-registered-variable-empty', 'Ansible Registered Variable Empty',
    'Fix Ansible issues when registered variables contain unexpected empty values',
    body_template('Ansible Registered Variable Empty',
        'Ansible registered variable is empty or missing expected content.',
        "ERROR! 'stdout_lines' is undefined",
        ['Task output captured incorrectly',
         'Command produces no stdout',
         'Variable registered before task ran',
         'Conditional prevented task execution'],
        """```yaml\n- name: Run command\n  ansible.builtin.command: echo "hello"\n  register: result\n  changed_when: false\n\n- name: Check output\n  ansible.builtin.debug:\n    var: result.stdout_lines\n  when: result.stdout_lines is defined\n\n# Use default values\n- name: Safe access\n  ansible.builtin.debug:\n    msg: "{{ result.stdout_lines | default(['no output']) }}"\n```""")))

PAGES.append(('ansible-set-fact-cacheable', 'Ansible set_fact Cacheable Error',
    'Fix Ansible set_fact cacheable parameter configuration issues',
    body_template('Ansible set_fact Cacheable Error',
        'Ansible set_fact with cacheable parameter not working as expected.',
        "ERROR! set_fact: cacheable must be a boolean value",
        ['cacheable value not boolean',
         'Fact caching not enabled',
         'Cache plugin not configured'],
        """```yaml\n- name: Set persistent fact\n  ansible.builtin.set_fact:\n    app_version: "1.2.3"\n    cacheable: true\n```\n\n```ini\n[defaults]\nfact_caching = jsonfile\nfact_caching_connection = /tmp/ansible_facts\nfact_caching_timeout = 3600\n```""")))

PAGES.append(('ansible-variable-type-conflict', 'Ansible Variable Type Conflict',
    'Fix Ansible errors when variables have unexpected types',
    body_template('Ansible Variable Type Conflict',
        'Ansible encounters unexpected variable types during operations.',
        "ERROR! Unexpected type for variable: expected string, got list",
        ['Variable defined as list but used as string',
         'Extra-vars override changing type',
         'Variable inheritance type mismatch'],
        """```yaml\n- name: Safe type usage\n  ansible.builtin.debug:\n    msg: "Name: {{ app_name | string }}"\n\n- name: Type checking\n  ansible.builtin.debug:\n    msg: "Type: {{ my_var | type_debug }}"\n\n# Handle mixed types\n- name: Process value\n  ansible.builtin.debug:\n    msg: >\n      {% if my_var is iterable and my_var is not string %}\n      {{ my_var | join(', ') }}\n      {% else %}\n      {{ my_var | string }}\n      {% endif %}\n```""")))

# ====== 5. TEMPLATE/JINJA2 ERRORS ======

PAGES.append(('ansible-jinja2-unexpected-paren', 'Ansible Jinja2 Unexpected Closing Parenthesis',
    'Fix Jinja2 syntax errors with unmatched parentheses in Ansible templates',
    body_template('Ansible Jinja2 Unexpected Closing Parenthesis',
        'Jinja2 template has an unexpected closing parenthesis.',
        "ERROR! Jinja2 Template Error: unexpected ')'",
        ['Extra closing parenthesis',
         'Missing opening parenthesis',
         'Parentheses in wrong position'],
        """```yaml\n# WRONG\n- name: Bad template\n  ansible.builtin.debug:\n    msg: "{{ variable }})"\n\n# CORRECT\n- name: Good template\n  ansible.builtin.debug:\n    msg: "{{ variable }}"\n\n# Complex expressions need matching parens\n- name: Nested parens\n  ansible.builtin.debug:\n    msg: "{{ (var1 | int) + (var2 | int) }}"\n```""")))

PAGES.append(('ansible-inline-if-syntax-error', 'Ansible Inline If Syntax Error',
    'Fix Jinja2 inline if (ternary) expression syntax errors in Ansible',
    body_template('Ansible Inline If Syntax Error',
        'Ansible Jinja2 inline if expression has incorrect syntax.',
        "ERROR! Jinja2 Template Error: unexpected 'else'",
        ['Missing if keyword',
         'Missing else clause',
         'Wrong order of condition/value/else'],
        """```yaml\n# Jinja2 inline if syntax:\n# {{ value_if_true if condition else value_if_false }}\n\n# WRONG\n- name: Bad ternary\n  ansible.builtin.debug:\n    msg: "{{ 'active' else 'inactive' if enabled }}"\n\n# CORRECT\n- name: Good ternary\n  ansible.builtin.debug:\n    msg: "{{ 'active' if enabled else 'inactive' }}"\n```\n\n```yaml\n# Chained ternary\n- name: Complex condition\n  ansible.builtin.debug:\n    msg: "{{ 'prod' if env == 'production' else ('staging' if env == 'staging' else 'dev') }}"\n```""")))

PAGES.append(('ansible-macro-undefined', 'Ansible Jinja2 Macro Undefined',
    'Fix Ansible errors when Jinja2 macros are not defined in templates',
    body_template('Ansible Jinja2 Macro Undefined',
        'Ansible template references an undefined Jinja2 macro.',
        "ERROR! Jinja2 Template Error: UndefinedError: 'my_macro' is undefined",
        ['Macro not defined in template',
         'Macro in wrong scope',
         'Typo in macro name',
         'Macro file not imported'],
        """```yaml\n# Define macro in template\n# templates/config.j2\n# {% macro server_block(name, port) %}\n# server {\n#     listen {{ port }};\n#     server_name {{ name }};\n# }\n# {% endmacro %}\n\n# Import macros from file\n# templates/main.j2\n# {% from 'macros/network.j2' import firewall_rule %}\n# {{ firewall_rule('allow_http', 80, 'tcp') }}\n```""")))

PAGES.append(('ansible-block-not-closed', 'Ansible Jinja2 Block Not Closed',
    'Fix Ansible Jinja2 template block closure errors',
    body_template('Ansible Jinja2 Block Not Closed',
        'Ansible template has an unclosed Jinja2 block.',
        "ERROR! Jinja2 Template Error: Block 'if' not closed",
        ['Missing {% endif %}',
         'Missing {% endfor %}',
         'Missing {% endblock %}',
         'Nested blocks without proper closure'],
        """```yaml\n# All blocks must be properly closed\n# CORRECT:\n# {% if condition %}\n# Do something\n# {% endif %}\n\n# Nested blocks\n# {% for server in servers %}\n#   {% if server.enabled %}\n#     server {{ server.name }};\n#   {% endif %}\n# {% endfor %}\n```""")))

PAGES.append(('ansible-regex-error', 'Ansible Regex Template Error',
    'Fix Ansible Jinja2 regex filter errors in templates and tasks',
    body_template('Ansible Regex Template Error',
        'Ansible regex filter encounters an error during template evaluation.',
        'ERROR! Jinja2 Template Error: bad escape in end of string',
        ['Invalid regex syntax',
         'Unescaped special characters',
         'Missing regex module'],
        """```yaml\n- name: Match pattern\n  ansible.builtin.debug:\n    msg: "{{ 'server1.example.com' is match('server.*\\\\.example\\\\.com') }}"\n\n- name: Extract IP\n  ansible.builtin.debug:\n    msg: "{{ 'IP: 192.168.1.100' | regex_search('(\\\\d+\\\\.\\\\d+\\\\.\\\\d+\\\\.\\\\d+)') }}"\n\n- name: Replace pattern\n  ansible.builtin.debug:\n    msg: "{{ 'Hello World' | regex_replace('World', 'Ansible') }}"\n```""")))

PAGES.append(('ansible-date-template-error', 'Ansible Date Template Error',
    'Fix Ansible Jinja2 date formatting template errors',
    body_template('Ansible Date Template Error',
        'Ansible date formatting filter produces errors.',
        'ERROR! Jinja2 Template Error: unsupported format character',
        ['Wrong date format syntax',
         'Missing date filter',
         'Non-date value passed to date filter'],
        """```yaml\n- name: Format current date\n  ansible.builtin.debug:\n    msg: "{{ ansible_date_time.iso8601 }}"\n\n# Custom date format\n- name: Custom format\n  ansible.builtin.debug:\n    msg: "{{ ansible_date_time.date }}"\n\n# Use to_datetime filter\n- name: Parse date\n  ansible.builtin.debug:\n    msg: "{{ '2024-01-15' | to_datetime('%Y-%m-%d') }}"\n```""")))

# ====== 6. ROLE/COLLECTION ERRORS ======

PAGES.append(('ansible-role-not-found', 'Ansible Role Not Found',
    'Fix Ansible role not found errors during playbook execution',
    body_template('Ansible Role Not Found',
        'Ansible cannot locate the specified role.',
        "ERROR! the role 'webserver' was not found",
        ['Role not installed',
         'Incorrect role name',
         'roles_path not configured',
         'Role directory structure incorrect'],
        """```bash\nansible-galaxy install role_name\nansible-galaxy install -r requirements.yml\n```\n\n```ini\n[defaults]\nroles_path = ./roles:/etc/ansible/roles\n```""")))

PAGES.append(('ansible-role-dependency-cycle', 'Ansible Role Dependency Cycle',
    'Fix circular role dependencies in Ansible playbooks and roles',
    body_template('Ansible Role Dependency Cycle',
        'Ansible detects a circular dependency between roles.',
        "ERROR! Recursive include detected: role 'web' depends on 'common' which depends on 'web'",
        ['Role A depends on Role B which depends on Role A',
         'Meta dependencies creating infinite loops'],
        """```yaml\n# Break the dependency cycle\n# roles/web/meta/main.yml\n---\ndependencies:\n  - role: common\n\n# roles/common/meta/main.yml\n---\ndependencies: []\n```\n\n# Flat dependency structure\n- name: Full stack deployment\n  hosts: all\n  roles:\n    - role: base\n    - role: common\n    - role: nginx\n    - role: app\n```""")))

PAGES.append(('ansible-role-name-conflict', 'Ansible Role Name Conflict',
    'Fix Ansible role name conflicts between local and galaxy roles',
    body_template('Ansible Role Name Conflict',
        'Ansible encounters a role name conflict between local and installed roles.',
        "WARNING: role 'common' found at both ./roles/common and /etc/ansible/roles/common",
        ['Same role name in local and global paths',
         'Role downloaded with conflicting name',
         'Role renamed locally'],
        """```ini\n# ansible.cfg - specify exact role path\n[defaults]\nroles_path = ./roles\n```\n\n# Use unique role names\n# ./roles/app-common/\n# ./roles/system-common/\n\n# Or use namespace convention\n# ./roles/mycompany.common/\n# ./roles/mycompany.nginx/\n```""")))

PAGES.append(('ansible-collection-not-installed', 'Ansible Collection Not Installed',
    'Fix Ansible errors when required collections are not installed',
    body_template('Ansible Collection Not Installed',
        'Ansible cannot find the specified collection.',
        "ERROR! couldn't resolve module/action 'community.docker.docker_container'",
        ['Collection not installed',
         'Collection version mismatch',
         'Collection from different namespace'],
        """```bash\nansible-galaxy collection install community.docker\nansible-galaxy collection install -r requirements.yml\n```\n\n```yaml\n# requirements.yml\n---\ncollections:\n  - name: community.docker\n    version: ">=3.0.0"\n  - name: community.general\n  - name: amazon.aws\n```""")))

PAGES.append(('ansible-galaxy-error', 'Ansible Galaxy Error',
    'Fix Ansible Galaxy errors when installing roles and collections',
    body_template('Ansible Galaxy Error',
        'Ansible Galaxy fails to download or install roles/collections.',
        'ERROR! - AnsibleError: Failed to install role/collection from Galaxy',
        ['Network connectivity issues',
         'Galaxy API rate limiting',
         'Authentication required',
         'Role/collection does not exist'],
        """```bash\ncurl -I https://galaxy.ansible.com\nansible-galaxy role install nginx -vvv\nansible-galaxy login --github\n```\n\n```yaml\n# requirements.yml\n---\nroles:\n  - name: nginx\n    version: "3.1.0"\n  - src: https://github.com/user/role.git\n    name: my-role\n    version: master\n```""")))

PAGES.append(('ansible-requirements-file-error', 'Ansible Requirements File Error',
    'Fix Ansible requirements.yml syntax and format errors',
    body_template('Ansible Requirements File Error',
        'Ansible fails to parse the requirements file.',
        'ERROR! - AnsibleError: Error parsing requirements.yml',
        ['Invalid YAML syntax',
         'Missing required fields',
         'Wrong format version'],
        """```yaml\n# Correct requirements.yml format\n---\nroles:\n  - name: nginx\n    version: "3.1.0"\n  - name: docker\n    src: https://github.com/user/role.git\n    version: master\n\ncollections:\n  - name: community.general\n    version: ">=5.0.0"\n  - name: community.docker\n```""")))

PAGES.append(('ansible-default-role-path-missing', 'Ansible Default Role Path Missing',
    'Fix Ansible errors when default role directories do not exist',
    body_template('Ansible Default Role Path Missing',
        'Ansible cannot find the default role path.',
        "ERROR! the role 'common' was not found in any of the known roles paths",
        ['Default roles_path does not exist',
         'Custom roles_path not configured',
         'Role directory permissions wrong'],
        """```bash\nmkdir -p ~/.ansible/roles\nmkdir -p /etc/ansible/roles\n\n# Or configure custom path\n```\n\n```ini\n[defaults]\nroles_path = ./roles:~/.ansible/roles:/usr/share/ansible/roles\n```\n\n```bash\nansible-config dump | grep roles_path\n```""")))

PAGES.append(('ansible-galaxy-key-invalid', 'Ansible Galaxy API Key Invalid',
    'Fix Ansible Galaxy authentication key errors',
    body_template('Ansible Galaxy API Key Invalid',
        'Ansible Galaxy rejects the API key for authentication.',
        'ERROR! - AnsibleError: Invalid Galaxy API key',
        ['Expired API key',
         'Wrong key format',
         'Key copied incorrectly'],
        """```bash\nansible-galaxy login --github\n```\n\n```ini\n# ansible.cfg\n[galaxy]\nserver_list = galaxy, automation_hub\n\n[galaxy_server.galaxy]\nurl = https://galaxy.ansible.com/\ntoken = your_galaxy_token\n```""")))

PAGES.append(('ansible-namespace-not-found', 'Ansible Galaxy Namespace Not Found',
    'Fix Ansible Galaxy namespace resolution errors',
    body_template('Ansible Galaxy Namespace Not Found',
        'Ansible Galaxy cannot find the specified namespace.',
        "ERROR! - AnsibleError: Namespace 'invalid_namespace' not found on Galaxy",
        ['Namespace name typo',
         'Namespace does not exist',
         'Collection not published to namespace'],
        """```bash\nansible-galaxy collection install community.general\nansible-galaxy collection list | grep namespace\n```\n\n```yaml\n# Correct FQCN usage\n- name: Install package\n  ansible.builtin.apt:\n    name: nginx\n    state: present\n```""")))

# ====== 7. VAULT ERRORS ======

PAGES.append(('ansible-vault-error', 'Ansible Vault Error',
    'Fix Ansible Vault encryption and decryption errors',
    body_template('Ansible Vault Error',
        'Ansible Vault encounters an error during encryption or decryption.',
        'ERROR! Ansible Vault requires a vault password to decrypt file.yml',
        ['File not properly vault-encrypted',
         'Vault format corrupted',
         'Wrong vault password',
         'Mixed encrypted and plaintext'],
        """```bash\nansible-vault encrypt group_vars/prod/secrets.yml\nansible-vault rekey secrets.yml\nansible-vault view secrets.yml\nansible-vault edit secrets.yml\n```\n\n```bash\nansible-playbook site.yml --ask-vault-pass\nansible-playbook site.yml --vault-password-file .vault_pass\n```""")))

PAGES.append(('ansible-vault-password-required', 'Ansible Vault Password Required',
    'Fix Ansible vault password prompt issues during playbook execution',
    body_template('Ansible Vault Password Required',
        'Ansible prompts for vault password during execution.',
        'Vault password:',
        ['Vault-encrypted variables in playbook',
         'No vault password file configured',
         'Password not provided via CLI'],
        """```bash\nansible-playbook site.yml --ask-vault-pass\nansible-playbook site.yml --vault-password-file ~/.vault_pass\n```\n\n```ini\n# ansible.cfg\n[defaults]\nvault_password_file = ~/.vault_pass\n```\n\n```bash\necho "MyStr0ngP@ssw0rd" > ~/.vault_pass\nchmod 600 ~/.vault_pass\n```""")))

PAGES.append(('ansible-vault-password-file-missing', 'Ansible Vault Password File Missing',
    'Fix Ansible errors when vault password file is not found',
    body_template('Ansible Vault Password File Missing',
        'Ansible cannot find the vault password file.',
        'ERROR! The vault password file /path/to/.vault_pass was not found',
        ['File path incorrect',
         'File not created yet',
         'Permission denied',
         'Wrong working directory'],
        """```bash\necho "MyStr0ngP@ssw0rd" > ~/.vault_pass\nchmod 600 ~/.vault_pass\nls -la ~/.vault_pass\n```\n\n```ini\n[defaults]\nvault_password_file = ~/.vault_pass\n```""")))

PAGES.append(('ansible-vault-decrypt-failed', 'Ansible Vault Decrypt Failed',
    'Fix Ansible vault decryption failures during playbook execution',
    body_template('Ansible Vault Decrypt Failed',
        'Ansible cannot decrypt vault-encrypted content.',
        "ERROR! AnsibleVaultEncryptedUnicode has no attribute 'encrypt'",
        ['Wrong vault password',
         'Vault password changed',
         'File corrupted',
         'Multiple vault IDs mismatched'],
        """```bash\nansible-vault decrypt secrets.yml --vault-password-file .vault_pass\nansible-vault encrypt secrets.yml --vault-password-file .new_vault_pass\nansible-vault view secrets.yml --vault-password-file .vault_pass\n```\n\n```bash\nansible-playbook site.yml --ask-vault-pass -vvv\n```""")))

PAGES.append(('ansible-vault-encrypt-failed', 'Ansible Vault Encrypt Failed',
    'Fix Ansible vault encryption failures when protecting sensitive files',
    body_template('Ansible Vault Encrypt Failed',
        'Ansible cannot encrypt files with vault.',
        "ERROR! Failed to encrypt: 'NoneType' object has no attribute 'encrypt'",
        ['Vault password not provided',
         'File already encrypted',
         'Encryption library issues',
         'File permissions wrong'],
        """```bash\nansible-vault encrypt secrets.yml --vault-password-file .vault_pass\nansible-vault encrypt_string 'secret_value' --name 'db_password'\nansible-vault encrypt secrets.yml --vault-id prod@prompt\n```\n\n```bash\nfor file in group_vars/prod/*.yml; do\n    ansible-vault encrypt "$file" --vault-password-file .vault_pass\ndone\n```""")))

PAGES.append(('ansible-vault-id-not-matched', 'Ansible Vault ID Not Matched',
    'Fix Ansible vault identity mismatch errors',
    body_template('Ansible Vault ID Not Matched',
        'Ansible vault ID does not match any configured vault identity.',
        "ERROR! Vault password id 'prod' not found in vault identity list",
        ['Vault encrypted with different ID',
         'Vault identity not in ansible.cfg',
         'ID name typo'],
        """```ini\n# ansible.cfg\n[defaults]\nvault_identity_list = prod@~/.vault_prod,dev@~/.vault_dev\n```\n\n```bash\nansible-playbook site.yml --vault-id prod@prompt --vault-id dev@prompt\n```\n\n```yaml\n- name: Deploy\n  hosts: all\n  vars_files:\n    - name: vars/common.yml\n    - name: vars/prod_secrets.yml\n      vault_id: prod\n```""")))

PAGES.append(('ansible-vault-secret-not-found', 'Ansible Vault Secret Not Found',
    'Fix Ansible vault errors when secrets cannot be located',
    body_template('Ansible Vault Secret Not Found',
        'Ansible vault cannot find the encrypted secret.',
        "ERROR! The vault secret 'prod' was not found in the vault password files",
        ['Vault password file missing',
         'Vault secret not configured',
         'Wrong vault password file path'],
        """```bash\necho "prod_password" > ~/.vault_prod\necho "dev_password" > ~/.vault_dev\nchmod 600 ~/.vault_prod ~/.vault_dev\n```\n\n```ini\n[defaults]\nvault_identity_list = prod@~/.vault_prod,dev@~/.vault_dev\n```\n\n```bash\nexport ANSIBLE_VAULT_PASSWORD_FILE=~/.vault_${ENV}\nansible-playbook site.yml\n```""")))

PAGES.append(('ansible-vault-unrecognized-format', 'Ansible Vault Format Unrecognized',
    'Fix Ansible vault format detection and parsing errors',
    body_template('Ansible Vault Format Unrecognized',
        'Ansible cannot recognize the vault file format.',
        'ERROR! Vault format not recognized',
        ['File header missing or corrupted',
         'Mixed vault and plaintext content',
         'File encoding issues',
         'Not a valid vault file'],
        """```bash\nhead -1 secrets.yml\n# Should show: $ANSIBLE_VAULT;1.1;AES256\n\nansible-vault decrypt old_secrets.yml --vault-password-file .vault_pass\nansible-vault encrypt new_secrets.yml --vault-password-file .vault_pass\n\nfile secrets.yml\ndos2unix secrets.yml\n```""")))

# ====== 8. FACT/CACHE ERRORS ======

PAGES.append(('ansible-facts-error', 'Ansible Facts Error',
    'Fix Ansible fact gathering and processing errors',
    body_template('Ansible Facts Error',
        'Ansible encounters an error while gathering or processing facts.',
        'ERROR! Failed to gather facts',
        ['gather_facts disabled',
         'Python interpreter issues',
         'Connection timeout during fact gathering',
         'Fact module failure'],
        """```yaml\n- name: Deploy with facts\n  hosts: all\n  gather_facts: true\n  tasks:\n    - name: Use facts\n      ansible.builtin.debug:\n        msg: "OS: {{ ansible_distribution }}"\n\n# Selective fact gathering\n- name: Gather only network\n  ansible.builtin.setup:\n    gather_subset:\n      - network\n```""")))

PAGES.append(('ansible-fact-caching-disabled', 'Ansible Fact Caching Disabled',
    'Enable and configure Ansible fact caching for better performance',
    body_template('Ansible Fact Caching Disabled',
        'Ansible fact caching is not enabled, causing repeated fact gathering.',
        'WARNING: Fact caching is disabled',
        ['fact_caching not set in ansible.cfg',
         'Cache plugin not configured',
         'Cache timeout set to 0'],
        """```ini\n# ansible.cfg - JSON file caching\n[defaults]\nfact_caching = jsonfile\nfact_caching_connection = /tmp/ansible_facts_cache\nfact_caching_timeout = 3600\n\n# Redis-backed caching\n[defaults]\nfact_caching = redis\nfact_caching_connection = localhost:6379:0\nfact_caching_prefix = ansible_facts\n```\n\n```ini\n# Memcached-backed caching\n[defaults]\nfact_caching = memcached\nfact_caching_connection = localhost:11211\nfact_caching_timeout = 7200\n```""")))

PAGES.append(('ansible-cache-plugin-not-found', 'Ansible Cache Plugin Not Found',
    'Fix Ansible cache plugin configuration and availability errors',
    body_template('Ansible Cache Plugin Not Found',
        'Ansible cannot find the specified cache plugin.',
        "ERROR! Cache plugin 'redis' not found",
        ['Cache plugin not installed',
         'Plugin name incorrect',
         'Required Python libraries missing'],
        """```bash\npip install redis\npip install python-memcached\n```\n\n```ini\n[defaults]\nfact_caching = jsonfile\nfact_caching_connection = /tmp/ansible_cache\nfact_caching_timeout = 3600\n```\n\n```bash\nansible-doc -t cache -l\nansible localhost -m setup --cache\n```""")))

PAGES.append(('ansible-cache-timeout-error', 'Ansible Cache Timeout Error',
    'Fix Ansible fact cache timeout configuration issues',
    body_template('Ansible Cache Timeout Error',
        'Ansible cache timeout is set incorrectly or expired.',
        'WARNING: Fact cache timeout expired',
        ['Cache timeout too short',
         'Cache timeout set to 0 (disabled)',
         'Clock sync issues'],
        """```ini\n[defaults]\nfact_caching = jsonfile\nfact_caching_connection = /tmp/ansible_cache\nfact_caching_timeout = 3600  # 1 hour\n\n# Disable timeout (cache forever)\n# fact_caching_timeout = 0\n\n# 24 hour cache\n# fact_caching_timeout = 86400\n```""")))

PAGES.append(('ansible-json-query-failed', 'Ansible json_query Filter Failed',
    'Fix Ansible json_query filter errors when querying JSON data',
    body_template('Ansible json_query Filter Failed',
        'Ansible json_query filter fails to parse or execute the query.',
        'ERROR! Failed to evaluate json_query: jmespath.exceptions.ParseError',
        ['Invalid JMESPath syntax',
         'Missing community.general collection',
         'Query references non-existent path'],
        """```bash\nansible-galaxy collection install community.general\n```\n\n```yaml\n- name: Query JSON data\n  ansible.builtin.debug:\n    msg: "{{ data | community.general.json_query('servers[*].name') }}"\n\n- name: Find active servers\n  ansible.builtin.debug:\n    msg: "{{ servers | community.general.json_query('[?status==`active`].name') }}"\n```""")))

PAGES.append(('ansible-fact-merge-conflict', 'Ansible Fact Merge Conflict',
    'Fix Ansible fact merging conflicts when combining facts from multiple sources',
    body_template('Ansible Fact Merge Conflict',
        'Ansible encounters conflicts when merging facts from different sources.',
        "ERROR! Conflicting fact 'ansible_default_ipv4' from multiple sources",
        ['Multiple fact sources overwriting same keys',
         'Custom facts conflicting with setup module',
         'set_fact overwriting gathered facts'],
        """```yaml\n- name: Deploy\n  hosts: all\n  gather_facts: true\n  gather_subset:\n    - "!all"\n    - network\n  tasks:\n    - name: Add custom facts\n      ansible.builtin.set_fact:\n        custom_fact: "value"\n\n# Merge facts safely\n- name: Combine facts\n  ansible.builtin.set_fact:\n    combined_config: "{{ default_config | combine(custom_config | default({})) }}"\n```""")))

PAGES.append(('ansible-fact-namespace-error', 'Ansible Fact Namespace Error',
    'Fix Ansible fact namespacing and organization errors',
    body_template('Ansible Fact Namespace Error',
        'Ansible encounters errors with fact namespacing.',
        "ERROR! Fact 'ansible_os' conflicts with namespace 'ansible'",
        ['Custom facts using ansible_ prefix',
         'Fact naming collision',
         'Deprecated fact namespacing'],
        """```yaml\n# Use custom namespace for custom facts\n- name: Set custom fact\n  ansible.builtin.set_fact:\n    custom_app_version: "1.0.0"  # Don't use ansible_ prefix\n\n# Access with proper namespace\n- name: Show facts\n  ansible.builtin.debug:\n    msg: "App version: {{ custom_app_version }}"\n```""")))

PAGES.append(('ansible-fact-prefix-collision', 'Ansible Fact Prefix Collision',
    'Fix Ansible fact naming collisions between different modules',
    body_template('Ansible Fact Prefix Collision',
        'Ansible facts from different modules collide.',
        "WARNING: Fact prefix collision: 'ansible_service_mgr' already set",
        ['Multiple modules setting same fact',
         'Custom module overwriting standard facts',
         'Fact priority conflicts'],
        """```yaml\n# Use unique fact names\n- name: Set fact\n  ansible.builtin.set_fact:\n    myapp_service_manager: "systemd"  # Custom prefix\n\n# Check existing facts before setting\n- name: Show service manager\n  ansible.builtin.debug:\n    msg: "Service manager: {{ ansible_service_mgr }}"\n```\n\n# Safe naming convention\n- name: Set app facts\n  ansible.builtin.set_fact:\n    myapp_{{ item.name }}_version: "{{ item.version }}"\n  loop:\n    - { name: nginx, version: "1.18" }\n    - { name: postgresql, version: "13.0" }\n```""")))

# ====== 9. ASYNC/POLL ERRORS ======

PAGES.append(('ansible-async-error', 'Ansible Async Error',
    'Fix Ansible asynchronous task execution errors',
    body_template('Ansible Async Error',
        'Ansible encounters an error with asynchronous task execution.',
        'ERROR! Async task failed',
        ['Module does not support async mode',
         'Async timeout too short',
         'Job ID expired or not found',
         'Poll interval misconfigured'],
        """```yaml\n- name: Long-running task\n  ansible.builtin.command: /opt/scripts/compute.sh\n  async: 3600\n  poll: 0\n  register: async_result\n\n- name: Wait for completion\n  ansible.builtin.async_status:\n    jid: "{{ async_result.ansible_job_id }}"\n  register: job_status\n  until: job_status.finished\n  retries: 60\n  delay: 60\n```""")))

PAGES.append(('ansible-async-task-not-supported', 'Ansible Async Task Not Supported',
    'Fix Ansible async execution errors for unsupported task types',
    body_template('Ansible Async Task Not Supported',
        'Ansible cannot run the specified task asynchronously.',
        'ERROR! Async is not supported for this task type',
        ['Module does not support async mode',
         'Local connection with async',
         'Module requires synchronous execution'],
        """```yaml\n# Modules that support async: command, shell, script, raw, expect\n# Modules that DON'T: copy, template, file, service, systemd\n\n- name: Long-running task\n  ansible.builtin.command: /opt/scripts/compute.sh\n  async: 3600\n  poll: 0\n  register: async_result\n\n# Alternative for non-async tasks\n- name: Wait for completion\n  ansible.builtin.wait_for:\n    path: /tmp/long_task.pid\n    state: absent\n    timeout: 3600\n```""")))

PAGES.append(('ansible-async-timeout', 'Ansible Async Task Timeout',
    'Fix Ansible async task timeout and polling errors',
    body_template('Ansible Async Task Timeout',
        'Ansible async task times out or fails to complete within the specified timeout.',
        'ERROR! Async task timed out after 3600 seconds',
        ['Async timeout too short',
         'Task takes longer than expected',
         'Polling interval too infrequent'],
        """```yaml\n- name: Long task with extended timeout\n  ansible.builtin.command: /opt/scripts/heavy_computation.sh\n  async: 14400\n  poll: 0\n  register: job\n\n- name: Wait for job\n  ansible.builtin.async_status:\n    jid: "{{ job.ansible_job_id }}"\n  register: job_result\n  until: job_result.finished\n  retries: 100\n  delay: 60\n```""")))

PAGES.append(('ansible-jid-not-found', 'Ansible Async Job ID Not Found',
    'Fix Ansible async_status errors when job ID cannot be found',
    body_template('Ansible Async Job ID Not Found',
        'Ansible async_status cannot find the specified job ID.',
        "ERROR! Could not find job ID '12345678901234'",
        ['Job ID expired',
         'Job ID incorrect',
         'Async control files cleaned up',
         'PID file removed'],
        """```yaml\n- name: Start async task\n  ansible.builtin.command: /opt/scripts/task.sh\n  async: 3600\n  poll: 0\n  register: async_task\n\n- name: Wait for task\n  ansible.builtin.async_status:\n    jid: "{{ async_task.ansible_job_id }}"\n  register: task_status\n  until: task_status.finished\n  retries: 60\n  delay: 60\n```""")))

PAGES.append(('ansible-async-finished-incorrectly', 'Ansible Async Task Finished Incorrectly',
    'Fix Ansible async task completion status errors',
    body_template('Ansible Async Task Finished Incorrectly',
        'Ansible async task finished but not as expected.',
        'ERROR! Async task failed with unexpected status',
        ['Task returned error code',
         'Task was killed by system',
         'Task timed out silently',
         'Output not captured correctly'],
        """```yaml\n- name: Start task\n  ansible.builtin.command: /opt/scripts/task.sh\n  async: 3600\n  poll: 0\n  register: async_result\n\n- name: Wait and check\n  ansible.builtin.async_status:\n    jid: "{{ async_result.ansible_job_id }}"\n  register: status\n  until: status.finished\n  retries: 60\n  delay: 60\n\n- name: Handle failure\n  ansible.builtin.debug:\n    msg: "Task failed: {{ status.msg | default('unknown error') }}"\n  when: status.failed\n```""")))

PAGES.append(('ansible-async-retention-limit', 'Ansible Async Retention Limit',
    'Fix Ansible async job retention and cleanup issues',
    body_template('Ansible Async Retention Limit',
        'Ansible async job files exceed retention limits or are cleaned up prematurely.',
        'WARNING: Async job files older than retention period have been cleaned up',
        ['Too many async jobs running simultaneously',
         'Default retention period too short',
         'Disk space issues'],
        """```ini\n[defaults]\nasync_dir = /tmp/.ansible_async\n```\n\n```yaml\n# Clean up old async files\n- name: Clean async files\n  ansible.builtin.find:\n    paths: /tmp/.ansible_async\n    age: "7d"\n  register: old_files\n\n- name: Remove old files\n  ansible.builtin.file:\n    path: "{{ item.path }}"\n    state: absent\n  loop: "{{ old_files.files | default([]) }}"\n```""")))

# ====== 10. DEPLOYMENT/STRATEGY ERRORS ======

PAGES.append(('ansible-delegate-error', 'Ansible Delegate Error',
    'Fix Ansible task delegation errors in playbooks',
    body_template('Ansible Delegate Error',
        'Ansible encounters an error while delegating a task to another host.',
        'ERROR! Task delegation failed',
         ['Target host unreachable',
          'Delegation target not in inventory',
          'Connection issue with delegated host',
          'Delegation loop detected'],
        """```yaml\n- name: Run on local machine\n  hosts: webservers\n  tasks:\n    - name: Local backup\n      ansible.builtin.command: tar czf /tmp/backup.tar.gz /etc\n      delegate_to: localhost\n      run_once: true\n\n    - name: Fetch backup\n      ansible.builtin.fetch:\n        src: /tmp/backup.tar.gz\n        dest: ./backups/\n        flat: true\n```""")))

PAGES.append(('ansible-free-strategy-not-compatible', 'Ansible Free Strategy Not Compatible',
    'Fix Ansible free strategy compatibility issues in playbooks',
    body_template('Ansible Free Strategy Not Compatible',
        'Ansible free strategy is not compatible with certain playbook features.',
        "ERROR! 'free' strategy is not compatible with 'serial'",
        ['Using free strategy with serial',
         'Using free strategy with rescue/always blocks',
         'Incompatible role features'],
        """```yaml\n# Free strategy without serial\n- name: Independent execution\n  hosts: all\n  strategy: free\n  tasks:\n    - name: Run independently\n      ansible.builtin.command: /opt/scripts/setup.sh\n\n# Use linear with serial\n- name: Rolling update\n  hosts: webservers\n  strategy: linear\n  serial: 2\n```""")))

PAGES.append(('ansible-linear-strategy-failure', 'Ansible Linear Strategy Failure',
    'Fix Ansible linear strategy execution failures in playbooks',
    body_template('Ansible Linear Strategy Failure',
        'Ansible linear strategy fails to execute tasks in order.',
        'ERROR! Linear strategy failed: task execution order disrupted',
        ['Task ordering conflicts',
         'Role dependencies affecting order',
         'include_tasks changing execution order'],
        """```yaml\n- name: Ordered deployment\n  hosts: all\n  strategy: linear\n  tasks:\n    - name: Step 1 - Stop service\n      ansible.builtin.service:\n        name: nginx\n        state: stopped\n\n    - name: Step 2 - Update code\n      ansible.builtin.git:\n        repo: https://github.com/example/app.git\n        dest: /opt/app\n\n    - name: Step 3 - Start service\n      ansible.builtin.service:\n        name: nginx\n        state: started\n```""")))

PAGES.append(('ansible-mitogen-connection-error', 'Ansible Mitogen Connection Error',
    'Fix Ansible Mitogen strategy connection and compatibility errors',
    body_template('Ansible Mitogen Connection Error',
        'Ansible Mitogen connection plugin fails to establish connections.',
        'ERROR! mitogen: ConnectionError: [Errno 111] Connection refused',
        ['Mitogen not installed',
         'Mitogen incompatible with Ansible version',
         'Python version mismatch',
         'Connection type not supported by Mitogen'],
        """```bash\npip install mitogen\npython3 -c "import mitogen; print(mitogen.__version__)"\n```\n\n```ini\n# ansible.cfg\n[defaults]\nstrategy = mitogen_linear\nstrategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy\n```\n\n```yaml\n- name: Fast execution with Mitogen\n  hosts: all\n  strategy: mitogen_linear\n```""")))

PAGES.append(('ansible-strategy-plugin-missing', 'Ansible Strategy Plugin Missing',
    'Fix Ansible strategy plugin not found errors',
    body_template('Ansible Strategy Plugin Missing',
        'Ansible cannot find the specified strategy plugin.',
        "ERROR! the strategy plugin 'my_strategy' was not found",
        ['Plugin not installed',
         'Plugin path not configured',
         'Plugin name incorrect'],
        """```ini\n[defaults]\nstrategy_plugins = /path/to/custom/strategy/plugins\nstrategy = custom_strategy\n```\n\n```bash\nansible-doc -t strategy -l\nansible-doc -t strategy linear\n```""")))

PAGES.append(('ansible-throttle-exceeded', 'Ansible Throttle Exceeded',
    'Fix Ansible throttle limit exceeded errors in task execution',
    body_template('Ansible Throttle Exceeded',
        'Ansible throttle limit is exceeded during task execution.',
        'ERROR! Throttle limit exceeded for task',
        ['Throttle value exceeds available forks',
         'Too many concurrent tasks',
         'Resource exhaustion'],
        """```yaml\n- name: API calls with reduced concurrency\n  hosts: all\n  tasks:\n    - name: Call API\n      ansible.builtin.uri:\n        url: "https://api.example.com/endpoint"\n      throttle: 5\n\n# Or increase forks in ansible.cfg\n# [defaults]\n# forks = 50\n```""")))

PAGES.append(('ansible-serial-batch-too-small', 'Ansible Serial Batch Too Small',
    'Fix Ansible serial batch size configuration errors',
    body_template('Ansible Serial Batch Too Small',
        'Ansible serial batch is too small for effective deployment.',
        'ERROR! Serial batch too small: 0 hosts selected',
        ['Serial value set to 0',
         'Serial value larger than available hosts',
         'Percentage calculation results in 0 hosts'],
        """```yaml\n- name: Rolling update\n  hosts: webservers\n  serial: 1\n  tasks:\n    - name: Update\n      ansible.builtin.apt:\n        upgrade: dist\n\n# Multi-stage serial\n- name: Progressive rollout\n  hosts: webservers\n  serial:\n    - 1\n    - "25%"\n    - "50%"\n    - "100%"\n```""")))

PAGES.append(('ansible-max-fail-percentage-exceeded', 'Ansible Max Fail Percentage Exceeded',
    'Fix Ansible max_fail_percentage threshold errors during rolling updates',
    body_template('Ansible Max Fail Percentage Exceeded',
        'Ansible rolling update stops because too many hosts have failed.',
        'FAILED - max_fail_percentage reached, aborting playbook',
        ['max_fail_percentage set too low',
         'Too many hosts failing',
         'Infrastructure issue affecting multiple hosts'],
        """```yaml\n- name: Rolling update with higher threshold\n  hosts: webservers\n  serial: "25%"\n  max_fail_percentage: 30\n  tasks:\n    - name: Update package\n      ansible.builtin.apt:\n        name: nginx\n        state: latest\n\n# Set to 0 for no tolerance\n- name: Strict update\n  hosts: webservers\n  serial: 1\n  max_fail_percentage: 0\n  any_errors_fatal: true\n```""")))

PAGES.append(('ansible-any-errors-fatal-triggered', 'Ansible Any Errors Fatal Triggered',
    'Fix Ansible any_errors_fatal configuration that stops playbook on first error',
    body_template('Ansible Any Errors Fatal Triggered',
        'Ansible playbook stops immediately when any host encounters an error.',
        'FATAL: any_errors_fatal triggered, aborting remaining hosts',
        ['any_errors_fatal: true set on play or task',
         'Critical task failure',
         'Infrastructure issue'],
        """```yaml\n- name: Deploy application\n  hosts: webservers\n  any_errors_fatal: false\n  tasks:\n    - name: Deploy with rescue\n      block:\n        - name: Deploy code\n          ansible.builtin.git:\n            repo: https://github.com/example/app.git\n            dest: /opt/app\n\n        - name: Restart service\n          ansible.builtin.service:\n            name: nginx\n            state: restarted\n      rescue:\n        - name: Rollback on failure\n          ansible.builtin.git:\n            repo: https://github.com/example/app.git\n            dest: /opt/app\n            version: HEAD~1\n```""")))

# ====== 11. WINDOWS-SPECIFIC ======

PAGES.append(('ansible-winrm-winrm-connection-timeout', 'Ansible WinRM Connection Timeout',
    'Fix Ansible WinRM timeout issues when connecting to Windows hosts',
    body_template('Ansible WinRM Connection Timeout',
        'WinRM connection times out when Ansible tries to reach Windows hosts.',
        'UNREACHABLE! => "winrm connection error: timed out"',
        ['WinRM service not started',
         'Firewall blocking ports 5985/5986',
         'Host overloaded',
         'Network latency'],
        """```powershell\n# On Windows\nwinrm quickconfig -force\n```\n\n```yaml\n[win]\nwinserver ansible_host=10.0.0.50 ansible_winrm_operation_timeout_sec=60\n\n# Or in playbook vars\n- hosts: win\n  vars:\n    ansible_winrm_operation_timeout_sec: 120\n    ansible_winrm_read_timeout_sec: 120\n```""")))

PAGES.append(('ansible-winrm-winrm-certificate-error', 'Ansible WinRM Certificate Error',
    'Fix WinRM SSL certificate errors in Ansible Windows management',
    body_template('Ansible WinRM Certificate Error',
        'WinRM connection fails due to SSL certificate issues.',
        'UNREACHABLE! => SSLError: certificate verify failed',
        ['Self-signed certificate',
         'Certificate not trusted',
         'Hostname mismatch'],
        """```ini\n# ansible.cfg (testing only)\n[winrm]\nserver_cert_validation = ignore\n```\n\n```powershell\nNew-SelfSignedCertificate -DnsName "winserver" -CertStoreLocation Cert:\\LocalMachine\\My\n```""")))

PAGES.append(('ansible-winrm-winrm-basic-auth-disabled', 'Ansible WinRM Basic Auth Disabled',
    'Enable basic authentication for WinRM in Ansible Windows management',
    body_template('Ansible WinRM Basic Auth Disabled',
        'WinRM rejects basic authentication.',
        'UNREACHABLE! => "Basic auth is not enabled"',
        ['Basic auth disabled on Windows host',
         'Group policy restrictions',
         'WinRM misconfiguration'],
        """```powershell\nwinrm set winrm/config/service/auth '@{Basic="true"}'\nwinrm set winrm/config/service '@{AllowUnencrypted="true"}'\n```\n\n```yaml\n[win]\nwinserver ansible_connection=winrm ansible_winrm_transport=basic\n```""")))

PAGES.append(('ansible-winrm-winrm-negotiate-error', 'Ansible WinRM Negotiate Error',
    'Fix WinRM negotiate authentication errors in Ansible Windows playbooks',
    body_template('Ansible WinRM Negotiate Error',
        'WinRM negotiate authentication fails.',
        'UNREACHABLE! => "winrm connection error: negotiate auth failed"',
        ['Kerberos not configured',
         'Time sync issues',
         'NTLM not enabled'],
        """```yaml\n[win]\nwinserver ansible_connection=winrm ansible_winrm_transport=ntlm ansible_user=administrator\n```\n\n```bash\nsudo apt-get install krb5-user python3-winrm\n```""")))

PAGES.append(('ansible-powershell-not-available', 'Ansible PowerShell Not Available',
    'Fix Ansible errors when PowerShell is not found on Windows hosts',
    body_template('Ansible PowerShell Not Available',
        'Ansible cannot find PowerShell on the Windows host.',
        'FAILED! => "PowerShell not found on remote host"',
        ['PowerShell not installed',
         'PowerShell not in PATH',
         'PowerShell execution policy restricted'],
        """```powershell\nInstall-WindowsFeature -Name PowerShell -IncludeAllSubFeature\n```\n\n```yaml\n- hosts: win\n  vars:\n    ansible_powershell_executable: "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"\n  tasks:\n    - name: Run PowerShell command\n      ansible.windows.win_shell: Write-Output "Hello"\n```""")))

PAGES.append(('ansible-windows-feature-not-found', 'Ansible Windows Feature Not Found',
    'Fix Ansible errors when Windows features cannot be found or installed',
    body_template('Ansible Windows Feature Not Found',
        'Ansible cannot find or install a Windows feature.',
        "FAILED! => Feature 'Web-Server' not found",
        ['Feature name incorrect',
         'Feature not available on OS version',
         'Source files missing'],
        """```yaml\n- name: List Windows features\n  ansible.windows.win_feature_info:\n  register: features\n\n- name: Install IIS\n  ansible.windows.win_feature:\n    name:\n      - Web-Server\n      - Web-Mgmt-Tools\n    state: present\n    include_sub_features: true\n    include_management_tools: true\n```""")))

PAGES.append(('ansible-chocolatey-package-error', 'Ansible Chocolatey Package Error',
    'Fix Ansible Chocolatey package manager errors on Windows',
    body_template('Ansible Chocolatey Package Error',
        'Ansible Chocolatey module fails to manage packages.',
        'FAILED! => "choco install failed: The package was not found"',
        ['Package name incorrect',
         'Chocolatey not installed',
         'Package not in Chocolatey repository'],
        """```yaml\n# Install Chocolatey first\n- name: Install Chocolatey\n  ansible.windows.win_shell: >\n    Set-ExecutionPolicy Bypass -Scope Process -Force;\n    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))\n\n# Install packages\n- name: Install packages via Chocolatey\n  community.windows.win_chocolatey:\n    name:\n      - googlechrome\n      - notepadplusplus\n      - vscode\n    state: present\n```""")))

PAGES.append(('ansible-iis-module-failed', 'Ansible IIS Module Failed',
    'Fix Ansible IIS management module errors on Windows',
    body_template('Ansible IIS Module Failed',
        'Ansible IIS module fails to manage IIS configuration.',
        'FAILED! => "IIS module failed: WebAdministration module not available"',
        ['IIS not installed',
         'WebAdministration module missing',
         'Insufficient permissions'],
        """```yaml\n# Install IIS first\n- name: Install IIS\n  ansible.windows.win_feature:\n    name: Web-Server\n    state: present\n\n# Then manage IIS\n- name: Create IIS site\n  community.windows.win_iis_webbinding:\n    name: "Default Web Site"\n    port: 80\n    protocol: http\n    state: present\n```""")))

PAGES.append(('ansible-windows-reboot-timeout', 'Ansible Windows Reboot Timeout',
    'Fix Ansible Windows reboot timeout errors during patch management',
    body_template('Ansible Windows Reboot Timeout',
        'Ansible Windows reboot operation times out.',
        'FAILED! => "Reboot timeout exceeded"',
        ['Windows update taking too long',
         'Service preventing reboot',
         'Timeout value too low',
         'System hanging during shutdown'],
        """```yaml\n- name: Reboot with extended timeout\n  ansible.windows.win_reboot:\n    reboot_timeout: 1200  # 20 minutes\n    pre_reboot_delay: 5\n    post_reboot_delay: 30\n    msg: "Rebooting for updates"\n\n# Or handle with async\n- name: Reboot server\n  ansible.windows.win_reboot:\n    reboot_timeout: 3600\n  async: 3600\n  poll: 60\n```""")))

PAGES.append(('ansible-win-psexec-not-found', 'Ansible win_psexec Not Found',
    'Fix Ansible win_psexec module errors when managing remote Windows processes',
    body_template('Ansible win_psexec Not Found',
        'Ansible win_psexec module is not available or not working.',
        "ERROR! The 'ansible.windows.win_psexec' module is not available",
        ['ansible.windows collection not installed',
         'PSExec not available on target',
         'Module name incorrect'],
        """```bash\nansible-galaxy collection install ansible.windows\n```\n\n```yaml\n- name: Run command via PSExec\n  ansible.windows.win_psexec:\n    command: whoami\n    host: 10.0.0.50\n    username: administrator\n    password: "{{ vault_win_password }}"\n    interactive: true\n```\n\n```yaml\n# Full example\n- name: Execute remote command\n  ansible.windows.win_psexec:\n    command: "cmd.exe /c echo hello > C:\\\\temp\\\\output.txt"\n    host: "{{ target_host }}"\n    username: "{{ win_user }}"\n    password: "{{ win_password }}"\n    executable: C:\\\\Windows\\\\System32\\\\psexec.exe\n    elevated: true\n```""")))

# ====== 12. INVENTORY ERRORS ======

PAGES.append(('ansible-inventory-script-failed', 'Ansible Inventory Script Failed',
    'Fix Ansible dynamic inventory script execution errors',
    body_template('Ansible Inventory Script Failed',
        'Ansible dynamic inventory script fails to execute or return valid JSON.',
        'ERROR! Failed to parse inventory script',
        ['Script not executable',
         'Script returns invalid JSON',
         'Script dependencies missing',
         'Script timeout'],
        """```bash\n# Make script executable\nchmod +x inventory_script.py\n\n# Test manually\n./inventory_script.py --list\n./inventory_script.py --host web1\n```\n\n```ini\n[defaults]\ninventory = ./inventory_script.py\n```\n\n```yaml\n# Inventory script must return JSON\n# --list output:\n{\n  "webservers": {\n    "hosts": ["web1", "web2"],\n    "vars": {"http_port": 80}\n  }\n}\n\n# --host output:\n{"ansible_host": "192.168.1.100"}\n```""")))

PAGES.append(('ansible-inventory-plugin-not-found', 'Ansible Inventory Plugin Not Found',
    'Fix Ansible inventory plugin configuration and availability errors',
    body_template('Ansible Inventory Plugin Not Found',
        'Ansible cannot find the specified inventory plugin.',
        "ERROR! Could not find inventory plugin 'aws_ec2'",
        ['Plugin not installed',
         'Collection not installed',
         'Plugin name incorrect'],
        """```bash\n# Install required collection\nansible-galaxy collection install amazon.aws\n\n# List available inventory plugins\nansible-doc -t inventory -l\n```\n\n```yaml\n# aws_ec2.yml inventory\nplugin: amazon.aws.aws_ec2\nregions:\n  - us-east-1\nkeyed_groups:\n  - key: tags.Name\n    prefix: tag\nfilters:\n  tag:Environment: production\n```\n\n```ini\n# Use in ansible.cfg\n[defaults]\ninventory = aws_ec2.yml\n```""")))

PAGES.append(('ansible-invalid-inventory-format', 'Ansible Invalid Inventory Format',
    'Fix Ansible inventory file format and syntax errors',
    body_template('Ansible Invalid Inventory Format',
        'Ansible cannot parse the inventory file format.',
        'ERROR! Failed to parse inventory file',
        ['YAML syntax errors in inventory',
         'INI format issues',
         'Mixed format not supported',
         'Missing required fields'],
        """```ini\n# INI format\n[webservers]\nweb1 ansible_host=192.168.1.100\nweb2 ansible_host=192.168.1.101\n\n[webservers:vars]\nhttp_port=80\nansible_user=admin\n\n# YAML format\n---\nall:\n  children:\n    webservers:\n      hosts:\n        web1:\n          ansible_host: 192.168.1.100\n        web2:\n          ansible_host: 192.168.1.101\n      vars:\n        http_port: 80\n```""")))

PAGES.append(('ansible-host-range-overflow', 'Ansible Host Range Overflow',
    'Fix Ansible host range syntax errors in inventory files',
    body_template('Ansible Host Range Overflow',
        'Ansible host range generates too many hosts or is invalid.',
        'ERROR! Host range overflow: too many hosts generated',
        ['Range too large',
         'Invalid range syntax',
         'Memory issues with large ranges'],
        """```ini\n# CORRECT ranges\n[webservers]\nweb[01:10].example.com     # web01 to web10\napp-[a:f].example.com       # app-a to app-f\n\n# WRONG - too large\n# server[0001:99999].example.com  # Don't do this\n\n# Use patterns wisely\n[webservers]\nweb-01.example.com\nweb-02.example.com\nweb-03.example.com\n```""")))

PAGES.append(('ansible-group-not-found', 'Ansible Group Not Found',
    'Fix Ansible errors when referenced inventory groups do not exist',
    body_template('Ansible Group Not Found',
        'Ansible playbook references an inventory group that does not exist.',
        "ERROR! No hosts matched for group 'nonexistent_group'",
        ['Group name typo',
         'Group not defined in inventory',
         'Dynamic inventory not returning group',
         'Group defined in wrong inventory file'],
        """```ini\n# Verify group exists\nansible-inventory --list | grep group_name\n\n# Check group hosts\nansible webservers --list-hosts\n```\n\n```yaml\n# Define group properly\n[webservers]\nweb1 ansible_host=192.168.1.100\nweb2 ansible_host=192.168.1.101\n\n[dbservers]\ndb1 ansible_host=192.168.1.200\n```\n\n```yaml\n# Use group with fallback\n- name: Deploy\n  hosts: "{{ target_group | default('all') }}"\n```""")))

PAGES.append(('ansible-parent-group-not-found', 'Ansible Parent Group Not Found',
    'Fix Ansible errors when parent groups in inventory hierarchy are missing',
    body_template('Ansible Parent Group Not Found',
        'Ansible inventory references a parent group that does not exist.',
        "ERROR! Parent group 'production' not found",
        ['Parent group not defined',
         'Group hierarchy typo',
         'Dynamic inventory missing parent'],
        """```ini\n# Define parent group properly\n[production:children]\nwebservers\ndbservers\n\n[staging:children]\nstaging_web\nstaging_db\n\n[webservers]\nweb1 ansible_host=192.168.1.100\n\n[dbservers]\ndb1 ansible_host=192.168.1.200\n\n# For dynamic inventory\n# Script must return parent group relationships\n```""")))

PAGES.append(('ansible-group-recursion-detected', 'Ansible Group Recursion Detected',
    'Fix Ansible circular group membership in inventory files',
    body_template('Ansible Group Recursion Detected',
        'Ansible detects circular group membership.',
        'ERROR! Circular group membership detected',
        ['Group A contains Group B which contains Group A',
         'Group inherits from itself',
         'Recursive children definition'],
        """```ini\n# WRONG - circular\n[group_a:children]\ngroup_b\n\n[group_b:children]\ngroup_a\n\n# CORRECT - flat hierarchy\n[production:children]\nwebservers\ndbservers\n\n[webservers]\nweb1\nweb2\n\n[dbservers]\ndb1\ndb2\n\n# Use :vars for shared variables\n[production:vars]\nenv=production\n```""")))

PAGES.append(('ansible-inventory-cache-expired', 'Ansible Inventory Cache Expired',
    'Fix Ansible inventory caching issues with dynamic inventory',
    body_template('Ansible Inventory Cache Expired',
        'Ansible dynamic inventory cache has expired or is invalid.',
        'WARNING: Inventory cache expired, refreshing...',
        ['Cache timeout set too short',
         'Cache file corrupted',
         'Dynamic source changed while cache valid'],
        """```ini\n# ansible.cfg - inventory caching\n[defaults]\ncache = True\ncache_connection = /tmp/ansible_inventory_cache\ncache_timeout = 300  # 5 minutes\n\n# For specific plugin\n[inventory_plugins.aws_ec2]\ncache = True\ncache_timeout = 600\n```\n\n```bash\n# Force cache refresh\nansible-inventory --refresh-cache -i aws_ec2.yml\n\n# Clear cache manually\nrm -f /tmp/ansible_inventory_cache*\n```""")))

PAGES.append(('ansible-host-file-not-found', 'Ansible Host File Not Found',
    'Fix Ansible errors when the inventory host file is missing',
    body_template('Ansible Host File Not Found',
        'Ansible cannot find the specified inventory or host file.',
        'ERROR! Could not find inventory file /path/to/hosts',
        ['File path incorrect',
         'File not created',
         'File permissions wrong',
         'Working directory different'],
        """```ini\n# ansible.cfg\n[defaults]\ninventory = ./inventory/hosts\n```\n\n```bash\n# Create inventory directory and file\nmkdir -p inventory\ncat > inventory/hosts << 'EOF'\n[webservers]\nweb1 ansible_host=192.168.1.100\n\n[dbservers]\ndb1 ansible_host=192.168.1.200\nEOF\n\n# Verify inventory\nansible-inventory --list\nansible-inventory --graph\n```""")))

# ====== 13. HANDLER AND SPECIAL ERRORS ======

PAGES.append(('ansible-handler-error', 'Ansible Handler Error',
    'Fix Ansible handler notification and execution errors',
    body_template('Ansible Handler Error',
        'Ansible handler fails to execute or is notified incorrectly.',
        'ERROR! Handler "restart nginx" not found',
        ['Handler name typo',
         'Handler not defined in handlers section',
         'Handler in wrong file',
         'Notification name mismatch'],
        """```yaml\n# Define handler in handlers/main.yml\n---\n- name: restart nginx\n  ansible.builtin.service:\n    name: nginx\n    state: restarted\n\n# Notify with correct name\n- name: Update config\n  ansible.builtin.template:\n    src: nginx.conf.j2\n    dest: /etc/nginx/nginx.conf\n  notify: restart nginx\n```""")))

PAGES.append(('ansible-block-rescue-error', 'Ansible Block Rescue Error',
    'Fix Ansible block/rescue/always error handling patterns',
    body_template('Ansible Block Rescue Error',
        'Ansible block/rescue/always pattern has errors.',
        'ERROR! Invalid block structure',
        ['Missing rescue or always block',
         'Tasks not inside block',
         'Nested block errors',
         'Variable scope in rescue'],
        """```yaml\n- name: Deploy with error handling\n  hosts: webservers\n  tasks:\n    - name: Deploy application\n      block:\n        - name: Deploy code\n          ansible.builtin.git:\n            repo: https://github.com/example/app.git\n            dest: /opt/app\n\n        - name: Restart service\n          ansible.builtin.service:\n            name: nginx\n            state: restarted\n      rescue:\n        - name: Rollback\n          ansible.builtin.git:\n            repo: https://github.com/example/app.git\n            dest: /opt/app\n            version: HEAD~1\n      always:\n        - name: Check status\n          ansible.builtin.service:\n            name: nginx\n            state: started\n```""")))

PAGES.append(('ansible-assert-error', 'Ansible Assert Error',
    'Fix Ansible assert module validation failures',
    body_template('Ansible Assert Error',
        'Ansible assert module fails a validation check.',
        'FAIL! Assertion failed: custom_msg',
        ['Condition evaluates to false',
         'Variable not as expected',
         'Validation logic incorrect'],
        """```yaml\n- name: Validate variables\n  ansible.builtin.assert:\n    that:\n      - deploy_env is defined\n      - deploy_env in ['dev', 'staging', 'production']\n      - app_version is defined\n    fail_msg: "Required variables not set correctly"\n    success_msg: "All validations passed"\n\n# With custom message\n- name: Check disk space\n  ansible.builtin.assert:\n    that:\n      - ansible_mounts | selectattr('mount', 'equalto', '/') | map(attribute='size_available') | first > 1073741824\n    fail_msg: "Less than 1GB free space on root"\n```""")))

PAGES.append(('ansible-service-error', 'Ansible Service Error',
    'Fix Ansible service management module errors',
    body_template('Ansible Service Error',
        'Ansible service module fails to manage system services.',
        'FAILED! => "Service "nginx" not found"',
        ['Service name incorrect',
         'Service not installed',
         'Init system not supported',
         'Service file missing'],
        """```yaml\n- name: Start nginx service\n  ansible.builtin.service:\n    name: nginx\n    state: started\n    enabled: true\n\n# Or use systemd explicitly\n- name: Start with systemd\n  ansible.builtin.systemd:\n    name: nginx\n    state: started\n    enabled: true\n    daemon_reload: true\n```\n\n```bash\n# Check available services\nsystemctl list-unit-files | grep nginx\n```""")))

PAGES.append(('ansible-copy-error', 'Ansible Copy Error',
    'Fix Ansible copy module file transfer errors',
    body_template('Ansible Copy Error',
        'Ansible copy module fails to transfer files.',
        'FAILED! => "Could not find or access source file"',
        ['Source file not found',
         'Destination path invalid',
         'Permission denied',
         'Disk space full'],
        """```yaml\n- name: Copy configuration file\n  ansible.builtin.copy:\n    src: files/app.conf\n    dest: /etc/app/app.conf\n    owner: root\n    group: root\n    mode: '0644'\n    backup: true\n\n# Copy with content\n- name: Create config file\n  ansible.builtin.copy:\n    content: |\n      server_name {{ inventory_hostname }}\n      listen 80\n    dest: /etc/nginx/conf.d/default.conf\n```""")))

PAGES.append(('ansible-set-fact-error', 'Ansible set_fact Error',
    'Fix Ansible set_fact module configuration errors',
    body_template('Ansible set_fact Error',
        'Ansible set_fact module fails to set or register a variable.',
        'ERROR! set_fact failed',
        ['Invalid variable name',
         'Expression evaluation error',
         'Cacheable option wrong type',
         'Variable name conflicts with built-in'],
        """```yaml\n# Set simple fact\n- name: Set application name\n  ansible.builtin.set_fact:\n    app_name: "my-application"\n\n# Set complex fact\n- name: Set server config\n  ansible.builtin.set_fact:\n    server_config:\n      port: 80\n      ssl: true\n      max_connections: 1000\n\n# Set with cacheable\n- name: Set persistent fact\n  ansible.builtin.set_fact:\n    detected_os: "{{ ansible_distribution }}"\n    cacheable: true\n```\n\n# Variable naming:\n# GOOD: app_name, server_config, deploy_version\n# BAD: ansible_distribution, inventory_hostname (reserved)\n```""")))

# ====== MAIN EXECUTION ======

count = 0
skipped = 0
for slug, title, desc, body in PAGES:
    if slug in EXISTING:
        print(f"SKIP (exists): {slug}")
        skipped += 1
        continue
    content = make_page(title, desc, body)
    path = os.path.join(BASE, f"{slug}.md")
    with open(path, 'w') as f:
        f.write(content)
    count += 1
    print(f"CREATED: {slug}")

print(f"\nTotal pages defined: {len(PAGES)}")
print(f"Skipped (already exist): {skipped}")
print(f"Created: {count}")
print(f"Total ansible pages now: {len(EXISTING) + count}")
