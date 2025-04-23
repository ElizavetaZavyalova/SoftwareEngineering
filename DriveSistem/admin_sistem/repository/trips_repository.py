from bson import ObjectId
from pymongo import MongoClient

from admin_sistem.entity.trips.mongo.trip import TripDB


class TripsRepository:
    _TRIPS_COLLECTION = 'trips'

    def __init__(self, url: str):
        self.client = MongoClient(url)
        self.db = self.client['trips']
        self.collection = self.db['trips']

    def get_all_trips(self):
        trips_collection = list(self.collection.find())
        trips = []
        for trip in trips_collection:
            trip["id"] = str(trip.pop("_id"))
            trips.append(TripDB(**trip).model_dump(exclude_none=True, by_alias=True))
        return trips

    def get_trips(self) -> list:
        return self.get_all_trips()

    def update_trip_info(self, id: str, updated_info: dict):
        result = self.collection.update_one({'_id': ObjectId(id)}, {'$set': updated_info})
        return result.modified_count > 0

    def delete_trip(self, id: str):
        result = self.collection.delete_one({'_id': ObjectId(id)})
        return result.deleted_count

    def get_trip(self, id: str):
        trip = self.collection.find_one({'_id': ObjectId(id)})
        trip["id"] = str(trip.pop("_id"))
        return trip

    def change_trip(self, id: str, trip: dict):
        result = self.collection.replace_one({'_id': ObjectId(id)}, trip)
        return result.modified_count

    def create_trip(self, trip: dict):
        result = self.collection.insert_one(trip)
        return str(result.inserted_id)
