workspace "Name" "Description" {
    !identifiers hierarchical
    model {
        user = person "Пользователь" {
            tags "User"
        }
        driver = person "Водитель" {
            tags "Driver"
        }
        paySistem = SoftwareSystem "Система Платежей" {
            tags PAY_SISTEM
            authorization = container "Сервис авторизации"{
                tags AUTORIZATION
            }
            payment =  container "Сервис оплаты поездки"{
                tags PAY
            }
            paybd =  container "База данных платежей"{
                tags RDBMS
            }
        }
        driveSistem = SoftwareSystem "Система Поездок" {
            tags DRIVE_SISTEM
            driverFounder =  container "Сервис поиска ближайших водителей"{
                tags FINDER
            }
            addingRoute =  container "Сервис добаления маршрутов"{
                tags ROUTE
            }
            connectingTrips =  container "Сервис подключения к поездке"{
                tags TRIPS
            }
            bd =  container "База данных поездок"{
                tags RDBMS
            }
        }

        user -> paySistem.authorization "авторизируется"
        driver -> paySistem.authorization "авторизируется"
        paySistem.authorization -> paySistem.paybd "Получение доступа к счету"

        driver -> driveSistem.addingRoute "Добавляет/Удаляет информацию о маршруте"
        driveSistem.addingRoute -> driveSistem.bd "Запись информации о маршрутах"

        user -> driveSistem.driverFounder "Ищет ближайших водителей"
        driveSistem.driverFounder -> driveSistem.bd "Использует данные о поездках"

        user -> driveSistem.connectingTrips "Подключается к поездке"

        driveSistem.connectingTrips -> driver "Отпраляет сообщение водителю"
        driveSistem.connectingTrips -> paySistem.payment "Оплата поездки"
        driveSistem.connectingTrips -> driveSistem.bd "Добавляет информацию о новой поездке"

        paySistem.payment -> paySistem.paybd "Произведение платежа"


    }
    views {
        systemContext driveSistem "DriveSistem" {
            include *
        }
        systemContext paySistem "PaySistem" {
            include *
        }
        container driveSistem "DriveSistemWorks" {
            include *
        }
        container paySistem "PaySistemWorks" {
            include *
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
            element "AUTORIZATION" {
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
            element "PAY_SISTEM" {
                background #6495ed
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