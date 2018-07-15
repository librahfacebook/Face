'''
每天定时更新数据库，使其打卡记录置为0
'''
import datetime, platform, time
from UserManage import *


def run_Task():
    os_platform = platform.platform()
    if os_platform.startswith('Window'):
        update_Data()
    elif os_platform.startswith('Darwin'):
        update_Data()


def update_Data():
    dbHelper = DBHelper()
    sql = "update record set success=0"
    result = dbHelper.execute(sql, None)
    if result:
        print('更新成功')
    else:
        print('更新失败')
    time.sleep(60)


def timerRun(h, m):
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour == h and now.minute == m:
                break
            time.sleep(20)
        run_Task()
        print('已更新数据库...')
