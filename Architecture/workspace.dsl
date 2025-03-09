workspace "Name" "Description" {
    !identifiers hierarchical
    model {
        user = person "Пользователь" {
            tags "User"
        }
        driver = person "Водитель" {
            tags "Driver"
        }
        authorization = softwareSystem "Сервис авторизации"
        drive = softwareSystem "Сервис поездок"
        route = softwareSystem "Сервис поиска путей"
        payment = softwareSystem "Сервис оплаты поездки"
        user -> payment "оплачивает поездку"
        payment -> driver "начисляет деньги водителю"

        user -> authorization "авторизируется"
        driver -> authorization "авторизируется"

        driver -> drive "Добавляет/Удаляет информацию о поездке"

        user -> route "Ищет маршрут"

    }

    views {
        systemContext authorization "Authorization" {
            include *
            autolayout lr
        }
        systemContext payment "Payment" {
            include *
            autolayout lr
        }
        systemContext drive "Drive" {
            include *
            autolayout lr
        }
        systemContext route "Route" {
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
        }
    }
}