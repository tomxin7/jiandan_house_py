import tomxin.tx_mysql

class Record(object):
    id = ""
    city_name = ""
    key_word = ""
    remind = ""
    remind_type = ""

    def __init__(self, id, city_name, key_word, remind, remind_type):
        self.id = id
        self.city_name = city_name
        self.key_word = key_word
        self.remind = remind
        self.remind_type = remind_type


def get_record(city):
    recordList = []
    user_sql = "select id,city_name,key_word,remind,remind_type from record where city_name = " + "'" + city + "' and status = 1"
    results = tomxin.tx_mysql.select(user_sql)
    for row in results:
        record = Record(row[0], row[1], row[2], row[3], row[4])
        recordList.append(record)
    return recordList