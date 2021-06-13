# print("Index: ", [token.i for token in doc])
# print("Orth:", [token.orth for token in doc]) 
# print("Text: ", tokenizeWord('text')) 
# print("is_alpha: ", tokenizeWord('is_alpha'))
# print("is_punct: ", tokenizeWord('is_punct'))
# print("like_num: ", tokenizeWord('like_num'))
# print("is_stopword", tokenizeWord('like_num'))


# # # # spaCy Labels Explained # # #

# # def spacy_explain(label):
# # 	print(spacy.explain(label))


# # spacy_explain('DET')
# # spacy_explain('DET')
# # # # Linguistic Features # # #
# # doc = analyze_text('We ate a pizza yesterday!')

# # for token in doc:
# #     # The part-of-speech tag of the token head.
# #     print('Part of speech', token.text, '-->', token.pos_)
# #     # The syntactic relation connecting child to head.
# #     print('Dependency parser', token.text, '-->', token.dep_)
# #     # The original text of the token head.
# #     print('Head Text', token.head.text, '-->', token.text)


# # # # # Predicting Named Entities # # #

# # # doc = analyze_text('Apple is looking at buying U.K. startup for $1 Billion')

# # # for ent in doc.ents:
# # #     print(ent.text, '-->', ent.label_)




# # # # # Matcher Patterns # # #

# # ### LEMMA attribute###
# # # Lemma (Finds the root word "win" -> ["won", "winning", "winner"]), 
# # # (Stemming “winning” -> “winn” and that’s not an english word!)

# # # doc = analyze_text('The man')
# # def lemmatisation():
	


# matcher = Matcher(nlp.vocab)

# def sportsPatterns(sport):
# 	return [
# 		{'IS_DIGIT': True},
# 		{'LOWER': f'{sport}', 'OP': '?'},
# 		{'LOWER': 'world'},
# 		{'LOWER': 'cup'},
# 		{'IS_PUNCT': True},
# 	]


# def emotionPatterns(emotion):
# 	return [
# 		{'LEMMA': f'{emotion}', 'POS': 'VERB'},
# 	]


# def gadgetPatterns(gadget, extensionName):
# 	return [
# 		{'LOWER': f'{gadget}'}, 
# 		{'LOWER': f'{extensionName}', 'OP': '?'}
# 	]


# fifa = sportsPatterns(sport='fifa')
# rugby = sportsPatterns(sport='rugby')

# love = emotionPatterns(emotion='love')
# hate = emotionPatterns(emotion='hate')

# phone = gadgetPatterns(gadget='iphone', extensionName='x')
# computer = gadgetPatterns(gadget='mac', extensionName=' ')


# # # # Using The Matcher # # #
# # Fix Add 2 sets matchers

# def add_matchers(matcher):
# 	matcher.add("World_Cups", [fifa, rugby]);
# 	matcher.add("Emotion", [love, hate]);
# 	matcher.add("Gadgets", [phone, computer]);


# add_matchers(matcher)

# def showMatcher(doc):
# 	matches = matcher(doc)
# 	for match_id, start, end in matches:
# 		string_id = nlp.vocab.strings[match_id]  # Get string representation of matcher
# 		span = doc[start:end]  # The matched span
# 		print(
# 			f"""match_id: {match_id},
# string_id: {string_id},
# start: {start},
# end: {end},
# TEXT: {span.text}
# 		""")

# def showRepresentationOfMatchers():
# 	doc = analyze_text('Upcoming Mac Pro, has leaked the release date')
# 	doc2 = analyze_text('2018 FIFA world cup: France won!')
# 	doc3 = analyze_text('I loved dogs now I love cats more')
# 	doc4 = analyze_text('I hate tomatoes')
# 	showMatcher(doc)
# 	showMatcher(doc2)
# 	showMatcher(doc3)
# 	showMatcher(doc4)


# showRepresentationOfMatchers()


# # # # # # Efficient Phrase Matcher # # #

# matcher = PhraseMatcher(nlp.vocab)
# pattern = analyze_text('Golden Retriever')
# pattern2 = analyze_text('Golden Retriever')
# matcher.add('DOG', [pattern, pattern2])
# doc = nlp("I have a Golden Retriever")

# for match_id, start, end in matcher(doc):
#     span = doc[start:end]
#     print('Matched phrase: ', span.text)

# # # # # Similarity # # #

# # # # 2 documents
# # # doc1 = analyze_text('I like fast food')
# # # doc2 = analyze_text('I love pizza')
# # # print(f"{round(doc1.similarity(doc2) * 100, 2)}%")

# # # # # 2 tokens
# # # doc = analyze_text('I like pizza and pasta')
# # # print(f"{round(doc[2].similarity(doc[4]) * 100, 2)}%")

# # # # # document and token
# # # d = analyze_text('I love pizza')
# # # t = analyze_text('soap')[0]

# # # print(f"{round(d.similarity(t) * 100, 2)}%")

# # # # span and document
# # # span = analyze_text('I like pizza and pasta')[2: 5]
# # # document = analyze_text('MacDonald\'s sells burgers')

# # # print(f"{round(span.similarity(document) * 100, 2)}%")
