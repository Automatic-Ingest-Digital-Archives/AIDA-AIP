mets : "allerlei attributen die horen bij dit header-element" # Al wat volgt is een child element van dit element

# Alles wat voorafgegaan wordt door "@" is een attribuut in de XML

metsHdr:
	@RECORDSTATUS: "New"
	@CREATEDATE: "2020-04-08T09:12:36"
	agent:
		@TYPE: "OTHER" # Voor info over hoe deze attributen te gebruiken: Zie blz. 36 van de CSIP specificatie 2.0.3.
		@ROLE: "CREATOR"
		@OTHERTYPE: "SOFTWARE"
		name: "AIDA-repo"
		note: "version 2.2"
	metsDocumentID: "METS.xml"

amdSec:
	@ID: "Een zot UUID 1" # Het ID van deze amdSec
	digiprovMD: # Staat voor "DIGItalPROVenanceMetaData". In principe zijn dit de events en de agents. De technicalmetadata zou je kunnen splitsen, maar moet niet.
		@ID: "Een zot UUID 2" # Het ID van dit digiprovMD-element
		mdRef: # Staat voor "MetaDataREFerence". Hiermee verwijzen we naar de PREMIS van rep-001
			@MIMETYPE: "application/xml"
			@"xlink:href": "./metadata/preservation/premis.xml" # Hier staat hij in het AIP
			@LOCTYPE: "URL"
			@CREATED: "2020-04-08T09:12:18"
			@CHECKSUM: "een hash"
			@"xlink:type": "simple"
			@ID: "Een zot UUID 3" # Dit is het ID dat de PREMIS heeft gekregen in ons repo. We zullen het nog terugzien in de structMap
			@MDTYPE: "PREMIS"
			@CHECKSUMTYPE: "SHA-256"

fileSec:
	fileGrp:
		@USE: "Data for rep-001" # Zie blz. 45 van de CSIP specificatie 2.0.3.
		@ID: "Een zot UUID 4" 	# Het ID van deze fileGrp
		
		file: 					# Ons eerste doc-file. Veel wordt ook opgeslagen in de PREMIS. In principe zijn checksums, informatie over size enz. hier niet nodig, maar E-ARK heeft deze eigenschappen gedefinieerd als een MUST.
			@MIMETYPE: "application/msword"
			@USE: "Datafile" 	# Ik vermoed dat dit een fout is in het standaarddocument. Er is nergens een beschrijving in de dictionary. Ik laat het hier ter documentatie, maar neem het niet mee in verdere voorbeelden.
			@CHECKSUMTYPE: "SHA-256"
			@CREATED: "2001-09-08T12:45:36"
			@CHECKSUM: "een hash"
			@ID: "een zot UUID 5" # Het ID van dit file. We zullen het nog terugzien in de structMap, maar ook in de rep-001-PREMIS
			@SIZE: "2038937"
			FLocat: 			# Hier staat het file in de AIP
				@"xlink:href": "data/01/spaties_en_apostroph-s.doc"
				@"xlink:type": "simple"
				@LOCTYPE: "URL"
				
				
		file: 					# Ons tweede doc-file.
			@MIMETYPE: "application/msword"
			@CHECKSUMTYPE: "SHA-256"
			@CREATED: "2005-09-08T12:45:00"
			@CHECKSUM: "een hash"
			@ID: "een zot UUID 6"
			@SIZE: "983028839"
			FLocat: 			
				@"xlink:href": "data/01/spaties_en_trema-s.doc"
				@"xlink:type": "simple"
				@LOCTYPE: "URL"
				
	# Ik vermoed dat hier nog een filegroup moet volgen over onze metadatabestanden (de PREMIS). Ik vind niks terug echter in de voorbeelden.			

structMap:
	@TYPE: "physical"
	@LABEL: "CSIP structMap" # Hieronder volgt de mappenstructuur, met folders 01, 02 en 03, waarbij 03 een subfolder is van 01. (Een lege subfolder, kan normaal niet, maar is puur voor de illustratie). Ik denk dat het beter is om in plaats van folders in de data-map te steken, met een platte lijst te werken van bestanden. In dat geval hebben we nog altijd onderstaande structMap nodig. Alleen zal TYPE de value "logical" krijgen en zal LABEL de value "original SIP structure". Er komen dus twee structMaps. Een fysieke die de platte lijst van bestanden oplijst, en een logische die de oorspronkelijke mappenstructuur documenteert.
		div:									# De representatiefolder
			@LABEL: "rep-001"
			div:								# De metadatafolder
				@LABEL: "metadata"
				fptr:							# Er zitten files in deze folder. Dit geven we aan met het FilePoinTeR - element
					@FILEID: "Een zot UUID 3" 	# Zoek 'm in de amdSec!
			div:								# Er is nog een map. De datafolder uiteraard
				@LABEL: "data"
				div:
					@LABEL: "01"					# Er zitten files in deze folder.
					fptr:						# File 1...
						@FILEID: "een zot UUID 5"						# Zoek 'm in de fileSec!
					fptr:						# En file 2...
						@FILEID: "een zot UUID 6"
					div:						# Slechte pre-processing. Er zit nog een nutteloze lege folder in
						@LABEL: "03"				
				div:							# En nog een nutteloze lege folder
					@LABEL: "02"				
				
	
	
	
			
		
		

	
