"""
This file has handlers for all intents in the travel domain.
"""

from .root import app

@app.handle(intent='get_flights')
def send_flights(request, responder):
    """
    When the user asks for flights, invoke the AutoFill
    to get required entities required in order to fulfill the intent.
    """
    responder.reply("Here are your flights!")