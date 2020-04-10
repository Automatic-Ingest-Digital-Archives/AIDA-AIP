# Ik ga uit van 2 doc-files in de map "01" van Maartens voorbeeld AIP

# Deze representatie is het resultaat van snel-en-veel-pipeline:
	# Viruscontrole
	# Fixity gecheckt
	# Bestandsnamen sanitized
	# Bestandsformaten geïdentificeerd

# Opmerkingen voor dit document:
	# Het is verplicht een event te linken aan een object. Omgekeerd is dat niet. Doen wij dat toch? Ik raad af van niet.
	# Gebruiken we xmlid's. Ze maken het mogelijk om vanuit XML's te linken naar elementen in andere XML's. Ik denk dat dit handig is.
	# Het gemakkelijkst automatiseerbaar is overal UUID's te gebruiken. We moeten sowieso UUID's gebruiken voor de objecten. Via die UUID's leggen we de linken tussen de files in de METS-fileSec en de objecten in deze PREMIS.

premis_eventtypes : http://id.loc.gov/vocabulary/preservation/eventType.html # Controlled vocabulary
premis_agenttypes: http://id.loc.gov/vocabulary/preservation/agentType.html # Controlled vocabulary
premis_relationshiptypes: http://id.loc.gov/vocabulary/preservation/relationshipType.html # Controlled vocabulary
premis_relationshipsubtypes: http://id.loc.gov/vocabulary/preservation/relationshipSubType.html # Controlled vocabulary

#Hier beschrijvingen voor agents die we nodig zullen hebben tijdens ingest in de snel-en-veel pipeline. Het gaat hier om de software die wordt gebruikt.

# Een element dat wordt voorafgegaan door "@" is een attribuut in de XML

premis : "allerlei attributen die horen bij dit headerelement" # Al wat volgt is een child element van dit element

agent :
	@xmlid: "xml-agent-1" # alle xmlid's zijn attributes in ieder agent-, object- of event-element. Kunnen ook UUID's zijn.
	agentIdentifier :
		agentIdentifierType : "local"
		agentIdentifierValue : "agent-1" # Kunnen ook UUID's zijn.
	agentName : "AIDA-snel-en-veel-ingestor"
	agentType : "software"
	agentVersion : "2019-05-03" # Version kan een officieel nummer zijn, maar ook de datum van issue.
	
agent :
	@xmlid: "xml-agent-2"
	agentIdentifier :
		agentIdentifierType : "local"
		agentIdentifierValue : "agent-2"
	agentName : "droid of siegfried"
	agentType : "software"
	agentVersion : "1.2"
	
agent :
	@xmlid: "xml-agent-3"
	agentIdentifier :
		agentIdentifierType : "local"
		agentIdentifierValue : "agent-3"
	agentName : "AIDA-names-sanitizer"
	agentType : "software"
	agentVersion : "3.2"
	
agent :
	@xmlid: "xml-agent-4"
	agentIdentifier :
		agentIdentifierType : "local"
		agentIdentifierValue : "agent-4"
	agentName : "AIDA-bagit-module"
	agentType : "software"
	agentVersion : "4.1"
	
agent :
	@xmlid: "xml-agent-5"
	agentIdentifier :
		agentIdentifierType : "local"
		agentIdentifierValue : "agent-5"
	agentName : "AIDA-virus-scan"
	agentType : "software"
	agentVersion : "6.2"
	
agent :
	@xmlid: "xml-agent-6"
	agentIdentifier :
		agentIdentifierType : "local"
		agentIdentifierValue : "agent-6"
	agentName : "Maarten Savels"
	agentType : "person"

# Er zijn events die op niveau van de representatie worden geregistreerd. (De representatie is ook een object in PREMIS). Bv. ingest, sanitize names, checksumcontrole, viruscontrole... Ik toon hier ingest en checksumcontrole

