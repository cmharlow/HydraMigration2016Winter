#CUL Fedora 4 Digital Collections (main) Migration Docs


---

This is Christina's copy of this documentation, for sake of capturing details and having a place to store F4 scripts. Official project documentation of record is stored in Box and Cornell's Confluence wiki, and will be updated with details from this when they are ready.

---

##TOC for this Repository's Documentation

- [Repository Overview](README.md)
- [Collections to be Migrated with links to Collection-Specific Mapping Notes and Analysis](Docs/toBeMigrated.md)
- [CUL Digital Collections Metadata Application Profile & Metadata Work Plan](Docs/CULPCDM.md)
- [CUL Digital Collections MAP to Solr Concepts Mapping](Docs/MappingsToConcepts.md)
- [Existing Fedora 3 Metadata Analysis](Docs/Fedora3/Fedora3MetadataNotes.md)

##Scope
Focus is on DLXS metadata already migrated or to be migrated to Hydra. These metadata and associated objects will be stored in Fedora then accessed there by Solr, not on other collections (like SharedShelf) where Solr access the metadata and objects from a different object store.

##Overview of All DLXS Metadata in/from DLXS
Fields being used in DLXS, currently mapped 1-1 to Fedora objects with OM/XML records. Some collections included here that have already been mapped and migrated to Hydra using Fedora 3; others (the bulk), not yet migrated.

Note that some fields displaying as not used in following reports/overviews are technical metadata fields that don't have text, just a series of attributes on the XML elements. There seems to be a procedure in place for handling these.

Fields being used across all collections that contain text values (including those already migrated) in DLXS, as found in the XML data dumps provided (this does not include all fields possible for technical metadata capture in self-closing XML elements):

```
             /record/ENCODINGDESC/EDITORIALDECL/P: |=========================|  16902/16902 | 100%
             /record/FILEDESC/EDITIONSTMT/EDITION: |                         |     69/16902 |   0%
                          /record/FILEDESC/EXTENT: |======================== |  16899/16902 |  99%
                  /record/FILEDESC/NOTESSTMT/NOTE: |===========              |   7619/16902 |  45%
/record/FILEDESC/PUBLICATIONSTMT/AVAILABILITY/DIV: |                         |      2/16902 |   0%
  /record/FILEDESC/PUBLICATIONSTMT/AVAILABILITY/P: |                         |    102/16902 |   0%
            /record/FILEDESC/PUBLICATIONSTMT/IDNO: |======================== |  16899/16902 |  99%
       /record/FILEDESC/PUBLICATIONSTMT/PUBLISHER: |======================== |  16899/16902 |  99%
        /record/FILEDESC/PUBLICATIONSTMT/PUBPLACE: |======================== |  16899/16902 |  99%
              /record/FILEDESC/SERIESSTMT/TITLE/A: |====                     |   2853/16902 |  16%
          /record/FILEDESC/SOURCEDESC/BIBL/AUTHOR: |=======================  |  16099/16902 |  95%
            /record/FILEDESC/SOURCEDESC/BIBL/DATE: |======================== |  16889/16902 |  99%
            /record/FILEDESC/SOURCEDESC/BIBL/NOTE: |=========                |   6656/16902 |  39%
       /record/FILEDESC/SOURCEDESC/BIBL/PUBLISHER: |=====================    |  14476/16902 |  85%
        /record/FILEDESC/SOURCEDESC/BIBL/PUBPLACE: |======================== |  16585/16902 |  98%
           /record/FILEDESC/SOURCEDESC/BIBL/TITLE: |======================== |  16899/16902 |  99%
                /record/FILEDESC/TITLESTMT/AUTHOR: |======================== |  16343/16902 |  96%
                 /record/FILEDESC/TITLESTMT/TITLE: |=========================|  16902/16902 | 100%
                    /record/PROFILEDESC/TEXTCLASS: |                         |     60/16902 |   0%
           /record/PROFILEDESC/TEXTCLASS/KEYWORDS: |===========              |   8048/16902 |  47%
      /record/PROFILEDESC/TEXTCLASS/KEYWORDS/TERM: |=============            |   8794/16902 |  52%
               /record/TEXT/BODY/DIV1/DIV2/AUTHOR: |===                      |   2445/16902 |  14%
                 /record/TEXT/BODY/DIV1/DIV2/HEAD: |                         |    363/16902 |   2%
                    /record/TEXT/BODY/DIV1/DIV2/P: |                         |    264/16902 |   1%
                /record/TEXT/BODY/DIV1/DIV2/TITLE: |====                     |   2725/16902 |  16%
                      /record/TEXT/BODY/DIV1/HEAD: |=========================|  16902/16902 | 100%
                         /record/TEXT/BODY/DIV1/P: |                         |    328/16902 |   1%
                              /record/TEXT/BODY/P: |                         |      3/16902 |   0%
```

