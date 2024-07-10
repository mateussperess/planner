import uuid, pytest
from datetime import datetime, timedelta
from .participants_repository import ParticipantsRepository
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
email_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())
activity_id = str(uuid.uuid4())
participant_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco") # * passed
def test_record_participants():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants_infos = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": email_id,
        "name": "inserindo participante"
    }

    participants = participants_repository.record_participants(participants_infos)
    print()
    print(participants)

@pytest.mark.skip(reason="interacao com o banco") # * passed
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants = participants_repository.find_participants_from_trip(trip_id)
    print()
    print(participants)
