from toscaparser import shell as parser_shell
from toscaparser.common.exception import TOSCAException


def run_verifier(file):
    bug_type = ""
    bug_data = ""
    try:
        parser_shell.ParserShell().parse(file)
    except TOSCAException as general_error:
        bug_type = type(general_error)
        bug_data = general_error.message
    if bug_type:
        return {"error_type": str(bug_type.__name__),
                "error_info": str(bug_data).split(".\n\t\t")[0]}, bug_type, bug_data
    else:
        return {}, bug_type, bug_data
