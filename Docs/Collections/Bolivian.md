#Bolivian.xml
Notes here primarily for metadata normalization + entity matching work planned, confirmed mappings (for 'interim Simple RDF' plan) moved to the finalized mappings document: https://docs.google.com/spreadsheets/d/1SV2hP1tKQpPQrI1cEBWgx6NyO56YhjUCkOD_vxrzlEQ/edit?usp=sharing.

##Overview of Existing Metadata Usage in DLXS XML for Bolivian
```
       /record/ENCODINGDESC/EDITORIALDECL/P: |=========================|    712/712 | 100% 
                    /record/FILEDESC/EXTENT: |=========================|    712/712 | 100% 
      /record/FILEDESC/PUBLICATIONSTMT/IDNO: |=========================|    712/712 | 100% 
 /record/FILEDESC/PUBLICATIONSTMT/PUBLISHER: |=========================|    712/712 | 100% 
  /record/FILEDESC/PUBLICATIONSTMT/PUBPLACE: |=========================|    712/712 | 100% 
    /record/FILEDESC/SOURCEDESC/BIBL/AUTHOR: |=========================|    712/712 | 100% 
      /record/FILEDESC/SOURCEDESC/BIBL/DATE: |=========================|    712/712 | 100% 
      /record/FILEDESC/SOURCEDESC/BIBL/NOTE: |=========================|    712/712 | 100% 
 /record/FILEDESC/SOURCEDESC/BIBL/PUBLISHER: |======================== |    710/712 |  99% 
  /record/FILEDESC/SOURCEDESC/BIBL/PUBPLACE: |======================== |    711/712 |  99% 
     /record/FILEDESC/SOURCEDESC/BIBL/TITLE: |=========================|    712/712 | 100% 
          /record/FILEDESC/TITLESTMT/AUTHOR: |=========================|    712/712 | 100% 
           /record/FILEDESC/TITLESTMT/TITLE: |=========================|    712/712 | 100% 
/record/PROFILEDESC/TEXTCLASS/KEYWORDS/TERM: |=========================|    712/712 | 100% 
                /record/TEXT/BODY/DIV1/HEAD: |=========================|    712/712 | 100%  
```

##Overview of Existing Solr Usage for Bolivian in Fedora 3
```
                   _version_: |=========================|    710/710 | 100% 
     active_fedora_model_ssi: |=========================|    710/710 | 100% 
        author_creator_tesim: |=========================|    710/710 | 100% 
                    author_t: |=========================|    710/710 | 100% 
                author_tesim: |=========================|    710/710 | 100% 
        bibl_titletype_tesim: |=========================|    710/710 | 100% 
                  book_id_ts: |=========================|    710/710 | 100% 
              book_ocr_tesim: |=========================|    710/710 | 100% 
            collection_tesim: |=========================|    710/710 | 100% 
creation_site_location_tesim: |======================== |    709/710 |  99% 
         creator_facet_tesim: |=========================|    710/710 | 100% 
                   creator_t: |=========================|    710/710 | 100% 
       editorialdecl_n_tesim: |=========================|    710/710 | 100% 
         editorialdecl_tesim: |=========================|    710/710 | 100% 
                extent_tesim: |=========================|    710/710 | 100% 
                format_tesim: |=========================|    710/710 | 100% 
              has_model_ssim: |=========================|    710/710 | 100% 
              has_pages_ssim: |=========================|    710/710 | 100% 
                          id: |=========================|    710/710 | 100% 
                  lang_tesim: |=========================|    710/710 | 100% 
             latest_date_isi: |=========================|    710/710 | 100% 
          object_profile_ssm: |=========================|    710/710 | 100% 
            object_state_ssi: |=========================|    710/710 | 100% 
               pubdate_tesim: |=========================|    710/710 | 100% 
             publisher_tesim: |======================== |    708/710 |  99% 
              pubplace_tesim: |======================== |    709/710 |  99% 
          pubstmt_idno_tesim: |=========================|    710/710 | 100% 
     pubstmt_idno_type_tesim: |=========================|    710/710 | 100% 
     pubstmt_publisher_tesim: |=========================|    710/710 | 100% 
      pubstmt_pubplace_tesim: |=========================|    710/710 | 100% 
      repository_place_tesim: |=========================|    710/710 | 100% 
            repository_tesim: |=========================|    710/710 | 100% 
                       score: |=========================|    710/710 | 100% 
               subject_tesim: |=========================|    710/710 | 100% 
          system_create_dtsi: |=========================|    710/710 | 100% 
        system_modified_dtsi: |=========================|    710/710 | 100% 
                   timestamp: |=========================|    710/710 | 100% 
                   title_ssi: |=========================|    710/710 | 100% 
                 title_tesim: |=========================|    710/710 | 100% 
      titlestmt_author_tesim: |=========================|    710/710 | 100% 
       titlestmt_title_tesim: |=========================|    710/710 | 100% 
   titlestmt_titletype_tesim: |=========================|    710/710 | 100% 
```

