from tosca import TOSCASyntaxVerifier


class TestSyntaxChecks:

    def test_file(self):
        errors, bug_type, bug_data = TOSCASyntaxVerifier.run_verifier(
            'testResources/tosca_single_instance_wordpress.yaml')
        errors2, bug_type2, bug_data2 = TOSCASyntaxVerifier.run_verifier('testResources/tosca_helloworld.yaml')
        import json
        js = json.loads(json.dumps(errors, sort_keys=False, indent=4))
        js2 = json.loads(json.dumps(errors2, sort_keys=False, indent=4))
        error_type = js["error_type"]
        error_info = js["error_info"]
        assert 'ValidationError' == error_type
        assert 'MissingRequiredFieldError' != bug_type
        assert 'UnknownFieldError' != error_type
        assert 'InvalidTemplateVersion' != error_type
        assert 'TOSCAException' != error_type
        assert 0 == len(js2)
        assert 0 == len(bug_data2)
        assert 0 == len(bug_type2)
        assert len(error_info) > 0
        assert len(bug_data) > 0
