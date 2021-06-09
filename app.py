# Supports so many graphs, mainly used for machine learning
import streamlit as st

# # NLP basics
import spacy
from spacy import displacy

# Summaristion
from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

from googletrans import Translator
translator = Translator()

nlp = spacy.load('en_core_web_sm')
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

def translate_text(doc, lang): 
    text = translator.translate(doc, dest=f'{lang}')
    return text


def summary_analyzer(doc):
    text = translate_text(doc, "en")
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, 10)
    summary_list = [str(sen) for sen in summary]
    result = ' '.join(summary_list)
    return result


def text_analyzer(doc):
    doc = analyze_text(doc)
    tokens = [(f'Text: {token.text} Token Hash: {token.orth}, Lemma: {token.lemma_}, P.O.S: {token.pos_} ') for token in doc]
    return tokens


# There are more comprehensive ways to extract even, train spacy to recognize your own entities
def entities_extracted(doc):
    doc = nlp(doc)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities


def analyze_text(text):
	return nlp(text)


# Runs StreamLit App
def main():
        """NLP App with Streamlit"""
        st.title("NLP App with Streamlit Simplified")
        st.subheader("Natural Language Processing on the Go")

        # Tokenization
        if st.checkbox("Show Tokens and Lemma"):
            st.subheader("Tokenize your word, sentence or paragraph")
            message = st.text_area("Tokenization & Lemmas", "")
            if st.button('Analyze'):
                nlp_result = text_analyzer(message)
                st.json(nlp_result)

        # Named Entities
        if st.checkbox("Show Entities"):
            st.subheader("Named Entity Recognition with Spacy")
            message = st.text_area("Entities", "")
            if st.button("Extract"):
                doc = analyze_text(message)
                html = displacy.render(doc, style="ent")
                html = html.replace("\n\n","\n")
                st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)

        # Text Summarisation
        if st.checkbox("Show Summarization"):
            st.subheader("Summarization paragraph(s)")
            message = st.text_area("Summarizer", "")
            choice = st.selectbox('Choose your summarizer...', ('Gensim', 'Sumy'))
            if st.button('Summarize'):
                if choice == 'Gensim':
                    st.text('Using Gensim...')
                    summarize_result = summarize(translate_text(message, "en"))
                elif choice == 'Sumy':
                    st.text('Using Sumy...')
                    summarize_result = summary_analyzer(translate_text(message, "en"))
                else:
                    st.warning('Using Default Summarizer...')
                    st.text('Using Gensim...')
                    summarize_result = summarize(translate_text(message, "en"))
                st.success(summarize_result)
    
        st.sidebar.subheader('About App')
        st.sidebar.text('NLP Basics built with streamlit')
        st.sidebar.info("Cudo's to Streamlit Team")


if __name__ == '__main__':
    main()
