###Hunt.xml

**Overview of Metadata Usage in DLXS XML for Hunt**

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

**Overview of Metadata Usage in Solr JSON for Hunt**

```

```

**Proposed Mapping to "Simple" RDF**

Field | Concept | RDF Mapping | Notes
--- | --- | --- | ---
ENCODINGDESC/EDITORIALDECL/P | *Note* | pcdm:file[for OCR text if kept as separate file?] dcterms:description [literal value] | All of these notes are on the OCR process, so really should be stored with technical metadata describing the file object (and not indexed as part of descriptive metadata). Move Solr concept to technical note.
FILEDESC/EXTENT | Extent? | pcdm:object[for File(s)] dcterms:extent [literal value] | This is extent for collection of digital objects/files attached to one resource/work. Should really be pushed to technical metadata too, but doesn't describe each file at the file-level. Ex: "112 600dpi TIFF page images"
FILEDESC/PUBLICATIONSTMT/IDNO | Identifier | pcdm:object[dpla:SourceResource] dcterms:identifier [value] | there only seems to be these dlxs identifiers used, wondering if we'll need to type this later on.
FILEDESC/PUBLICATIONSTMT/PUBLISHER | Repository | pcdm:object[dpla:sourceResource] **edm:currentLocation** [literal value] | can't find other property that adequately covers repository without going beyond scope of DPLA (and by extension, EDM) MAPs as well as dcterms/dc elements options.
FILEDESC/PUBLICATIONSTMT/PUBPLACE | Repository location? | keep? | This is the location of the repository, captured above. Do we need? Otherwise can repeat edm:currentLocation or concatenate fields in some way.
FILEDESC/SOURCEDESC/BIBL/AUTHOR | Creator | pcdm:object[dpla:SourceResource] dcterms:creator [literal value] | Some are two creators concatenated, others (many) contains role terms. Look into possibility of using more specific marcrel properties for these role terms (and removing role term from literal value). e.g. "Wells, Roger A.E., compiler"
FILEDESC/SOURCEDESC/BIBL/DATE | Date | pcdm:object[dpla:SourceResource] dcterms:created [literal value] | 1 value has a reprint note attached, some use of dashes (inconsistent) for ranges, 1 questionable/unknown value. Look into remediation for then assigning encoding datatype to these literals?
FILEDESC/SOURCEDESC/BIBL/NOTE | Extent (not originally mapped) | pcdm:object[dplaSourceResource] dcterms:extent [literal value] | this is the physical resource extent and should be attached to the object describing that resource (unlike extent above, which is more about digital file extent)
FILEDESC/SOURCEDESC/BIBL/PUBLISHER | Publisher | pcdm:object[dpla:SourceResource] dcterms:publisher [value] | this is the physical resource's actual publisher, not the digitizer nor the repository. Looks transcribed, so normalization is limited.
FILEDESC/SOURCEDESC/BIBL/PUBPLACE | Creation location | pcdm:object[dpla:SourceResource] *dcterms:spatial* [literal value] | I don't like dcterms:spatial for this, but could be well documented use going forward until more palatable property surfaces (shouldn't be conflicts of use until then as 1. subjects are typed now into geographic/person/etc, all just generic topics, and 2. could use broader dcterms:coverage if we do run into that.)
FILEDESC/SOURCEDESC/BIBL/TITLE[@TYPE='main'] | Title | pcdm:object[dpla:SourceResource] dcterms:title [literal value] | same values appears as FILEDESC/TITLESTMT/TITLE (below)
FILEDESC/TITLESTMT/AUTHOR | skip | skip | Creator values, appears to be same as FILEDESC/SOURCEDESC/BIBL/AUTHOR which is mapped
FILEDESC/TITLESTMT/TITLE | skip | skip | Title values, appears to be same as FILEDESC/SOURCEDESC/BIBL/TITLE which is mapped
PROFILEDESC/TEXTCLASS/KEYWORDS/TERM | Subject | pcdm:object[dpla:SourceResource] dc:subject [literal value] | dcterms:subject is meant to be used with non-literal values, according to DCMI. Can consider using when we map these to external URIs (most should be fairly straight forward entity matching). Replace ' - ' with '--' is first step towards LC-influenced normalization.
TEXT/BODY/DIV1/HEAD | structural metadata | pcdm:object(for generic file object) *dcterms:title??* [literal value] | this appears to be the label/kind of files represented in the requisite wrapper element.
BODY | Structural Metadata | |
DIV1 | Structural Metadata | |
PB | Structural Metadata | |


**Notes:**

-
