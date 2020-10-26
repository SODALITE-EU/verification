from pnmlpy import WorkflowVerifier


class TestAdminByDefault:

    def test_file(self):
        errors = WorkflowVerifier.run_verifier('testResources/runningexample.pnml')
        import json
        js = json.loads(json.dumps(errors, sort_keys=False, indent=4))
        assert True == js["soundness"]
        assert 3 == int(js["cycles"])
