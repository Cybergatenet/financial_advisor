from . import ml_models

def process_chat_message(message: str) -> dict:
    nlu_result = ml_models.nlu.classify(message)
    intent = nlu_result["intent"]
    # Simple rule-based responses for demo
    if intent == "ask_performance":
        reply = "Based on recent trends, the expected market return is around 7-9% annually. However, past performance does not guarantee future results."
    elif intent == "ask_risk":
        reply = "Your portfolio risk depends on your asset allocation. A diversified mix of stocks and bonds typically reduces volatility."
    elif intent == "trade_suggestion":
        reply = "I recommend consulting the AI advice dashboard for specific buy/sell suggestions tailored to your risk profile."
    else:
        reply = "I'm your financial assistant. You can ask about performance, risk, or investment strategies."
    return {"reply": reply, "intent": intent}