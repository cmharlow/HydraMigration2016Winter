import requests
import rdflib
import sys


fedora_base = "http://hydraedit-dev.library.cornell.edu:8080/"
update_hdr = {'Content-Type': 'application/sparql-update'}
update_format = """
PREFIX dc: <http://purl.org/dc/elements/1.1/>
INSERT
  { <> dc:format "Book" . } WHERE {};
DELETE
  { <> dc:format "" . } WHERE {}
"""


def addFormat(listOfResources):
    for res in listOfResources:
        res_str = res.toPython().replace("cornell.edu/fedora/",
                                         'cornell.edu:8080/fedora/')
        print(res_str)
        patch = requests.patch(res_str, data=update_format, headers=update_hdr)
        print(patch.text)


if __name__ == '__main__':
    if len(sys.argv) != 1:
        sys.exit("need to pass a list")
    resources = sys.argv[1]
    addFormat(resources)
