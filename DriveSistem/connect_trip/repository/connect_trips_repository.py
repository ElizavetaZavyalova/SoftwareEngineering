

from bson import ObjectId
from fastapi import HTTPException
from pymongo import MongoClient

from connect_trip.entity.passenger.rest.passenger import PassengerInfo
from connect_trip.entity.trips.db.trip import TripDB


class ConnectTripsRepository:
    _TRIPS_COLLECTION = 'trips'

    def __init__(self, url: str):
        self.client = MongoClient(url)
        self.db = self.client['trips']
        self.collection = self.db['trips']

    def connect_to_trip(self, id: str, passenger: PassengerInfo):
        result = self.collection.update_one(
            {"_id": ObjectId(id), "passengers": {"$not": {"$elemMatch": passenger.model_dump(exclude_none=True, by_alias=True)}}},
            {"$addToSet": {"passengers":passenger.model_dump(exclude_none=True, by_alias=True)}}
        )
        if result.modified_count == 0:
            raise HTTPException(status_code=400, detail="Not Found")
        return result.modified_count

    def cancel_trip(self,id: str,  passenger: PassengerInfo):
        result = self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$pull": {"passengers": passenger.model_dump(exclude_none=True, by_alias=True)}}
        )
        if result.modified_count == 0:
            raise HTTPException(status_code=400, detail="Not Found")
        return result.modified_count

    def get_connected_trip(self, id: str, passenger: PassengerInfo):
        trip = self.collection.find_one({
            "_id": ObjectId(id),
            "passengers": {
                "$elemMatch": {
                    "account_id": passenger.account_id
                }
            }
        })
        if trip is None:
            raise HTTPException(status_code=400, detail="Not Found")
        trip["id"] = str(trip.pop("_id"))
        return TripDB(**trip)

    def get_trips(self, title: str):
        trips_collection = self.collection.find({
            "trip.title": title
        })
        trips = []
        for trip in trips_collection:
            trip["id"] = str(trip.pop("_id"))
            trips.append(TripDB(**trip).model_dump(exclude_none=True, by_alias=True))
        return trips

    def get_connected_trips(self, passenger: PassengerInfo):
        trips_collection = self.collection.find({
            "passengers": {
                "$elemMatch": {
                    "account_id": passenger.account_id
                }
            }
        })
        trips = []
        for trip in trips_collection:
            trip["id"] = str(trip.pop("_id"))
            trips.append(TripDB(**trip).model_dump(exclude_none=True, by_alias=True))
        return trips