event :
	@xmlid: "xml-event-1"
	eventIdentifier :
		eventIdentifierType : "local"
		eventIdentifierValue : "event-1"
	eventType : "ingestion"
	eventDateTime : "2020-04-08T11:39:24/2020-04-08T12:56:01" # ISO8061. Een slash geeft de duur aan.
	eventOutcomeInformation : 
		eventOutcome : "Success"
	linkingAgentIdentifier :
		linkingAgentIdentifierType: "local"
		linkingAgentIdentiferValue : "agent-1" # D.w.z. de ingest pipeline waarmee de ingest verliep
	linkingAgentIdentifier :
		linkingAgentIdentifierType: "local"
		linkingAgentIdentifierValue : "agent-6" # D.w.z. Maarten Savels heeft deze ingest gedaan
	linkingObjectIdentifier : 
		objectIdentifierType : "repository"
		objectIdentifierValue : "een zot UUID 1" # Het object dat de volledige representatie "representeert"

event :
	@xmlid : "xml-event-2"
	eventIdentifier :
		eventIdentifierType : "local"
		eventIdentifierValue : "event-2"
	eventType : "fixity check"
	eventDateTime : "2020-04-08T11:39:30/2020-04-08T12:01:01"
	eventOutcomeInformation : 
		eventOutcome : "Valid"
	linkingAgentIdentifier :
		linkingAgentIdentifierType: "local"
		linkingAgentIdentiferValue : "agent-4" # D.w.z. onze bagit-module
	linkingObjectIdentifier:
		objectIdentifierType : "repository"
		objectIdentifierValue : "een zot UUID 1" # Het object dat de volledige representatie "representeert" (Dit is eigenlijk zelfs overbodig, want we relateren dit event aan het ingest-event, dat al verwijst naar de representatie)
	relatedEventIdentification :
		relatedEventIdentifierType : "local"
		relatedEventIdentifierValue : "event-1" # Zijnde event "ingest". Wordt iets gedaan tijdens een tweede ingest of een re-ingest, wordt dit zo gedocumenteerd
	
# Niet alle events wil je registreren op representatieniveau, omdat ze info genereren die specifiek zijn voor een file. File-identification is er één van. Als er ooit een nieuwe versie van DROID of Siegfried ontstaat, kan er een nieuwe identificatie zijn. Deze nieuwe waarde schrijf je dus toe aan een nieuw identificatie-event.	

event :
	@xmlid: "xml-event-3"
	eventIdentifier :
		eventIdentifierType : "local"
		eventIdentifierValue : "event-3"
	eventType : "format identification"
	eventDateTime : "2020-04-08T12:56:01" #Hier geen duur, maar een specifiek tijdsstip"
	evenOutcomeInformation : 
		eventOutcome : "Success"
		#Hier is het later mogelijk om een element "eventOutcomeDetail" te definiëren, waarin dan weer een subelement "eventOutcomeDetailExtension" kan worden toegevoegd. Hierin kan XML-informatie van een DROID of Siegfried worden toegevoegd.
	linkingAgentIdentifier :
		linkingAgentIdentifierType: "local"
		linkingAgentIdentiferValue : "agent-2" # Zijnde agent "droid of siegfried"
	linkingObjectIdentifier : 
		objectIdentifierType : "repository"
		objectIdentifierValue : "een zot UUID 3"
	relatedEventIdentification :
		relatedEventIdentifierType : "local"
		relatedEventIdentifierValue : "event-1" # Zijnde event "ingest". Wordt iets gedaan tijdens een tweede ingest of een re-ingest, wordt dit zo gedocumenteerd
		
event :
	@xmlid: "xml-event-4"
	eventIdentifier :
		eventIdentifierType : "local"
		eventIdentifierValue : "event-4"
	eventType : "format identification"
	eventDateTime : "2020-04-08T12:56:33"
	evenOutcomeInformation : 
		eventOutcome : "Success"
	linkingAgentIdentifier :
		linkingAgentIdentifierType: "local"
		linkingAgentIdentiferValue : "agent-2" # Zijnde agent "droid of siegfried"
	linkingObjectIdentifier : 
		objectIdentifierType : "repository"
		objectIdentifierValue : "een zot UUID 2"
	relatedEventIdentification :
		relatedEventIdentifierType : "local"
		relatedEventIdentifierValue : "event-1" # Zijnde event "ingest". Wordt iets gedaan tijdens een tweede ingest of een re-ingest, wordt dit zo gedocumenteerd		

# Hier komen de drie objecten. De representatie en de twee tekstverwerkingsdocumenten

