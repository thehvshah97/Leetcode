from datetime import date

class DaysBetweenDates:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        s1 = date1.split("-")
        s2 = date2.split("-")


if __name__ == '__main__':
    obj = DaysBetweenDates()
    print(obj.daysBetweenDates("2020-01-29", "2019-06-30"))



