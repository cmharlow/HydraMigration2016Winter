#DLXS to Fedora 4 + Hydra Metadata Migration Notes
Notes here primarily for metadata normalization + entity matching work planned, confirmed mappings (for 'interim Simple RDF' plan) moved to the finalized mappings document: https://docs.google.com/spreadsheets/d/1SV2hP1tKQpPQrI1cEBWgx6NyO56YhjUCkOD_vxrzlEQ/edit?usp=sharing.

##Collection by Collection Mappings
Go to the relevant page as listed [here](toBeMigrated.md). If a page doesn't exist, it hasn't been mapped yet. Listed in order of migration work due date.

##Proposed PCDM Model for 'Simple RDF' interim
A lot of this is written with short and mid term future metadata work (normalization, entity resolution/URI retrieval, more robust dig collection descriptive metadata ontology written) in mind.

Structure of Digital Objects in our Fedora 4/Hydra stack using PCDM:

###PCDM Object > Subclass of this : Class Label at CUL (set up for making CUL object ontology?)
Notes on this class.

Descriptive metadata so far mapped for this class:

- **the metadata term** = the value or mapping for our test collection, Huntington, along with notes for near future metadata work on these => the Solr 'concept' (to keep in line with other collections that go directly to Solr)

RDF Relationships on this class:

The RDF relationships expected for this class, symmetry of those properties not assumed (hence A -> B and B -> A are both given)

###PCDM:Collection > HydraWorks:Collection : Digital Collection
This is the digital collection that current maps to the dlxs identifier sets (i.e. 'hunt', 'bol', etc.). This is required. Can be repeated/nested as needed.

Descriptive metadata available on this class:

- **dcterms:title** = literal =>collection_title
- **dcterms:abstract** = literal => collection_abstract
- **dcterms:created** = literal => collection_date
- **dcterms:identifier** = literal => collection_bibid
- **dc:publisher** = literal => collection_publ
- **dcterms:publisher** = literal => collection_publ
- **dcterms:relation** = URL => collection_relatedURL

PCDM + Other RDF Relationships on this class:

If no secondary PCDM:Collection for Set:
*Digital Collection -PCDM:hasMember-> Intellectual Work*

*Digital Collection <-PCDM:isMemberOf- Intellectual Work*

If there is a secondary PCDM:Collection for Set:
*Digital Collection -PCDM:hasMember-> Set*

*Digital Collection <-PCDM:isMemberOf- Set*

If there is a related object PCDM:Object for Collection:
*Digital Collection -PCDM:hasRelatedObject-> Digital Collection Related Object*

*Digital Collection <-PCDM:relatedObjectOf- Digital Collection Related Object*

###PCDM:Collection > HydraWorks:Collection : Digital Collection Related Object
This is an object that relates to the Digital Collection but isn't part of that collection. Not required.

Descriptive metadata available on this class:

- **dcterms:title** = literal =>relObject_title
- **dcterms:abstract** = literal => relObject_abstract
- **dcterms:created** = literal => relObject_date
- **dcterms:identifier** = literal => relObject_bibid
- **dc:publisher** = literal => relObject_publ
- **dcterms:publisher** = literal => relObject_publ
- **dcterms:relation** = URL => relObject_relatedURL
- others to be added as encountered

PCDM + Other RDF Relationships on this class:
*Digital Collection -PCDM:hasRelatedObject-> Digital Collection Related Object*

*Digital Collection <-PCDM:relatedObjectOf- Digital Collection Related Object*

###PCDM:Collection > HydraWorks:Collection : Set
This is a generic set used as needed for further differentiation of works and collections. Not required.

Descriptive metadata available on this class:

- **dcterms:title** = literal => set_title
- **dcterms:abstract** = literal => set_abstract
- **dcterms:created** = literal => set_date
- **dcterms:identifier** = literal => set_id
- **dc:publisher** = literal => set_publ
- **dcterms:publisher** = URI < dcterms:Agent => set_publ
- **dcterms:relation** = URL => set_relatedURL

