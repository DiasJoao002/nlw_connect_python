from flask import Blueprint, jsonify, request

event_route_bp = Blueprint("event_route", __name__)

from src.http_types.http_request import HttpRequest
from src.validators.events_creator_validator import events_creator_validator
from src.controllers.events.events_creator import EventsCreator
from src.model.repositories.eventos_repository import EventosRepository

@event_route_bp.route("/event", methods=["POST"])

def create_new_event():
    events_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    eventos_repo = EventosRepository()
    events_creator = EventsCreator(eventos_repo)

    htttp_response = events_creator.create(http_request)

    # retorna um body e um status code
    return jsonify(htttp_response.body), htttp_response.status_code