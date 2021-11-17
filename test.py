import scispacy
import spacy

# model for biomedical domain
#nlp = spacy.load("en_core_sci_sm")

# for NER
nlp = spacy.load("en_ner_bionlp13cg_md")

text = "Myeloid derived suppressor cells (MDSC) are immature myeloid cells with immunosuppressive activity. They accumulate in tumor-bearing mice and humans with different types of cancer, including hepatocellular carcinoma (HCC)."

doc = nlp(text)

print(list(doc.sents))

# output
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

