import os
from pydo import Client

connection = Client(token=os.getenv("DO_TOKEN"))

print(dir(connection.droplets))

ssh_keys = connection.ssh_keys.list()
# print(ssh_keys['ssh_keys'])

sshKeyName = "abdul-ssh-key"


for key in ssh_keys['ssh_keys']:
    if sshKeyName == key['name']:
        sshKeyId = key['id']

body = {'name': 'module-droplet', 'size': 's-1vcpu-1gb', 'image': 'ubuntu-20-04-x64', 'ssh_keys': [sshKeyId]}

new_droplet = connection.droplets.create(body)
print(new_droplet)






