#CUL DLXS + SharedShelf Migration Docs


##Review of XML dumps in Metadata/Projects/DLXStoHydra Directory

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

###Antislavery.xml

**Overview of Metadata Usage in Record Items**

```

```

**Notes:**

- These are not elements in any namespace

**Enhancement possibilities:**

-


