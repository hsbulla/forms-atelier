import eel, sqlite3

eel.init('../markup-forms')

@eel.expose
def processOrderDetails(orderDetails):
    data_api_to_DB = orderDetails
    lines = data_api_to_DB.split(',\n')
    data_dict = {}
    for line in lines:
        key, value = line.split(': ')
        key = key.strip()
        value = value.strip()
        data_dict[key] = value
    manager = data_dict['Менеджер']
    lastName = data_dict['Фамилия']
    firstName = data_dict['Имя']
    middleName = data_dict['Отчество']
    measurements = data_dict['Измерения']
    fabricType = data_dict['Тип ткани']
    deliveryOption = data_dict['Способ доставки']


    sqlite_connection = sqlite3.connect('../../web-container/backend-container/forms/db.sqlite3')
    cursor = sqlite_connection.cursor()
    sqlite_insert_with_param = """INSERT INTO forms_atelier_data
                              (manager, lastName, firstName, middleName, measurements, fabricType, deliveryOption)
                              VALUES (?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (manager, lastName, firstName, middleName, measurements, fabricType, deliveryOption)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    sqlite_connection.commit()

eel.start('index.html')


