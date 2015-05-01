# coding: utf-8

"""
Domain specific language for DBpedia quepy.
"""

from quepy.dsl import FixedType, HasKeyword, FixedRelation, FixedDataRelation

# Setup the Keywords for this application
HasKeyword.relation = "<my:opencollege:studentvocab/resource/Students_First+Name>"		#rdfs:label
#HasKeyword.language = "en"

class IsFirstName(FixedType):
    fixedtype = "<my:opencollege:studentvocab/resource/Students_First+Name>"


class IsPerson(FixedType):
    fixedtype = "foaf:Person"
	

class IsPlace(FixedType):
    fixedtype = "dbpedia:Place"


class IsCountry(FixedType):
    fixedtype = "dbpedia-owl:Country"


class IsBand(FixedType):
    fixedtype = "dbpedia-owl:Band"


class IsAlbum(FixedType):
    fixedtype = "dbpedia-owl:Album"


class IsTvShow(FixedType):
    fixedtype = "dbpedia-owl:TelevisionShow"


class IsMovie(FixedType):
    fixedtype = "dbpedia-owl:Film"


class HasShowName(FixedDataRelation):
    relation = "dbpprop:showName"
    language = "en"

class HasPlace(FixedDataRelation) :
    relation = "<my:opencollege:studentvocab/resource/Students_City%2FTown>"

class HasName(FixedDataRelation):
    relation = "dbpprop:name"
    language = "en"


class DefinitionOf(FixedRelation):
    relation = "rdfs:comment"		
    reverse = True	

class DefinitionOfSI(FixedRelation):
    relation = "<my:opencollege:studentvocab/resource/Students_SI>"		
    reverse = True	

class DefinitionOfLN(FixedRelation):
    relation = "<my:opencollege:studentvocab/resource/Students_Last+Name>"			
    reverse=True

class DefinitionOfFN(FixedRelation):
    relation = "<my:opencollege:studentvocab/resource/Students_First+Name>"			
    reverse=True

class LabelOf(FixedRelation):
    relation = "rdfs:label"
    reverse = True


class UTCof(FixedRelation):
    relation = "dbpprop:utcOffset"
    reverse = True


class Principal(FixedRelation):
    relation = "dbpprop:leaderTitle"
    reverse = True


class IncumbentOf(FixedRelation):
    relation = "dbpprop:incumbent"
    reverse = True


class CapitalOf(FixedRelation):
    relation = "dbpedia-owl:capital"
    reverse = True


class LanguageOf(FixedRelation):
    relation = "dbpprop:officialLanguages"
    reverse = True


class PopulationOf(FixedRelation):
    relation = "dbpprop:populationCensus"
    reverse = True


class IsMemberOf(FixedRelation):
    relation = "dbpedia-owl:bandMember"
    reverse = True


class ActiveYears(FixedRelation):
    relation = "dbpprop:yearsActive"
    reverse = True


class MusicGenreOf(FixedRelation):
    relation = "dbpedia-owl:genre"
    reverse = True


class ProducedBy(FixedRelation):
    relation = "dbpedia-owl:producer"


class BirthDateOf(FixedRelation):
    relation = "<my:opencollege:studentvocab/resource/Students_Date+Of+Birth>"
    reverse = True


class PlaceOf(FixedRelation):
    relation = "<my:opencollege:studentvocab/resource/Students_Area>"
    reverse = True


class ReleaseDateOf(FixedRelation):
    relation = "dbpedia-owl:releaseDate"
    reverse = True


class StarsIn(FixedRelation):
    relation = "dbpprop:starring"
    reverse = True


class NumberOfEpisodesIn(FixedRelation):
    relation = "dbpedia-owl:numberOfEpisodes"
    reverse = True


class ShowNameOf(FixedRelation):
    relation = "dbpprop:showName"
    reverse = True


class HasActor(FixedRelation):
    relation = "dbpprop:starring"


class CreatorOf(FixedRelation):
    relation = "dbpprop:creator"
    reverse = True


class NameOf(FixedRelation):
    relation = "foaf:name"
    # relation = "dbpprop:name"
    reverse = True


class DirectedBy(FixedRelation):
    relation = "dbpedia-owl:director"


class DirectorOf(FixedRelation):
    relation = "dbpedia-owl:director"
    reverse = True


class DurationOf(FixedRelation):
    # DBpedia throws an error if the relation it's
    # dbpedia-owl:Work/runtime so we expand the prefix
    # by giving the whole URL.
    relation = "<http://dbpedia.org/ontology/Work/runtime>"
    reverse = True


class HasAuthor(FixedRelation):
    relation = "dbpedia-owl:author"


class AuthorOf(FixedRelation):
    relation = "dbpedia-owl:author"
    reverse = True


class IsBook(FixedType):
    fixedtype = "dbpedia-owl:Book"


class LocationOf(FixedRelation):
    relation = "dbpedia-owl:location"
    reverse = True
