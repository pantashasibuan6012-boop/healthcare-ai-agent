#!/usr/bin/env python3
"""Healthcare AI Agent."""

import json, sys
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Symptom:
    name: str
    severity: int
    duration: str

@dataclass
class Assessment:
    symptoms: list
    triage_level: str
    possible_conditions: list
    recommendations: list
    urgency: str

class HealthcareAgent:
    TRIAGE_RULES = {
        "emergency": ["chest pain", "difficulty breathing", "unconscious", "severe bleeding"],
        "urgent": ["high fever", "severe pain", "persistent vomiting", "head injury"],
        "moderate": ["fever", "rash", "persistent cough", "abdominal pain"],
        "low": ["cold", "mild headache", "minor cut", "allergies"],
    }

    def assess(self, description: str) -> Assessment:
        lower = description.lower()
        symptoms = self._extract_symptoms(lower)
        triage = self._determine_triage(lower)
        conditions = self._suggest_conditions(symptoms)
        recs = self._recommendations(triage, symptoms)

        return Assessment(
            symptoms=[s.name for s in symptoms],
            triage_level=triage,
            possible_conditions=conditions,
            recommendations=recs,
            urgency=triage,
        )

    def _extract_symptoms(self, text: str) -> list:
        symptom_db = {
            "headache": Symptom("headache", 3, "acute"),
            "fever": Symptom("fever", 4, "acute"),
            "cough": Symptom("cough", 2, "subacute"),
            "pain": Symptom("pain", 3, "acute"),
            "rash": Symptom("rash", 2, "subacute"),
            "nausea": Symptom("nausea", 2, "acute"),
        }
        found = []
        for keyword, symptom in symptom_db.items():
            if keyword in text:
                found.append(symptom)
        return found if found else [Symptom("general discomfort", 1, "unknown")]

    def _determine_triage(self, text: str) -> str:
        for level, keywords in self.TRIAGE_RULES.items():
            if any(kw in text for kw in keywords):
                return level
        return "low"

    def _suggest_conditions(self, symptoms: list) -> list:
        conditions = []
        names = [s.name for s in symptoms]
        if "fever" in names and "headache" in names:
            conditions.append("Viral infection")
        if "cough" in names and "fever" in names:
            conditions.append("Respiratory infection")
        if not conditions:
            conditions.append("General assessment recommended")
        return conditions

    def _recommendations(self, triage: str, symptoms: list) -> list:
        if triage == "emergency":
            return ["Call emergency services immediately", "Do not drive yourself to hospital"]
        elif triage == "urgent":
            return ["Visit urgent care within 2 hours", "Monitor symptoms closely"]
        elif triage == "moderate":
            return ["Schedule doctor appointment within 24 hours", "Rest and stay hydrated"]
        return ["Monitor symptoms", "Over-the-counter medication if needed", "See doctor if symptoms persist"]

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py assess 'symptoms description'")
        sys.exit(1)
    agent = HealthcareAgent()
    desc = " ".join(sys.argv[2:])
    result = agent.assess(desc)
    print(json.dumps(result.__dict__, indent=2, default=str))

if __name__ == "__main__":
    main()
