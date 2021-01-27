from tosca import TOSCASyntaxVerifier


class TestSyntaxChecks:

    def test_file(self):
        errors = TOSCASyntaxVerifier.run_verifier('testResources/tosca_single_instance_wordpress.yaml')
        errors2 = TOSCASyntaxVerifier.run_verifier('testResources/tosca_helloworld.yaml')
        import json
        js = json.loads(json.dumps(errors, sort_keys=False, indent=4))
        js2 = json.loads(json.dumps(errors2, sort_keys=False, indent=4))
        error_type = js["error_type"]
        assert 'ValidationError' == error_type
        assert 'MissingRequiredFieldError' != error_type
        assert 'UnknownFieldError' != error_type
        assert 'InvalidTemplateVersion' != error_type
        assert 'TOSCAException' != error_type
        assert 0 == len(js2)
