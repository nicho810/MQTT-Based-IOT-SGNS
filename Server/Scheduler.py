from apscheduler.schedulers.blocking import BlockingScheduler
import db
import time


def job_insert_hour():
    db.do_update_average_date_hour(int(str(get_currentTime_hour()) + "0000"))


def job_insert_day():
    db.do_update_average_date_day(int(str(get_currentTime_day()) + "000000"))


def get_currentTime_hour():
    return time.strftime("%Y%m%d%H", time.localtime())


def get_currentTime_day():
    return time.strftime("%Y%m%d", time.localtime())


def do_scheduler():
    sched = BlockingScheduler()
    sched.add_job(job_insert_hour, 'interval', minutes=60)
    sched.add_job(job_insert_day, 'interval', hours=24)
    sched.start()


if __name__ == '__main__':
    do_scheduler()

