import requests

class HeFeng():
    def __init__(self):
        self.url = "https://cdn.heweather.com/china-city-list.txt"
        self.encoding = "utf8"
        self.pre_request="https://free-api.heweather.net/s6/weather/now?location="
        self.sub_request="&key=2e6db1e6686547afb45e3ec1c2835478"

    def today_weather(self,city_code):
        dict = self.get_weather(city_code)
        print(dict["HeWeather6"][0]['now']['tmp'])

    def get_all_weather(self,count_of_cities):
        codes=self.get_city_code()
        i=0
        weathers=[]
        while i<count_of_cities:
            each=self.get_weather(next(codes))
            weathers.append(each)
            i=i+1
        return weathers

    def get_weather(self,city_code):
        url=self.pre_request+city_code+self.sub_request
        info=requests.get(url)
        info.encoding=self.encoding
        return info.json()


    def get_city_code(self):
        cities = self.get_cities()
        for each in cities:
            yield each[2:13]

    def get_cities(self):
        html = requests.get(self.url)
        html.encoding = self.encoding
        cities = html.text.split('\n')
        return cities[6:]


if __name__ == '__main__':
    hefeng = HeFeng()
    codes = hefeng.get_city_code()
    for i in range(10):
        hefeng.today_weather(codes.__next__())