import unittest

from tosca import TOSCASyntaxVerifier


class TestAdminByDefault(unittest.TestCase):

    def test_file(self):

        errors = TOSCASyntaxVerifier.run_verifier('testResources/tosca_single_instance_wordpress.yaml')
        errors2 = TOSCASyntaxVerifier.run_verifier('testResources/tosca_helloworld.yaml')
        import json
        js = json.loads(json.dumps(errors, sort_keys=False, indent=4))
        js2 = json.loads(json.dumps(errors2, sort_keys=False, indent=4))
        self.assertEqual('ValidationError', js["error_type"])
        self.assertEqual(0, len(js2))

if __name__ == '__main__':
    unittest.main()