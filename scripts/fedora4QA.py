import rdflib
from rdflib.namespace import *

fedora_baseURL = 'http://hydraedit-dev.library.cornell.edu/fedora/rest/dev/'
dct = rdflib.Namespace('http://purl.org/dc/terms/')
edm = rdflib.Namespace('http://www.europeana.eu/schemas/edm/')
pcdm = rdflib.Namespace('http://pcdm.org/models#')
fedora = rdflib.Namespace('http://fedora.info/definitions/v4/repository#')
hydra = rdflib.Namespace('http://opaquenamespace.org/hydra/')
vivo = rdflib.Namespace('http://vivoweb.org/ontology/core#')
hydraworks = rdflib.Namespace('http://projecthydra.org/works/models#')
lcrel = rdflib.Namespace('http://id.loc.gov/vocabulary/relators/')
fedoraconfig = rdflib.Namespace('http://fedora.info/definitions/v4/config#')
ldp = rdflib.Namespace('http://www.w3.org/ns/ldp#')

colls = ['huntingtonDev']

for coll in colls:
    coll_g = rdflib.Graph()
    coll_uri = rdflib.URIRef(fedora_baseURL + coll)
    coll_g.parse(coll_uri)
    coll_props = set(p for s, p, o in coll_g.triples((coll_uri, None, None)))
    for coll_prop in coll_props:
        print(coll_prop)
        coll_prop_objs = set(o for s, p, o in coll_g.triples((coll_uri,
                                                              coll_prop,
                                                              None)))
        for coll_prop_obj in coll_prop_objs:
            print(coll_prop_obj)
        print('-------------------------------')
    pcdm_objs = set(o for s, p, o in coll_g.triples((coll_uri, pcdm.hasMember,
                                                     None)))
    pcdm_objs_props = set()
    for pcdm_obj in pcdm_objs:
        coll_g.parse(pcdm_obj)
        for s, p, o in coll_g.triples((pcdm_obj, None, None)):
            pcdm_objs_props.add(p)
    print('-------------------------------')
    for pcdm_obj_prop in pcdm_objs_props:
        print(pcdm_obj_prop)
    print('-------------------------------')
    for pcdm_obj in pcdm_objs:
        for pcdm_obj_prop in pcdm_objs_props:
            print(pcdm_obj_prop)
            pcdm_obj_prop_objs = set(o for s, p, o in coll_g.triples((pcdm_obj, pcdm_obj_prop, None)))
            for o in pcdm_obj_prop_objs:
                print(o)
            print('-------------------------------')
        print('-------------------------------')
