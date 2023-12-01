# dynamic_inventory.py
# A simple dynamic inventory script for testing

import json

inventory = {
    'web_servers': {
        'hosts': ['localhost'], # ['web-server-1', 'web-server-2'],
        'vars': {
            'ansible_ssh_user': 'your_ssh_user',
            'web_server_type': 'nginx',  # Change to 'apache' if you prefer Apache
            'webpage_title': 'My Ansible Webpage',
            'welcome_message': 'Welcome to Ansible Automation!'
        }
    }
}

print(json.dumps(inventory))
