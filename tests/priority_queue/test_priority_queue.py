from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    file_process_mock_1 = {
        'qtd_linhas': 3
    }
    file_process_mock_2 = {
        'qtd_linhas': 6
    }
    queue = PriorityQueue()

    queue.enqueue(file_process_mock_1)
    assert len(queue.high_priority) == 1
    assert len(queue.regular_priority) == 0

    queue.enqueue(file_process_mock_2)
    assert len(queue.high_priority) == 1
    assert len(queue.regular_priority) == 1

    search1 = queue.search(0)
    search2 = queue.search(1)
    assert search1 == file_process_mock_1
    assert search2 == file_process_mock_2

    queue.dequeue()
    assert len(queue.high_priority) == 0
    assert len(queue.regular_priority) == 1

    queue.dequeue()
    assert len(queue.high_priority) == 0
    assert len(queue.regular_priority) == 0

    with pytest.raises(IndexError):
        queue.search(0)
