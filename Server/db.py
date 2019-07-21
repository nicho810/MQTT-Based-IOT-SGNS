import sqlite3
import time


def creat_table_time():
    conn = sqlite3.connect('ioseed_sensor_node_1.db')
    print("Opened database successfully")
    c = conn.cursor()
    c.execute('''CREATE TABLE sensor_data
           ( TIME PRIMARY KEY     NOT NULL,
           TEMPERATURE     INT    NOT NULL,
           PRESSURE        INT    NOT NULL,
           HUMIDITY        INT    NOT NULL,
           GAS             INT    NOT NULL,
           LIGHT           INT    NOT NULL,
           SOLID           INT    NOT NULL
           );''')
    print("Table created successfully")
    conn.commit()
    conn.close()


def creat_table_hour():
    conn = sqlite3.connect('ioseed_sensor_node_1.db')
    print("Opened database successfully")
    c = conn.cursor()
    c.execute('''CREATE TABLE sensor_data_hour
           ( TIME PRIMARY KEY     NOT NULL,
           TEMPERATURE     INT    NOT NULL,
           PRESSURE        INT    NOT NULL,
           HUMIDITY        INT    NOT NULL,
           GAS             INT    NOT NULL,
           LIGHT           INT    NOT NULL,
           SOLID           INT    NOT NULL
           );''')
    print("Table created successfully")
    conn.commit()
    conn.close()


def creat_table_day():
    conn = sqlite3.connect('ioseed_sensor_node_1.db')
    print("Opened database successfully")
    c = conn.cursor()
    c.execute('''CREATE TABLE sensor_data_day
           ( TIME PRIMARY KEY     NOT NULL,
           TEMPERATURE     INT    NOT NULL,
           PRESSURE        INT    NOT NULL,
           HUMIDITY        INT    NOT NULL,
           GAS             INT    NOT NULL,
           LIGHT           INT    NOT NULL,
           SOLID           INT    NOT NULL
           );''')
    print("Table created successfully")
    conn.commit()
    conn.close()


def insert_value(insert_data="{0,1,2,3,4,5}"):
    command_text = "INSERT INTO sensor_data (TIME,TEMPERATURE,PRESSURE,HUMIDITY,GAS,LIGHT,SOLID) VALUES (" + get_currentTime() + "," + insert_data[1:-1] + ")"
    conn = sqlite3.connect('ioseed_sensor_node_1.db')
    print("Opened database successfully")
    c = conn.cursor()
    c.execute(command_text)
    conn.commit()
    print("Records created successfully" + "  at:" + get_currentTime())
    conn.close()


def do_db_select(command_text="null"):
    conn = sqlite3.connect('ioseed_sensor_node_1.db')
    # print("Opened database successfully")
    c = conn.cursor()
    c.execute(command_text)
    return_value = c.fetchall()
    conn.commit()
    conn.close()
    return return_value


def do_select_latest_sensordata():
    # command_text = "SELECT TIME,TEMPERATURE,PRESSURE,HUMIDITY,GAS,LIGHT,SOLID FROM sensor_data"
    command_text_0 = "SELECT max(TIME) FROM sensor_data"
    command_text = "SELECT TIME,TEMPERATURE,PRESSURE,HUMIDITY,GAS,LIGHT,SOLID FROM sensor_data WHERE  TIME=" + str(do_db_select(command_text_0))[2:-3]
    return do_db_select(command_text)


def do_update_average_date_hour(which_data=20190406180000):
    data_start = which_data
    data_end = which_data + 10000
    Temperature_avg = "SELECT avg(TEMPERATURE) FROM sensor_data WHERE TIME >=" + str(data_start) + " AND TIME <" + str(data_end)
    pressure_avg = "SELECT avg(PRESSURE) FROM sensor_data WHERE TIME >=" + str(data_start) + " AND TIME <" + str(data_end)
    humidity_avg = "SELECT avg(HUMIDITY) FROM sensor_data WHERE TIME >=" + str(data_start) + " AND TIME <" + str(data_end)
    gas_avg = "SELECT avg(GAS) FROM sensor_data WHERE TIME >=" + str(data_start) + " AND TIME <" + str(data_end)
    light_avg = "SELECT avg(LIGHT) FROM sensor_data WHERE TIME >=" + str(data_start) + " AND TIME <" + str(data_end)
    solid_avg = "SELECT avg(SOLID) FROM sensor_data WHERE TIME >=" + str(data_start) + " AND TIME <" + str(data_end)
    insert_data = str(int(do_db_select(Temperature_avg)[0][0])) + "," + str(int(do_db_select(pressure_avg)[0][0])) + "," + str(int(do_db_select(humidity_avg)[0][0])) + "," + str(int(do_db_select(gas_avg)[0][0])) + "," + str(int(do_db_select(light_avg)[0][0])) + "," + str(int(do_db_select(solid_avg)[0][0]))
    command_text = "INSERT INTO sensor_data_hour (TIME,TEMPERATURE,PRESSURE,HUMIDITY,GAS,LIGHT,SOLID) VALUES (" + str(which_data) + "," + insert_data + ")"
    conn = sqlite3.connect('ioseed_sensor_node_1.db')
    # print("Opened database successfully")
    c = conn.cursor()
    c.execute(command_text)
    conn.commit()
    print("Records created successfully" + "  at:" + get_currentTime())
    conn.close()


def do_update_average_date_day(which_data=20190406000000):
    data_start = which_data
    data_end = which_data + 1000000
    Temperature_avg = "SELECT avg(TEMPERATURE) FROM sensor_data_hour WHERE TIME >=" + str(data_start) + " AND TIME <" + str(data_end)
    pressure_avg = "SELECT avg(PRESSURE) FROM sensor_data_hour WHERE TIME >=" + str(data_start) + " AND TIME <" + str(data_end)
    humidity_avg = "SELECT avg(HUMIDITY) FROM sensor_data_hour WHERE TIME >=" + str(data_start) + " AND TIME <" + str(data_end)
    gas_avg = "SELECT avg(GAS) FROM sensor_data_hour WHERE TIME >=" + str(data_start) + " AND TIME <" + str(data_end)
    light_avg = "SELECT avg(LIGHT) FROM sensor_data_hour WHERE TIME >=" + str(data_start) + " AND TIME <" + str(data_end)
    solid_avg = "SELECT avg(SOLID) FROM sensor_data_hour WHERE TIME >=" + str(data_start) + " AND TIME <" + str(data_end)
    insert_data = str(int(do_db_select(Temperature_avg)[0][0])) + "," + str(int(do_db_select(pressure_avg)[0][0])) + "," + str(int(do_db_select(humidity_avg)[0][0])) + "," + str(int(do_db_select(gas_avg)[0][0])) + "," + str(int(do_db_select(light_avg)[0][0])) + "," + str(int(do_db_select(solid_avg)[0][0]))
    command_text = "INSERT INTO sensor_data_day (TIME,TEMPERATURE,PRESSURE,HUMIDITY,GAS,LIGHT,SOLID) VALUES (" + str(which_data) + "," + insert_data + ")"
    conn = sqlite3.connect('ioseed_sensor_node_1.db')
    # print("Opened database successfully")
    c = conn.cursor()
    c.execute(command_text)
    conn.commit()
    print("Records created successfully" + "  at:" + get_currentTime())
    conn.close()


def get_currentTime():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())


if __name__ == '__main__':
    pass


