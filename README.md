# NLP_Basics

Understanding how a machine understands context of language. "We are Human, thought to patterns to making Machines" J.P.M.C

## Need to set-up virtualenv
$ pip install virtualenv
$ virtualenv venv

# Set-up
$ source venv/bin/activate

## Install Packages

$ pip install requirements.txt

`To reduce you can reduce`
`pip install (each): streamlit, spacy, gensim, sumy i.e`
$ pip install streamlit

`If spacy is installed the following is important to install`
$ python -m spacy download en_core_web_sm
$ python -m spacy download en_core_web_md
$ python -m spacy download en_core_web_lg

## Starting the app

$ streamlit run app.py
