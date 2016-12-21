"""Grab Collections Graphs from Fedora, Iterate, and load into local Fuseki."""
import rdflib
from rdflib.namespace import *
from argparse import ArgumentParser
import sys
from rdflib.plugins.stores import sparqlstore

fcrepo_base = 'http://hydraedit-dev.library.cornell.edu:8080/fedora/rest/dev/'
EDM = rdflib.Namespace('http://www.europeana.eu/schemas/edm/')
PCDM = rdflib.Namespace('http://pcdm.org/models#')
FEDORA = rdflib.Namespace('http://fedora.info/definitions/v4/repository#')
ONS = rdflib.Namespace('http://opaquenamespace.org/hydra/')
VIVO = rdflib.Namespace('http://vivoweb.org/ontology/core#')
HW = rdflib.Namespace('http://projecthydra.org/works/models#')
MARCREL = rdflib.Namespace('http://id.loc.gov/vocabulary/relators/')
FCONFIG = rdflib.Namespace('http://fedora.info/definitions/v4/config#')
LDP = rdflib.Namespace('http://www.w3.org/ns/ldp#')
endpoint = 'http://localhost:3030/fcrepo/query'
store = sparqlstore.SPARQLUpdateStore()
store.open((endpoint, endpoint))
fuseki = rdflib.Graph(store)


def grabCollContainers(cont, fcrepo):
    """Query fedora for all resources of the selected collection."""
    print("Generating graph.")
    cont_g = fcrepo.parse(cont)
    s = 0
    print("Parsing graph objects.")
    for obj in cont_g.objects(cont, LDP.contains):
        # Parse recursively on that graph.
        cont_g.parse(obj)
        if (s % 10) == 0 and s != 0:
            print("%d URIs processed" % s)
        s += 1
    return(cont_g)


def main():
    """Create or expand existing graph with Fedora collection data."""
    parser = ArgumentParser(description="Pass Collections URIs.")
    parser.add_argument("-c", "--container", dest="cont")
    parser.add_argument("-l", "--containerList", dest="contList")

    args = parser.parse_args()

    if not len(sys.argv) > 1:
        parser.print_help()
        parser.exit()

    fcrepo = rdflib.Graph()
    if args.cont:
        cont = rdflib.term.URIRef(args.cont)
        fcrepo = grabCollContainers(cont, fcrepo)
    elif args.contList:
        for n in contList:
            cont = rdflib.term.URIRef(n)
            fcrepo = grabCollContainers(args.cont, fcrepo)

    print("Writing Graph to file.")
    fcrepo.serialize("fcrepo.ttl", format="turtle")
    fuseki.update('INSERT DATA { %s }' % fcrepo.serialize(format='nt'))


if __name__ == '__main__':
    main()
