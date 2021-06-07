import spacy_streamlit

models = ["en_core_web_sm", "en_core_web_md"]
default_text = "I love coding in Python and using NLP packages like SpaCy"
spacy_streamlit.visualize(models, default_text)
