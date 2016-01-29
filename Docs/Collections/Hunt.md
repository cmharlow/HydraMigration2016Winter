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

Structure of the following section:

###PCDM Object > Subclass of this : Class Label at CUL (set up for making CUL object ontology?)
Notes on this class.

####Descriptive metadata so far mapped for this class:
- **the metadata term** = the value or mapping for our test collection, Huntington => the Solr 'concept' (to keep in line with other collections that go directly to Solr)

####RDF Relationships on this class:
The RDF relationships expected for this class, symmetry of those properties not assumed (hence A -> B and B -> A are both given)

###PCDM:Collection > HydraWorks:Collection : Digital Collection
This is the digital collection that current maps to the dlxs identifier sets (i.e. 'hunt', 'bol', etc.). There can be a secondary PCDM:Collection: Set if/as the need arises.

####Descriptive metadata available on this class:

- **dcterms:title** = "Huntington Free Library Native American Collection" =>collection_title (think this is currently just collection_tesim in Solr)
- **dcterms:abstract** = "One of the largest collections of books and manuscripts of its kind, the Huntington collection contains extensive materials documenting the history, culture, languages, and arts of the native tribes of both North and South America. Contemporary politics and human rights issues are also important components of the collection.
Full text of a selection of 91 books from the Huntington Free Library Native American Collection representing the various genres in the collection." => collection_abstract
- **dcterms:created** = "2010" => collection_date
- **dcterms:identifier** = "6790930" => collection_bibid (can we type objects for MARC ids versus other identifiers that may appear?)
- **dcterms:description** = "Mode of access: World Wide Web." => collection_note
- **dcterms:publisher** = "Cornell University. Library" => collection_publ
- **dcterms:relation** = http://ebooks.library.cornell.edu/h/hunt/ => collection_relatedURL

####PCDM + Other RDF Relationships on this class:

*Digital Collection -PCDM:hasMember-> Digital Object*

*Digital Collection <-PCDM:isMemberOf- Digital Object*

###PCDM:Object > HydraWorks:Work : Digital Work
This is the digital work as a whole - so any information about the digitization, the filesets are related directly to this object, but descriptive metadata about the intellectual work (the bulk of the descriptive metadata) is used with the Intellectual Work class. This allows us to make descriptive metadata assertions (such as format = manuscripts, or rights = digital asset viewing and reuse rights) that aren't in conflict with digital object descriptions (format = jpeg or rights = physical resource access or reuse rights). The Digital Works can have PCDM:Objects children for Parts that need separate description (if the pages of a book are all separate filesets and require separate technical/descriptive/administrative metadata, for example).

####Descriptive metadata available on this class:

- **dcterms:title** = title for the digital object, usually taken directly from the intellectual work title. => only display the intellectual work title via Solr for the time being. This is more for better management of Fedora objects in Fedora.
- **dcterms:rightsHolder** = digital asset rights holder if they exist (none do at present for Huntington) => digital_rightsHolder
- **dcterms:description** = ENCODINGDESC/EDITORIALDECL/P => digital_tech_note
- **dcterms:identifier** = FILEDESC/PUBLICATIONSTMT/IDNO => digital_identifier (this is the DLXS identifier, not the intellectual concept identifier)

####PCDM + Other RDF Relationships on this class:

*Digital Object -PCDM:hasMember-> Work/Resource*

*Digital Object -EDM:aggregatedCHO-> Work/Resource*

*Digital Object <-PCDM:isMemberOf- Work/Resource*

###PCDM:Object > HydraWorks:Work & > dpla:SourceResource : Intellectual Work
This is the intellectual work represented by the Digital Work. The bulk of the descriptive metadata is here. Eventually, we may look into the option of having this object generated through a RDF Shape on an external triplestore containing more robust intellectual work metadata (and metadata ontologies). While one could, theoretically, have an Intellectual Work for each Digital Work Object Level (or the Digital Collection itself), we are limiting Intellectual Works for the time being to those represented roughly by bibliographic objects - with an eye to system efficiency and object interoperability in delineating this (especially when we get into journals). Resource abstractions/domain models like FRBR or RDA:Work etc. are not to be used here. 'Work' is used in a broader way.

Need to rdfs:type this object always as an instance of dpla:SourceResource in the ActiveFedora model (I believe that the pcdm:object typing is automatic when using the HydraWorks gem - need to verify).

