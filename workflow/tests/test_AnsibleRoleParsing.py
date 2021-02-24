from pnmlpy.ansible_model import AnsibleRoleParser


class TestAnsibleRoleParsing:

    def test_ansible(self):
        parser = AnsibleRoleParser()
        tasks = parser.parse('testResources/main.yml')
        for task in tasks:
            assert task.name is not None
