import os

from pm4py.objects.petri.check_soundness import check_easy_soundness_net_in_fin_marking
from pm4py.objects.petri import utils
from pm4py.objects.petri.importer import importer as petri_importer


def run_verifier(file):
    net, initial_marking, final_marking = petri_importer.apply(file)
    cycles = utils.get_cycles_petri_net_places(net)
    soundness = check_easy_soundness_net_in_fin_marking(net, initial_marking, final_marking)
    return {"soundness": soundness, "cycles": len(cycles)}
