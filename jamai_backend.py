from jamai import JamAI

def ask_jamai(prompt):
    jamai = JamAI(api_key="jamai_pat_49188da586bc90838807d00bb0d2ce9b585633f7d9ab07ca")
    return jamai.chat(prompt)

