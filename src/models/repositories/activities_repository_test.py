import uuid, pytest
from datetime import datetime, timedelta
from .activities_repository import ActivitiesRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
email_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())
activity_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco") # * passed
def test_record_activity():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities_trips_infos = {
        "id": activity_id,
        "trip_id": trip_id,
        "title": "um role legal",
        "occurs_at": "01-07-2024"
    }

    activities = activities_repository.record_activity(activities_trips_infos)
    print()
    print(activities_trips_infos)

@pytest.mark.skip(reason="interacao com o banco") # * passed
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities = activities_repository.find_activities_from_trip("740300bb-8bb9-4928-90e6-f24c2660dd9c")
    print()
    print(activities)
