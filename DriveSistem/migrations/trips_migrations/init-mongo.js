db = db.getSiblingDB('trips');

// создаём пользователя с правами на базу (если нужно)
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
db.createCollection('trips');