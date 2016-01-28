#Hunt.xml

##Overview of Existing Metadata Usage in DLXS XML for Hunt

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

##Overview of Existing Solr Usage for Hunt in Fedora 3

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

##Proposed PCDM Model for 'Simple RDF' interim
###PCDM:Collection > HydraWorks:Collection : Digital Collection
This is the digital collection that current maps to the dlxs identifier sets (i.e. 'hunt', 'bol', etc.). There can be a secondary PCDM:Collection: Set if/as the need arises.

Descriptive metadata available on this class:

- **dcterms:title** = "Huntington Free Library Native American Collection" =>collection_title (think this is currently just collection_tesim in Solr)
- **dcterms:abstract** = "Cornell's Native American collection includes a significant concentration of native language dictionaries, documenting the development of dozens of languages." => collection_abstract_tesim
- **dcterms:publisher** = "Cornell University. Library" => collection_publ_tesim
- **dcterms:relation** = http://ebooks.library.cornell.edu/h/hunt/ => collection_relatedURL

PCDM + Other RDF Relationships on this class:

*Digital Collection -PCDM:hasMember-> Digital Object*

*Digital Collection <-PCDM:isMemberOf- Digital Object*

###PCDM:Object > HydraWorks:Work : Digital Work
This is the digital work as a whole - so any information about the digitization, the filesets are related directly to this object, but descriptive metadata about the intellectual work (the bulk of the descriptive metadata) is used with the Intellectual Work class. This allows us to make descriptive metadata assertions (such as format = manuscripts, or rights = digital asset viewing and reuse rights) that aren't in conflict with digital object descriptions (format = jpeg or rights = physical resource access or reuse rights). The Digital Works can have PCDM:Objects children for Parts that need separate description (if the pages of a book are all separate filesets and require separate technical/descriptive/administrative metadata, for example).

Descriptive metadata available on this class:

- **dcterms:title** = title for the digital object, usually taken directly from the intellectual work title. => only display the intellectual work title via Solr for the time being. This is more for better management of Fedora objects in Fedora.
- **dcterms:rights** = digital asset rights statements if they exist (none do at present for Huntington) => digital_rights
- **dcterms:rightsHolder** = digital asset rights holder if they exist (none do at present for Huntington) => digital_rightsHolder

PCDM + Other RDF Relationships on this class:

*Digital Object -PCDM:hasMember-> Work/Resource*

*Digital Object -EDM:aggregatedCHO-> Work/Resource*

*Digital Object <-PCDM:isMemberOf- Work/Resource*

###PCDM:Object > HydraWorks:Work > dpla:SourceResource : Intellectual Work
This is the intellectual work represented by the Digital Work. The bulk of the descriptive metadata is here. Eventually, we may look into the option of having this object generated through a RDF Shape on an external triplestore containing more robust intellectual work metadata (and metadata ontologies). While one could, theoretically, have an Intellectual Work for each Digital Work Object Level (or the Digital Collection itself), we are limiting Intellectual Works for the time being to those represented roughly by bibliographic objects or intellectual works - with an eye to system efficiency and object interoperability in delineating this (especially when we get into journals). Resource abstractions like FRBR or RDA are not to be used here.

Descriptive metadata available on this class:

- **dcterms:abstract** = Nothing in existing DLXS XML to map => abstract
- **dcterms:alternative** = Nothing in existing DLXS XML to map => alt_title
- **dcterms:creator** = FILEDESC/SOURCEDESC/BIBL/AUTHOR => creator
- **dcterms:created** =
- property :extent, predicate: ::RDF::Vocab::DC.format, multiple: true
- property :id, predicate: ::RDF::Vocab::DC.identifier, multiple: true
- property :note, predicate: ::RDF::Vocab::DC.description, multiple: true
- property :publ_place, predicate: ::RDF::Vocab::VIVO.placeOfPublication, multiple: true
- property :publisher, predicate: ::RDF::Vocab::DC.publisher, multiple: true
- property :repository, predicate: ::RDF::Vocab::EDM.currentLocation, multiple: false
- property :rights, predicate: ::RDF::Vocab::DC.rights, multiple: false
- property :subject, predicate: ::RDF::Vocab::DC11.subject, multiple: true
- property :title, predicate: ::RDF::Vocab::DC.title, multiple: false

PCDM + Other RDF Relationships on this class:

*Digital Work -PCDM:hasMember-> Secondary Digital Work(s) if needed*

*Digital Work <-PCDM:isMemberOf- Secondary Digital Work(s) if needed*

###PCDM:Object > HydraWorks:Work == Secondary Digital Work, as needed

Descriptive metadata available on this class:

- to be added as encountered. 
- dcterms:title (if used at part-level)
- this class is not intended to be paired with secondary level Work/Resource; digitization and description efforts should work to capture discrete Works/Resources such that the metadata on the Work/Resource class instance covers the parts as needed.

PCDM + Other RDF Relationships on this class:

*Digital Work|Secondary Digital Work(s) -PCDM:hasMember-> File Set*

