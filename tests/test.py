from asa.AnsibleAssembler import AnsibleAssembler

import os

cwd = os.getcwd()
print(cwd)
ccd = os.path.join(cwd, '../config/ansible.yaml')

assembler = AnsibleAssembler(cwd, ccd)

assembler.createAnsibleRepo()
assembler.createRole('user')
