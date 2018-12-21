from asgiref.sync import async_to_sync
from asyncio import sleep
from celery import Celery
from celery.task import periodic_task

app = Celery()
app.conf.result_backend = 'db+sqlite:///results.sqlite'
app.conf.broker_url = 'redis://'
app.conf.result_backend = 'cache+memcached://localhost:11211/'


async def return_hello():
    await sleep(1)
    return 'hello'


@periodic_task(
    run_every=2,
    name='return_hello',
)
def task_return_hello():
    async_to_sync(return_hello)()