object : # Het representatieobject
	@xmlid : "een zot UUID 7" # Bekijken of dit UUID ergens terugkomt in de representation-METS (Bv. in de structMap). In principe is dit niet nodig.
	objectIdentifier:
		objectIdentifierType : "repository"
		eventIdentifierValue : "een zot UUID 7"
	objectCategory : "representation"	

object : # Eén worddocument
	@xmlid : "een zot UUID 5" # Deze UUID vind je ook in de fileSec rep-001-METS.
	objectIdentifier:
		objectIdentifierType : "repository"
		eventIdentifierValue : "een zot UUID 5"
	objectCategory : "file"
	objectCharacteristics :
		fixity:
			messageDigestAlgorithm : "SHA-256"
			messageDigest : "een hash"
			messageDigestOriginator : "Amsab-ISG" # Idee is om tijdens ingest checksums te checken. Niet om ze te maken. Hier geef je aan wie de oorspronkelijke checksum genereerde.
		size: "2038937"
		format:
			formatDesignation :
				formatName: "Microsoft Word for MS-DOS Document"
				formatVersion: "3.0"
			formatRegistry : 
				formatRegistryName: "PRONOM"
				formatRegistryKey: "x-fmt/273"
				formatRegistryRole : "specification"
		# Zijn uiteraard ook nog mogelijk: Andere PREMIS-velden. Of externe velden zoals exif-data. Dit kan in element objectCharacteristicsExtension. Zie hiervoor de PREMIS-specificatie
	originalName: "SIP/floppyx/joliet/01/spaties en apostroph's.doc" # Checken of het originalName-element ook het oorspronkelijke path kan bevatten
	storage:
		contentLocation :
			contentLocationType: "URI"
			contentLocationValue: "./data/01/spaties_en_apostroph-s.doc" # Mogelijk kiezen we voor platte lijst. Dan verliezen we de "01"
	relationship: # Hier gaan we een relatie definiëren met de representatie. Als we bv. een nieuwe fixity check doen op de volledige representatie, dan weten we dat dit ook voor dit file gold. Het event registreren we dan enkel bij de representatie = lichtere PREMIS.
		relationshipType: "structural"
		relationshipSubType: "is Included In" # Een specificatie van een structurele relatie. Gebruik deze term om te zeggen dat een file deel uitmaakt van een representatie.
		relatedObjectIdentifier:
			relatedObjectIdentifierType: "repository"
			relatedObjectIdentifierValue: "een zot UUID 7" # Het ID van de representatie
			# Puur ter info. Stel je hebt 3 video's van 1 interview, dan is er een element ter beschikking waarmee je de volgorde van de video's kunt aangeven.
				
object : # Een tweede Worddocument
	@xmlid : "een zot UUID 6" # Deze UUID vind je ook in de rep-001-METS, in de fileSec
	objectIdentifier:
		objectIdentifierType : "repository"
		eventIdentifierValue : "een zot UUID 6"
	objectCategory : "file"
	objectCharacteristics:
		fixity:
			messageDigestAlgorithm : "SHA-256"
			messageDigest : "een hash"
			messageDigestOriginator : "Amsab-ISG"
		size : "983028839"
		format:
			formatDesignation :
				formatName: "Microsoft Word Document"
				formatVersion: "6.0/95"
			formatRegistry : 
				formatRegistryName: "PRONOM"
				formatRegistryKey: "fmt/39"
				formatRegistryRole : "specification"
	originalName: "SIP/01/spaties en trëma's.doc" # Checken of het originalName-element ook het oorspronkelijke path kan bevatten. Vermoedelijk wel, is sowieso nodig als je de rationale van het PREMIS-element, zoals genoemd in de standaard, wil behalen.
	storage:
		contentLocation :
			contentLocationType: "URI"
			contentLocationValue: "./data/01/spaties_en_trema-s.doc" # Mogelijk kiezen we voor platte lijst. Dan verliezen we de "01". Die vind je dan terug bij "originalName"
	relationship:
		relationshipType: "structural"
		relationshipSubType: "is Included In"
		relatedObjectIdentifier:
			relatedObjectIdentifierType: "repository"
			relatedObjectIdentifierValue: "een zot UUID 7"	
	
