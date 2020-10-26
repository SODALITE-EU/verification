import os

from pm4py.objects.petri import check_soundness
from pm4py.objects.petri import utils
from pm4py.objects.petri.importer import pnml as pnml_importer


def run_verifier(file):
    net, initial_marking, final_marking = pnml_importer.import_net(file)
    cycles = utils.get_cycles_petri_net_places(net)
    soundness = check_soundness.check_petri_wfnet_and_soundness(net)
    return {"soundness": soundness, "cycles": len(cycles)}