*Digital Work|Secondary Digital Work(s) <-PCDM:isMemberOf- File Set*

###PCDM:Object < HydraWorks:FileSet : File Set

Descriptive metadata available on this class:

- anything file set specific, as encountered (crossing into technical metadata)

PCDM + Other RDF Relationships on this class:

*File Set -PCDM:hasFile-> File(s)*

*File Set <-PCDM:isFileOf- File(s)*

##PCDM:File < HydraWorks:File : File

Descriptive metadata available on this class:

- anything this file specific, as encountered (crossing into technical metadata)

##Mapping to "Simple RDF" from DLXS XML

Field | Concept | RDF Mapping | Notes
--- | --- | --- | ---
**ENCODINGDESC/EDITORIALDECL/P** | *Note* | pcdm:object[hydraWork:GenericWork] dcterms:description [literal] | OCR is not kept as separate file, but text referred to by descriptive metadata. Move Solr concept to technical note.
**FILEDESC/EXTENT** | Extent | pcdm:object[hydraWork:GeneralFile] dcterms:extent [literal] | This is extent for collection of digital objects/files attached to one resource/work. Doesn't describe each file at the file-level. Ex: "112 600dpi TIFF page images"
**FILEDESC/PUBLICATIONSTMT/IDNO** | Identifier | pcdm:object[dpla:SourceResource] dcterms:identifier [literal] | there only seems to be these dlxs identifiers used, wondering if we'll need to type this later on.
**FILEDESC/PUBLICATIONSTMT/PUBLISHER** | Repository | pcdm:object[dpla:sourceResource] **edm:currentLocation** [literal] | can't find other property that adequately covers repository without going beyond scope of current options. Prime entity resolution candidate.
**FILEDESC/PUBLICATIONSTMT/PUBPLACE** | Repository location? | Don't map | This is the location of the repository, captured above. Do we need? Otherwise can repeat edm:currentLocation or concatenate fields in some way.
**FILEDESC/SOURCEDESC/BIBL/AUTHOR** | Creator | pcdm:object[dpla:SourceResource] dcterms:creator [literal] | Some are many creators concatenated, others contain role terms. Look into possibility of using more specific marcrel properties for these role terms (and removing role term from literal value). e.g. "Wells, Roger A.E., compiler" => pcdm:object marcrel:compiler "Wells, Roger A.E."@en. Prime entity resolution candidate.
**FILEDESC/SOURCEDESC/BIBL/DATE** | Date | pcdm:object[dpla:SourceResource] dcterms:created [literal] | 1 value has a reprint note attached, some use of dashes (inconsistent) for ranges, 1 questionable/unknown value. Look into remediation for then assigning encoding datatype to these literals? EDTF or a more generic ISO standard?
**FILEDESC/SOURCEDESC/BIBL/NOTE** | Extent (not originally mapped) | pcdm:object[dplaSourceResource] dcterms:extent [literal] | this is the physical resource extent and should be attached to the object describing that resource (unlike extent above, which is more about digital file extent).
**FILEDESC/SOURCEDESC/BIBL/PUBLISHER** | Publisher | pcdm:object[dpla:SourceResource] dcterms:publisher [literal] | this is the physical resource's actual publisher, not the digitizer nor the repository. Looks transcribed, so normalization is limited (pick this up with RDA folks in LTS at some point).  Otherwise, entity resolution candidate.
**FILEDESC/SOURCEDESC/BIBL/PUBPLACE** | Creation location | pcdm:object[dpla:SourceResource] vivo:placeOfPublication [literal] | LD4L option has domain/range restrictions that make it not good option for this. Not sure I like the data property route - what if we want to normalize/resolve placenames (i.e. make into objects)? Need to keep looking.
**FILEDESC/SOURCEDESC/BIBL/TITLE[@TYPE='main']** | Title | pcdm:object[dpla:SourceResource] dcterms:title [literal] | same values appears as FILEDESC/TITLESTMT/TITLE (below)
**FILEDESC/TITLESTMT/AUTHOR** | skip | skip | Creator values, appears to be same as FILEDESC/SOURCEDESC/BIBL/AUTHOR which is mapped
**FILEDESC/TITLESTMT/TITLE** | skip | skip | Title values, appears to be same as FILEDESC/SOURCEDESC/BIBL/TITLE which is mapped
**PROFILEDESC/TEXTCLASS/KEYWORDS/TERM** | Subject | pcdm:object[dpla:SourceResource] dc:subject [literal] | dcterms:subject is meant to be used with non-literal values, according to DCMI. Can consider using when we map these to external URIs (most should be fairly straight forward entity matching). Replace ' - ' with '--' is first step towards LC-influenced normalization.
**TEXT/BODY/DIV1/HEAD** | structural metadata | pcdm:object(hydraWork:GeneralFile) rds:label [literal] | this appears to be the label/kind of files represented in the requisite wrapper element.
**BODY** | Structural Metadata | |
**DIV1** | Structural Metadata | |
**PB** | Structural Metadata | |

**Normalization Notes:**

-
