## knowledgebase.py
import pymongo
from typing import List

class KnowledgeBase:
    def __init__(self, uri: str = "mongodb://localhost:27017/", db_name: str = "vehicle_knowledgebase"):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]
        self.issues_collection = self.db["issues"]

    def get_repair_suggestions(self, issue: str) -> List[str]:
        """
        Retrieve repair suggestions for a given issue from the knowledgebase.

        :param issue: A string representing the issue for which repair suggestions are needed.
        :return: A list of strings, each representing a repair suggestion.
        """
        suggestions = []
        query = {"issue": issue}
        results = self.issues_collection.find(query)

        for result in results:
            if "suggestions" in result:
                suggestions.extend(result["suggestions"])

        return suggestions
