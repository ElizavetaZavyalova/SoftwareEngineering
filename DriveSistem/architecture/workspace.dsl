workspace "Name" "Description" {
    !identifiers hierarchical
    model {
        passenger = person "Пасажир" {
            tags "PASSENGER"
        }
        driver = person "Водитель" {
            tags "DRIVER"
        }
        admin = person "Администратор"{
            tags "ADMIN"
        }
        email = SoftwareSystem "Email" {
            tags  EMAIL
        }
        passengerAccountSystem = SoftwareSystem "Система Аккаунтов пассажиров" {
            tags ACCOUNT
            passengerDB = container "База данных пользователей" {
                tags RDBMS
            }
            passengerAccount = container "Сервис информации об аккаунте пасажира" {
                tags REGISTER
            }
            passengerRedis = container "Хранилище ключей регистрации пасажиров" {
                tags REDIS
            }
            passengerCash = container "Кеш пасажиров" {
                tags REDIS
            }
        }
        driverAccountSystem = SoftwareSystem "Система Аккаунтов водителей" {
            driverCash = container "Кеш водителей" {
                tags REDIS
            }
            driverRedis = container "Хранилище ключей регистрации водителей" {
                tags REDIS
            }
            driverAccount = container "Сервис информации об аккаунте водителя" {
                tags REGISTER
            }
            driverDB = container "База данных водителей" {
                tags RDBMS
            }
        }
        adminSystem = SoftwareSystem "Система администрирования" {
            tags ADMIN
            adminestration = container "Сервис администрирования" {
                tags ADMINISTRATION
            }
        }
        tripsSystem = SoftwareSystem "Система Поездок" {
            tags TRIPS_SISTEM
            addingTrip = container "Сервис добавления поездок" {
                tags FINDER
            }
            connectTrip = container "Сервис добаления маршрутов" {
                tags ROUTE
            }
            tripsDB = container "База данных поездок" {
                tags MONGO
            }
        }
        admin -> adminSystem.adminestration "Получает доступ ко всем базам данных системы"
        adminSystem.adminestration -> passengerAccountSystem.passengerDB "Получение информации об аккаунтах"
        adminSystem.adminestration -> driverAccountSystem.driverDB "Получение информации об аккаунтах"
        adminSystem.adminestration -> tripsSystem.tripsDB "Получение информации о поезках"

        passenger -> passengerAccountSystem.passengerAccount "Регистрация/Вход в акаунт"
        passengerAccountSystem.passengerAccount -> passengerAccountSystem.passengerDB "Редактирование данных акаунта"
        passengerAccountSystem.passengerAccount -> passengerAccountSystem.passengerRedis "Получение кода подтверждения подлиности email"
        passengerAccountSystem.passengerAccount -> passengerAccountSystem.passengerCash "Keширование информации об аккаунте"
        passengerAccountSystem.passengerAccount -> email "Отправка кода подтверждения"
        passenger -> email "Чтение письма с кодом подтверждения email"

        driver -> driverAccountSystem.driverAccount "Регистрация/Вход в акаунт"
        driverAccountSystem.driverAccount -> driverAccountSystem.driverDB "Редактирование данных акаунта"
        driverAccountSystem.driverAccount -> driverAccountSystem.driverRedis "Получение кода подтверждения подлиности email"
        driverAccountSystem.driverAccount -> driverAccountSystem.driverCash "Keширование информации об аккаунте"
        driverAccountSystem.driverAccount -> email "Отправка кода подтверждения"
        driver -> email "Чтение письма с кодом подтверждения email"

        driver ->  tripsSystem.addingTrip "Добавление новой поездки"
        tripsSystem.addingTrip -> tripsSystem.tripsDB "Получение информации о поездке"
        tripsSystem.addingTrip -> driverAccountSystem.driverDB "Получение инфлормации об аккаунте"

        passenger ->  tripsSystem.connectTrip "Подключение к поездке"
        tripsSystem.connectTrip -> tripsSystem.tripsDB "Получение информации о поездке"
        tripsSystem.connectTrip -> passengerAccountSystem.passengerDB "Получение инфлормации об аккаунте"


    }
    views {
        systemContext tripsSystem "TripsSystem" {
            include *
        }
        container tripsSystem "TripsSystemWorks" {
            include *
        }
        systemContext adminSystem  "AdminSystem" {
            include *
        }
        container adminSystem  "AdminSystemWorks" {
            include *
        }
        systemContext passengerAccountSystem "passengerAccountSystem" {
            include *
        }
        container passengerAccountSystem "passengerAccountSystemWorks" {
            include *
        }
        systemContext driverAccountSystem "driverAccountSystem" {
            include *
        }
        container driverAccountSystem "driverAccountSystemWorks" {
            include *
        }
        styles {
            element "Software System" {
                background #008000
                color #ffffff
                shape RoundedBox
            }
            element "PASSENGER" {
                background #D2B48C
                color #ffffff
                shape person
            }
            element "DRIVER" {
                background #696969
                color #ffffff
                shape robot
            }
            element "ADMIN" {
                background #696969
                color #ffffff
                shape RoundedBox
            }
            element "EMAIL" {
                background #696969
                color #ffffff
                shape RoundedBox
            }
            element "RDBMS" {
                background #696969
                color #ffffff
                shape cylinder
            }
            element "MONGO" {
                background #2F4F4F
                color #ffffff
                shape cylinder
            }
            element "REDIS" {
                background #2F4F4F
                color #ffffff
                shape cylinder
            }
        }
    }
}