"""
This file has handlers for all intents in the recommendations domain.
"""

from .root import app

@app.handle(intent='by_experiences')
def send_recommendations_by_experience(request, responder):
    """
    When the user asks for recommendations relating to having 
    a particular experience, get the locations that provide the asked experience
    and reply with proper natural language response.
    """
    responder.reply("Visit location A for experience B.")