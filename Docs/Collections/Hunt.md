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
                /record/ENCODINGDESC/EDITORIALDECL/P: |=========================|     49/49 | 100%
                /record/FILEDESC/EDITIONSTMT/EDITION: |====                     |      9/49 |  18%
                             /record/FILEDESC/EXTENT: |======================== |     48/49 |  97%
                     /record/FILEDESC/NOTESSTMT/NOTE: |========                 |     16/49 |  32%
   /record/FILEDESC/PUBLICATIONSTMT/AVAILABILITY/DIV: |=                        |      2/49 |   4%
               /record/FILEDESC/PUBLICATIONSTMT/IDNO: |======================== |     48/49 |  97%
          /record/FILEDESC/PUBLICATIONSTMT/PUBLISHER: |======================== |     48/49 |  97%
           /record/FILEDESC/PUBLICATIONSTMT/PUBPLACE: |======================== |     48/49 |  97%
             /record/FILEDESC/SOURCEDESC/BIBL/AUTHOR: |======================== |     48/49 |  97%
               /record/FILEDESC/SOURCEDESC/BIBL/DATE: |======================== |     48/49 |  97%
          /record/FILEDESC/SOURCEDESC/BIBL/PUBLISHER: |======================   |     45/49 |  91%
           /record/FILEDESC/SOURCEDESC/BIBL/PUBPLACE: |======================   |     45/49 |  91%
/record/FILEDESC/SOURCEDESC/BIBL/TITLE[@TYPE='main']: |======================== |     48/49 |  97%
                   /record/FILEDESC/TITLESTMT/AUTHOR: |=========================|     49/49 | 100%
       /record/FILEDESC/TITLESTMT/TITLE[@TYPE='245']: |=========================|     49/49 | 100%
                       /record/PROFILEDESC/TEXTCLASS: |                         |      1/49 |   2%
         /record/PROFILEDESC/TEXTCLASS/KEYWORDS/TERM: |======================== |     48/49 |  97%
                  /record/TEXT/BODY/DIV1/DIV2/AUTHOR: |                         |      1/49 |   2%
                   /record/TEXT/BODY/DIV1/DIV2/TITLE: |                         |      1/49 |   2%
                         /record/TEXT/BODY/DIV1/HEAD: |=========================|     49/49 | 100%
```

**Proposed Mapping to RDF**

```
Field | Concept | RDF Property
--- | --- | ---
FILEDESC/SOURCEDESC/BIBL/PUBPLACE | Creation location | pcdm:obj
BIBL/AUTHOR | Creator | pcdm:obj dcterms:creator [value]
DATE | Date | pcdm:object dcterms:created [value]
EXTENT | Extent? | pcdm:object dcterms:extent [value]
IDNO | Identifier | pcdm:object dcterms:identifier [value]
NOTE | Note | pcdm:object dcterms:description [value]
P | Note | pcdm:object dcterms:description [value]
BIBL/PUBLISHER | Publisher | pcdm:object dcterms:publisher [value]
PUBLICATIONSTMT/PUBPLACE | Repository Location? |
PUBLICATIONSTMT/PUBLISHER | Repository |
TERM | Subject |
BIBL/TITLE | Title |
HEAD | | |
BODY | Structural Metadata | |
DIV1 | Structural Metadata | |
EDITORIALDECL | |
KEYWORDS | |
PB | Structural Metadata |
SOURCEDESC | |
```


**Notes:**

-
