import spacy
import sys, os
from spacy.lang.xx import MultiLanguage
os.system("python -m spacy download xx_ent_wiki_sm")

def NER(text, language_code):
    # Load the appropriate spaCy model for the specified language code
    nlp = spacy.load("xx_ent_wiki_sm")
    # Process the input text with the loaded spaCy model
    doc = nlp(text)
    print(doc)

    # Extract entities from the processed text
    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "type": ent.label_,
            "start_pos": ent.start_char,
            "end_pos": ent.end_char
        })

    # Return the list of entities
    return entities
if __name__ == '__main__':
    text = "Hello George Washington, how are you ? I am in Washington, George, talking with Washington. PS : wikiNER is lame"
    lang = "en"
    entities = NER(text,lang)
    print(entities)