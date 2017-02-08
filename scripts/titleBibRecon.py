"""Match Work Titles to Catalog Bibs for Grabbing Bib IDs in Fedora."""
import rdflib
from rdflib.namespace import *
import requests
from SPARQLWrapper import SPARQLWrapper, JSON
from argparse import ArgumentParser
import json
from xml.etree import ElementTree

fcrepo_base = 'http://hydraedit-dev.library.cornell.edu:8080/fedora/rest/dev/'
yaz_base = "http://yazproxy.library.cornell.edu:9000/voyager?version=1.1&operation=searchRetrieve&startRecord=1&maximumRecords=10&query="
EDM = rdflib.Namespace('http://www.europeana.eu/schemas/edm/')
FCONFIG = rdflib.Namespace('http://fedora.info/definitions/v4/config#')
FEDORA = rdflib.Namespace('http://fedora.info/definitions/v4/repository#')
FEDORASYS = rdflib.Namespace('info:fedora/fedora-system:def/model#')
HW = rdflib.Namespace('http://projecthydra.org/works/models#')
LDP = rdflib.Namespace('http://www.w3.org/ns/ldp#')
MARCREL = rdflib.Namespace('http://id.loc.gov/vocabulary/relators/')
PCDM = rdflib.Namespace('http://pcdm.org/models#')
ONS = rdflib.Namespace('http://opaquenamespace.org/hydra/')
VIVO = rdflib.Namespace('http://vivoweb.org/ontology/core#')
# MARCXML stuff
ns = {"zs": "http://www.loc.gov/zing/srw/",
      "marc": "http://www.loc.gov/MARC21/slim"}
marc_record = './zs:records/zs:record/zs:recordData/marc:record'
marc_id = './marc:controlfield[@tag="001"]'
marc_899 = './marc:datafield[@tag="899"]'
marc_a = './marc:subfield[@code="a"]'
marc_856 = './marc:datafield[@tag="856"]'
marc_u = './marc:subfield[@code="u"]'


def matchTitle(val):
    lookup = yaz_base + val
    resp = requests.get(lookup)
    tree = ElementTree.fromstring(resp.content)
    yazRecs = tree.findall(marc_record, namespaces=ns)
    if not yazRecs:
        if '=' in val:
            lookup = yaz_base + val.split('=')[0]
        elif ';' in val:
            lookup = yaz_base + val.split(';')[0]
        elif '/' in val:
            lookup = yaz_base + val.split('/')[0]
        elif '  ' in val:
            lookup = yaz_base + val.split('  ')[0]
        elif '...' in val:
            lookup = yaz_base + val.split('...')[0]
        resp = requests.get(lookup)
        tree = ElementTree.fromstring(resp.content)
        yazRecs = tree.findall(marc_record, namespaces=ns)
        if not yazRecs:
            lookup = yaz_base + val[0:30]
            resp = requests.get(lookup)
            tree = ElementTree.fromstring(resp.content)
            yazRecs = tree.findall(marc_record, namespaces=ns)
    if yazRecs:
        return(yazRecs)
    else:
        return(None)


def handleTitles(val, URI, yazRecs):
    matched = None
    for yazRec in yazRecs:
        IDs = yazRec.findall(marc_id, namespaces=ns)
        ID = IDs[0].text
        Repos = yazRec.findall(marc_899, namespaces=ns)
        if Repos:
            Repo = Repos[0].find(marc_a, namespaces=ns).text
        else:
            Repo = None
        Links = yazRec.findall(marc_856, namespaces=ns)
        if Links:
            Link = Links[0].find(marc_u, namespaces=ns).text
        else:
            Link = None

        if Repo:
            if 'Dig' in Repo and Link:
                matched = {"URI": URI, "title": val}
                matched['dcterms:identifier'] = ID
            elif 'HFLC' in Repo:
                matched = {"URI": URI, "title": val}
                matched['dcterms:source'] = ID
    return(matched)