**SubClasses**
Can have more refined ActiveFedora models here for things like 'Intellecual Work - Book', 'Intellectual Work - Journal', perhaps for validation of different fields required for each work type (though the metadata fields should be used consistently, just obligation would change).

####Descriptive metadata available on this class (at least for Huntington):

- **dcterms:abstract** = Nothing in existing DLXS XML to map => abstract
- **dcterms:alternative** = Nothing in existing DLXS XML to map => alt_title
- **dcterms:collection** = "Huntington Free Library Native American Collection" (DPLA types range of this as dcmitype:collection - may have reprecussions further down the ontology development for these digital collections)
- **dcterms:contributor** = Nothing in existing DLXS XML to map => contributor
- **dcterms:creator** = FILEDESC/SOURCEDESC/BIBL/AUTHOR => creator
- (additional role terms will be added from RDAU or LoC Relators as encountered in mappings)
- **dcterms:created** = FILEDESC/SOURCEDESC/BIBL/DATE => date (currently taking literals, would like to type as date/fix encoding. may want separate date text and date key fields in that instance.)
- **dcterms:description** = Nothing in existing DLXS XML to map => description
- **dcterms:extent** = FILEDESC/SOURCEDESC/BIBL/NOTE => intell_extent
- **dcterms:format** = "books" => form
- **dcterms:identifier** = Nothing in existing DLXS XML to map => identifier
- **dcterms:language** = Nothing in existing DLXS XML to map => language
- **VIVO:placeOfPublication** = FILEDESC/SOURCEDESC/BIBL/PUBPLACE => pubplace
- **dcterms:publisher** = FILEDESC/SOURCEDESC/BIBL/PUBLISHER => publisher
- **EDM.currentLocation** = FILEDESC/PUBLICATIONSTMT/PUBLISHER => repository
- **dcterms:rights** = Nothing in existing DLXS XML to map => intell_rights
- **dcterms:rightsHolder** = intellectual resource rights holder if they exist (none do at present for Huntington) => intell_rightsHolder
- **dc:subject** = PROFILEDESC/TEXTCLASS/KEYWORDS/TERM => subject (all types together at present)
- **dcterms:title** = FILEDESC/SOURCEDESC/BIBL/TITLE[@TYPE='main'] => title
- **dcterms:type** = "Text" => item_type
- **dcterms:relation** = OCR Text => ocr (wanted more granular term to capture this field - as we don't keep the OCR as a separate file - but just am not finding anything without domain/range restrictions).

####PCDM + Other RDF Relationships on this class:

*Digital Work -PCDM:hasMember-> Secondary Digital Work(s) if needed*

*Digital Work <-PCDM:isMemberOf- Secondary Digital Work(s) if needed*

###PCDM:Object > HydraWorks:Work == Secondary Digital Work, as needed

####Descriptive metadata available on this class:

- to be added as encountered. 
- **dcterms:title** (if used at part-level)
- this class is not intended to be paired with secondary level Intellectual Work; digitization and description efforts should work to capture discrete Intellectual Works such that the metadata on the top level Intellectual Work class instance covers the parts as needed.

####PCDM + Other RDF Relationships on this class:

*Digital Work|Secondary Digital Work(s) -PCDM:hasMember-> File Set*

*Digital Work|Secondary Digital Work(s) <-PCDM:isMemberOf- File Set*

###PCDM:Object < HydraWorks:FileSet : File Set

####Descriptive metadata available on this class:

- **dcterms:extent** = FILEDESC/EXTENT => files_extent
- **dcterms:title** = TEXT/BODY/DIV1/HEAD => fileset_title
- anything else file set specific, as encountered (crossing into technical metadata)

####PCDM + Other RDF Relationships on this class:

*File Set -PCDM:hasFile-> File(s)*

*File Set <-PCDM:isFileOf- File(s)*

###PCDM:File < HydraWorks:File : File

####Descriptive metadata available on this class:

- anything each file specific, as encountered (crossing into technical metadata). following is taken from PCDM technical metadata recommendations (which we should take with a grain of salt, if at all)
- **ebucore:filename** = filename
- **ebucore:fileSize** = file size in bytes
- **rdfs:label** = file label
- **ebucore:dateCreated** = date file was created


##Mapping from DLXS XML to "Simple RDF" (with normalization notes)

Field | Concept | RDF Mapping | Notes
--- | --- | --- | ---
**ENCODINGDESC/EDITORIALDECL/P** | *Note* | pcdm:object[hydraWork:GenericWork] dcterms:description [literal] | OCR is not kept as separate file, but text referred to by descriptive metadata. Move Solr concept to technical note.
**FILEDESC/EXTENT** | Extent | pcdm:object[hydraWork:GeneralFile] dcterms:extent [literal] | This is extent for collection of digital objects/files attached to one resource/work. Doesn't describe each file at the file-level. Ex: "112 600dpi TIFF page images"
**FILEDESC/PUBLICATIONSTMT/IDNO** | Identifier | pcdm:object[dpla:SourceResource] dcterms:identifier [literal] | there only seems to be these dlxs identifiers used, wondering if we'll need to type this later on.
**FILEDESC/PUBLICATIONSTMT/PUBLISHER** | Repository | pcdm:object[dpla:sourceResource] **edm:currentLocation** [literal] | can't find other property that adequately covers repository without going beyond scope of current options. Prime entity resolution candidate.
**FILEDESC/PUBLICATIONSTMT/PUBPLACE** | Repository location? | Don't map | This is the location of the repository, captured above. Do we need? Otherwise can repeat edm:currentLocation or concatenate fields in some way.
**FILEDESC/SOURCEDESC/BIBL/AUTHOR** | Creator | pcdm:object[dpla:SourceResource] dcterms:creator [literal] | Some are many creators concatenated, others contain role terms. Look into possibility of using more specific marcrel properties for these role terms (and removing role term from literal value). e.g. "Wells, Roger A.E., compiler" => pcdm:object marcrel:compiler "Wells, Roger A.E."@en. Prime entity resolution candidate.
**FILEDESC/SOURCEDESC/BIBL/DATE** | Date | pcdm:object[dpla:SourceResource] dcterms:created [literal] | 1 value has a reprint note attached, some use of dashes (inconsistent) for ranges, 1 questionable/unknown value. Look into remediation for then assigning encoding datatype to these literals? EDTF or a more generic ISO standard?
**FILEDESC/SOURCEDESC/BIBL/NOTE** | Extent (not originally mapped) | pcdm:object[dplaSourceResource] dcterms:extent [literal] | this is the physical resource extent and should be attached to the object describing that resource (unlike extent above, which is more about digital file extent). Not sure why it is in a Note field.
**FILEDESC/SOURCEDESC/BIBL/PUBLISHER** | Publisher | pcdm:object[dpla:SourceResource] dcterms:publisher [literal] | this is the physical resource's actual publisher, not the digitizer nor the repository. Looks transcribed, so normalization is limited (pick this up with RDA folks in LTS at some point).  Otherwise, entity resolution candidate.
**FILEDESC/SOURCEDESC/BIBL/PUBPLACE** | Creation location | pcdm:object[dpla:SourceResource] vivo:placeOfPublication [literal] | LD4L option has domain/range restrictions that make it not good option for this. Not sure I like the data property route - what if we want to normalize/resolve placenames (i.e. make into objects)? Need to keep looking.
**FILEDESC/SOURCEDESC/BIBL/TITLE[@TYPE='main']** | Title | pcdm:object[dpla:SourceResource] dcterms:title [literal] | same values appears as FILEDESC/TITLESTMT/TITLE (below)
**FILEDESC/TITLESTMT/AUTHOR** | skip | skip | Creator values, appears to be same as FILEDESC/SOURCEDESC/BIBL/AUTHOR which is mapped
**FILEDESC/TITLESTMT/TITLE** | skip | skip | Title values, appears to be same as FILEDESC/SOURCEDESC/BIBL/TITLE which is mapped
**PROFILEDESC/TEXTCLASS/KEYWORDS/TERM** | Subject | pcdm:object[dpla:SourceResource] dc:subject [literal] | dcterms:subject is meant to be used with non-literal values, according to DCMI. Can consider using when we map these to external URIs (most should be fairly straight forward entity matching). Replace ' - ' with '--' is first step towards LC-influenced normalization.
**TEXT/BODY/DIV1/HEAD** | structural metadata | pcdm:object(hydraWork:GeneralFile) dcterms:title [literal] | this appears to be the label/kind of files represented in the requisite wrapper element.
**BODY** | Structural Metadata | |
**DIV1** | Structural Metadata | |
**PB** | Structural Metadata | |

