import json

from pnmlpy import WorkflowVerifier
from pnmlpy.pmnl_model import PNMLModelGenerator

errors = WorkflowVerifier.run_verifier("../testResources/runningexample.pnml")
js = json.dumps(errors, sort_keys=False, indent=4)
print(js)
from pnmlpy.ansible_model import AnsibleRoleParser

parser = AnsibleRoleParser()
tasks = parser.parse('../testResources/main.yml')
for task in tasks:
    print(task.name)
    print(task.condition)
    print(task.loop)

pnml_model_gen = PNMLModelGenerator()
print(pnml_model_gen.generate(tasks))