##Proposed PCDM Model for 'Simple RDF' interim
A lot of this is written with short and mid term future metadata work (normalization, entity resolution/URI retrieval, more robust dig collection descriptive metadata ontology written) in mind.

Structure of the following section:

###PCDM Object > Subclass of this : Class Label at CUL (set up for making CUL object ontology?)
Notes on this class.

Descriptive metadata so far mapped for this class:

- **the metadata term** = the value or mapping for our test collection, Huntington, along with notes for near future metadata work on these => the Solr 'concept' (to keep in line with other collections that go directly to Solr)

RDF Relationships on this class:

The RDF relationships expected for this class, symmetry of those properties not assumed (hence A -> B and B -> A are both given)

###PCDM:Collection > HydraWorks:Collection : Digital Collection
This is the digital collection that current maps to the dlxs identifier sets (i.e. 'hunt', 'bol', etc.). This is required.

Descriptive metadata available on this class:

- **dcterms:abstract** = "A collection of 715 digitized pamphlets documenting a century of Bolivian literate culture, beginning in 1848. They show a nation's struggle to establish viable institututions, to develop its economy, to educate its children and the back and forth of political argument." [literal] => collection_abstract
- **dcterms:date** = "2010" (want to add EDTF encoding since we know it in this case?) => collection_date
- **dcterms:identifier** = "6791057" => collection_bibid (can we type objects for MARC ids versus other identifiers that may appear?)
- **dc:publisher** = "Cornell University. Library" [literal] => collection_publ
- **dcterms:publisher** = http://id.loc.gov/authorities/names/n85179829 => collection_publ
- **dcterms:relation** = http://resolver.library.cornell.edu/misc/6791057 => collection_relatedURL
- **dcterms:title** = "Alfred Montalvo Bolivian Digital Pamphlets Collection" [literal] => collection_title

PCDM + Other RDF Relationships on this class:

If no secondary PCDM:Collection for Set:
*Digital Collection -PCDM:hasMember-> Intellectual Work*

*Digital Collection <-PCDM:isMemberOf- Intellectual Work*

If there is a secondary PCDM:Collection for Set:
*Digital Collection -PCDM:hasMember-> Set*

*Digital Collection <-PCDM:isMemberOf- Set*

###PCDM:Collection > HydraWorks:Collection : Set
This is a generic set used as needed for further differentiation of works and collections. Not required. Not used in Huntington.

Descriptive metadata available on this class:

- **dcterms:title** = n/a [literal] => set_title
- **dcterms:abstract** = n/a [literal] => set_abstract
- **dcterms:created** = n/a [literal, EDTF] => set_date
- **dcterms:identifier** = n/a [literal, typed as able] => set_id
- **dc:publisher** = n/a [literal] => set_publ
- **dcterms:publisher** = n/a [URI < dcterms:Agent] => set_publ
- **dcterms:relation** = n/a [URL] => set_relatedURL

