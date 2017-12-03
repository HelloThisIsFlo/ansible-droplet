import click
import os.path
from os import symlink
import subprocess

SCRIPT_DIR = os.path.dirname(__file__)

ANSIBLE = os.path.join(SCRIPT_DIR, 'ansible')
REQUIREMENTS = 'roles/roles-on-droplet/roles-from-ansible-galaxy'
CONFIGURATION = 'group_vars'
CONFIGURATION_FILE = 'all'
INVENTORY = 'inventory'
INVENTORY_DROPLETS_LINK = 'ansible-droplets'
INVENTORY_DROPLETS_FILE = '.ansible-droplet-inventory'
CREATE_PLAYBOOK = 'create-droplet-playbook.yml'
DESTROY_PLAYBOOK = 'delete-droplet-playbook.yml'

DEFAULT_SSH_KEY = '{{ ansible_env.HOME }}/.ssh/id_rsa.pub'
# DEFAULT_DO_TOKEN = '"{{ ansible_env.HOME }}/secrets/digitalocean/token"'

def _install_requirements_if_needed():
    if not _are_requirements_installed():
        _install_requirements()

def _are_requirements_installed():
    return os.path.exists(os.path.join(ANSIBLE, REQUIREMENTS))

def _install_requirements():
    cmd = [
        'ansible-galaxy', 'install',
        '-r', './requirements.yml',
        '-p', '%s' % os.path.join("./", REQUIREMENTS)
    ]
    _run(cmd)

def _set_configuration_if_needed():
    if not _is_configured():
        ssh_key, do_token = _ask_for_configuration()
        _create_configuration_file(ssh_key, do_token)

    if not _has_droplet_inventory_symlink():
        _create_droplet_inventory_symlink()

def _is_configured():
    return os.path.isfile(os.path.join(ANSIBLE, CONFIGURATION, CONFIGURATION_FILE))

def _ask_for_configuration():
    ssh_key = click.prompt('Your ssh public key path', type=str, default=DEFAULT_SSH_KEY)
    do_token = click.prompt('Your digital ocean token path', type=str)
    return ssh_key, do_token

def _create_configuration_file(ssh_key, do_token):
    if not os.path.exists(os.path.join(ANSIBLE, CONFIGURATION)):
        os.makedirs(os.path.join(ANSIBLE, CONFIGURATION))

    with open(os.path.join(ANSIBLE, CONFIGURATION, CONFIGURATION_FILE), "w+") as file:
        file.write('ssh_pub_key_name_on_digitalocean: "Main SSH Key"\n')
        file.write('ssh_pub_key_to_load_on_droplet_location: "{0}"\n'.format(ssh_key))
        file.write('digitalocean_token_location: "{0}"\n'.format(do_token))

def _has_droplet_inventory_symlink():
    return os.path.islink(os.path.join(ANSIBLE, INVENTORY, INVENTORY_DROPLETS_LINK))

def _create_droplet_inventory_symlink():
    inventory_link = os.path.join(ANSIBLE, INVENTORY, INVENTORY_DROPLETS_LINK)
    inventory_file = os.path.join(os.path.expanduser("~"), INVENTORY_DROPLETS_FILE)

    if not os.path.isfile(inventory_file):
        raise AssertionError(
            "Please ensure you didn't delete the generated inventory in the HOME dir\n" +
            "In case you did, just create a new empty file at '{0}'".format(inventory_file)
        )

    symlink(inventory_file, inventory_link)

def _delete_current_configuration():
    try:
        os.remove(os.path.join(ANSIBLE, CONFIGURATION, CONFIGURATION_FILE))
    except OSError:
        pass

def _create_droplet(name, droplet_spec):
    cmd = [
        'ansible-playbook',
        '%s' % os.path.join("./", CREATE_PLAYBOOK),
        '--extra-vars',
        'droplet_name=%s droplet_spec_name=%s' % (name, droplet_spec)
    ]
    _run(cmd)

def _destroy_droplet(name):
    cmd = [
        'ansible-playbook',
        '%s' % os.path.join("./", DESTROY_PLAYBOOK),
        '--extra-vars',
        'droplet_name=%s' % (name)
    ]
    _run(cmd)

def _run(cmd):
    subprocess.Popen(cmd, cwd=ANSIBLE).communicate()


#########################
##### Cli functions #####
#########################
def start():
    cli = click.Group()

    @cli.command('create')
    @click.argument('name', type=str)
    @click.argument('droplet-spec', type=click.Choice(['micro', 'mini', 'power']), default='micro')
    def create(name, droplet_spec):
        _set_configuration_if_needed()
        _install_requirements_if_needed()
        _create_droplet(name, droplet_spec)

    @cli.command('destroy')
    @click.argument('name', type=str)
    def destroy(name):
        _set_configuration_if_needed()
        _destroy_droplet(name)

    @cli.command('config')
    def config():
        _delete_current_configuration()
        _set_configuration_if_needed()

    cli()
