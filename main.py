import requests
from bs4 import BeautifulSoup
import time

from seleniumClient.getSelenium import SeleinumObject

## ========================
# 작성자 : JunHyeon.Kim
# 작성일 : 2021-12-29
# t
## ========================
class Utube:

    def __init__(self):
        self.req_url = "https://youtu.be/MLajZlfSylw"
        self.chrome_client = SeleinumObject.ret_chrome_object(chrome_file_path="./chromedriver/chromedriver.exe")

    def get_utube_data(self):
        """

        :return:
        """
        self.chrome_client.get(self.req_url)
        time.sleep(3)

        html_source = self.chrome_client.page_source
        bs_object = BeautifulSoup(html_source, "html.parser")

        count = bs_object.select_one("span.view-count.style-scope.ytd-video-view-count-renderer")
        print(count.string)

    def __del__(self):
        try:
            self.chrome_client.quit()
        except:
            pass

if __name__ == "__main__":
    o = Utube()
    o.get_utube_data()