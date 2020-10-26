from tosca import TOSCASyntaxVerifier


class TestAdminByDefault:

    def test_file(self):
        errors = TOSCASyntaxVerifier.run_verifier('testResources/tosca_single_instance_wordpress.yaml')
        errors2 = TOSCASyntaxVerifier.run_verifier('testResources/tosca_helloworld.yaml')
        import json
        js = json.loads(json.dumps(errors, sort_keys=False, indent=4))
        js2 = json.loads(json.dumps(errors2, sort_keys=False, indent=4))
        assert 'ValidationError' == js["error_type"]
        assert 0 == len(js2)
