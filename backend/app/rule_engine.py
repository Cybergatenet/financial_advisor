import json
import os
from typing import Dict, Any, List, Tuple

# Load rules from JSON file
RULES_FILE = "data/rules.json"

def load_rules():
    if not os.path.exists(RULES_FILE):
        # Default rules if file missing
        default_rules = [
            {
                "id": 1,
                "condition": "profile['risk_tolerance'] == 'low' and user_age > 60",
                "action": "recommend_bonds",
                "explanation": "Low-risk tolerance and age above 60 suggest shifting to fixed income.",
                "priority": 10
            },
            {
                "id": 2,
                "condition": "profile['savings'] < profile['annual_income'] * 0.25",
                "action": "recommend_emergency_fund",
                "explanation": "Emergency fund should cover at least 3-6 months of expenses.",
                "priority": 8
            }
        ]
        os.makedirs(os.path.dirname(RULES_FILE), exist_ok=True)
        with open(RULES_FILE, 'w') as f:
            json.dump(default_rules, f, indent=2)
        return default_rules
    with open(RULES_FILE, 'r') as f:
        return json.load(f)

class RuleEngine:
    def __init__(self):
        self.rules = load_rules()
        # Sort by priority descending
        self.rules.sort(key=lambda x: x.get('priority', 0), reverse=True)

    def evaluate(self, profile: Dict[str, Any], user_age: int = None) -> List[Tuple[str, str, float]]:
        """
        Returns list of (action, explanation, priority_score)
        """
        results = []
        # Add age to profile for condition evaluation
        eval_context = {'profile': profile, 'user_age': user_age}
        for rule in self.rules:
            if not rule.get('is_active', True):
                continue
            try:
                # Safe evaluation of condition (simplified; in production use a restricted sandbox)
                condition_str = rule['condition']
                # Replace dictionary access with safe eval
                # This is a simplified demo; for production use a proper expression evaluator
                if eval(condition_str, {"__builtins__": {}}, eval_context):
                    results.append((rule['action'], rule['explanation'], rule.get('priority', 0)))
            except Exception as e:
                print(f"Rule evaluation error: {e}")
        return results

    def get_recommendation_text(self, actions: List[Tuple[str, str, float]]) -> str:
        """Convert actions to natural language advice."""
        if not actions:
            return "Your financial profile looks balanced. Consider reviewing your long-term goals."
        advice_parts = []
        for action, explanation, _ in actions:
            if action == "recommend_bonds":
                advice_parts.append(f"Bond allocation: {explanation}")
            elif action == "recommend_emergency_fund":
                advice_parts.append(f"Emergency fund: {explanation}")
            else:
                advice_parts.append(explanation)
        return " ".join(advice_parts)