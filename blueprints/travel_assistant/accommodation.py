"""
This file has handlers for all intents in the accommodation domain.
"""

from .root import app

@app.handle(intent='get_hotel_availability')
def send_hotel_availability(request, responder):
    """
    When the user asks for accommodations (hotels, homestays, etc) then 
    invoke AutoFill to get all the entities required to proceed with 
    fulfilling the intent.
    """
    responder.reply("Here is hotel availability")