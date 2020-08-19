import fire
import os 


# class Calculator(object):
#     """A simple calculator class."""
#     def hello(self, name="World"):
#         return "Hello %s!" % name

#     def double(self, number):
#         return 2* number


class Comands(object):
    """Main commands ...."""
    def data(self):
        """ List data dir ...."""
        os.chdir("data")
        print(os.listdir())

    def tarin(self):
        """
        print tarin process
        """
        print("tarin process .....")

    def result(self):
        """
        print result
        """
    def score(self):
        """
        print score
        """

    def log(self):
        """
        print current log
        """
        os.chdir("logs")
        print("logs....")

    def test(self):
        """
        test process
        """


if __name__ == '__main__':
    fire.Fire(Comands)
