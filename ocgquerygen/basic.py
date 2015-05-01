# coding: utf-8

"""
Basic queries for ocgquerygen quepy.
from dsl import *
"""

"""
People related regex
"""

from refo import Plus, Question
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate, Particle
from dsl import IsPerson, LabelOf, DefinitionOf, BirthDateOf, PlaceOf,IsFirstName, DefinitionOfSI, DefinitionOfLN, HasPlace, IsPlace, DefinitionOfFN


class Person(Particle):
    regex = Plus(Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens
        return HasKeyword(name)		#IsPerson + 

class Place(Particle):
    regex = Plus(Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens
        return HasPlace(name)


class WhoIs(QuestionTemplate):
    """
    Ex: "Who is Tom Cruise?"
    """

    regex = Lemma("who") + Lemma("be") + Person() + \
        Question(Pos("."))

    def interpret(self, match):
        definition =DefinitionOfLN(match.person) 
       	return definition, "define"

class WhenBornQuestion(QuestionTemplate):
    """
    Ex: "When was Bob Dylan born?".
    """

    regex = Pos("WRB") + Lemma("be") + Person() + Lemma("born") + \
        Question(Pos("."))

    def interpret(self, match):
        birth_date = BirthDateOf(match.person)
        return birth_date


class WhereIsFromQuestion(QuestionTemplate):
    """
    Ex: "Where is Bill Gates from?"
    """

    regex = Lemmas("where be") + Person() + Lemma("from") + \
        Question(Pos("."))

    def interpret(self, match):
        place = PlaceOf(match.person)
       	return place, "define"

class PlacesNearPlace(QuestionTemplate):
    """
    Ex: "List Places near Ernakulam?"
    """
    regex = Lemma("list") + Lemma("place") + Lemma("near") +  Place() + Question(Pos("."))


    def interpret(self, match):
        place = PlaceOf(match.place)
       	return place, "define"   

class WhoAllFromPlace(QuestionTemplate):
    """
    Ex: "Who all are from Ernakulam?"
    """

    regex = Lemmas("who") + Lemma("all") + Lemma("be") + Lemma("from")+ Place() + Question(Pos("."))

    def interpret(self, match):
	people = DefinitionOfFN(match.place) 
       	return people, "define"  

