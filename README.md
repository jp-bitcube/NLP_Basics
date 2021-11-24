# NLP_Basics

Understanding how a machine understands context of language i.e a simple Quote: "We are Human, and a thought to the patterns in making Machines". J.P.M.C

## Need to set-up virtualenv

$ pip install virtualenv
$ virtualenv venv

# Activate App
$ source venv/bin/activate

## Install Packages

$ pip install requirements.txt

## Extra features to install
`pip install (each): streamlit, spacy, gensim, sumy i.e`
$ pip install streamlit

`If spacy is installed the following is important to install`
$ python -m spacy download en_core_web_sm
$ python -m spacy download en_core_web_md
$ python -m spacy download en_core_web_lg

## Starting the app
$ streamlit run app.py
