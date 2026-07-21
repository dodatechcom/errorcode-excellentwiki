#!/usr/bin/env python3
import os

OUTPUT_DIR = "/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/vagrant"
TOOL = "vagrant"

existing = set()
for f in os.listdir(OUTPUT_DIR):
    if f.endswith(".md") and f != "_index.md":
        existing.add(f.replace(".md", ""))

pages = [
    ("vagrant-vagrantfile-syntax-error", "Vagrantfile Syntax Error", "Fix Vagrantfile Ruby syntax errors."),
    ("vagrant-config-vm-box-not-specified", "Vagrant config.vm.box Not Specified", "Resolve missing box configuration errors."),
    ("vagrant-box-not-found", "Vagrant Box Not Found", "Fix box not found errors when running vagrant up."),
    ("vagrant-box-download-failed", "Vagrant Box Download Failed", "Resolve box download failure errors."),
    ("vagrant-box-outdated", "Vagrant Box Outdated", "Fix outdated box warning and version errors."),
    ("vagrant-box-version-constraint", "Vagrant Box Version Constraint Error", "Resolve box version constraint errors."),
    ("vagrant-provider-not-found", "Vagrant Provider Not Found", "Fix provider not found errors in Vagrant."),
    ("vagrant-virtualbox-not-installed", "Vagrant VirtualBox Not Installed", "Resolve VirtualBox not installed errors."),
    ("vagrant-vmware-not-available", "Vagrant VMware Not Available", "Fix VMware provider availability errors."),
    ("vagrant-hyperv-not-available", "Vagrant Hyper-V Not Available", "Resolve Hyper-V provider availability errors."),
    ("vagrant-libvirt-provider-error", "Vagrant Libvirt Provider Error", "Fix libvirt provider configuration errors."),
    ("vagrant-provider-specific-config", "Vagrant Provider Specific Config Error", "Resolve provider-specific configuration errors."),
    ("vagrant-synced-folder-error", "Vagrant Synced Folder Error", "Fix synced folder configuration errors."),
    ("vagrant-nfs-mount-failed", "Vagrant NFS Mount Failed", "Resolve NFS mount failure errors."),
    ("vagrant-smb-mount-failed", "Vagrant SMB Mount Failed", "Fix SMB mount failure errors in Vagrant."),
    ("vagrant-rsync-sync-error", "Vagrant RSync Sync Error", "Resolve RSync synchronization errors."),
    ("vagrant-virtualbox-shared-folder", "Vagrant VirtualBox Shared Folder Error", "Fix VirtualBox shared folder errors."),
    ("vagrant-folder-not-found", "Vagrant Folder Not Found", "Resolve folder not found errors in Vagrant."),
    ("vagrant-host-path-not-exist", "Vagrant Host Path Not Exist", "Fix host path not exist errors."),
    ("vagrant-guest-path-not-exist", "Vagrant Guest Path Not Exist", "Resolve guest path not exist errors."),
    ("vagrant-network-config-error", "Vagrant Network Configuration Error", "Fix network configuration errors."),
    ("vagrant-private-network-ip-conflict", "Vagrant Private Network IP Conflict", "Resolve private network IP conflict errors."),
    ("vagrant-public-network-bridge", "Vagrant Public Network Bridge Error", "Fix public network bridge configuration errors."),
    ("vagrant-forwarded-port-conflict", "Vagrant Forwarded Port Conflict", "Resolve forwarded port conflict errors."),
    ("vagrant-port-collision", "Vagrant Port Collision", "Fix port collision errors in Vagrant."),
    ("vagrant-auto-correct-port", "Vagrant Auto Correct Port", "Resolve auto_correct port configuration errors."),
    ("vagrant-hostname-not-set", "Vagrant Hostname Not Set", "Fix hostname configuration errors."),
    ("vagrant-ssh-connection-refused", "Vagrant SSH Connection Refused", "Resolve SSH connection refused errors."),
    ("vagrant-ssh-auth-failed", "Vagrant SSH Auth Failed", "Fix SSH authentication failure errors."),
    ("vagrant-ssh-key-not-found", "Vagrant SSH Key Not Found", "Resolve SSH key not found errors."),
    ("vagrant-ssh-agent-forwarding", "Vagrant SSH Agent Forwarding Error", "Fix SSH agent forwarding configuration errors."),
    ("vagrant-insecure-key-replaced", "Vagrant Insecure Key Replaced", "Resolve insecure key replacement warnings."),
    ("vagrant-guest-addition-version-mismatch", "Vagrant Guest Addition Version Mismatch", "Fix guest addition version mismatch errors."),
    ("vagrant-vm-boot-timeout", "Vagrant VM Boot Timeout", "Resolve VM boot timeout errors."),
    ("vagrant-halt-timeout", "Vagrant Halt Timeout", "Fix halt timeout errors in Vagrant."),
    ("vagrant-suspend-failed", "Vagrant Suspend Failed", "Resolve suspend failure errors."),
    ("vagrant-resume-failed", "Vagrant Resume Failed", "Fix resume failure errors in Vagrant."),
    ("vagrant-destroy-error", "Vagrant Destroy Error", "Resolve destroy error and cleanup failures."),
    ("vagrant-package-vm-error", "Vagrant Package VM Error", "Fix VM packaging errors in Vagrant."),
    ("vagrant-package-output-error", "Vagrant Package Output Error", "Resolve package output path errors."),
    ("vagrant-share-error", "Vagrant Share Error", "Fix vagrant share configuration errors."),
    ("vagrant-cloud-error", "Vagrant Cloud Error", "Resolve Vagrant Cloud interaction errors."),
    ("vagrant-atlas-login-failed", "Vagrant Atlas Login Failed", "Fix Vagrant Cloud (Atlas) login failures."),
    ("vagrant-box-upload-error", "Vagrant Box Upload Error", "Resolve box upload errors to Vagrant Cloud."),
    ("vagrant-box-release-error", "Vagrant Box Release Error", "Fix box release creation errors."),
    ("vagrant-provider-plugin-not-installed", "Vagrant Provider Plugin Not Installed", "Resolve provider plugin not installed errors."),
    ("vagrant-plugin-install-error", "Vagrant Plugin Install Error", "Fix vagrant plugin install failure errors."),
    ("vagrant-plugin-not-found", "Vagrant Plugin Not Found", "Resolve plugin not found errors in Vagrant."),
    ("vagrant-plugin-conflict", "Vagrant Plugin Conflict", "Fix plugin conflict errors in Vagrant."),
    ("vagrant-provision-error", "Vagrant Provision Error", "Resolve provisioner execution errors."),
    ("vagrant-shell-provisioner-error", "Vagrant Shell Provisioner Error", "Fix shell provisioner configuration errors."),
    ("vagrant-ansible-provisioner-not-found", "Vagrant Ansible Provisioner Not Found", "Resolve Ansible provisioner not found errors."),
    ("vagrant-ansible-local-provisioner", "Vagrant Ansible Local Provisioner Error", "Fix Ansible local provisioner errors."),
    ("vagrant-chef-provisioner-error", "Vagrant Chef Provisioner Error", "Resolve Chef provisioner configuration errors."),
    ("vagrant-puppet-provisioner-error", "Vagrant Puppet Provisioner Error", "Fix Puppet provisioner configuration errors."),
    ("vagrant-docker-provisioner-error", "Vagrant Docker Provisioner Error", "Resolve Docker provisioner errors in Vagrant."),
    ("vagrant-provisioner-run-order", "Vagrant Provisioner Run Order Error", "Fix provisioner run order configuration errors."),
    ("vagrant-provision-once-vs-always", "Vagrant Provision Once vs Always", "Resolve provision once vs always configuration errors."),
    ("vagrant-up-error", "Vagrant Up Error", "Fix vagrant up execution errors."),
    ("vagrant-reload-error", "Vagrant Reload Error", "Resolve vagrant reload failure errors."),
    ("vagrant-halt-error", "Vagrant Halt Error", "Fix vagrant halt execution errors."),
    ("vagrant-destroy-error-new", "Vagrant Destroy Error New", "Resolve vagrant destroy execution errors."),
    ("vagrant-status-error", "Vagrant Status Error", "Fix vagrant status display errors."),
    ("vagrant-global-status-error", "Vagrant Global Status Error", "Resolve vagrant global-status errors."),
    ("vagrant-snapshot-error", "Vagrant Snapshot Error", "Fix snapshot management errors in Vagrant."),
    ("vagrant-snapshot-save-failed", "Vagrant Snapshot Save Failed", "Resolve snapshot save failure errors."),
    ("vagrant-snapshot-restore-error", "Vagrant Snapshot Restore Error", "Fix snapshot restore failure errors."),
    ("vagrant-multi-machine-config", "Vagrant Multi-Machine Config Error", "Resolve multi-machine configuration errors."),
    ("vagrant-machine-not-defined", "Vagrant Machine Not Defined", "Fix machine not defined errors in Vagrantfile."),
    ("vagrant-primary-machine-not-set", "Vagrant Primary Machine Not Set", "Resolve primary machine configuration errors."),
    ("vagrant-machine-autostart", "Vagrant Machine Autostart Error", "Fix machine autostart configuration errors."),
    ("vagrant-machine-boot-order", "Vagrant Machine Boot Order Error", "Resolve machine boot order configuration errors."),
    ("vagrant-trigger-error", "Vagrant Trigger Error", "Fix trigger configuration errors in Vagrant."),
    ("vagrant-trigger-action-syntax", "Vagrant Trigger Action Syntax Error", "Resolve trigger action syntax errors."),
    ("vagrant-trigger-on-guest", "Vagrant Trigger On Guest Error", "Fix trigger on:guest configuration errors."),
    ("vagrant-trigger-blocking", "Vagrant Trigger Blocking Error", "Resolve trigger blocking configuration errors."),
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
        + desc + ' This error occurs when Vagrant encounters virtual machine, configuration, or provider problems.\n\n'
        '## Common Causes\n\n'
        '- Incorrect Vagrantfile configuration\n'
        '- Provider not installed or misconfigured\n'
        '- Network or synced folder issues\n'
        '- Virtual machine resource constraints\n\n'
        '## How to Fix\n\n'
        '### Solution 1: Check Vagrantfile Syntax\n\n'
        'Validate your Vagrantfile Ruby syntax:\n\n'
        '```ruby\n'
        'Vagrant.configure("2") do |config|\n'
        '  config.vm.box = "ubuntu/focal64"\n'
        '  config.vm.network "forwarded_port", guest: 80, host: 8080\n'
        'end\n'
        '```\n\n'
        '### Solution 2: Verify Provider\n\n'
        '```bash\n'
        '# Check available providers\n'
        'vagrant status\n\n'
        '# Verify provider is installed\n'
        'vagrant plugin list\n'
        '```\n\n'
        '### Solution 3: Debug with Verbose Output\n\n'
        '```bash\n'
        'vagrant up --debug\n'
        '```\n\n'
        'The `--debug` flag provides detailed logging for troubleshooting.\n\n'
        '## Example\n\n'
        '```ruby\n'
        '# Vagrantfile example\n'
        'Vagrant.configure("2") do |config|\n'
        '  config.vm.box = "ubuntu/focal64"\n'
        '  config.vm.provider "virtualbox" do |vb|\n'
        '    vb.memory = "2048"\n'
        '    vb.cpus = 2\n'
        '  end\n'
        'end\n'
        '```\n\n'
        '## Related Links\n\n'
        '- [Vagrant Documentation](https://www.vagrantup.com/docs)\n'
        '- [Vagrant Troubleshooting](https://www.vagrantup.com/docs/troubleshooting)\n'
    )
    filepath = os.path.join(OUTPUT_DIR, slug + ".md")
    with open(filepath, "w") as f:
        f.write(content)
    count += 1
    existing.add(slug)

print("Vagrant: created " + str(count) + " new pages (total: " + str(count + 30) + ")")
