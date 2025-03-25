workspace "Name" "Description" {
    !identifiers hierarchical
    model {
        user = person "Пользователь" {
            tags "User"
        }
        driver = person "Водитель" {
            tags "Driver"
        }
        registerSistem = SoftwareSystem "Система Регистрации" {
            bdUser = container "База данных пользователей" {
                tags RDBMS
            }
            registration = container "Сервис регистрации" {
                tags REGISTER
            }
            bdDriver = container "База данных водителей" {
                tags RDBMS
            }
        }
        driveSistem = SoftwareSystem "Система Поездок" {
            tags DRIVE_SISTEM
            driverFounder = container "Сервис поиска ближайших водителей" {
                tags FINDER
            }
            addingRoute = container "Сервис добаления маршрутов" {
                tags ROUTE
            }
            connectingTrips = container "Сервис подключения к поездке" {
                tags TRIPS
            }
            approveConnectingTrips = container "Сервис подтверждения поездки" {
                tags APPROVE
            }
            bd = container "База данных поездок" {
                tags RDBMS
            }
        }
        driver ->  driveSistem.addingRoute "Добавление информации о местонахождении"
        driveSistem.addingRoute -> registerSistem.bdDriver "Проверка наличия в системе"
        driveSistem.addingRoute -> driveSistem.bd "Добавляет информацию о  местонахождении водителя"

        user -> driveSistem.driverFounder "Поиск ближайших водителей"
        driveSistem.driverFounder -> driveSistem.bd "Получение информации о  местонахождении свободных водителей"

        user -> driveSistem.connectingTrips "Запрос на приезд водителя"
        driveSistem.connectingTrips -> driver "Запрос на разрешение подключения"

        driver -> driveSistem.approveConnectingTrips "Подтверждение/отклонение подключения"
        driveSistem.approveConnectingTrips -> user "Информация о решении водителя"

        driveSistem.approveConnectingTrips -> driveSistem.bd "Обновление инфориации"
        driveSistem.driverFounder -> registerSistem.bdUser "Информация о пользователях"

        registerSistem.registration ->  registerSistem.bdUser "Регистрация как User"
        registerSistem.registration ->  registerSistem.bdDriver "Регистрация как Водитель"
        driver ->  registerSistem.registration "Регистрация"
        user ->  registerSistem.registration "Регистрация"
    }
    views {
        systemContext driveSistem "DriveSistem" {
            include *
        }
        container driveSistem "DriveSistemWorks" {
            include *
            exclude registerSistem
        }
        container registerSistem "RegisterSistemWorks" {
            include *
            exclude driveSistem
        }
        styles {
            element "Software System" {
                background #008000
                color #ffffff
                shape RoundedBox
            }
            element "User" {
                background #D2B48C
                color #ffffff
                shape person
            }
            element "Driver" {
                background #696969
                color #ffffff
                shape robot
            }
            element "RDBMS" {
                background #2F4F4F
                color #ffffff
                shape cylinder
            }
            element "FINDER" {
                background #008080
                color #ffffff
                shape RoundedBox
            }
            element "APPROVE" {
                background #2F4FFF
                color #ffffff
                shape RoundedBox
            }
            element "PAY" {
                background #FF4F4F
                color #ffffff
                shape RoundedBox
            }
            element "TRIPS" {
                background #FF4F4F
                color #ffffff
                shape RoundedBox
            }
            element "ROUTE" {
                background #9932cc
                color #ffffff
                shape RoundedBox
            }
            element "DRIVE_SYSTEM" {
                background #9932cc
                color #ffffff
                shape RoundedBox
            }
        }
    }
}