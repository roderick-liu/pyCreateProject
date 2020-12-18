import pytest
if __name__ == '__main__':
    pytest.main("-s {{ name }}")


class Test_{{classname}}:
    def setup(self):
        print("------->setup")
