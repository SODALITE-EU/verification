import os
from pm4py.objects.petri.importer import pnml as pnml_importer
from pm4py.objects.petri import utils


def run_verifier(file):
    net, initial_marking, final_marking = pnml_importer.import_net(
        os.path.join("tests", "input_data", file))
    cycles = utils.get_cycles_petri_net_places(net)
    return cycles
