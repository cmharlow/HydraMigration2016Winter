"""Storing SPARQL updates for later use on Fedora repo."""
import requests
import sys
import json

fedora_base = "http://hydraedit-dev.library.cornell.edu:8080/fedora/rest/dev/"
update_hdr = {'Content-Type': 'application/sparql-update'}

# SPARQL Update / Patches
add_formatURI = """
    PREFIX dcterms: <http://purl.org/dc/terms/>

    INSERT { <> dcterms:format <http://vocab.getty.edu/aat/300028051> . }
    WHERE { <> dcterms:format "" . } ;
    DELETE { <> dcterms:format "" . } WHERE {}
    """

add_bibID = """
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    INSERT { <> dcterms:identifier "%s"^^xsd:string . }
    WHERE { }
    """

add_sourceID = """
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    INSERT { <> dcterms:source "%s"^^xsd:string . }
    WHERE { }
    """

add_type = """
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    INSERT { <> dcterms:type <http://purl.org/dc/dcmitype/Text> ;
                dc:type "Text" . }
    WHERE { <> dcterms:type "" ;
               dc:type "" } ;
    DELETE { <> dcterms:type "" ;
                dc:type "" . } WHERE {}
    """

remove_empty = """
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX vivo: <http://vivoweb.org/ontology/core#>

    DELETE { <> <%s> "" . }
    WHERE { }
    """

add_repository = """
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>

    DELETE { <> edm:currentLocation "" . } WHERE {} ;
    INSERT { <> edm:currentLocation "Cornell University. Library. Division of Rare and Manuscript Collections" . }
    WHERE {}
    """


def fcrepoAddPerURI(URIs, matchFile):
    """Add a value that differs according to URI."""
    for URI in URIs:
        if URI in matchFile:
            info = matchFile[URI]
            if 'dcterms:identifier' in matchFile[URI]:
                sparqlPatch = add_bibID % info['dcterms:identifier']
                print("Updating according to")
                print(sparqlPatch)
                requests.patch(URI, data=sparqlPatch, headers=update_hdr)
            if 'dcterms:source' in matchFile[URI]:
                sparqlPatch = add_sourceID % info['dcterms:source']
                print("Updating according to")
                print(sparqlPatch)
                requests.patch(URI, data=sparqlPatch, headers=update_hdr)


def fcrepoSimplePatch(URIs, sparqlPatch):
    """Get list of resources feedback."""
    print('Updating according to:')
    print(sparqlPatch)
    for URI in URIs:
        print(URI)
        requests.patch(URI, data=sparqlPatch, headers=update_hdr)


def main():
    """Update Fedora URIs with variety of AF-based patches."""
    if len(sys.argv) != 2:
        sys.exit("need to pass a list file.")

    resources = sys.argv[1]
    with open(resources) as fh:
        URIs = [line.strip('\n') for line in fh]
    # fcrepoPatch(URIs, remove_empty % "predicate URI")
    matchFile = json.load(open('recon/recon.json', 'r'))
    fcrepoAddPerURI(URIs, matchFile)


if __name__ == '__main__':
    main()