from typing import Dict
from src.drivers.email_sender import send_email 
import uuid

class TripCreator:
    def __init__(self, __trip_repository, __emails_repository) -> None:
        self.__trip_repository = __trip_repository
        self.__emails_repository = __emails_repository
    
    def create(self, body) -> Dict:
        try:
            emails = body.get("emails_to_invite")
            trip_id = str(uuid.uuid4())

            trip_infos = { **body, "id": trip_id }
            self.__trip_repository.create_trip(trip_infos)
            
            if emails:
                for email in emails:
                    self.__emails_repository.record_emails({
                        "email": email,
                        "trip_id": trip_id,
                        "id": str(uuid.uuid4()),
                    })
                    
            send_email(
                [body["owner_email"]], 
                f"http://localhost:3000/trips/{trip_id}/confirm"
            )
            
            return {
                "body": { "id": trip_id },
                "status_code": 201
            }
        
        except Exception as exception:
            return {
                "body": { "error" : "bad request", "message": str(exception)},
                "status_code": 400
            }


        
        