PCDM + Other RDF Relationships on this class:
*Set -PCDM:hasMember-> Intellectual Work*

*Set <-PCDM:isMemberOf- Intellectual Work*

###PCDM:Object > HydraWorks:Work : Intellectual Work
This is the intellectual work represented by the Digital Work. The bulk of the descriptive metadata is here. Resource abstractions/domain models like FRBR or RDA:Work etc. are not to be used here. 'Work' is used in a broader way. Can be repeated/nested as needed (should be clarified in Collection mapping notes).

Descriptive metadata available on this class (constantly being expanded as collections are mapped):

- **dcterms:abstract** = literal => abstract
- **dcterms:alternative** = literal => alt_title
- **dc:contributor** = literal => contributor
- **dcterms:contributor** = URI => contributor_uri
- **dc:creator** = literal => creator
- **dcterms:creator** = URI => creator_uri
- (additional role terms will be added from RDAU or LoC Relators as encountered)
- **dcterms:created** = literal => date
- **dcterms:description** = literal => description
- **dcterms:extent** = literal (to become URI in enhancement work) => intell_extent
- **dc:format** = literal => form
- **dcterms:format** = URI => form_URI
- **dcterms:identifier** = literal => identifier
- **dcterms:language** = literal? => language
- **VIVO:placeOfPublication** = literal => pubplace 
- **dc:publisher** = literal => publisher
- **dcterms:publisher** = URI => publisher
- **EDM.currentLocation** = literal (to become URI in enhancement work) => repository
- **dc:rights** = literal => intell_rights
- **dcterms:rights** = URI => intell_rights_URI
- **dcterms:rightsHolder** = URI => intell_rightsHolder_URI
- **dc:subject** = literal => subject
- **dcterms:subject** = URI => subject
- **dcterms:title** = literal => title
- **dc:type** = literal (DCMI type) => item_type
- **dcterms:type** = URI => item_type_URI
- **dc:relation** = literal => ocr
- **dcterms:isPartOf** = literal? (cheat for solr) => need to discuss further.

PCDM + Other RDF Relationships on this class:

If there is a Part:
*Intellectual Work -PCDM:hasMember-> Part*

*Intellectual Work <-PCDM:isMemberOf- Part*

If there is no Part:
*Intellectual Work -PCDM:hasMember-> File Set*

*Intellectual Work <-PCDM:isMemberOf- File Set*

###PCDM:Object > HydraWorks:Work == Part (Secondary Intellectual Work), as needed
Digitization and description efforts should work to capture discrete Intellectual Works such that the metadata on the top level Intellectual Work class instance covers the parts as needed. 

Descriptive metadata available on this class:

- to be added as encountered. 
- **dcterms:title** literal (if used at part-level)
- **dc:subject** literal (if used at part-level)
- **dc:relation** literal OCR (if used at part-level)

PCDM + Other RDF Relationships on this class:

*Digital Work|Part -PCDM:hasMember-> File Set*

*Digital Work|Part <-PCDM:isMemberOf- File Set*

###PCDM:Object < HydraWorks:FileSet : File Set / Digital Work
This is the digital work as represented by file sets - so any information about the digitization and the filesets are related directly to these objects, but descriptive metadata about the intellectual work (the bulk of the descriptive metadata) is used with the Intellectual Work class. This allows us to make descriptive metadata assertions (such as format = manuscripts, or rights = digital asset viewing and reuse rights) that aren't in conflict with digital object descriptions (format = jpeg or rights = physical resource access or reuse rights).

Descriptive metadata available on this class:

- **dcterms:rights**
- **dcterms:rightsHolder**
- **dc:rights**
- **dcterms:description**
- **dcterms:identifier**
- **dcterms:extent** = literal => files_extent
- **dcterms:title** = literal => fileset_title
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

