from jamai import JamAI

def ask_jamai(prompt):
    jamai = JamAI(api_key="YOUR_JAMAI_KEY")
    return jamai.chat(prompt)

