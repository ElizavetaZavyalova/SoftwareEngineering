db = db.getSiblingDB('trips');
db.createUser({
    user: 'trips_user',
    pwd: 'trips_pass',
    roles: [
        {
            role: 'readWrite',
            db: 'trips'
        }
    ]
});
db.createCollection("trips", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["driver", "trip", "passengers"],
            properties: {
                driver: {
                    bsonType: "object",
                    required: ["account_id", "first_name", "last_name", "patronymic", "phone_number", "requisites", "car_number"],
                    properties: {
                        account_id: {bsonType: "int"},
                        first_name: {bsonType: "string", pattern: "^[A-Za-zА-Яа-яЁё]{2,50}$"},
                        last_name: {bsonType: "string", pattern: "^[A-Za-zА-Яа-яЁё]{2,50}$"},
                        patronymic: {bsonType: "string", pattern: "^[A-Za-zА-Яа-яЁё]{2,50}$"},
                        phone_number: {bsonType: "string", pattern: "^\\+?\\d{10,15}$"},
                        requisites: {bsonType: "string"},
                        car_number: {bsonType: "string"}
                    }
                },
                trip: {
                    bsonType: "object",
                    required: ["title", "info"],
                    properties: {
                        title: {bsonType: "string"},
                        info: {bsonType: "object"}
                    }
                },
                passengers: {
                    bsonType: "array",
                    items: {
                        bsonType: "object",
                        required: ["account_id", "first_name", "last_name", "patronymic", "phone_number", "home_address"],
                        properties: {
                            account_id: {bsonType: "int"},
                            first_name: {bsonType: "string", pattern: "^[A-Za-zА-Яа-яЁё]{2,50}$"},
                            last_name: {bsonType: "string", pattern: "^[A-Za-zА-Яа-яЁё]{2,50}$"},
                            patronymic: {bsonType: "string", pattern: "^[A-Za-zА-Яа-яЁё]{2,50}$"},
                            phone_number: {bsonType: "string", pattern: "^\\+?\\d{10,15}$"},
                            home_address: {bsonType: "string"}
                        }
                    }
                }
            }
        }
    },
    validationLevel: "strict",
    validationAction: "error"
});
db.trips.createIndex({ "driver.account_id": 1 })
db.trips.createIndex({ "passengers.account_id": 1 })
db.trips.createIndex({ "trip.title": 1 })