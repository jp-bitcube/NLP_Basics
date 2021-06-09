import random
import spacy
from spacy.tokens import Doc, Span, Token
import spacy
from spacy.matcher import Matcher, PhraseMatcher
from spacy.lang.en import English
from spacy.language import Language

nlp = spacy.load('en_core_web_sm')

def analyze_text(text):
	return nlp(text)


# # Basic Lexical Properties of spacy model # # #

# doc = nlp('It costs $5.')
# print("Index: ", [token.i for token in doc])
# print("Orth:", [token.orth for token in doc])
# print("Text: ", [token.text for token in doc])
# print("is_alpha: ", [token.is_alpha for token in doc])
# print("is_punct: ", [token.is_punct for token in doc])
# print("like_num: ", [token.like_num for token in doc])


# # # Explain Spacy Labels # # #

# print(spacy.explain('GPE'))
# print(spacy.explain('NNP'))
# print(spacy.explain('nsubj'))


# # # Linguistic Features # # #
# doc = nlp('She ate the pizza!')

# for token in doc:
#     # he part-of-speech tag of the token head.
#     print('Part of speech', token.text, '-->', token.pos_)
#     # The syntactic relation connecting child to head.
#     print('Dependency parser', token.text, '-->', token.dep_)
#     # The original text of the token head.
#     print('Head Text', token.text, '-->', token.head.text)

# # # Predicting Named Entities # # #

# doc = nlp('Apple is looking at buying U.K. startup for $1 Billion')

# for ent in doc.ents:
#     print(ent.text, '-->', ent.label_)


# # # Matcher Patterns # # #
# pattern = [
#     {'IS_DIGIT': True},
#     {'LOWER': 'fifa'},
#     {'LOWER': 'world'},
#     {'LOWER': 'cup'},
#     {'IS_PUNCT': True},
# ]
# pattern1 = [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]
# pattern2 = [{'LOWER': 'iphone'}, {'LOWER': 'x'}]
# pattern3 = [
#     {'LEMMA': 'buy'},
#     {'POS': 'DET', 'OP': '?'},  # Optional: matches 0 - 1 times
#     {'POS': 'NOUN'}
# ]
# pattern4 = [
#     {'LEMMA': 'love', 'POS': 'VERB'},
#     {'POS': 'NOUN'}
# ]

# # # Using The Matcher # # #

# matcher = Matcher(nlp.vocab)
# matcher.add("PATTERN_NAME", [pattern, pattern1, pattern2, pattern3, pattern4])
# # doc = nlp('Upcoming iPhone X, has leaked the release date')
# # doc2 = nlp('2018 FIFA world cup: France won!')
# # doc3 = nlp('I loved dogs now I love cats more')
# doc4 = nlp('I have bought a smart phone. now I\'m buying apps')

# matches = matcher(doc4)
# for match_id, start, end in matches:
#     string_id = nlp.vocab.strings[match_id]  # Get string representation
#     span = doc4[start:end]  # The matched span
#     print(match_id, string_id, start, end, span.text)

# # #  StringStore  # # #

# coffee_hash = nlp.vocab.strings["coffee"]
# coffee_string = nlp.vocab.strings[coffee_hash]

# print(coffee_string, coffee_hash)

# #  Lexemes  # # #

doc = nlp('I love coffee')
lexeme = nlp.vocab["coffee"]

print(lexeme.text, lexeme.orth, lexeme.is_alpha)

# # #  Doc Object and Span object  # # #

# model = English()

# words = ['Hello', 'World', '!']
# spaces = [True, False, False]

# # Creating a doc manually
# doc = Doc(model.vocab, words=words, spaces=spaces)

# span = Span(doc, 0, 2)

# span_with_label = Span(doc, 0, 2, label="GREETING")

# doc.ents = [span_with_label]

# print(doc.ents)

# # # Similarity # # #

# # 2 documents
# doc1 = nlp('I like fast food')
# doc2 = nlp('I love pizza')
# print(doc1.similarity(doc2))

# # 2 tokens
# doc = nlp('I like pizza and pasta')
# print(doc[2].similarity(doc[4]))

# # document and token
# d = nlp('I love pizza')
# t = nlp('soap')[0]

# print(d.similarity(t))

# # span and document
# span = nlp('I like pizza and pasta')[2: 5]
# document = nlp('MacDonalds sells burgers')

# print(span.similarity(document))
# # Vectors
# print(document[2].vector)

# # # Adding Statistical predictions # # #

# matcher = Matcher(nlp.vocab)
# pattern = [
#     {'LOWER': 'golden'},
#     {'LOWER': 'retriever'},
# ]
# matcher.add('DOG', [pattern])
# doc = nlp("I have a Golden Retriever")

# for match_id, start, end in matcher(doc):
#     span = doc[start:end]
#     print('Matched Span: ', span.text)
#     # Get the span root token and root head
#     print('Root token: ', span.root.text)
#     print('Root head: ', span.root.head.text)
#     # Get the previous token and its POS tag
#     print("Previous token: ", doc[start-1].text, doc[start-1].pos_)

# # # Efficient Phrase Matcher # # #

# matcher = PhraseMatcher(nlp.vocab)
# pattern = nlp('Golden Retriever')
# matcher.add('DOG', [pattern])
# doc = nlp("I have a Golden Retriever")

# for match_id, start, end in matcher(doc):
#     span = doc[start:end]
#     print('Matched phrase: ', span.text)

# # # Pipeline attributes # # #

# print(nlp.pipe_names)
# print(nlp.pipeline)

# # # Simple Custom Pipeline Component # # #

# @Language.component("length")
# def custom_component(doc):
#     print('DOC LENGTH: ', len(doc))
#     return doc


# nlp.add_pipe('length', first=True)
# d = nlp("This is a sentence.")

# print('Pipelines', nlp.pipe_names, d)

# def has_token(doc, token_text):
#     in_doc = token_text in [token.text for token in doc]
#     return in_doc


# Doc.set_extension('has_token', method=has_token)


# doc = nlp("The sky is Blue, the sky is magnificent, and the word colour in South Africa and English is correct. Only coding we drop the 'u'")

# print(doc._.has_token("blue"), '--> blue')
# print(doc._.has_token("color"), '--> color')