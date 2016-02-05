#Unused PCDM implementation.

Kept for legacy/comparison/future testing purposes.

WE ARE NOT FOLLOWING THIS AT PRESENT AT CUL.

###PCDM Object > Subclass of this : Class Label at CUL (set up for making CUL object ontology?)
Notes on this class.

Descriptive metadata so far mapped for this class:

- **the metadata term** = the value or mapping for our test collection, Huntington, along with notes for near future metadata work on these => the Solr 'concept' (to keep in line with other collections that go directly to Solr)

RDF Relationships on this class:

The RDF relationships expected for this class, symmetry of those properties not assumed (hence A -> B and B -> A are both given)

###PCDM:Collection > HydraWorks:Collection : Digital Collection
This is the digital collection that current maps to the dlxs identifier sets (i.e. 'hunt', 'bol', etc.). There can be a secondary PCDM:Collection:Set if/as the need arises.

Descriptive metadata available on this class:

- **dcterms:title** = "Huntington Free Library Native American Collection" =>collection_title
- **dcterms:abstract** = "One of the largest collections of books and manuscripts of its kind, the Huntington collection contains extensive materials documenting the history, culture, languages, and arts of the native tribes of both North and South America. Contemporary politics and human rights issues are also important components of the collection.
Full text of a selection of 91 books from the Huntington Free Library Native American Collection representing the various genres in the collection." => collection_abstract
- **dcterms:created** = "2010" (want to add EDTF encoding since we know it in this case?) => collection_date
- **dcterms:identifier** = "6790930" => collection_bibid (can we type objects for MARC ids versus other identifiers that may appear?)
- **dc:publisher** = "Cornell University. Library" [literal] => collection_publ
- **dcterms:publisher** = (entity resolution/URI work candidate, nothing for now) => collection_publ
- **dcterms:relation** = http://ebooks.library.cornell.edu/h/hunt/ => collection_relatedURL

PCDM + Other RDF Relationships on this class:

*Digital Collection -PCDM:hasMember-> Digital Object*

*Digital Collection <-PCDM:isMemberOf- Digital Object*

###PCDM:Object > HydraWorks:Work : Digital Work
This is the digital work as a whole - so any information about the digitization, the filesets are related directly to this object, but descriptive metadata about the intellectual work (the bulk of the descriptive metadata) is used with the Intellectual Work class. This allows us to make descriptive metadata assertions (such as format = manuscripts, or rights = digital asset viewing and reuse rights) that aren't in conflict with digital object descriptions (format = jpeg or rights = physical resource access or reuse rights). The Digital Works can have PCDM:Objects children for Parts that need separate description (if the pages of a book are all separate filesets and require separate technical/descriptive/administrative metadata, for example).

Descriptive metadata available on this class:

- **dcterms:title** = title for the digital object, usually taken directly from the intellectual work title. literal. => only display the intellectual work title via Solr for the time being. This is more for better management of Fedora objects in Fedora.
- **dcterms:rightsHolder** = digital asset rights holder if they exist (none do at present for Huntington) [dcterms:Agent > external authority URI? Create local URI for storing other information about this person? Otherwise generic rights statement] => digital_rightsHolder
- **dcterms:description** = ENCODINGDESC/EDITORIALDECL/P => digital_tech_note
- **dcterms:identifier** = FILEDESC/PUBLICATIONSTMT/IDNO => digital_identifier (this is the DLXS identifier, not the intellectual concept identifier)

PCDM + Other RDF Relationships on this class:

*Digital Object -PCDM:hasMember-> Work/Resource*

*Digital Object -EDM:aggregatedCHO-> Work/Resource*

*Digital Object <-PCDM:isMemberOf- Work/Resource*

###PCDM:Object > HydraWorks:Work & > dpla:SourceResource : Intellectual Work
This is the intellectual work represented by the Digital Work. The bulk of the descriptive metadata is here. Eventually, we may look into the option of having this object generated through a RDF Shape on an external triplestore containing more robust intellectual work metadata (and metadata ontologies). While one could, theoretically, have an Intellectual Work for each Digital Work Object Level (or the Digital Collection itself), we are limiting Intellectual Works for the time being to those represented roughly by bibliographic objects - with an eye to system efficiency and object interoperability in delineating this (especially when we get into journals). Resource abstractions/domain models like FRBR or RDA:Work etc. are not to be used here. 'Work' is used in a broader way.

