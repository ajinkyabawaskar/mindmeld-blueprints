# -*- coding: utf-8 -*-
"""This module contains a Travel Assistant MindMeld application"""
from travel_assistant.root import app

# import files 
import travel_assistant.general
import travel_assistant.travel
import travel_assistant.accommodation
import travel_assistant.recommendations

__all__ = ['app']

@app.handle(default=True)
def default(request, responder):
    """
    This is a default handler.
    """
    replies = ["Could you please be more clear?",
    "Didn't get you there, maybe say it a bit differently?"]
    responder.reply(replies)