workspace "Name" "Description" {
    !identifiers hierarchical
    model {
        user = person "Пользователь" {
            tags "User"
        }
        driver = person "Водитель" {
            tags "Driver"
        }
        authorizationSistem = SoftwareSystem "Система Авторизации" {
            authorization = container "Сервис авторизации"
        }
        driveSistem = SoftwareSystem "Система Поездок" {
            driverFounder =  container "Сервис поиска ближайших водителей"
            bd =  container "Поездки"{
                tags "RDBMS"
            }
        }
        paySistem = SoftwareSystem "Система Оплаты" {
            payment =  container "Сервис оплаты поездки"
            bd =  container "Хранилище информации о Счете"{
                tags "RDBMS"
            }
        }

        user -> authorizationSistem "авторизируется"
        driver -> authorizationSistem "авторизируется"
        paySistem.bd -> authorizationSistem.authorization "Получание доступа к номеру счета"

        user -> driveSistem "Отправляет геолокацию"
        driver -> driveSistem "Отправляет геолокацию"
        driveSistem.driverFounder -> user "Отправляет список ближайших водителей"
        driveSistem.driverFounder -> driver "Добавляет информацию о пользователе"

        driveSistem.driverFounder -> driveSistem.bd "информация о водители и поездке"

        driveSistem.bd -> paySistem.payment "Получает информацию о поездке"
        paySistem.payment -> paySistem.bd "Отправляет информацию о платеже"

    }
    views {
        systemContext driveSistem "DriveSistem" {
            include *
            autolayout lr
        }
        container driveSistem "DriveSistemWorks" {
            include *
            autolayout lr
        }
        systemContext authorizationSistem "AuthorizationSistem" {
            include *
            autolayout lr
        }
        container authorizationSistem "AuthorizationSistemWorks" {
            include *
            autolayout lr
        }
        systemContext paySistem "PaySistem" {
            include *
            autolayout lr
        }
        container paySistem "PaySistemWorks" {
            include *
            autolayout lr
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
                background #2F4F4F
                color #ffffff
                shape robot
            }
            element "RDBMS" {
                background #2F4F4F
                color #ffffff
                shape cylinder
            }
        }
    }
}