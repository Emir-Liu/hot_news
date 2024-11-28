import time

import schedule

from duckducksearch import duck_search, save_search_res

def daily_func():
    querys = ['AI科技','纺织']
    for query in querys:
        search_res = duck_search(query=query)
        save_search_res(query=query, data=search_res)

schedule.every().day.at('01:00').do(daily_func)

while True:
    schedule.run_pending()  # 检查并运行已安排的任务
    time.sleep(50)  # 等待 50 秒
