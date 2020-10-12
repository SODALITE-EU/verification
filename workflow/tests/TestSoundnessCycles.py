import unittest

from pnmlpy import WorkflowVerifier


class TestAdminByDefault(unittest.TestCase):

    def test_file(self):
        errors = WorkflowVerifier.run_verifier('../../testResources/runningexample.pnml')
        import json
        js = json.loads(json.dumps(errors, sort_keys=False, indent=4))
        self.assertEqual(True, js["soundness"])
        self.assertEqual(3, int(js["cycles"]))