def grabFields(work, field):
    """Query Fuseki for the field of a specific URI."""
    fuseki = SPARQLWrapper("http://localhost:3030/fcrepo/sparql")
    fuseki.setQuery(
        """PREFIX acl: <http://www.w3.org/ns/auth/acl#>
           PREFIX dc: <http://purl.org/dc/elements/1.1/>
           PREFIX dcterms: <http://purl.org/dc/terms/>
           PREFIX ebucore: <http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#>
           PREFIX edm: <http://www.europeana.eu/schemas/edm/>
           PREFIX fedora: <http://fedora.info/definitions/v4/repository#>
           PREFIX fedoraconfig: <http://fedora.info/definitions/v4/config#>
           PREFIX fedorasys: <info:fedora/fedora-system:def/model#>
           PREFIX foaf: <http://xmlns.com/foaf/0.1/>
           PREFIX hw: <http://projecthydra.org/works/models#>
           PREFIX image: <http://www.modeshape.org/images/1.0>
           PREFIX jcr: <http://www.jcp.org/jcr/1.0>
           PREFIX ldp: <http://www.w3.org/ns/ldp#>
           PREFIX marcrel: <http://id.loc.gov/vocabulary/relators/>
           PREFIX mix: <http://www.jcp.org/jcr/mix/1.0>
           PREFIX mode: <http://www.modeshape.org/1.0>
           PREFIX nt: <http://www.jcp.org/jcr/nt/1.0>
           PREFIX ons: <http://opaquenamespace.org/terms/>
           PREFIX ore: <http://www.openarchives.org/ore/terms/>
           PREFIX pcdm: <http://pcdm.org/models#>
           PREFIX premis: <http://www.loc.gov/premis/rdf/v1#>
           PREFIX rdau: <http://rdaregistry.info/Elements/u/>
           PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
           PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
           PREFIX sv: <http://www.jcp.org/jcr/sv/1.0>
           PREFIX test: <info:fedora/test/>
           PREFIX vivo: <http://vivoweb.org/ontology/core#>
           PREFIX xml: <http://www.w3.org/XML/1998/namespace>
           PREFIX xmlns: <http://www.w3.org/2000/xmlns/>
           PREFIX xsi: <http://www.w3.org/2001/XMLSchema-instance>
           PREFIX xs: <http://www.w3.org/2001/XMLSchema>

           SELECT DISTINCT ?obj ?subj
           WHERE { ?subj fedorasys:hasModel "%s" ;
                         %s ?obj . }""" % (work, field))

    fuseki.setReturnFormat(JSON)
    results = fuseki.query().convert()
    return(results)


def main():
    """Create or expand existing graph with Fedora collection data."""
    parser = ArgumentParser(description="Work type & field to be matched.")
    parser.add_argument("-w", "--work", dest="work")
    parser.add_argument("-f", "--field", dest="field")
    args = parser.parse_args()

    if not args.work:
        args.work = "Book"
    if not args.field:
        args.work = "dcterms:title"

    # start manual review file
    with open('recon/review.txt', 'w') as fh:
        fh.write("Review needed for: " + args.work + ", " + args.field + "\n")

    results = grabFields(args.work, args.field)
    matches = {}
    for result in results['results']['bindings']:
        val = result['obj']['value']
        URI = result['subj']['value']
        yazRecs = matchTitle(val)
        if yazRecs:
            matched = handleTitles(val, URI, yazRecs)
            if matched:
                matches[URI] = matched
                if "dcterms:identifier" not in matches[URI] and "dcterms:source" not in matches[URI]:
                    with open('recon/review.txt', 'a') as fh:
                        fh.write("URI: " + URI + " title: " + val + "\n")
        else:
            with open('recon/review.txt', 'a') as fh:
                fh.write("URI: " + URI + " title: " + val + "\n")
    with open('recon/recon.json', 'w') as output:
        json.dump(matches, output)



if __name__ == '__main__':
    main()