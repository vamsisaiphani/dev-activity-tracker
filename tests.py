from main import read_logs, write_log
import os

TEST_LOG = "2026-02-11 10:00:00,Testing,2,None,Testing logs\n"


def test_write_and_read():
    write_log(TEST_LOG)
    logs = read_logs()
    assert TEST_LOG in logs


def test_log_format():
    logs = read_logs()
    if logs:
        parts = logs[-1].split(",")
        assert len(parts) == 5


if __name__ == "__main__":
    test_write_and_read()
    test_log_format()
    print("✅ All tests passed")
