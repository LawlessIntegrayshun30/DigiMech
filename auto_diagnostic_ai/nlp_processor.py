## nlp_processor.py
import spacy
from typing import Dict

class NLPProcessor:
    def __init__(self, model: str = "en_core_web_sm"):
        """
        Initialize the NLPProcessor with a specific language model.

        :param model: The spaCy language model to load.
        """
        self.nlp = spacy.load(model)

    def process_input(self, input_text: str) -> Dict[str, str]:
        """
        Process the input text and extract relevant information for diagnostics.

        :param input_text: A string containing the symptoms described by the user.
        :return: A dictionary with extracted information.
        """
        doc = self.nlp(input_text)
        processed_data = {}

        # Extract entities and label them in the processed_data dictionary
        for ent in doc.ents:
            processed_data[ent.label_] = ent.text

        return processed_data
