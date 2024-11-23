## diagnostics.py
from typing import Optional, Dict, List
from nlp_processor import NLPProcessor
from knowledgebase import KnowledgeBase
from obd_interface import OBDInterface

class Diagnostics:
    def __init__(self):
        self.nlp_processor = NLPProcessor()
        self.knowledge_base = KnowledgeBase()
        self.obd_interface = OBDInterface()

    def diagnose_symptoms(self, symptoms: str) -> str:
        """
        Diagnose vehicle issues based on textual symptoms provided by the user.

        :param symptoms: A string describing the symptoms.
        :return: A string with the diagnosis result.
        """
        processed_symptoms = self.nlp_processor.process_input(symptoms)
        issue = self._determine_issue(processed_symptoms)
        suggestions = self.knowledge_base.get_repair_suggestions(issue)
        return self._format_diagnosis(issue, suggestions)

    def diagnose_obd_data(self, obd_data: Optional[Dict[str, str]] = None) -> str:
        """
        Diagnose vehicle issues based on OBD-II data.

        :param obd_data: A dictionary containing OBD-II data, if already retrieved.
        :return: A string with the diagnosis result.
        """
        if obd_data is None:
            obd_data = self.obd_interface.get_data()
        issue = self._determine_issue(obd_data)
        suggestions = self.knowledge_base.get_repair_suggestions(issue)
        return self._format_diagnosis(issue, suggestions)

    def _determine_issue(self, data: Dict[str, str]) -> str:
        """
        Determine the issue based on processed data.

        :param data: A dictionary containing processed symptoms or OBD-II data.
        :return: A string representing the determined issue.
        """
        # This is a placeholder for the logic to determine the issue based on the data.
        # The actual implementation would involve complex logic and is not provided here.
        # For demonstration purposes, we'll just return a generic issue.
        return "generic_issue"

    def _format_diagnosis(self, issue: str, suggestions: List[str]) -> str:
        """
        Format the diagnosis result into a readable string.

        :param issue: A string representing the determined issue.
        :param suggestions: A list of strings representing repair suggestions.
        :return: A formatted string with the diagnosis and suggestions.
        """
        diagnosis = f"Issue diagnosed: {issue}\n"
        if suggestions:
            diagnosis += "Suggested repairs:\n" + "\n".join(f"- {suggestion}" for suggestion in suggestions)
        else:
            diagnosis += "No repair suggestions available."
        return diagnosis
