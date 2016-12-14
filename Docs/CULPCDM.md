# DLXS to Fedora 4 + Hydra Metadata Migration Notes

Notes here primarily for metadata normalization + entity matching work planned, confirmed mappings (for 'interim Simple RDF' plan) moved to the finalized mappings  [Box spreadsheet](https://cornell.box.com/s/egu0slwx19xz9euxcgj428c9esvpuyzq).

## Collection by Collection Mappings
Go to the relevant page as listed [here](toBeMigrated.md). If a page doesn't exist, it hasn't been mapped yet. Listed in order of migration work due date.

## DLXS <=> SharedShelf Solr Concepts Interop Mapping
For making sure updated DLXS to Fedora4 mappings make sense with existing SharedShelf Solr mappings, relevant notes are kept [here](MappingsToConcepts.md). It should represent the latest Solr mappings and config files for both datasets.

## Proposed PCDM Model for 'Simple RDF' interim
A lot of this is written with short and mid term future metadata work (normalization, entity resolution/URI retrieval, more robust descriptive metadata ontology) in mind.

---

Structure of the following documentation:

###PCDM Object > Subclass of this : Class Label at CUL (set up for making CUL object ontology?)
Notes on this class.

#### Descriptive Metadata Profile:

- **the metadata term** = the value or mapping for our test collection, Huntington, along with notes for near future metadata work on these.

#### Structural Profile:
The RDF relationships expected for this class, symmetry of those properties not assumed (hence A -> B and B -> A are both given)

---

Structure of Digital Objects in our Fedora 4/Hydra stack using PCDM:

### PCDM:Collection > HydraWorks:Collection : Digital Collection
This is the digital collection that current maps to the dlxs identifier sets (i.e. 'hunt', 'bol', etc.). This is required. Can be repeated/nested as needed.

#### Descriptive Metadata Profile:

- **dcterms:abstract** = string
- **dcterms:alternative** = string
- **rdau:P60376** [curator] = string (phase 2 removal)
- **rdau:P60376** [curator] = Agent URI (phase 2 addition)
- **dcterms:date** = EDTF literal
- **dcterms:identifier** = string
- **dc:language** = string (phase 2 removal)
- **dc:publisher** = string (phase 2 removal)
- **dcterms:publisher** = Agent URI (phase 2 addition)
- **dcterms:relation** = URL
- **dc:subject** = string (phase 2 removal)
- **dcterms:subject** = Concept URI (phase 2 addition)
- **dcterms:title** = literal

#### Structural Profile:
If no secondary PCDM:Collection for Set:

- *Digital Collection -PCDM:hasMember-> Intellectual Work*
- *Digital Collection <-PCDM:isMemberOf- Intellectual Work*

If there is a secondary PCDM:Collection for Set:

- *Digital Collection -PCDM:hasMember-> Set*
- *Digital Collection <-PCDM:isMemberOf- Set*

If there is a related object PCDM:Object for Collection:

- *Digital Collection -PCDM:hasRelatedObject-> Digital Collection Related Object*
- *Digital Collection <-PCDM:relatedObjectOf- Digital Collection Related Object*

If there is are members PCDM:Object(s) for this Collection (should always be true if there are not sets/sub-collections):

- *Digital Collection -PCDM:hasMember-> Repository Object*
- *Digital Collection <-PCDM:isMemberOf- Repository Object*

### PCDM:Object : Digital Collection Related Object
This is an object that relates to the Digital Collection but isn't part of that collection. Not required.

#### Descriptive Metadata Profile:

- **dcterms:abstract** = xs:string with language tagging
- **dcterms:date** = EDTF date
- **dcterms:identifier** = xs:string with identifier tagging (where able)
- **dc:publisher** = string (phase 2 removal)
- **dcterms:publisher** = Agent URI (phase 2 addition)
- **dcterms:relation** = URL
- **dcterms:title** = xs:string with language tagging

#### Structural Profile:

- *Digital Collection -PCDM:hasRelatedObject-> Digital Collection Related Object*
- *Digital Collection <-PCDM:relatedObjectOf- Digital Collection Related Object*

###PCDM:Collection > HydraWorks:Collection : Set
This is a generic set or sub-collection (nested collection) used as needed for further differentiation of works and collections. Not required.

Repeats profile and relationships from Digital Collection (above).

###PCDM:Object > HydraWorks:Work : Repository Work
This is the repository, intellectual work represented by the delivery digital asset(s). The bulk of the descriptive metadata for search, identification and discovery is here. We are limiting Repository Works for the time being to those represented roughly by bibliographic objects - with an eye to system efficiency and object interoperability in delineating this. Resource abstractions/domain models like FRBR or RDA:Work etc. are not to be used here. 'Work' is used in a broader way. Can be repeated/nested as needed (should be clarified in Collection mapping notes).

Specific forms (dcterms:format, normally also represented by the used ActiveFedora model) may follow more specific profiles, i.e., journals as opposed to books as opposed to photographs, etc.

#### Descriptive Metadata Profile:

- **dcterms:abstract** = literal
- **dcterms:alternative** = literal
- **dcterms:bibliographicCitation** = literal
- **rdau:P50189** [compiler] = literal (phase 2 enhancement)
- **marcrel:crp** [correspondent] = literal (phase 2 enhancement)
- **dc:contributor** = string (phase 2 removal)
- **dcterms:contributor** = Agent URI (phase 2 addition)
- **rdau:P60069** (copyright date) = EDTF-typed string
- **dc:creator** = string (phase 2 removal)
- **dcterms:creator** = Agent URI (phase 2 addition)
- (additional role terms will be added from RDAU or LoC Relators as encountered)
- **dcterms:date** = EDTF-typed string
- **dcterms:description** = language-typed string
- **bibo:edition** = literal
- **rdau:P60393** [editor] = literal (phase 2 enhancement)
- **dcterms:extent** = literal (to become URI in enhancement work)
- **dc:format** = string (phase 2 removal)
- **dcterms:format** = Concept URI (phase 2 addition)
- **dcterms:identifier** = identifier-typed string (where identifier type exists)
- **rdau:P60374** [issuing body] = string (phase 2 enhancement)
- **dc:language** = string (phase 2 removal)
- **dcterms:language** = Language URI (phase 2 addition)
- **dc:relation** = literal (OCR)
- **VIVO:placeOfPublication** = literal
- **dc:publisher** = string (phase 2 removal)
- **dcterms:publisher** = Agent URI (phase 2 addition)
- **EDM.currentLocation** = literal (to become URI in enhancement work)
- **dc:rights** = literal
- **dcterms:rights** = Rights Statement URI (phase 2 addition)
- **dcterms:rightsHolder** = Agent URI (phase 2 addition)
- **dcterms:source** = xs:string with identifier tagging (where able)
- **dc:subject** =  string (phase 2 removal)
- **dcterms:subject** = Concept URI (phase 2 addition)
- **dcterms:title** = language-tagged string
- **rdau:P60613** [translator] = literal (phase 2 enhancement)
- **dc:type** =  string (DCMI types; phase 2 removal)
- **dcterms:type** = Type URI (phase 2 addition)

#### Structural Profile:
If there is a Part:

- *Repository Work -PCDM:hasMember-> Part*
- *Repository Work <-PCDM:isMemberOf- Part*

If there is no Part:

- *Repository Work -PCDM:hasMember-> File Set*
- *Repository Work <-PCDM:isMemberOf- File Set*

###PCDM:Object (not HydraWorks:Work) == Part
Digitization and description efforts should work to capture discrete parts as needed to differentiate with more specificity for parts of a repository object or work.

#### Descriptive Metadata Profile:

- **dcterms:title** literal (if used at part-level)
- **dc:subject** literal (if used at part-level)
- **dc:relation** literal OCR (if used at part-level)
- Any other fields from the above Repository Work profile as applicable to the part-level (and only applicable at the part-level).

#### Structural Profile:

- *Digital Work|Part -PCDM:hasMember-> Fileset*
- *Digital Work|Part <-PCDM:isMemberOf- Fileset*

###PCDM:Object < HydraWorks:FileSet : Fileset / Digital Work
This is the digitization output as represented by filesets - so any information about the digitization and the filesets are related directly to these objects, but descriptive metadata about the intellectual work (the bulk of the descriptive metadata) is used with the Intellectual Work class. This allows us to make descriptive metadata assertions (such as format = manuscripts, or rights = digital asset viewing and reuse rights) that aren't in conflict with digital object descriptions (format = jpeg or rights = physical resource access or reuse rights).

#### Descriptive Metadata Profile:

- **dcterms:rights**
- **dcterms:rightsHolder**
- **dc:rights**
- **dcterms:description**
- **dcterms:identifier**
- **dcterms:extent** = literal => files_extent
- **dcterms:title** = literal => fileset_title
- anything else file set specific, as encountered (crossing into technical metadata)

#### Structural Profile:

- *Fileset -PCDM:hasFile-> File(s)*
- *Fileset <-PCDM:isFileOf- File(s)*

### PCDM:File < HydraWorks:File : File

The following is taken from PCDM technical metadata recommendations (which we should take with a grain of salt):

- **ebucore:filename** = filename
- **ebucore:fileSize** = file size in bytes
- **rdfs:label** = file label
- **ebucore:dateCreated** = date file was created

