##Detailed Review of DLXS Metadata already in Hydra with Fedora 3

Fields being used/exposed in Solr Json in Blacklight at present for DLXS objects already migrated to Hydra (this doesn't touch on underlying OM/XML records currently in Fedora, which are a 1-1 match from DLXS metadata, just what is exposed via Solr/Blacklight). Also, some fields are Solr-specific:

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

##Active Fedora Model

All 834 are following the Book ActiveFedora Model.

##author_creator_tesim = author_t = author_tesim

Unique values in that field (note, the apostrophes are not mine - they appear in the repo/discovery layer):

   - "Aguirre Achá, José"
   - "Aguirre, Miguel"
   - "Aguirre, Nataniel"
   - "Aillon, Jacobo"
   - "Aldunate, José Valerio"
   - "Aliaga y Nava, Felipe"
   - "Ameller, Juan José"
   - "Anaya, Jacinto"
   - "Andrade y Portugal, Crispin"
   - "Antequera, Benjamin"
   - "Antezana, Napolean Fernandez, and Francisco S. Sanchez"
   - "Aramayo, Carlos Víctor"
   - "Aramayo, Félix Avelino"
   - "Arce Lacaze, Luis"
   - "Argandoña, Luis de"
   - "Armentía, Nicolás"
   - "Arraya, Francisco"
   - "Arrien, Victor"
   - "Ascarrunz, Jenaro"
   - "Aspiazu, Agustín"
   - "Bacia, José"
   - "Balboa, Enrique Mallea"
   - "Balcazar, Juan Manuel"
   - "Baldivia, Juan José"
   - "Ballivian, Adolfo"
   - "Ballivian, Manuel V. "
   - "Ballivián, Manuel V."
   - "Ballón, Wenceslao Z."
   - "Barreto, José María and E. Solís Bergara"
   - "Bayá, Eulogio"
   - "Beltrán, Aurelio"
   - "Benavente, Juan de Mata"
   - "Bernal, Natalio"
   - "Berrios, José David"
   - "Blanco, Federico"
   - "Boada, Luis"
   - "Bosque, Juan de Dios"
   - "Bustamante y Barrera, Mariano"
   - "Bustillos, José E."
   - "Cabrera, Ladislao"
   - "Calderón, Abdón"
   - "Calderón, Ignacio"
   - "Calvimontes, Senon"
   - "Camacho, Eliodoro"
   - "Campero, Eduardo J."
   - "Campero, Issac S."
   - "Campero, Narciso "
   - "Campero, Narciso and Nicanor Flores"
   - "Canedo, Francisco de"
   - "Canedo, José Rafael"
   - "Carrasco, José and Ignacio Calderón"
   - "Carrasco, José"
   - "Castro, Martin"
   - "Chacón, Juan W."
   - "Clarin, Alas"
   - "Collazos Lara, Leonor"
   - "Corrales, Roberto N."
   - "Cortes, José Domingo"
   - "Crespo, Luis S."
   - "Criales, Isaac"
   - "Criales, Issac"
   - "Céspedes Rivero, Julián"
   - "Dalence, Zenón"
   - "Damiron, Ph and Bernardo Mendeo"
   - "Diez de Medina, Alberto"
   - "Diez de Medina, E."
   - "Dávalos, Benjamin A."
   - "Díez de Medina, Federico"
   - "Eduardo, Isaac G."
   - "Escalier, Jose Maria and Ismael Montes"
   - "Escobari, Isaac"
   - "Escobarí, Marcario D."
   - "Espinosa, Manuela"
   - "Eyzaguirre, Julio J."
   - "Fajardo, Francisco"
   - "Fernández Moya, Félix"
   - "Fernández, José C."
   - "Fernández, Nicolás"
   - "Fillol Herrera, Luis"
   - "Foster, Julio M."
   - "Frontanilla, Fernando"
   - "Frías, Luís"
   - "Fuente, Modesto de la"
   - "Galdo Justiana, Diego Araníbar"
   - "Ganci, Salvador"
   - "Gillet-Damitte, Jean-Jacques-Julien"
   - "Gomez, Manuel M."
   - "González, Abel"
   - "Granado, Francisco M. del"
   - "Guachalla, Fernando"
   - "Gutiérrez Guerra, José"
   - "Gutiérrez Guerra, René"
   - "Gutiérrez de la Huerta, Francisco"
   - "Gutiérrez, Heriberto"
   - "Gutiérrez, Jose Rosendo"
   - "Gutiérrez, Pedro"
   - "Gutiérrez, Toribio"
   - "Guzman, Jose Benito"
   - "Guzmán, Alcibiades"
   - "Guzmán, Aleibadesá"
   - "Guzmán, Benigno"
   - "Guzmán, Benjamín"
   - "Guzmán, Leonardo"
   - "Guzmán, Luis F."
   - "Guzmán, Luis Maríano"
   - "Hartmann, Roberto"
   - "Hernández, Benigno"
   - "Inojosa, Manuel de la Cruz"
   - "Irigoyen,  Natalio"
   - "Iturricha, Agustín"
   - "Jemio, Luis F."
   - "Jáuregui Rosquellas, Alfredo "
   - "Jémio, Luis F."
   - "Keller, José and Francisco Keller"
   - "Lagos Molina, Tomás de los"
   - "Laravia, José Venacio"
   - "Leclere, Carlos"
   - "Legizamon, Martiniano"
   - "Lema, Virginio"
   - "Lens, Benjamin"
   - "León, Angel M."
   - "Linares, Mariano"
   - "Loaiza, Guillermo C."
   - "Loaiza, Melquiades"
   - "Loaiza, Wenceslao V."
   - "Loayza, Wenceslao V. "
   - "Loaíza, M."
   - "Lopez, Julian Maria"
   - "Loza, León M."
   - "Loza, Paulino"
   - "López, Flavio"
   - "Machicado, José Santos"
   - "Machicado, Juan Manuel"
   - "Maidagan, Simón de"
   - "Mallea Balboa, Enrique"
   - "Manzano, Luis F."
   - "Marchant Y., Victor E."
   - "Mas, Juan"
   - "Medina, Elena G. de"
   - "Medina, Issac D."
   - "Melgar M., Adrián"
   - "Melo Samper, Miguel"
   - "Mendel, Bernardo"
   - "Mendez, Julio"
   - "Mercado M., Miguel"
   - "Mier, Adolfo"
   - "Miranda, Demitrio"
   - "Molina, Eulogio L."
   - "Molina, Francisco J."
   - "Molina, Tomás de los L."
   - "Montes, Ismael"
   - "Morales, Agustín"
   - "Morales, José A."
   - "Morales, Nestor D."
   - "Mujia, Juan Mariano"
   - "Murillo Dorado, Manuel"
   - "Más, José Ramón"
   - "Nava, José María"
   - "Nino, Bernardo de"
   - "Nogales, José N."
   - "Novillo Villarroel, Andrés "
   - "Noya, Germán"
   - "Oblitas, Jorge"
   - "Omiste, Modesto"
   - "Oropeza, Samuel"
   - "Orosco, Placido"
   - "Ortis, Luis"
   - "Ortiz, Manuel Crecencio, Juan Girdwood and Luis Blondel"
   - "Pabón, Manuel Acencio"
   - "Pacheco, Gregorio"
   - "Padilla, Ismael"
   - "Palacios, Adolfo"
   - "Palacios, Enrique"
   - "Palma y Velázquez, José"
   - "Palma, José"
   - "Palza S., Emiliano"
   - "Pando, José Manuel"
   - "Pando, Manuel"
   - "Paredes, Manuel Rigoberto"
   - "Paredes, Marco D."
   - "Paz, Luis"
   - "Paz, Román"
   - "Penaranda, Valentin"
   - "Peredo, Ricardo S."
   - "Pericón Barrientos, Conrado"
   - "Peña, Manuel José"
   - "Piccini, Vicente and Bernardo Mendel"
   - "Pifferi, Sebastián Francisco"
   - "Pinilla, Claudio"
   - "Pinilla, David"
   - "Pissaroso G., Samuel"
   - "Pizarro G., Felipe"
   - "Portillo, Victor"
   - "Priewasser, Wolfango"
   - "Prudencio, Almanzor"
   - "Prudencio, Fermin"
   - "Quijarro, Antonio and Emilio Reus"
   - "Quijarro, Antonio"
   - "Quintela, Andrés"
   - "Quinteros, José S."
   - "Quiroga, Torcuato and Felix Quiroga"
   - "Quispe A., Marcos"
   - "Rada, Nicolás"
   - "Ramallo, Maríano"
   - "Ramirez, Manuel Inocente"
   - "Reyes Ortiz, Felix"
   - "Reyes Ortiz, Serapio"
   - "Reyes, Agustín"
   - "Richter, Alfredo"
   - "Riva, Narciso de la"
   - "Rivero, Jose Claudio"
   - "Rodriguez, José D."
   - "Rodríguez Goitia, José M."
   - "Rojas, Casto"
   - "Rojas, Juan Antonio"
   - "Romero, José"
   - "Rostagno, Enrique"
   - "Saavedra, Bautista"
   - "Saavedra, Z. Rosa"
   - "Salamanca, Daniel"
   - "Salguero, Pascual"
   - "Salmón, Demetrio"
   - "Sanchez, Francisco S."
   - "Santa Cruz, Andres"
   - "Santalla, Calisto"
   - "Santiváñez, José María"
   - "Santos Machicado, José"
   - "Scapardini, Angel Jacinto"
   - "Simpson, Juan"
   - "Soliz Rodríguez, Abdón"
   - "Soliz, Abdón"
   - "Soliz, Félix, et al."
   - "Soliz, J. Genaro"
   - "Soria Galvarro, Rodolfo"
   - "Soruco, Alejandro"
   - "Suarez, Jose Manuel"
   - "Suárez Arana, Miguel"
   - "Tejada Sorzano, José Luis "
   - "Terrazas, M."
   - "Terán, Ignacio"
   - "Torrelio, Benjamin"
   - "Torres, Miguel D."
   - "Torrico, Ananias A."
   - "Torrico, Carlos"
   - "Trigo, Leocadio"
   - "Urdininea, José María"
   - "Urquidi, Alfredo"
   - "Valdés, Julio César"
   - "Vasquez, Donato"
   - "Velarde, Juan Francisco and George Earl Church"
   - "Velasco, Benjamín"
   - "Velasco, Lucio P."
   - "Velasco, Luis César"
   - "Villalobos, Rosendo"
   - "Villazón, Eliodoro"
   - "Villegas, Alberto de"
   - "Viscarra, Domingo and Jerman Aliaga"
   - "Viscarra, Eufronio"
   - "Vásquez, Rufino"
   - "Vázquez, Angel"
   - "Wannag, Jorge"
   - "Zaconeta, José Víctor"
   - "Zalles B., Elias"
   - "Zalles, Luis C."
   - "Zambrana, Mariano"
   - "Zamora, Julio"
   - "Zarco, Anjel"
   - "Zuazo, Federico"
   - "del Granado, Francisco Mari?a"
   - Argos
   - Arnous de Riviere
   - Atoche Hilarión P.
   - Banco Hipotecario Nacional
   - Banco Nacional de Bolivia
   - Banco Potosí
   - Baraga, Frederic
   - Baraga, Frederic and John B. Weikamp
   - Bolivia
   - Bolivia.
   - Bolivia. Cámara de Diputados
   - Bolivia. Cámara de Senadores
   - Bolivia. Ministerio de Hacienda e Industria
   - Bolivia. Ministerio de Hacienda.
   - Bolivian Railway Co.
   - Bompas, William Carpenter
   - Bompas, William Carpenter, translator
   - Boschi, John
   - Bradner, Lester
   - Brinton, Daniel Garrison, editor
   - Buechel, Eugene
   - Buschmann, Joh. Carl Ed. (Johann Carl Eduard)
   - Byington, Cyrus and Alfred Wright,  translators
   - Byington, Cyrus, translator
   - Ca. Consolidada de Conquencha
   - Canestrelli, Philip
   - Casa Nacional de la Moneda
   - Catholic Church
   - Cherokee Nation, Oklahoma
   - Church of England
   - Church of England in Canada
   - Clark, Ann Nolan
   - Claus, Daniel
   - Club de La Paz
   - Cojejio Nacional
   - Colejio Nacional Ayacucho
   - Colejio de Educandas
   - Compañia Minera de Collquiri
   - Compañía Estañífera de Llallagua
   - Compañía Lipez
   - Compañía Nueva Virginia
   - Compañía Quinas de Cusilluni
   - Compañía minera y agricola Oploca de Bolivia
   - Consejo Municipal de Oruro
   - Davis, Solomon, compiler
   - Departamento de Potosí
   - Du Ponceau, Peter Stephen
   - El Novel
   - Eliot, John
   - Episcopal Church
   - Facultad Medicina de La Paz
   - Fernandez y Gonzalez, F.
   - Fernández, Hilarión
   - Girling, H., translator
   - Glass, E. B.
   - Gueguen, Jean Pierre
   - Guyot, A.
   - Hamilton, William
   - Harrison, C. (Charles)
   - Horden, John
   - Horden, John and Rev. J Sanders, translators
   - Horden, John, translator
   - Hunter, James, translator
   - Hunter, Jean Ross
   - I.M.
   - Instituto Médico Sucre
   - J.L.J. [Julio Lucas Jaimes]
   - James, Edwin
   - Jones, John and Peter Jones, translators
   - Kirkby, W. W.
   - La Grasserie, Raoul de
   - La Paz (Bolivia). Seminario.
   - La Paz. H. Consejo Municipal
   - Lacombe, Albert
   - Laurent, Joseph
   - Le Goff, Laurent
   - Lemoine Joaquin de
   - Lemoine, George Joseph Guyon
   - Loughridge, R.M., translator
   - Lykins, Johnston, compiler
   - M V
   - M.C.
   - Matthews, Washington
   - McGuffey, William Holmes
   - Michelson, Truman
   - Ministerio de Gobierno y Colonización.
   - Montgomery, William B.
   - Mortimer, Favell Lee
   - Morvillo, Anthony
   - Nemo
   - No Author
   - Oxenden, Ashton
   - Pareja, Francisco de
   - Parisot, Jean
   - Partido Republicano (Bolivia)
   - Peck, E.J. et. al., translators
   - Peck, Edmund, editor
   - Perez, Manuel
   - Pickering, John
   - Powell, John Wesley
   - Prado Manuel María
   - Ramsey, James Ross, translator
   - Riggs, Stephen R and John P. Williamson, editors
   - Sapir, Edward
   - Sociedad Agustín Aspiazu
   - Sociedad Católica de Socorros Mútuos
   - Sociedad Minera Huainacucho de Aullagas
   - Sociedad Progresista de Bolivia
   - Sociedad de Propietarios de Yungas
   - Thalbitzer, William
   - Thomas, Edward Harper
   - Tims, J. W, translator
   - United Church of England and Ireland
   - Unknown Author
   - Wells, Roger A.E., compiler
   - Williams, Roger
   - Williamson, John Poage
   - Williamson, Thomas S. and Stephen R. Riggs, translators
   - Wright, Alfred
   - Wright, Alfred, translator
   - Wright, Asher
   - Zeisberger, David

##bibl_titletype_tesim

All say 'main' - ?

##book_id_ts

Same as id, but without colon. 834 unique values.

##book_ocr_tesim

Mad amounts of OCR text. Pretty poor state generally.

##collection_tesim

2 collection names so far - Alfred Montalvo Bolivian Digital Pamphlets, Huntington Free Library Native American. Are these archival collections or digital projects? Both? Are there URLs or other for the Archival collections?

##creation_site_location_tesim

Values look transcribed. Look into desire (or not) to grab URIs, coordinates for these.

   - 1 Aberdeen, S.D.
   - 1 Antwerp
   - 1 Berlin
   - 1 Bethlehem
   - 2 Bolivia
   - 5 Boston
   - 1 Boston [Mass.]
   - 1 Brussels
   - 3 Buenos Aires
   - 1 Buffalo Creek Reservation
   - 1 Cambridge [Mass.]
   - 1 Chicoutimi
   - 2 Cincinnati
   - 72 Cochabamba
   - 4 Cochabmaba
   - 1 Copenhagen
   - 1 Corocoro
   - 1 Desmet, Idaho
   - 1 Edinburgh
   - 1 Iquique
   - 361 La Paz
   - 1 Laguna, N.M.
   - 1 Laibach, Autriche
   - 2 Lawrence, KS.
   - 1 Leavenworth, Kansas
   - 1 Leyden
   - 5 Lima
   - 38 London
   - 1 Madrid
   - 1 Mexico
   - 1 Milwaukee, Wis; Boston
   - 11 Montreal
   - 1 Nancy
   - 20 New York
   - 1 New York,Cincinnati [etc.]
   - 1 New York,Cincinnati,Chicago
   - 2 Oklahoma
   - 56 Oruro
   - 1 Ottawa
   - 2 Pace [La Paz]
   - 2 Paraná
   - 4 Paris
   - 4 Paz de Ayacucho
   - 4 Philadelphia
   - 2 Portland, Or.
   - 36 Potosí
   - 1 Punata
   - 2 Puno
   - 1 Quebec
   - 14 S.l.
   - 1 Salta
   - 13 Santa Cruz
   - 1 Santiago
   - 5 Santiago de Chile
   - 1 Spokane, Wash.
   - 1 St. Louis
   - 1 St. Louis, Mo.; Freiburg, Germany
   - 1 Stolpen [Netherlands?]
   - 84 Sucre
   - 5 Tacna
   - 4 Tarata
   - 6 Tarija
   - 1 Toronto
   - 2 Tupiza
   - 2 Valparaiso
   - 7 Washington, D.C.
   - 1 Yotaú
   - 1 [Cochabamba]
   - 11 [La Paz]
   - 1 [Potosí]
   - 3 [S.I.]
   - 1 [Sucre]

