import json

from pnmlpy import WorkflowVerifier

errors = WorkflowVerifier.run_verifier(
    "C:\\Postdoc\\projects\\sodalite-eu\\verification\\workflow\\testResources\\runningexample.pnml")
js = json.dumps(errors, sort_keys=False, indent=4)
print(js)
