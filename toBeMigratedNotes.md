##Review of XML dumps in Metadata/Projects/DLXStoHydra Directory in preparation for Hydra

###Antislavery.xml

**Overview of Metadata Usage in Record Items**

```
                /record/ENCODINGDESC/EDITORIALDECL/P: |=========================|      4/4 | 100%
                             /record/FILEDESC/EXTENT: |=========================|      4/4 | 100%
                     /record/FILEDESC/NOTESSTMT/NOTE: |=========================|      4/4 | 100%
 /record/FILEDESC/PUBLICATIONSTMT/IDNO[@TYPE='dlps']: |=========================|      4/4 | 100%
          /record/FILEDESC/PUBLICATIONSTMT/PUBLISHER: |=========================|      4/4 | 100%
           /record/FILEDESC/PUBLICATIONSTMT/PUBPLACE: |=========================|      4/4 | 100%
             /record/FILEDESC/SOURCEDESC/BIBL/AUTHOR: |=========================|      4/4 | 100%
               /record/FILEDESC/SOURCEDESC/BIBL/DATE: |=========================|      4/4 | 100%
               /record/FILEDESC/SOURCEDESC/BIBL/NOTE: |=========================|      4/4 | 100%
          /record/FILEDESC/SOURCEDESC/BIBL/PUBLISHER: |=========================|      4/4 | 100%
           /record/FILEDESC/SOURCEDESC/BIBL/PUBPLACE: |=========================|      4/4 | 100%
/record/FILEDESC/SOURCEDESC/BIBL/TITLE[@TYPE='main']: |=========================|      4/4 | 100%
                   /record/FILEDESC/TITLESTMT/AUTHOR: |=========================|      4/4 | 100%
       /record/FILEDESC/TITLESTMT/TITLE[@TYPE='245']: |=========================|      4/4 | 100%
         /record/PROFILEDESC/TEXTCLASS/KEYWORDS/TERM: |=========================|      4/4 | 100%
                         /record/TEXT/BODY/DIV1/HEAD: |=========================|      4/4 | 100%
```

**Notes:**

- These are not elements in any namespace
- FILEDESC/TITLESTMT/TITLE and FILEDESC/SOURCEDESC/BIBL/TITLE are the same. Include shelf locator information - parse? (break off at first open parenthesis.) and date ranges. Check if date ranges of collection or item?
- filedesc wrapper seems to hold most of descriptive metadata
- editorialdesc/editorialdecl/p holds OCR quality statement ('we scanned, no promise of correction')
- filedesc/extent covers number of pages, resolution + filetype of scans
- filedesc/notesstmt/note is digitization note ('digitized by...')
- not sure of the source of the identifiers found in filedesc/publicationstatement/idno (dlps is a digization group?)
- FILEDESC/PUBLICATIONSTMT/PUBLISHER and FILEDESC/SOURCEDESC/BIBL/PUBLISHER is Cornell University Library, needs to be changed to reflect the repository.
- FILEDESC/PUBLICATIONSTMT/PUBPLACE and FILEDESC/SOURCEDESC/BIBL/PUBPLACE is Ithaca, NY. Remove? May also be repository location information.
- FILEDESC/SOURCEDESC/BIBL/AUTHOR and FILEDESC/TITLESTMT/AUTHOR are same, they both have one name (good form - last, first), 'Various Authors' also used in separate field. Suppress various authors?
- FILEDESC/SOURCEDESC/BIBL/DATE are all date ranges with spaces around dashes
- FILEDESC/SOURCEDESC/BIBL/NOTE are all pages - map to physical extent?
- PROFILEDESC/TEXTCLASS/KEYWORDS/TERM contains four different subject headings repeated:
  - Slavery
  - Abolition
  - Samuel J. May
  - Antislavery
- TEXT/BODY/DIV1/HEAD - title(s) of structural element section. Includes elements for all files, structural metadata attached to the digital object.

**Enhancement possibilities:**

- easy FAST URIs for subject headings
- 1 name to grab URI for name (is in naf)
- split title to have shelf locator in separate field?
- hide away entity to some technical metadata, use note for physical entity
- fields or information to add based off of digital project?

###Bees.xml

**Overview of Metadata Usage in Record Items**

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
           /record/FILEDESC/SOURCEDESC/BIBL/TITLE: |======================== |     48/49 |  97%
                /record/FILEDESC/TITLESTMT/AUTHOR: |=========================|     49/49 | 100%
                 /record/FILEDESC/TITLESTMT/TITLE: |=========================|     49/49 | 100%
                    /record/PROFILEDESC/TEXTCLASS: |                         |      1/49 |   2%
      /record/PROFILEDESC/TEXTCLASS/KEYWORDS/TERM: |======================== |     48/49 |  97%
               /record/TEXT/BODY/DIV1/DIV2/AUTHOR: |                         |      1/49 |   2%
                /record/TEXT/BODY/DIV1/DIV2/TITLE: |                         |      1/49 |   2%
                      /record/TEXT/BODY/DIV1/HEAD: |=========================|     49/49 | 100%
```

**Notes:**

- These are not elements in any namespace
- Sample XML is not well-formed - missing closing tag in one record. Repaired for sake of review.
- ENCODINGDESC/EDITORIALDECL/P is a note on the OCR process.
-

**Enhancement possibilities:**

-

