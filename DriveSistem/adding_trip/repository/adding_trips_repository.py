from http import client
from http.client import HTTPException

from bson import ObjectId
from pymongo import MongoClient

from adding_trip.entity.driver.rest.driver import DriverInfo
from adding_trip.entity.trips.db.trip import TripDB
from adding_trip.entity.trips.trip import TripDescription, create_trip_description


class AddingTripsRepository:
    _TRIPS_COLLECTION = 'trips'

    def __init__(self, url: str):
        self.client = MongoClient(url)
        self.db = self.client['trips']
        self.collection = self.db['trips']

    def create_trip(self, trip_info: TripDescription, driver: DriverInfo):
        trip = create_trip_description(trip_info=trip_info, driver=driver)
        result = self.collection.insert_one(trip.model_dump(exclude_none=True, by_alias=True))
        return result.inserted_id

    def get_all_trips(self, driver: DriverInfo):
        trips_collection = self.collection.find({"driver": driver.model_dump(exclude_none=True, by_alias=True)})
        trips = []
        for trip in trips_collection:
            trip["id"] = str(trip.pop("_id"))
            trips.append(TripDB(**trip).model_dump(exclude_none=True, by_alias=True))
        return trips

    def get_trip(self, id: str, driver: DriverInfo)->TripDB:
        result = self.collection.find_one({"_id": ObjectId(id),
                                        "driver": driver.model_dump(exclude_none=True, by_alias=True)})
        if result is None:
            raise HTTPException(status_code=400, detail="Not Found")
        result["id"] = str(result.pop("_id"))
        return TripDB(**result)

    def update_trip_info(self, id: str, trip_info: TripDescription, driver: DriverInfo):
        result = self.collection.update_one(
            {"_id": ObjectId(id),
            "driver": driver.model_dump(exclude_none=True, by_alias=True)},
            {"$set": {"trip": trip_info.model_dump(exclude_none=True, by_alias=True)}}
        )
        if result.modified_count == 0:
            raise HTTPException(status_code=400, detail="Not Found")
        return result.modified_count

    def delete_trip(self, id: str, driver: DriverInfo):
        result = self.collection.delete_one({"_id": ObjectId(id),
                                            "driver": driver.model_dump(exclude_none=True, by_alias=True)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=400, detail="Not Found")
        return result.deleted_count
