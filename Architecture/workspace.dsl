workspace "Name" "Description" {
    !identifiers hierarchical
    model {
        user = person "Пользователь" {
            tags "User"
        }
        driver = person "Водитель" {
            tags "Driver"
        }
        driveSistem = SoftwareSystem "Система Поездок" {
            driverFounder =  container "Сервис поиска ближайших водителей"{
                tags FINDER
            }
            authorization = container "Сервис авторизации"{
                tags AUTORIZATION
            }
            payment =  container "Сервис оплаты поездки"{
                tags PAY
            }
            bd =  container "База данных поездок"{
                tags RDBMS
            }
        }

        user -> driveSistem.authorization "авторизируется"
        driver -> driveSistem.authorization "авторизируется"

        driveSistem.authorization -> driveSistem.bd "Получание информации о юзере"
        driveSistem.driverFounder -> user "Отправляет список ближайших водителей"
        driver  -> driveSistem.driverFounder "Добавляет информацию о пользователе"

        driveSistem.driverFounder -> driveSistem.bd "информация о водители и поездке"

        driveSistem.payment -> driveSistem.bd "Оплата поездки"

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
            element "FINDER" {
                background #2FFF4F
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
        }
    }
}