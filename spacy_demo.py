import random
import spacy
from spacy.tokens import Doc, Span, Token
import spacy
from spacy.matcher import Matcher, PhraseMatcher
from spacy.lang.en import English
from spacy.language import Language

nlp = spacy.load('en_core_web_lg')

def analyze_text(text):
	return nlp(text)

# # # Basic Lexical Properties of spacy model # # #

# doc = nlp('It costs $5.')
# print("Index: ", [token.i for token in doc])
# print("Orth:", [token.orth for token in doc])
# print("Text: ", [token.text for token in doc])
# print("is_alpha: ", [token.is_alpha for token in doc])
# print("is_punct: ", [token.is_punct for token in doc])
# print("like_num: ", [token.like_num for token in doc])

# # # Explain Spacy Labels # # #

# print(spacy.explain('GPE'))
# print(spacy.explain('DET'))
# print(spacy.explain('OP'))

# # # Linguistic Features # # #
# doc = nlp('She ate the pizza!')

# for token in doc:
#     # The part-of-speech tag of the token head.
#     print('Part of speech', token.text, '-->', token.pos_)
#     # The syntactic relation connecting child to head.
#     print('Dependency parser', token.text, '-->', token.dep_)
#     # The original text of the token head.
#     print('Head Text', token.text, '-->', token.head.text)

# # # Predicting Named Entities # # #

# doc = nlp('Apple is looking at buying U.K. startup for $1 Billion')

# for ent in doc.ents:
#     print(ent.text, '-->', ent.label_)

### LEMMA ###

# # # Matcher Patterns # # #
matcher = Matcher(nlp.vocab)

def sportsPatterns(sport):
	return [
		{'IS_DIGIT': True},
		{'LOWER': f'{sport}', 'OP': '?'},
		{'LOWER': 'world'},
		{'LOWER': 'cup'},
		{'IS_PUNCT': True},
	]


def emotionPatterns(emotion):
	return [
		{'LEMMA': f'{emotion}', 'POS': 'VERB'},
	]


def gadjetsPatterns(gadget, extensionName):
	return [
		{'LOWER': f'{gadget}'}, 
		{'LOWER': f'{extensionName}', 'OP': '?'}
	]


fifa = sportsPatterns(sport='fifa')
rugby = sportsPatterns(sport='rugby')

love = emotionPatterns(emotion='love')
hate = emotionPatterns(emotion='hate')

phone = gadjetsPatterns(gadget='iphone', extensionName='x')
computer = gadjetsPatterns(gadget='mac', extensionName='proo')


# # # Using The Matcher # # #
# Fix Add 2 sets matchers

def add_matchers(matcher):
	matcher.add("World_Cups", [fifa, rugby]);
	matcher.add("Emotion", [love, hate]);
	matcher.add("Gadgets", [phone, computer]);


add_matchers(matcher)



def showMatcher(doc):
	matches = matcher(doc)
	for match_id, start, end in matches:
		string_id = nlp.vocab.strings[match_id]  # Get string representation of matcher
		span = doc[start:end]  # The matched span
		print(
			f"""match_id: {match_id},
string_id: {string_id},
start: {start},
end: {end},
TEXT: {span.text}
		""")

def showRepresentationOfMatchers():
	doc = nlp('Upcoming Mac Pro, has leaked the release date')
	doc2 = nlp('2018 FIFA world cup: France won!')
	doc3 = nlp('I loved dogs now I love cats more')
	doc4 = nlp('I hate tomatoes')
	showMatcher(doc)
	showMatcher(doc2)
	showMatcher(doc3)
	showMatcher(doc4)


showRepresentationOfMatchers()


# # # Efficient Phrase Matcher # # #

matcher = PhraseMatcher(nlp.vocab)
pattern = nlp('Golden Retriever')
pattern2 = nlp('Golden Retriever')
matcher.add('DOG', [pattern, pattern2])
doc = nlp("I have a Golden Retriever")

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print('Matched phrase: ', span.text)

# # # Similarity # # #

# # 2 documents
# doc1 = nlp('I like fast food')
# doc2 = nlp('I love pizza')
# print(f"{round(doc1.similarity(doc2) * 100, 2)}%")

# # # 2 tokens
# doc = nlp('I like pizza and pasta')
# print(f"{round(doc[2].similarity(doc[4]) * 100, 2)}%")

# # # document and token
# d = nlp('I love pizza')
# t = nlp('soap')[0]

# print(f"{round(d.similarity(t) * 100, 2)}%")

# # span and document
# span = nlp('I like pizza and pasta')[2: 5]
# document = nlp('MacDonald\'s sells burgers')

# print(f"{round(span.similarity(document) * 100, 2)}%")
