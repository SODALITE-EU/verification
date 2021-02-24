from pnmlpy.ansible_model import AnsibleRoleParser
from pnmlpy.pmnl_model import PNMLModelGenerator


class TestAnsibleRoleParsing:

    def test_ansible(self):
        parser = AnsibleRoleParser()
        tasks = parser.parse('testResources/main.yml')
        for task in tasks:
            assert task.name is not None
        pnml_model_gen = PNMLModelGenerator()
        pnml = pnml_model_gen.generate(tasks)
        assert pnml is not None
