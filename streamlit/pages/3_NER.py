import streamlit as st
from transformers import pipeline

from transformers import AutoTokenizer, AutoModelForTokenClassification

print("**Successfully imported transformers library...")

st.set_page_config(page_title="NER Tool", page_icon="⭐")

st.markdown("# Named Entity Recognition with HuggingFace")
st.sidebar.header("⭐ Named Entity Recognition")
st.write("We're using a 🤗 model fine-tuned on the English version of the standard CoNLL-2003 Named Entity Recognition dataset.")

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)

long_text = st.text_area('Please enter the paragraph to run NER on:', 
'''Russia is prepared to resume gas supplies to Europe via the Yamal-Europe gas pipeline, which was previously stopped for political reasons, Russia’s Deputy Prime Minister Alexander Novak told Russian state news agency TASS on Sunday. “The European market remains relevant, as the gas shortage persists, and we have every opportunity to resume supplies. For example, the Yamal-Europe pipeline, which was stopped for political reasons, remains unused,” Novak said.

From https://edition.cnn.com/2022/12/25/europe/russia-yamal-europe-gas-pipeline/index.html
''')

ner_results = nlp(long_text)
# st.write(ner_results['entity'])

persons = []
locations = []
organizations = [] 
miscs = [] 
for result in ner_results: 
  if 'PER' in str(result['entity']):
    persons.append(result['word'])
  elif 'LOC' in str(result['entity']): 
    locations.append(result['word'])
  elif 'ORG' in str(result['entity']): 
    organizations.append(result['word'])
  else: 
    miscs.append(result['word'])

# TO DO: make output prettier
st.write("People mentioned: ", str(persons))
st.write("Locations mentioned: ", str(locations))
st.write("Organizations mentioned: ", str(organizations))
st.write("Other entities mentioned: ", str(miscs))