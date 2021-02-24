from xml.dom import minidom
from xml.etree import ElementTree
from xml.etree.cElementTree import Element, SubElement, ElementTree, tostring


class PNMLModelGenerator:
    def generate(self, tasks):
        top = Element('pnml')

        child = SubElement(top, 'net',
                           attrib={'id': "net1", 'type': "http://www.pnml.org/version-2009/grammar/pnmlcoremodel"})

        page = SubElement(child, 'page',
                          attrib={'id': "n0"})
        index = 0
        for task in tasks:
            place = SubElement(page, 'place',
                               attrib={'id': "p" + str(index)})

            name = SubElement(place, 'name')
            text = SubElement(name, 'text')
            text.text = task.name
            index += 1

        finalmarkings = SubElement(child, 'finalmarkings')
        markings = SubElement(finalmarkings, 'markings')
        tree = ElementTree(top)
        return prettify(top)


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
