'''
 Literatuur
	https://www.loc.gov/standards/premis/guidelines2017-premismets.pdf
	https://www.ideals.illinois.edu/bitstream/handle/2142/18210/LinkingMETSandPREMIS.pdf (zeer interessant!!)
	Half beschikbaar op Googlebooks: https://books.google.be/books?id=as_DDQAAQBAJ&pg=PA171&lpg=PA171&dq=use+in+premis+id+of+METS?&source=bl&ots=MNfP5C2nkD&sig=ACfU3U3_PaFvH3Hx44BmM0W-ghUwGNzgPA&hl=nl&sa=X&ved=2ahUKEwjJjs_wl6HoAhVNDOwKHaJOBhoQ6AEwDXoECAgQAQ#v=onepage&q=use%20in%20premis%20id%20of%20METS%3F&f=true

 Algemene overweging 1: 
 E-ARK AIP gaat uit van een SIP's die zijn opgesteld volgens CSIP. Vandaar hun keuze voor een submissionfolder in de AIP. Je doet al zoveel moeite om een SIP te creëren, dus waarom deze niet bewaren. Voor mij maakt de submissionfolder het geheel nogal complex, zodat ik er geen fan van ben. Uiteindelijk heb ik me bedacht dat dit een kwestie van pipelines is. Indien we gedigitaliseerde tijdschriften zouden toevoegen, dan kun je een dergelijke complexe submissions-folder rechtvaardigen. Maar wij denken na over de pipeline snel-en-veel. Dit wil zeggen: we zullen geen complexe E-ARK SIPs opladen. Alles wat we submitten zal overigens in de ingest-procedure al worden verwerkt (sanitizeNames). Het houdt dus steek om alles meteen in de representatiefolder te steken en de boel wat simpeler te maken.

 Algemene overweging 2:  
Ik lees op pagina 4 van dit document https://www.loc.gov/standards/premis/guidelines2017-premismets.pdf volgende best practice: Logische structuren in de METS-structMap en eventueel de dmdSec. Structuren van belang voor preservatie ook in PREMIS. 
 Dus, wat doen we als er intellectuele eenheid (IE) als een website in het archief zit? Dit is zowel logisch belangrijk als voor preservatie. Dan zou ik opteren voor volgende keuze: IE's die we afbakenen bij submission of re-ingest worden én als div in de structMap genoteerd, én als object in PREMIS. 
 IE's die enkel het resultaat zijn van een preservatieoperatie (Bv. meerdere textfiles uit één wordfile) worden enkel opgeslagen als object in de PREMIS.

 Algemene overweging 3: 
 Ieder event, agent en object in de PREMIS en iedere sectie in de METS (file, div...) krijgt een xmlID (wellicht, maar niet noodzakelijk, in de vorm van een UUID) Dit laat toe om te cross-referencen vanuit XML-files naar elementen in andere XML-files. Zie https://www.ideals.illinois.edu/bitstream/handle/2142/18210/LinkingMETSandPREMIS.pdf, blz. 8. Dit is vooral belangrijk om te linken tussen de PREMIS-files van de verschillende representaties en om te linken tussen verschillende structMap-divs en PREMIS-elementen.

 AIP-structuur
'''

