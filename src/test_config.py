import pytest
if __name__ == '__main__':
    pytest.main("-s test_config.py")


class Test_Config:
    def setup(self):
        print("------->setup")
    def test___init__(self):
        pass

    def test_write_conf(self):
        pass

    def test_read_keyfile(self):
        pass

    def test_update_conf(self):
        pass

