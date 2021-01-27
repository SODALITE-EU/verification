from toscaparser import shell as parser_shell
from toscaparser.common.exception import TOSCAException, ValidationError, UnknownFieldError, MissingRequiredFieldError, \
    InvalidTemplateVersion


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
    except ValidationError as val_error:
        bug_data = str(val_error.message)
        bug_type = type(val_error)
    except UnknownFieldError as uf_error:
        bug_data = str(uf_error.message)
        bug_type = type(uf_error)
    except MissingRequiredFieldError as mrfe_error:
        bug_data = str(mrfe_error.message)
        bug_type = type(mrfe_error)
    except InvalidTemplateVersion as itv_error:
        bug_data = str(itv_error.message)
        bug_type = type(itv_error)
    except TOSCAException as general_error:
        bug_type = type(general_error)
        bug_data = general_error.message
    if bug_type:
        return {"error_type": str(bug_type.__name__),
                "error_info": str(bug_data).split(".\n\t\t")[0]}, bug_type, bug_data
    else:
        return {}, bug_type, bug_data
