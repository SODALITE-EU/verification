from toscaparser import shell as parser_shell
from toscaparser.common.exception import TOSCAException


def run_verifier(file):
    bug_type = ""
    bug_data = ""
    try:
        parser_shell.ParserShell().parse(file)
    except ValueError as value_error:
        bug_data = str(value_error)
        bug_type = type(value_error)
    except AttributeError as att_error:
        bug_data = str(att_error)
        bug_type = type(att_error)
    except TOSCAException as validation_error:
        # bug_data = str(validation_error)
        bug_type = type(validation_error).__name__
        bug_data = validation_error.message
    if bug_type:
        return {"error_type": str(bug_type),
                "error_info": str(bug_data)}
    else:
        return {}
