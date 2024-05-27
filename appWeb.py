import streamlit as st
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import docx

# Descargar recursos de NLTK si es necesario
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_text_from_docx(file): 
    doc = docx.Document(file)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

def get_named_entities(text): 
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    ner_chunks = ne_chunk(pos_tags)
    
    named_entities = []
    for chunk in ner_chunks:
        if isinstance(chunk, Tree):
            entity = " ".join([token for token, pos in chunk.leaves()])
            entity_type = chunk.label()
            named_entities.append((entity, entity_type))
    
    return named_entities

def main():
    st.title("Reconocimiento de Entidades Nombradas con NLTK")
    
    st.subheader("Cargar archivo DOCX")
    docx_file = st.file_uploader("Sube tu archivo DOCX", type=["docx"])

    if docx_file is not None:
        raw_text = extract_text_from_docx(docx_file)
        st.text_area("Texto del archivo DOCX", raw_text, height=200)
        
        if st.button("Reconocer Entidades"):
            named_entities = get_named_entities(raw_text)
            st.subheader("Entidades Reconocidas")
            if named_entities:
                for entity, entity_type in named_entities:
                    st.write(f'{entity} ({entity_type})')
            else:
                st.write("No se encontraron entidades nombradas.")

if __name__ == "__main__":
    main()
