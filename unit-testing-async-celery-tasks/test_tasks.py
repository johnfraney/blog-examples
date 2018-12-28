import pytest
from asyncio import sleep
from unittest.mock import patch

from tasks import return_hello, task_return_hello


@pytest.mark.asyncio
async def test_return_hello():
    result = await return_hello()
    assert result == 'hello'


@patch('tasks.return_hello')
def test_task_return_hello(return_hello_mock):
    """Ensure the task runs in Celery and calls the correct function."""
    task_return_hello.apply()
    assert return_hello_mock.called