AIP # Wij zouden dit noemen: BE_653717_0067-WM. Al de rest is niet VAi-specifiek, behalve de keuze voor een simpele dublincore als descriptieve metadata.
	METS.xml # Bevat amdSec, fileSec die verwijst naar metadata en representatieMETS'en + de verplichte structMap.
	submission # is leeg / wordt niet gebruikt voor deze pipeline
	metadata
		descriptive
			dublincore.xml # Bevat voor VAI max. een verwijzing naar het catalogusnummer, rights en access restrictions
		preservation
			premis-1.xml # Deze bevatten object-/event-/agent- metadata voor alle bestanden op rootniveau. Events die plaatsvinden op niveau van het AIP (meest typisch: het resultaat van checksumcontroles) worden opgeslagen in deze PREMIS. Het kan een voordeel zijn om deze PREMIS (en da andere PREMIS'en) op te splitsen in een digiprovmd-1.xml (alles wat objecten, events en agents aan elkaar linkt) en een techmd-1.xml (dat gewoon de technische gegevens verzamelt van de objecten). Dit kan leiden tot handzamere XML's, maar vereist linken tussen XML's. Te bekijken.
	representations
		rep-1 
		# Bevat niet gemigreerde content, maar de content zoals 'submitted', m.u.v. bestandsnamen die 'sanitized' zijn. Dit wordt aangegeven in de struct-map van de root-METS. Let op!! Voor de pipeline 'snel-en-veel' heeft rep-1 een heilige status. Het is de-facto onze submission en bevat de basislogica om DIP's te creëren.
		# (Indien we later andere bestanden toevoegen aan de AIP, lossen we dit gewoon op door die bestanden te linken aan een ander ingest-event.)
			METS.xml 
			# Bevat in de fileSec alle bestanden. Ieder bestand verwijst naar een object in de premis-1.xml
			# Bevat een structMap met de oorspronkelijke mappenstructuur. Ieder file-id wordt in deze structMap ingepast. Op die manier kan de oorspronkelijke mappenstructuur altijd worden gereconstrueerd. (Voor pipeline snel-en-veel moet het mogelijk zijn om DIP's te creëren op basis van een map in de mappenstructuur)
			# Een aparte structMap met de logische Intellectual Entities. Omdat ieder Intellectual Entity (IE) ook een overeenkomstig object in de premis-1.xml heeft is het hier niet nodig om nog eens de File-ID's van de overeenkomstige bestanden op te lijsten. Een verwijzing naar het IE-object in premis-1.xml volstaat.
			# Een aparte structMap om het gebruik van de bestanden te duiden. Welke bestanden komen in de DIP en welke niet? Dit wordt bepaald door de preservation-policy. Mogelijk kunnen we van DIP's van meerdere niveaus spreken. (Noot: dit kan mogelijk ook gerealiseerd worden door een fileGrp - en misschien heeft dit zelfs de voorkeur.)
			# Uit deze twee structMaps kan uiteindelijk het geheel worden gereconstrueerd worden voor de DIP. Dit maakt de rep-1-structMap "heilig".
			metadata
				descriptive # is leeg / wordt niet gebruikt
				preservation
					premis-1.xml 
					# Bevat alle objecten + events + actoren. In deze PREMIS worden de resultaten verwerkt van de events during ingest: sanitizeNames, file-identification, viruscheck, checksumcheck... Objecten kunnen zowel files als intellectuele eenheden zijn. Files worden aan hun intellectuele objecten gelinkt via de relationship-mogelijkheden van PREMIS. (Eventueel doen we een opsplitsing tussen digiProvmd en techmd)
					# ! Ieder object in een premis-bestand van een andere representatie moet uiteindelijk, via één of meerdere tussenstadia, teruglinken naar een object in deze premis-1.xml !
			data # bevat alle bestanden in hun mappenstructuur of in een platte lijst. Vermoedelijk het laatste. Sanitize-names moet hier wel rekening mee houden!
		rep-2 
		# Bevat enkel gemigreerde content. Ik prefereer om op dit moment enkel re-ingest pipelines te creëren die deze rep-2 vervangen. Oude rep-2's moeten niet worden bewaard.
		# De rep-2 bevat zowel gemigreerde content voor preservatie als voor toegankelijkheid. Welke bestanden waarvoor dienen wordt bepaald in de structMap van de METS.
			METS.xml # Beschrijft in de fileSec alle bestanden die het resultaat zijn van een migratie. Eventueel worden met fileGrp bestanden geklasseerd per gebruik. (maar dit kan ook in een structMap). Verder is een structMap niet nodig. Alle andere structurele info is "preservation"-gebaseerd en wordt dus opgeslagen in de PREMIS.
			metadata
				descriptive # is leeg / wordt niet gebruikt
				preservation
					premis-1.xml
					# Bevat alle objecten + events + actoren. In deze PREMIS worden de resultaten verwerkt van migratie-events (migration, validation, PREMIS-update...) Objecten kunnen zowel files als representations zijn. (Geen intellectuele eenheden, want migraties creëren enkel representaties) Files worden aan de representaties gelinkt via de relationship-mogelijkheden van PREMIS. 
					# Pas op: Als we alle Word-strategieën gaan toepassen (odt, pdf/a, text, meerdere afbeeldingen...) komt de onvermijdelijke trias "intellectuele eenheid - representatie - file" in het spel. Het meest veilige en duurzame (maar ook wat loggere) pad is om hier boven elk file ook steeds een representatie te plaatsen. Je krijgt dus deze twee linkstructuren:
						# file-object in rep-2 --> representatie-object in rep-2 --> file-object in rep-1
						# file-object in rep-2 --> representatie-object in rep-2 --> IE-object in rep-1
	documentation #Een standaard tekstbestand dat de structuur uitlegt van de snel-en-veel AIP, met bv. de "heilige status" van rep-1. Kan eventueel ook historische premissen en METS'en bevatten. Dus: wanneer materiaal wordt toegevoegd, of wanneer er een nieuwe migratie gebeurt, is dat een heel ingrijpende gebeurtenis. Je zou de METS'en en PREMIS'en van voor de wijziging als documentatie kunnen bewaren, in een folder per datum.
		

# Algemene architectuur van linken tot een gemigreerd bestand:

RootMETS | structMap linkt naar:
	--> rep-1 METS | div in structMap + file in fileSec linken naar:
		--> rep-1 PREMIS-object| linkt naar:
			--> eventueel bovenliggende objects of onderliggende objects (die weer verder linken naar events of agents)
			--> eventueel rep-2 PREMIS-object | linkt naar:
				--> eventueel bovenliggende objects of onderliggende objects.
				--> eventueel (ooit).  rep-3 PREMIS-object | enz.
			