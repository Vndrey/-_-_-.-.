import datetime

def day_of_week(day,month,year):
    week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    date = datetime.date(year, month, day)
    return week_days[date.weekday()]

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def calculate_age(year):
    today = datetime.date.today()
    age = today.year - year
    if today.month < month or (today.month == month and today.day < day):
        age -= 1
    return age

day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))

print("День недели вашего рождения:", day_of_week(day, month, year))
if is_leap_year(year):
    print("Год вашего рождения был високосным.")
else:
    print("Год вашего рождения не был високосным.")
print("Ваш возраст", calculate_age(year))

print(f'{"*"*2} {"*"*2} {"*"*4}')
