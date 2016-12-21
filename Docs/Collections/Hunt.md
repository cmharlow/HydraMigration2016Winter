# Hunt.xml

Notes here primarily for metadata normalization + entity matching work planned, confirmed mappings (for 'interim Simple RDF' plan) moved to the finalized mappings [Box spreadsheet](https://cornell.box.com/s/egu0slwx19xz9euxcgj428c9esvpuyzq).

Hunt or Huntington is 124 digitized books. Most books have bibliographic records in the Catalog for the analog versions.

## Overview of Existing Metadata Usage in DLXS XML for Hunt
```
       /record/ENCODINGDESC/EDITORIALDECL/P: |=========================|    124/124 | 100%
                    /record/FILEDESC/EXTENT: |=========================|    124/124 | 100%
      /record/FILEDESC/PUBLICATIONSTMT/IDNO: |=========================|    124/124 | 100%
 /record/FILEDESC/PUBLICATIONSTMT/PUBLISHER: |=========================|    124/124 | 100%
  /record/FILEDESC/PUBLICATIONSTMT/PUBPLACE: |=========================|    124/124 | 100%
    /record/FILEDESC/SOURCEDESC/BIBL/AUTHOR: |=========================|    124/124 | 100%
      /record/FILEDESC/SOURCEDESC/BIBL/DATE: |=========================|    124/124 | 100%
      /record/FILEDESC/SOURCEDESC/BIBL/NOTE: |=========================|    124/124 | 100%
 /record/FILEDESC/SOURCEDESC/BIBL/PUBLISHER: |=========================|    124/124 | 100%
  /record/FILEDESC/SOURCEDESC/BIBL/PUBPLACE: |=========================|    124/124 | 100%
     /record/FILEDESC/SOURCEDESC/BIBL/TITLE: |=========================|    124/124 | 100%
          /record/FILEDESC/TITLESTMT/AUTHOR: |=========================|    124/124 | 100%
           /record/FILEDESC/TITLESTMT/TITLE: |=========================|    124/124 | 100%
/record/PROFILEDESC/TEXTCLASS/KEYWORDS/TERM: |=========================|    124/124 | 100%
                /record/TEXT/BODY/DIV1/HEAD: |=========================|    124/124 | 100%
```

## Overview of Existing Solr Usage for Hunt in Fedora 3
```
                   _version_: |=========================|    124/124 | 100%
     active_fedora_model_ssi: |=========================|    124/124 | 100%
        author_creator_tesim: |=========================|    124/124 | 100%
                    author_t: |=========================|    124/124 | 100%
                author_tesim: |=========================|    124/124 | 100%
        bibl_titletype_tesim: |=========================|    124/124 | 100%
                  book_id_ts: |=========================|    124/124 | 100%
              book_ocr_tesim: |=======================  |    119/124 |  95%
            collection_tesim: |=========================|    124/124 | 100%
creation_site_location_tesim: |=========================|    124/124 | 100%
         creator_facet_tesim: |=========================|    124/124 | 100%
                   creator_t: |=========================|    124/124 | 100%
                  date_tesim: |=                        |      5/124 |   4%
       editorialdecl_n_tesim: |=========================|    124/124 | 100%
                extent_tesim: |=========================|    124/124 | 100%
                format_tesim: |=========================|    124/124 | 100%
              has_model_ssim: |=========================|    124/124 | 100%
              has_pages_ssim: |=========================|    124/124 | 100%
                          id: |=========================|    124/124 | 100%
             latest_date_isi: |=========================|    124/124 | 100%
          object_profile_ssm: |=========================|    124/124 | 100%
            object_state_ssi: |=========================|    124/124 | 100%
               pubdate_tesim: |=========================|    124/124 | 100%
             publisher_tesim: |=========================|    124/124 | 100%
              pubplace_tesim: |=========================|    124/124 | 100%
          pubstmt_idno_tesim: |=========================|    124/124 | 100%
     pubstmt_idno_type_tesim: |=========================|    124/124 | 100%
     pubstmt_publisher_tesim: |=========================|    124/124 | 100%
      pubstmt_pubplace_tesim: |=========================|    124/124 | 100%
      repository_place_tesim: |=========================|    124/124 | 100%
            repository_tesim: |=========================|    124/124 | 100%
                       score: |=========================|    124/124 | 100%
               subject_tesim: |=========================|    124/124 | 100%
          system_create_dtsi: |=========================|    124/124 | 100%
        system_modified_dtsi: |=========================|    124/124 | 100%
                   timestamp: |=========================|    124/124 | 100%
                   title_ssi: |=========================|    124/124 | 100%
                 title_tesim: |=========================|    124/124 | 100%
      titlestmt_author_tesim: |=========================|    124/124 | 100%
       titlestmt_title_tesim: |=========================|    124/124 | 100%
   titlestmt_titletype_tesim: |=========================|    124/124 | 100%
```

## Proposed PCDM Model for 'Simple RDF' interim
A lot of this is written with short and mid term future metadata work (normalization, entity resolution/URI retrieval, more robust dig collection descriptive metadata ontology written) in mind. See [the CUL Digital Collections Metadata Application Profile](../CULPCDM.md) for a high-level review of the PCDM model and profiles used.

### Current Huntington Structural Model in Digital Collections Fedora 4.7 Model

![Huntington structural diagram](diagrams/huntington_f4.jpg "Huntington structural diagram")

### PCDM:Collection > HydraWorks:Collection : Digital Collection
This is the collection resource representing Huntington Digital Collection.

#### Descriptive Profile

predicate | value | notes
--- | --- | ---
**dcterms:title** | "Huntington Free Library Native American Collection"^^xsd:string | Need language typing
**dcterms:abstract** | "One of the largest collections of books and manuscripts of its kind, the Huntington collection contains extensive materials documenting the history, culture, languages, and arts of the native tribes of both North and South America. Contemporary politics and human rights issues are also important components of the collection. Full text of a selection of 91 books from the Huntington Free Library Native American Collection representing the various genres in the collection."^^xs:string | Need language typing
**dcterms:date** | "2010"^^<http://id.loc.gov/datatypes/edtf> | Need date (data type) typing. Make sure is not dcterms:created
**dcterms:identifier** | "6790930" | identifier typing to be added in phase 2 of migration.
**dc:publisher** | "Cornell University. Library"@en-us | To be removed upon being able to leverage context class URIs (below)
**dcterms:publisher** | <http://id.loc.gov/authorities/names/n85179829> | leveraging this to be added in phase 2 of migration.
**dcterms:relation** | <https://rare.library.cornell.edu/collections/amerhist/amerindianhist> | n/a

#### Structural Profile

- *Digital Collection <-PCDM:isMemberOf- Repository Work* (only this due to the Fedora 4 inverse membership work around for performance)
- *Digital Collection <-ore:proxyFor- Repository Work Member of Collections Proxies (part of that inverse membership/inverse containment work as well)*
- *Digital Collection <-ldp:contains- Digital Collection Fedora Container under /rest/dev*

#### SPARQL Update for Huntington Collection Descriptive Metadata Repair

On <http://hydraedit-dev.library.cornell.edu:8080/fedora/rest/dev/hu/nt/in/gt/huntington>

```
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>

DELETE
  { <> dcterms:title "Huntington Collection must edit" . } WHERE {};
INSERT
  { <> dcterms:title "Huntington Free Library Native American Collection"^^xsd:string ;
       dcterms:abstract "One of the largest collections of books and manuscripts of its kind, the Huntington collection contains extensive materials documenting the history, culture, languages, and arts of the native tribes of both North and South America. Contemporary politics and human rights issues are also important components of the collection. Full text of a selection of 91 books from the Huntington Free Library Native American Collection representing the  various genres in the collection."@en-us ;
       dcterms:date "2010"^^<http://id.loc.gov/datatypes/edtf> ;
       dcterms:identifier "6790930"^^xsd:string ;
       dc:publisher "Cornell University. Library"@en-us ;
       dcterms:publisher <http://id.loc.gov/rwo/agents/n85179829> ;
       dcterms:relation <https://rare.library.cornell.edu/collections/amerhist/amerindianhist> ;
   } WHERE {};
```

### PCDM:Object > HydraWorks:Work | AF:Book : Repository Work
Huntington only contains Books, so the Book repository intellectual object is described here.

#### Post John Migration Analysis:

```
PREFIX ns012: <http://www.iana.org/assignments/relation/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX fedora: <http://fedora.info/definitions/v4/repository#>
PREFIX ebucore: <http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#>
PREFIX ldp: <http://www.w3.org/ns/ldp#>
PREFIX xs: <http://www.w3.org/2001/XMLSchema>
PREFIX dc: <http://purl.org/dc/elements/1.1/>

SELECT DISTINCT ?predicate (COUNT(?predicate) as ?count)
WHERE {
  ?subject fedorasys:hasModel "Book" ;
           ?predicate ?object .
}
GROUP BY ?predicate
```

```
SELECT DISTINCT ?obj (COUNT(DISTINCT ?subject) as ?count)
WHERE {
  ?subject fedorasys:hasModel "Book" ;
           [prefix] ?obj .
}
GROUP by ?obj
```

field | predicate | count (appearance on 124 Book resources, some fields appear more than once) | Note
--- | --- | --- |  ---
**metadata/administrative** ||
activefedora model         | info:fedora/fedora-system:def/model#hasModel                | 124   | left as is
created                    | http://fedora.info/definitions/v4/repository#created        | 124   | left as is
created by                 | http://fedora.info/definitions/v4/repository#createdBy      | 124   | left as is
date submitted             | http://purl.org/dc/terms/dateSubmitted                      | 124   | Removed (all values were empty)
depositor                  | http://id.loc.gov/vocabulary/relators/dpt                   | 124   | left as is
modified (fedora)          | http://fedora.info/definitions/v4/repository#lastModified   | 124   | left as is
modified (dc)              | http://purl.org/dc/terms/modified                           | 124   | removed empty values. Left 1 non-empty value as is. Why do we have this and fedora:lastModified?
modified by                | http://fedora.info/definitions/v4/repository#lastModifiedBy | 124   | left as is.
writable                   | http://fedora.info/definitions/v4/repository#writable       | 124   | left as is
**access** ||
access control             | http://www.w3.org/ns/auth/acl#accessControl                 | 124   | left as is
**structural** ||
contains                   | http://www.w3.org/ns/ldp#contains                           | 249   | what is listSource? Only appears for hunt0004
first                      | http://www.iana.org/assignments/relation/first              | 1     | Only appears for hunt0004. attaches to listSource.
has member                 | http://pcdm.org/models#hasMember                            | 33267 | All other hunt resources. Need to remove Jenn Page 1 test resource.
has parent                 | http://fedora.info/definitions/v4/repository#hasParent      | 124   | left as is. (rest/dev/)
last                       | http://www.iana.org/assignments/relation/last               | 1     | Only appears for hunt0004. attaches to listSource.
member Of                  | http://pcdm.org/models#memberOf                             | 124   | left as is. (huntington)
see also                   | http://www.w3.org/2000/01/rdf-schema#seeAlso                | 124   | removed empty values.
**descriptive** ||
alternative title          | http://purl.org/dc/terms/alternative                        | 124   | leaving for now. return to for more work.
compiler (incorrect URI)   | http://rdaregistry.info/Elements/u/P50189                   | 124   | Empty. remove.
creator                    | http://purl.org/dc/elements/1.1/creator                     | 124   | leave as is for now. return to for more work.
current location of analog | http://www.europeana.eu/schemas/edm/currentLocation         | 124   | Replace empty value with "Cornell University. Library. Division of Rare and Manuscript Collections"
date created               | http://purl.org/dc/terms/created                            | 124   | Removed '0000'. Find way to add typing with date as variable passed (to be done).
DCMI type                  | http://purl.org/dc/elements/1.1/type                        | 124   | 1 "Text", rest empty. Applied "Text" to all, removed empties.
DCMI type URI              | http://purl.org/dc/terms/type                               | 124   | Added <http://purl.org/dc/dcmitype/Text>.
extent                     | http://purl.org/dc/terms/extent                             | 124   | replace "p." with "pages" Same update issue as with created date.
editor                     | http://rdaregistry.info/Elements/u/P60393                   | 124   | remove (all empty). to be re-added after creator parse.
format                     | http://purl.org/dc/terms/format                             | 124   | Good - left as is.
format                     | http://purl.org/dc/elements/1.1/format                      | 124   | Good - left as is.
identifier                 | http://purl.org/dc/terms/identifier                         | 124   | Add bib identifiers. requires entity resolution.
language                   | http://purl.org/dc/elements/1.1/language                    | 123   | Removed empty assertions. To be re-added when better metadata is present.
note                       | http://purl.org/dc/terms/description                        | 124   | Removed empty assertions.
place of origin            | http://vivoweb.org/ontology/core#placeOfPublication         | 124   | Removed empty assertions.
publisher                  | http://purl.org/dc/elements/1.1/publisher                   | 124   | Needs further normalization (same issue as creation dates, above). To be done.
RDF type                   | http://www.w3.org/1999/02/22-rdf-syntax-ns#type             | 744   | Left as is.
subject                    | http://purl.org/dc/elements/1.1/subject                     | 201   | Needs further normalization (same issue as creation dates, above). To be done.
title                      | http://purl.org/dc/terms/title                              | 124   | to be cleaned up.
translator                 | http://rdaregistry.info/Elements/u/P60613                   | 124   | removed (all empty). to be re-added after creator parse.

#### Descriptive Profile

field name | predicate | mapping or collection-wide static value [range] | notes
--- | --- | --- | ---
abstract | **dcterms:abstract** | Nothing in existing DLXS XML to map [xs:string] | n/a
alternate title | **dcterms:alternative** | Nothing in existing DLXS XML to map [xs:string] | n/a
contributor | **dc:contributor** | Nothing in existing DLXS XML to map [literal] | n/a
contributor URI | **dcterms:contributor** | Nothing in existing DLXS XML to map [Agent URI] | n/a
creator | **dc:creator** | FILEDESC/SOURCEDESC/BIBL/AUTHOR [literal] | will need further clean-up post preliminary F4 migration.
creator URI | **dcterms:creator** | to be matched [Agent URIs] | part of phase 2 RDF migration work
date created | **dcterms:created** | FILEDESC/SOURCEDESC/BIBL/DATE | date [literal]  | need to assert EDTF type. review separating date text and date key fields.
note | **dcterms:description** | Nothing in existing DLXS XML to map [literal] | Remove empty assertions.
analog extent | **dcterms:extent** | FILEDESC/SOURCEDESC/BIBL/NOTE | should be URI but uncertain about possibility object_profile_ssm subclassing. literal for now. need to clean up post preliminary F4 migration.
form | **dc:format** | "Book" [literal] | n/a
form URI | **dcterms:format** | "books" Getty Vocab [Concept URI] | Add these now. Replace empty assertions.
identifier | **dcterms:identifier** | Nothing in existing DLXS XML to map [literal] | will want to type eventually for type of identifier (phase 2). Want to add dcterms:source for bib ids? Post preliminary RDF migration.
language | **dc:language** | Nothing in existing DLXS XML to map | We will want to add, remove empty assertions.
language URI | **dcterms:language** | Nothing in existing DLXS XML to map | we will want to add. Part of handling URIs for context classes.
OCR | **dc:relation** | OCR Text [literal] | wanted better term to assert this field as we don't keep the OCR as a separate file, but not finding anything without restrictions.
place of origin | **vivo:placeOfPublication** | FILEDESC/SOURCEDESC/BIBL/PUBPLACE [literal] | this is a datatype property. Remove empty assertions. Will need normalization post-preliminary migration.
publisher | **dc:publisher** | FILEDESC/SOURCEDESC/BIBL/PUBLISHER [literal] | will need further clean-up post preliminary F4 migration. Are mostly publisher statements.
publisher URI | **dcterms:publisher** | not used currently [Agent URI] | part of phase 2 RDF migration work
repository | **edm:currentLocation** | FILEDESC/PUBLICATIONSTMT/PUBLISHER [Repository URI] | will be external URI - cheat with literal until entity resolution project. Remove empty assertions.
rights | **dc:rights** | Nothing in existing DLXS XML to map [literal] | text statement when URI/community rights standard hasn't been used with dcterms:rights
rights URI | **dcterms:rights** | Nothing in existing DLXS XML to map [Rights Statement URI] | URI for any community-assigned rights.
rightsholder URI | **dcterms:rightsHolder** | Nothing in existing DLXS XML to map [Agent URI] | phase 2 effort.
subject | **dc:subject** | PROFILEDESC/TEXTCLASS/KEYWORDS/TERM [literal] | all subject types together at present. Will need post preliminary RDF migration clean-up.
subject URI | **dcterms:subject** | not currently used [Resource URI] | all subject types together at present.
title | **dcterms:title** | FILEDESC/SOURCEDESC/BIBL/TITLE[@TYPE='main']  [literal] | will want language typing. Phase 2.
type | **dc:type** | "Text" [literal] | Add. Is currently missing.
type URI | **dcterms:type** | DCMI Types URI for "Text" [URI] | Add URI. Is currently missing.

#### Structural Profile

- *Book -PCDM:hasMember-> Page*
- *Book <-PCDM:isMemberOf- Page*

#### SPARQL Updates for Huntington Books Descriptive Metadata Repair

**Remove erroneous alternate titles from all Huntington Book records.**

```
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX xs: <http://www.w3.org/2001/XMLSchema>
PREFIX dc: <http://purl.org/dc/elements/1.1/>

DELETE
  { <> dcterms:alternate ?title }
WHERE
  { <> dcterms:title ?title }
```

### PCDM:Object > HydraWorks:Work | AF:Page : Part
Only books / pages captured in Huntington, so these are Pages of those books. To be reviewed after Phase 2 of RDF migration: why these are HydraWorks:Work instances.

#### Descriptive Profile

field name | predicate | mapping or collection-wide static value [range] | notes
--- | --- | --- | ---
form | **dc:format** | "Page" [literal] | n/a
form URI | **dcterms:format** | "pages" Getty Vocab [Concept URI] | Add these now. Replace empty assertions.
heading | **ons:heading** |  [literal] | n/a
identifier | **dcterms:identifier** |  [literal] | Will need identifier typing (phase 2 work).
node | **ons:node** |  [literal] | n/a
node type | **ons:node_type** |  [literal] | n/a
OCR | **dc:relation** | [literal] OCR | Should only apply to the part.
page number | **ons:page_number** |  [xs:integer] | n/a
subject | **dc:subject** | Nothing in existing DLXS XML to map  [literal] | Should only apply to the part. Remove empty assertions.
title | **dcterms:title** |  [literal] | We will want to clean these up, make them human-readable.

#### Structural Profile

- *Page -PCDM:hasMember-> FileSet*
- *Page <-PCDM:isMemberOf- FileSet*

#### SPARQL Updates for Huntington Pages Descriptive Metadata Repair

```

```

### PCDM:Object < HydraWorks:FileSet : FileSet
This is the digital work as represented by file sets - so any information about the digitization and the filesets are related directly to these objects, but descriptive metadata about the intellectual work (the bulk of the descriptive metadata) is used with the above Work instances.

#### Technical & Provenance Metadata Profile

- **dcterms:rights**
- **dcterms:rightsHolder**
- **dc:rights**
- **dcterms:description**
- **dcterms:identifier**
- **dcterms:extent** = FILEDESC/EXTENT [should be resource, will be literal- see intellectual work extent for this issue] => files_extent
- **dcterms:title** = TEXT/BODY/DIV1/HEAD [literal] => fileset_title

#### Structural Profile

- *File Set -PCDM:hasFile-> File(s)*
- *File Set <-PCDM:isFileOf- File(s)*

### PCDM:File < HydraWorks:File : File

Files are kept in Amazon Web Service. Should check embedded metadata profile at a later date.

##Mapping from DLXS XML to "Simple RDF" (with normalization notes)

Field | Concept | RDF Mapping | Notes
--- | --- | --- | ---
**ENCODINGDESC/EDITORIALDECL/P** | *Note* | Book dcterms:description [xs:string] | OCR is not kept as separate file, but text referred to by descriptive metadata. Move Solr concept to technical note.
**FILEDESC/EXTENT** | Extent | pcdm:object[hydraWork:GeneralFile] ? [literal] | This is extent for collection of digital objects/files attached to one resource/work. Doesn't describe each file at the file-level. Ex: "112 600dpi TIFF page images"
**FILEDESC/PUBLICATIONSTMT/IDNO** | Identifier | pcdm:object[dpla:SourceResource] dcterms:identifier [literal] | there only seems to be these dlxs identifiers used, wondering if we'll need to type this later on.
**FILEDESC/PUBLICATIONSTMT/PUBLISHER** | Repository | pcdm:object[dpla:sourceResource] **edm:currentLocation** [literal until we can pull in external URIs] | can't find other property that adequately covers repository without going beyond scope of current options. Prime entity resolution candidate.
**FILEDESC/PUBLICATIONSTMT/PUBPLACE** | Repository location? | Don't map | This is the location of the repository, captured above. Do we need? Otherwise can repeat edm:currentLocation or concatenate fields in some way.
**FILEDESC/SOURCEDESC/BIBL/AUTHOR** | Creator | pcdm:object[dpla:SourceResource] dcterms:creator [literal until we can pull in external URIs] | Some are many creators concatenated, others contain role terms. Look into possibility of using more specific marcrel properties for these role terms (and removing role term from literal value). e.g. "Wells, Roger A.E., compiler" => pcdm:object marcrel:compiler "Wells, Roger A.E."@en. Prime entity resolution candidate.
**FILEDESC/SOURCEDESC/BIBL/DATE** | Date | pcdm:object[dpla:SourceResource] dcterms:created [literal] | 1 value has a reprint note attached, some use of dashes (inconsistent) for ranges, 1 questionable/unknown value. Look into remediation for then assigning encoding datatype to these literals? EDTF or a more generic ISO standard?
**FILEDESC/SOURCEDESC/BIBL/NOTE** | Extent (not originally mapped) | pcdm:object[dplaSourceResource] ?? [literal] | this is the physical resource extent and should be attached to the object describing that resource (unlike extent above, which is more about digital file extent). Not sure why it is in a Note field.
**FILEDESC/SOURCEDESC/BIBL/PUBLISHER** | Publisher | pcdm:object[dpla:SourceResource] dc:publisher [literal] | this is the physical resource's actual publisher, not the digitizer nor the repository. Looks transcribed, so normalization is limited (pick this up with RDA folks in LTS at some point).  Otherwise, entity resolution candidate (except this was turned down).
**FILEDESC/SOURCEDESC/BIBL/PUBPLACE** | Creation location | pcdm:object[dpla:SourceResource] vivo:placeOfPublication [literal] | LD4L option has domain/range restrictions that make it not good option for this. Not sure I like the data property route - what if we want to normalize/resolve placenames (i.e. make into objects)? Need to keep looking.
**FILEDESC/SOURCEDESC/BIBL/TITLE[@TYPE='main']** | Title | pcdm:object[dpla:SourceResource] dcterms:title [literal] | same values appears as FILEDESC/TITLESTMT/TITLE (below)
**FILEDESC/TITLESTMT/AUTHOR** | skip | skip | Creator values, appears to be same as FILEDESC/SOURCEDESC/BIBL/AUTHOR which is mapped
**FILEDESC/TITLESTMT/TITLE** | skip | skip | Title values, appears to be same as FILEDESC/SOURCEDESC/BIBL/TITLE which is mapped
**PROFILEDESC/TEXTCLASS/KEYWORDS/TERM** | Subject | pcdm:object[dpla:SourceResource] dc:subject [literal] | dcterms:subject is meant to be used with non-literal values, according to DCMI. Can consider using when we map these to external URIs (most should be fairly straight forward entity matching). Replace ' - ' with '--' is first step towards LC-influenced normalization.
**TEXT/BODY/DIV1/HEAD** | structural metadata | pcdm:object(hydraWork:GeneralFile) dcterms:title [literal] | this appears to be the label/kind of files represented in the requisite wrapper element.
**BODY** | Structural Metadata | |
**DIV1** | Structural Metadata | |
**PB** | Structural Metadata | |