More detailed notes on these fields is in [DLXStobeMigratedNotes.md](Docs/toBeMigratedNotes.md)

##Overview of DLXS Metadata already migrated to Hydra
Fields being used/exposed in Solr/as JSON in Blacklight at present for DLXS objects already migrated to Hydra with Fedora 3 (this doesn't touch on underlying OM/XML records currently in Fedora, which are a 1-1 match from DLXS metadata, just what is exposed via Solr/Blacklight). Also, some fields are Solr-specific:

```
                   _version_: |=========================|    834/834 | 100%
     active_fedora_model_ssi: |=========================|    834/834 | 100%
        author_creator_tesim: |=========================|    834/834 | 100%
                    author_t: |=========================|    834/834 | 100%
                author_tesim: |=========================|    834/834 | 100%
        bibl_titletype_tesim: |=========================|    834/834 | 100%
                  book_id_ts: |=========================|    834/834 | 100%
              book_ocr_tesim: |======================== |    829/834 |  99%
            collection_tesim: |=========================|    834/834 | 100%
creation_site_location_tesim: |======================== |    833/834 |  99%
         creator_facet_tesim: |=========================|    834/834 | 100%
                   creator_t: |=========================|    834/834 | 100%
                  date_tesim: |                         |      5/834 |   0%
       editorialdecl_n_tesim: |=========================|    834/834 | 100%
         editorialdecl_tesim: |=====================    |    710/834 |  85%
                extent_tesim: |=========================|    834/834 | 100%
                format_tesim: |=========================|    834/834 | 100%
              has_model_ssim: |=========================|    834/834 | 100%
              has_pages_ssim: |=========================|    834/834 | 100%
                          id: |=========================|    834/834 | 100%
                  lang_tesim: |=====================    |    710/834 |  85%
             latest_date_isi: |=========================|    834/834 | 100%
          object_profile_ssm: |=========================|    834/834 | 100%
            object_state_ssi: |=========================|    834/834 | 100%
               pubdate_tesim: |=========================|    834/834 | 100%
             publisher_tesim: |======================== |    832/834 |  99%
              pubplace_tesim: |======================== |    833/834 |  99%
          pubstmt_idno_tesim: |=========================|    834/834 | 100%
     pubstmt_idno_type_tesim: |=========================|    834/834 | 100%
     pubstmt_publisher_tesim: |=========================|    834/834 | 100%
      pubstmt_pubplace_tesim: |=========================|    834/834 | 100%
      repository_place_tesim: |=========================|    834/834 | 100%
            repository_tesim: |=========================|    834/834 | 100%
               subject_tesim: |=========================|    834/834 | 100%
          system_create_dtsi: |=========================|    834/834 | 100%
        system_modified_dtsi: |=========================|    834/834 | 100%
                   timestamp: |=========================|    834/834 | 100%
                   title_ssi: |=========================|    834/834 | 100%
                 title_tesim: |=========================|    834/834 | 100%
      titlestmt_author_tesim: |=========================|    834/834 | 100%
       titlestmt_title_tesim: |=========================|    834/834 | 100%
   titlestmt_titletype_tesim: |=========================|    834/834 | 100%
```

More detailed notes on these fields is in [ActiveHydraMetadataNotes.md](Docs/HydraMetadataNotes.md)

##Mappings
Two kinds of mappings need to occur:

1. Mappings of not migrated DLXS collections' metadata to the "simple" metadata concepts grouping used now and accessible at this [Box spreadsheet](https://cornell.box.com/s/egu0slwx19xz9euxcgj428c9esvpuyzq).
2. Mappings of the "simple" metadata concepts to a more complex, PCDM-based RDF model to be used with Fedora 4.7. This may or may not include full RDF graphs attached to the Fedora objects, or some properties attached to the Fedora objects and the rest of the metadata kept either in an external triplestore (this differentiation required as Fedora is an object store, not a triplestore, decisions on digital objects application profiles, etc.).

