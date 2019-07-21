from flask import Flask
from flask import render_template
import db

data_currently_sensorData = [0, 103, 203, 303, 403, 503, 603, 0, 0]
#  Temperature,pressure,humidity,gas,light,solid
data_chart_temp = [0, 24, 26, 31, 25, 24, 27, 28]
data_chart_light = [0, 62, 36, 25, 67, 89, 45, 34]
data_chart_humi = [0, 56, 53, 64, 53, 67, 76, 42]
data_chart_x_axis = ["0", "0401", "0402", "0403", "0404", "0405", "0406", "Today"]

# Get latest sensor data from database
for i in range(7):
    latest_data = db.do_select_latest_sensordata()[0]
    data_currently_sensorData[i] = latest_data[i]

# Get latest hour data from database
def get_latest_chart_data_from_database():
    latest_data_time = str(db.do_db_select("SELECT max(TIME) FROM sensor_data_hour"))[2:-3]
    latest_data_time = latest_data_time[4:-6]
    print(latest_data_time)



app = Flask(__name__)


@app.route('/')
def hello(sensorData=data_currently_sensorData, chart_temp=data_chart_temp, chart_light=data_chart_light,
          chart_humi=data_chart_humi, chart_day=data_chart_x_axis):
    return render_template('main.html', t_data_currently_sensorData=sensorData, t_data_chart_temp=chart_temp,
                           t_chart_light=chart_light, t_chart_humi=chart_humi, t_chart_day=chart_day)


if __name__ == '__main__':
    app.run()



