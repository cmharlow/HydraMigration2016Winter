"""Storing SPARQL updates for later use on Fedora repo."""
import requests
import rdflib
import sys


fedora_base = "http://hydraedit-dev.library.cornell.edu:8080/fedora/rest/dev/"
update_hdr = {'Content-Type': 'application/sparql-update'}
update_format = """
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
INSERT
  { <> dcterms:format <http://vocab.getty.edu/aat/300028051> . } WHERE { <> dcterms:format "" . };
DELETE
  { <> dcterms:format "" . } WHERE {}
"""


# 3. loads into fuseki for both visual assessment and running queries to get AF models then all ids for each model in play
# 4. then I iterate over the ids for each model to perform batch updates where possible by sending patch requests to Fedora API


def addFormat(listOfResources):
    """Get list of resources feedback."""
    for res in listOfResources:
        print(res_str)
        patch = requests.patch(res_str, data=update_format, headers=update_hdr)


def main():
    """Update Fedora collection data."""
    if len(sys.argv) != 1:
        sys.exit("need to pass a list")

    resources = sys.argv[1]
    addFormat(resources)
    fcrepo = rdflib.Graph()
    if args.cont:
        cont = rdflib.term.URIRef(args.cont)
        fcrepo = grabCollContainers(cont, fcrepo)
    elif args.contList:
        for n in contList:
            cont = rdflib.term.URIRef(n)
            fcrepo = grabCollContainers(args.cont, fcrepo)

    print("Writing Graph to file.")


if __name__ == '__main__':
    main()