PCDM + Other RDF Relationships on this class:
*Set -PCDM:hasMember-> Intellectual Work*

*Set <-PCDM:isMemberOf- Intellectual Work*

###PCDM:Object > HydraWorks:Work & > dpla:SourceResource : Intellectual Work
This is the intellectual work represented by the Digital Work. The bulk of the descriptive metadata is here. Eventually, we may look into the option of having this object generated through a RDF Shape on an external triplestore containing more robust intellectual work metadata (and metadata ontologies). While one could, theoretically, have an Intellectual Work for each Digital Work Object Level (or the Digital Collection itself), we are limiting Intellectual Works for the time being to those represented roughly by bibliographic objects - with an eye to system efficiency and object interoperability in delineating this (especially when we get into journals). Resource abstractions/domain models like FRBR or RDA:Work etc. are not to be used here. 'Work' is used in a broader way.

Descriptive metadata available on this class (at least for Bolivian, more to be added as other collections are mapped + migrated to Fedora 4):

- **dcterms:abstract** = Nothing in existing DLXS XML to map [literal] => abstract
- **dcterms:alternative** = Nothing in existing DLXS XML to map [literal] => alt_title
- **dc:creator** = FILEDESC/SOURCEDESC/BIBL/AUTHOR [literal] => creator
- **dcterms:creator** = to be matched [non-literal;entity resolution URIs] => creator_uri - no role terms included in values.
- **dcterms:created** = FILEDESC/SOURCEDESC/BIBL/DATE => date [literal] no encoding type asserted - this is the text date as provided.
- **dcterms:created** = FILEDESC/SOURCEDESC/BIBL/DATE normalized => date [literal^EDTF] EDTF encoding type asserted - this is the key date used for timeline searching.
- **dcterms:description** = Nothing in existing DLXS XML to map [literal] => description
- **dcterms:extent** = FILEDESC/SOURCEDESC/BIBL/NOTE [should be URI but uncertain about possibility object_profile_ssm subclassing/moving to resource for now] => extent (expand p. to page?)
- **dc:format** = "Pamphlets" [literal] => form
- **dcterms:format** = http://vocab.getty.edu/aat/300220572 [URI] => form
- **dcterms:identifier** = FILEDESC/PUBLICATIONSTMT/IDNO [literal] => identifier
- **dc:language** = "Spanish" [literal] => language
- **dcterms:language** = http://id.loc.gov/vocabulary/iso639-2/spa [URI < DCMI:LinguisticSystem] => language_URI
- **VIVO:placeOfPublication** = FILEDESC/SOURCEDESC/BIBL/PUBPLACE [literal; note: this is a datatype property] => pubplace 
- **dc:publisher** = FILEDESC/SOURCEDESC/BIBL/PUBLISHER => publisher
- **dcterms:publisher** = not used currently [URI;entity resolution candidate] => publisher
- **EDM.currentLocation** = FILEDESC/PUBLICATIONSTMT/PUBLISHER [non-literal, edm:Place instance] => repository (will be external URI - cheat with literal until entity resolution project?)
- **dc:rights** = Nothing in existing DLXS XML to map [literal; text statement when URI/community rights standard hasn't been used with dcterms:rights] => intell_rights
- **dcterms:rights** = Nothing in existing DLXS XML to map [non-literal; URI for any community-assigned rights] => intell_rights
- **dcterms:rightsHolder** = intellectual resource rights holder if they exist (none do at present for Huntington) [non-literal; will require probably local URI for entity] => intell_rightsHolder
- **dc:subject** = PROFILEDESC/TEXTCLASS/KEYWORDS/TERM [literal] => subject (all types together at present)
- **dcterms:subject** = not currently used [non-literal; will be the URIs for the resolved literals in dc:subject] => subject (all types together at present)
- **dcterms:title** = FILEDESC/SOURCEDESC/BIBL/TITLE[@TYPE='main']  [literal] => title
- **dc:type** = "Text" [literal: URI, entity resolution candidate to create dcterms:type] => item_type
- **dcterms:type** = external URI for "Text" [non-literal: URI, entity resolution candidate] => item_type
- **dc:relation** = OCR Text (the actual text, not a file/fedora obj URI) => ocr (wanted more granular term to capture this field - as we don't keep the OCR as a separate file - but just am not finding anything without domain/range restrictions).
- **dcterms:isPartOf** = PCDM:Collection URI < dcterms:Collection => need to discuss further, as part of ease of Solr creation for collection label. How to handle dcmi:Collection variances from PCDM:Collection?

PCDM + Other RDF Relationships on this class:

If there is a Part:
*Intellectual Work -PCDM:hasMember-> Part*

*Intellectual Work <-PCDM:isMemberOf- Part*

If there is no Part:
*Intellectual Work -PCDM:hasMember-> File Set*

*Intellectual Work <-PCDM:isMemberOf- File Set*

###PCDM:Object > HydraWorks:Work == Part (Secondary Intellectual Work), as needed
Digitization and description efforts should work to capture discrete Intellectual Works such that the metadata on the top level Intellectual Work class instance covers the parts as needed. We're not trying to create intellectual works all the way down, but the current Curation Concerns/HydraWork expectations of PCDM make this (and conflation of digital and intellectual works) hard to avoid.

Descriptive metadata available on this class:

- to be added as encountered. 
- **dcterms:title** [literal]  (if used at part-level)
- **dc:subject** [literal]  (if used at part-level)
- **dc:relation** [literal] OCR (if used at part-level)

PCDM + Other RDF Relationships on this class:

*Digital Work|Part -PCDM:hasMember-> File Set*

*Digital Work|Part <-PCDM:isMemberOf- File Set*

###PCDM:Object < HydraWorks:FileSet : File Set / Digital Work
This is the digital work as represented by file sets - so any information about the digitization and the filesets are related directly to these objects, but descriptive metadata about the intellectual work (the bulk of the descriptive metadata) is used with the Intellectual Work class. This allows us to make descriptive metadata assertions (such as format = manuscripts, or rights = digital asset viewing and reuse rights) that aren't in conflict with digital object descriptions (format = jpeg or rights = physical resource access or reuse rights).

Descriptive metadata available on this class:

- **dcterms:rights**
- **dcterms:rightsHolder**
- **dc:rights**
- **dcterms:description** = ENCODINGDESC/EDITORIALDECL/P [literal] => fileset_note (technical note? could go here or IW as we're keeping the actual OCR is there, but this is about our work on the digital surrogate, not the IW itself.)
- **dcterms:identifier**
- **dcterms:extent** = FILEDESC/EXTENT [should be resource, will be literal- see intellectual work extent for this issue] => files_extent
- **dcterms:title** = TEXT/BODY/DIV1/HEAD [literal] => fileset_title
- anything else file set specific, as encountered (crossing into technical metadata)

PCDM + Other RDF Relationships on this class:

*File Set -PCDM:hasFile-> File(s)*

*File Set <-PCDM:isFileOf- File(s)*

###PCDM:File < HydraWorks:File : File

Descriptive metadata available on this class:

- anything each file specific as stored in the original DLXS 'descriptive' metadata, as encountered (crossing into technical metadata). 
 
The following is taken from PCDM technical metadata recommendations (which we should take with a grain of salt, if at all)
- **ebucore:filename** = filename
- **ebucore:fileSize** = file size in bytes
- **rdfs:label** = file label
- **ebucore:dateCreated** = date file was created


##Mapping from DLXS XML to "Simple RDF" (with normalization notes)

Field | Concept | RDF Mapping | Notes
--- | --- | --- | ---
**ENCODINGDESC/EDITORIALDECL/P** | *Technical_Note* | pcdm:object[hydraWork:FileSet] dcterms:description [literal] | OCR creation note. The OCR itself is not kept as separate file, but text referred to by descriptive metadata. Move Solr concept to technical note.
**FILEDESC/EXTENT** | Fileset_Extent | pcdm:object[hydraWork:FileSet] dcterms:description [literal] | This is extent for collection of digital objects/files attached to one resource/work. Doesn't describe each file at the file-level. Ex: "112 600dpi TIFF page images"
**FILEDESC/PUBLICATIONSTMT/IDNO** | Identifier | pcdm:object[HydraWorks:Work] dcterms:identifier [literal] | there only seems to be these dlxs identifiers used, wondering if we'll need to type this later on.
**FILEDESC/PUBLICATIONSTMT/PUBLISHER** | Repository | pcdm:object[HydraWorks:Work] **edm:currentLocation** [literal until we can pull in external URIs] | can't find other property that adequately covers repository without going beyond scope of current options. Prime entity resolution candidate. Add RMC as repository.
**FILEDESC/PUBLICATIONSTMT/PUBPLACE** | Repository location? | Don't map | This is the location of the repository, captured above. Do we need? Otherwise can repeat edm:currentLocation or concatenate fields in some way.
**FILEDESC/SOURCEDESC/BIBL/AUTHOR** | Creator | pcdm:object[HydraWorks:Work] dc:creator [literal until we can pull in external URIs] | Some are many creators concatenated. Doesn't seem to include any role terms. Prime entity resolution candidate.
**FILEDESC/SOURCEDESC/BIBL/DATE** | Date | pcdm:object[HydraWorks:Work] dcterms:created [literal] | 1 value is implied range (1910s), rest are single year. Look into remediation for then assigning encoding datatype to these literals? EDTF or a more generic ISO standard?
**FILEDESC/SOURCEDESC/BIBL/NOTE** | Extent (not originally mapped) | pcdm:object[HydraWork:Work] dcterms:extent [literal for now] | this is the physical resource extent and should be attached to the object describing that resource (unlike extent above, which is more about digital file extent). Not sure why it is in a Note field.
**FILEDESC/SOURCEDESC/BIBL/PUBLISHER** | Publisher | pcdm:object[HydraWorks:Work] dc:publisher [literal] | this is the physical resource's actual publisher, not the digitizer nor the repository. Looks transcribed, so normalization is limited (pick this up with RDA folks in LTS at some point).  Otherwise, entity resolution candidate (except this was turned down).
**FILEDESC/SOURCEDESC/BIBL/PUBPLACE** | Creation location | pcdm:object[HydraWorks:Work] vivo:placeOfPublication [literal] | LD4L option has domain/range restrictions that make it not good option for this. Not sure I like the data property route - what if we want to normalize/resolve placenames (i.e. make into objects)? Need to keep looking.
**FILEDESC/SOURCEDESC/BIBL/TITLE[@TYPE='main']** | Title | pcdm:object[HydraWork:Work] dcterms:title [literal] | same values appears as FILEDESC/TITLESTMT/TITLE (below)
**FILEDESC/TITLESTMT/AUTHOR** | skip | skip | Creator values, appears to be same as FILEDESC/SOURCEDESC/BIBL/AUTHOR which is mapped
**FILEDESC/TITLESTMT/TITLE** | skip | skip | Title values, appears to be same as FILEDESC/SOURCEDESC/BIBL/TITLE which is mapped
**PROFILEDESC/TEXTCLASS/KEYWORDS/TERM** | Subject | pcdm:object[HydraWorks:Work] dc:subject [literal] | All of these are the same. Use form in line with LCSH, FAST: 'Bolivia--Pamphlets'.
**TEXT/BODY/DIV1/HEAD** | structural metadata | pcdm:object(HydraWorks:FileSet) dcterms:title [literal] | this appears to be the label/kind of files represented in the requisite wrapper element.
**BODY** | Structural Metadata | |
**DIV1** | Structural Metadata | |
**PB** | Structural Metadata | |

