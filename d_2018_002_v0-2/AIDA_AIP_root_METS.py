# opvallend: Alles wat in de metadatafolder staat wordt zowel in de fileSec als de structMap anders behandeld


mets : "allerlei attributen die horen bij dit header-element" # Al wat volgt is een child element van dit element

# Alles wat voorafgegaan wordt door "@" is een attribuut in de XML

metsHdr:
	@RECORDSTATUS: "New"
	@CREATEDATE: "2020-03-08T09:12:36"
	@LASTMODDATE: "2020-04-08T09:12:36"
	@OAISPACKAGETYPE: "AIP"
	agent:
		@TYPE: "OTHER" # Voor info over hoe deze attributen te gebruiken: Zie blz. 36 van de CSIP specificatie 2.0.3.
		@ROLE: "CREATOR"
		@OTHERTYPE: "SOFTWARE"
		name: "AIDA-repo"
		note: "version 2.2" # Hier kan nog een attribuut worden toegevoegd "note type". Om te zeggen dat je hier over een softwareversie spreekt

dmdSec:
	@ID: "Een zot UUID 10" # Het ID van deze dmdSec
	@CREATED: "2020-03-08T09:12:36"
	mdRef: # Staat voor "MetaDataREFerence". Hiermee verwijzen we naar de PREMIS van rep-001
		@MIMETYPE: "application/xml"
		@"xlink:href": "./metadata/descriptive/d_2018_002_export_adlib.xml" # Hier staat hij in het AIP
		@LOCTYPE: "URL"
		@CREATED: "2020-04-08T09:12:18"
		@CHECKSUM: "een hash"
		@"xlink:type": "simple"
		@ID: "Een zot UUID 3" # Dit is het ID dat de PREMIS heeft gekregen in ons repo. We zullen het nog terugzien in de structMap
		@MDTYPE: "Amsab Adlib XML-export"
		@MDTYPEVERSION: "2015" # Maartens XML-export is van versie 2015 (fictief)
		@CHECKSUMTYPE: "SHA-256"
		@SIZE: "879"
	

amdSec:
	# Om een beeld te krijgen hoe dit wordt vormgegeven: Zie de representatie-METS'en. Dit deel linkt naar een PREMIS die zal gelden voor de gehele AIP. Dus in dat geval bevat deze PREMIS enkel informatie over data die niet in de representaties zitten.

fileSec:
	fileGrp:
		@USE: "Documentation" 	# De folder "documentation". Alle metadatalogs van Maarten zitten hier in.
		@ID: "Een zot UUID 11" 	# Het ID van deze fileGrp
		
		file: # Dit verwijst naar één van de logfiles van Maarten. Zie de rep-001 METS over hoe dit werkt	
		file: # Dit verwijst naar een ander logfile van Maarten. Zie de rep-001 METS over hoe dit werkt
		...
		
	fileGrp:
		@USE: "Schemas" 	# De folder "schemas". Hierin zetten we de XML-schema's die we gebruiken.
		@ID: "Een zot UUID 12" 	# Het ID van deze fileGrp
		
		file: # Dit verwijst naar één van de xsd's die we gebruiken (niet in voorbeeldAIP) Zie de rep-001 METS over hoe dit werkt	
		file: # Dit verwijst naar een ander xsd. Zie de rep-001 METS over hoe dit werkt
		...
		
	fileGrp: # De filegrp voor rep-001 (de submission data)
		@USE: "Representations/rep-001" # Zie blz. 68-69 van de CSIP specificatie 2.0.3 
		@ID: "Een zot UUID 13" 	# Het ID van deze fileGrp
		file: # Het enige wat we hier doen is dus doorverwijzen naar de METS met de rest van de informatie.
			@MIMETYPE: "xml"
			@CHECKSUMTYPE: "SHA-256"
			@CREATED: "2020-09-08T12:45:00"
			@CHECKSUM: "een hash"
			@ID: "een zot UUID 14"
			@SIZE: "298"
			FLocat: 			
				@"xlink:href": "representations/rep-001/METS.xml"
				@"xlink:type": "simple"
				@LOCTYPE: "URL"
				
	fileGrp: # De filegrp voor rep-002 (de migrated data)
		@USE: "Representations/rep-002" # Zie blz. 68-69 van de CSIP specificatie 2.0.3 
		@ID: "Een zot UUID 15" 	# Het ID van deze fileGrp
		file: # Het enige wat we hier doen is dus doorverwijzen naar de METS met de rest van de informatie.
			@MIMETYPE: "xml"
			@CHECKSUMTYPE: "SHA-256"
			@CREATED: "2020-09-08T12:45:00"
			@CHECKSUM: "een hash"
			@ID: "een zot UUID 16"
			@SIZE: "298"
			FLocat: 			
				@"xlink:href": "representations/rep-002/METS.xml"
				@"xlink:type": "simple"
				@LOCTYPE: "URL"
		
	# ! Noteer dat bestanden die in de metadatafolder staan niet worden opgelijst in de fileSec. Blijkbaar een bewuste keuze.	

structMap:
	@TYPE: "physical"
	@LABEL: "CSIP"
		div:									# De gehele AIP
			@LABEL: "d_2018_002"
			@ID: "een zot UUID 17"
			div:								# De metadatafolder
				@LABEL: "Metadata"
				@ID: "een zot UUID 18"
				@DMDID: "Een zot UUID 10"		# ! Noteer hier dat het voorbeeld in het document niet de mappenstructuur van de metadatafolder geeft. "Een zot UUID 10" verwijst hier naar de dmdSec in deze METS, die op zijn beurt doorverwijst naar Maartens Adlibexport.
			div:								# De Documentationfolder
				@LABEL: "Documentation"
				@ID: "Een zot UUID 19"
					fptr: # Zie de representatieMETS over hoe dit werkt. Het lijst de logbestanden van Maarten op.
			div:								# De Schemasfolder
				@LABEL: "Schemas"
				@ID: "Een zot UUID 20"
					fptr: # Zie de representatieMETS over hoe dit werkt. Het lijst onze xsd's op.
			div:								# De folder met rep-001
				@LABEL: "Representations/rep-001"
				@ID: "Een zot UUID 21"
					mptr: # Om naar METS'en te pointen gebruiken we niet fptr, maar mptr
						@LOCTYPE: "URL"
						@"xlink:href": "representations/rep-001/METS.xml"
						@"xlink:type": "simple"
						@"xlink:title": "Een UUID" # Ik weet niet waarom
			div:								# De folder met rep-002
				@LABEL: "Representations/rep-002"
				@ID: "Een zot UUID 22"
					mptr:
						@LOCTYPE: "URL"
						@"xlink:href": "representations/rep-002/METS.xml"
						@"xlink:type": "simple"
						@"xlink:title": "Een UUID" # Ik weet niet waarom				
			
	
	
	
			
		
		

	
