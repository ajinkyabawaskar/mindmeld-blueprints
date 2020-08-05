from .root import app

@app.handle(intent='greet')
def welcome(request, responder):
    responder.reply("Hi, I am your travel assistant. Ask me about places to visit "
                    ", check for hotels and homestays or find flights for you. "
                    "You can say 'Find me a flight from Mumbai to Pune' or "
                    "Standard suites in Novotel Juhu?")

@app.handle(intent='confirm')
def confirm_action(request, responder):
    """
    When the user tries to confirm an action, no the necessary set of operations 
    and respond accordingly.
    """
    responder.reply("Confirmed!")

@app.handle(intent='help')
def provide_help(request, responder):
    """
    When the user asks for help, provide some sample queries they can try.
    """
    # Respond with examples demonstrating how the user can ask for flights from different locations.
    # For simplicity, we have a fixed set of demonstrative queries here, but they could also be
    # randomly sampled from a pool of example queries each time.
    replies = ["You can ask me to check flights for you.", "You can ask me to find hotels for you.", "You can tell me what your interests are and I can suggest you places to visit."]
    responder.reply(replies)

@app.handle(intent='exit')
def say_goodbye(request, responder):
    """
    When the user ends a conversation, clear the dialogue frame and say goodbye.
    """
    # Clear the dialogue frame to start afresh for the next user request.
    responder.frame = {}
    responder.reply(["Bye!", "GoodBye!", "Later.", "Have a nice day!"])

@app.handle(intent='unsupported')
def say_unsupported(request, responder):
    """
    When the user asks an unrelated question, convey the lack of understanding for the requested
    information and prompt to return to planning travel.
    """
    replies = ["Sorry, I couldn't understand it. You can ask me about hotels, flights or experiences that you want to have."]
    responder.reply(replies)