Need to rdf:type (fixed typo here) this object always as an instance of dpla:SourceResource in the ActiveFedora model (I believe that the pcdm:object typing is automatic when using the HydraWorks gem - need to verify).

Descriptive metadata available on this class (at least for Huntington, more to be added as other collections are mapped + migrated to Fedora 4):

- **dcterms:abstract** = Nothing in existing DLXS XML to map [literal] => abstract
- **dcterms:alternative** = Nothing in existing DLXS XML to map [literal] => alt_title
- **dc:contributor** = Nothing in existing DLXS XML to map [literal:prefLabel] => contributor
- **dcterms:contributor** = Nothing in existing DLXS XML to map [non-literal:external URI] => contributor_uri (would rather have this than literal/above, but is part of entity resolution project that comes after fedora 4 migration)
- **dc:creator** = FILEDESC/SOURCEDESC/BIBL/AUTHOR [literal] => creator
- **dcterms:creator** = to be matched [non-literal;entity resolution URIs] => creator_uri (same note re: URI/literal for dcterms:contributor)
- (additional role terms will be added from RDAU or LoC Relators as encountered in upcoming collections mappings)
- **dcterms:created** = FILEDESC/SOURCEDESC/BIBL/DATE => date [literal] no encoding type asserted (would like to type as date/fix encoding. may want separate date text and date key fields in that instance.)
- **dcterms:description** = Nothing in existing DLXS XML to map [literal] => description
- **dcterms:extent** = FILEDESC/SOURCEDESC/BIBL/NOTE [should be URI but uncertain about possibility object_profile_ssm subclassing/moving to resource for now] => intell_extent
- **dc:format** = "books" => form
- **dcterms:format** = "books" from chosen vocab URI [non-literal:external URI] => form (avoid until integrating fedora w/authorities + URIs is discussed)
- **dcterms:identifier** = Nothing in existing DLXS XML to map [literal] => identifier (will want to type eventually for type of identifier = marcbib, dlxs, other?)
- **dcterms:language** = Nothing in existing DLXS XML to map => language (we will want to add this in the mid-term future, but requires manual review? Also question of external URIs)
- **VIVO:placeOfPublication** = FILEDESC/SOURCEDESC/BIBL/PUBPLACE [literal; note: this is a datatype property] => pubplace 
- **dc:publisher** = FILEDESC/SOURCEDESC/BIBL/PUBLISHER => publisher
- **dcterms:publisher** = not used currently [non-literal;entity resolution candidate] => publisher
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

*Digital Work -PCDM:hasMember-> Secondary Digital Work(s) if needed*

*Digital Work <-PCDM:isMemberOf- Secondary Digital Work(s) if needed*

###PCDM:Object > HydraWorks:Work == Secondary Digital Work, as needed

Descriptive metadata available on this class:

- to be added as encountered. 
- **dcterms:title** [literal]  (if used at part-level)
- this class is not intended to be paired with secondary level Intellectual Work; digitization and description efforts should work to capture discrete Intellectual Works such that the metadata on the top level Intellectual Work class instance covers the parts as needed.

PCDM + Other RDF Relationships on this class:

*Digital Work|Secondary Digital Work(s) -PCDM:hasMember-> File Set*

*Digital Work|Secondary Digital Work(s) <-PCDM:isMemberOf- File Set*

###PCDM:Object < HydraWorks:FileSet : File Set

Descriptive metadata available on this class:

- **dcterms:extent** = FILEDESC/EXTENT [should be resource, will be literal- see intellectual work extent for this issue] => files_extent
- **dcterms:title** = TEXT/BODY/DIV1/HEAD [literal] => fileset_title
- anything else file set specific, as encountered (crossing into technical metadata)

PCDM + Other RDF Relationships on this class:

*File Set -PCDM:hasFile-> File(s)*

*File Set <-PCDM:isFileOf- File(s)*

###PCDM:File < HydraWorks:File : File

Descriptive metadata available on this class:

- anything each file specific, as encountered (crossing into technical metadata). following is taken from PCDM technical metadata recommendations (which we should take with a grain of salt, if at all)
- **ebucore:filename** = filename
- **ebucore:fileSize** = file size in bytes
- **rdfs:label** = file label
- **ebucore:dateCreated** = date file was created
