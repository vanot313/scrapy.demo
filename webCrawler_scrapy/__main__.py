from scrapy import cmdline
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import scrapy
from scrapy.crawler import CrawlerProcess
from webCrawler_scrapy.spiders import demo_spider


# TODO APScheduler 自动化管理

def spidertask(id):
    print("###id: " + id)

    # 创建一个CrawlerProcess对象
    process = CrawlerProcess()  # 括号中可以添加参数
    process.crawl(demo_spider)
    process.start()
    # cmdline.execute("scrapy crawl demo_spider".split())


def task_listener(event):
    if event.exception:
        print("tasks error")
    else:
        print("tasks finished")


# 配置调度器
jobstores = {
    'default': SQLAlchemyJobStore(url='mysql+pymysql://root:Ji1234@101.132.131.184/apscheduler?charset'
                                      '=utf8', tablename='api_job')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(10)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

if __name__ == "__main__":
    scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
    # 添加监听器
    scheduler.add_listener(task_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    scheduler.add_job(func=spidertask, args=['demo_spider', ], id='demo_spider', trigger='interval', seconds=1,
                      replace_existing=True)
    # 启动调度器
    scheduler.start()
