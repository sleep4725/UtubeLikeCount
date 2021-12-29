from selenium import webdriver

class SeleinumObject:

    @classmethod
    def ret_chrome_object(cls, chrome_file_path=None):
        """

        :return:
        """
        options = webdriver.ChromeOptions()
        options.headless = True

        if chrome_file_path:
            chrome = webdriver.Chrome(chrome_file_path, options=options)
            return chrome
        else:
            raise FileNotFoundError