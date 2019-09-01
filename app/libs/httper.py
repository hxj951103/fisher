import requests


class HTTP:
    """
    继承 object写不写有没有区别
    python3 没有区别
    python2  经典类和新式类区别 较多
    """
    @staticmethod
    def get(url, return_json= True):
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json() if return_json else resp.text

        return {} if return_json else ""
