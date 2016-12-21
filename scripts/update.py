"""Storing SPARQL updates for later use on Fedora repo."""
import requests
import sys


fedora_base = "http://hydraedit-dev.library.cornell.edu:8080/fedora/rest/dev/"
update_hdr = {'Content-Type': 'application/sparql-update'}

# SPARQL Update / Patches
add_formatURI = """
    PREFIX dcterms: <http://purl.org/dc/terms/>

    INSERT { <> dcterms:format <http://vocab.getty.edu/aat/300028051> . }
    WHERE { <> dcterms:format "" . } ;
    DELETE { <> dcterms:format "" . } WHERE {}
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

remove_empty_dateSubmitted = """
    PREFIX dcterms: <http://purl.org/dc/terms/>

    DELETE { <> dcterms:dateSubmitted "" . }
    WHERE { <> dcterms:dateSubmitted "" }
    """

remove_empty_dateModified = """
    PREFIX dcterms: <http://purl.org/dc/terms/>

    DELETE { <> dcterms:modified "" . }
    WHERE { <> dcterms:modified "" }
    """

remove_empty_notes = """
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX vivo: <http://vivoweb.org/ontology/core#>

    DELETE { <> dcterms:description "" ;
                vivo:placeOfPublication "" . }
    WHERE { }
    """

remove_empty_language = """
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    DELETE { <> dc:language "" . }
    WHERE { <> dc:language "" }
    """

remove_empty_seeAlso = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    DELETE { <> rdfs:seeAlso "" . }
    WHERE { <> rdfs:seeAlso "" }
    """

remove_empty_rdau = """
    PREFIX rdau: <http://rdaregistry.info/Elements/u/>

    DELETE { <> rdau:P50189 "" ;
                rdau:P60393 "" ;
                rdau:P60613 "" . }
    WHERE { <> rdau:P50189 "" ;
               rdau:P60393 "" ;
               rdau:P60613 "" }
    """

add_repository = """
    PREFIX edm: <http://www.europeana.eu/schemas/edm/>

    DELETE { <> edm:currentLocation "" . } WHERE {} ;
    INSERT { <> edm:currentLocation "Cornell University. Library. Division of Rare and Manuscript Collections" . }
    WHERE {}
    """


def fcrepoPatch(URIs, sparqlPatch):
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
    fcrepoPatch(URIs, remove_empty_notes)


if __name__ == '__main__':
    main()