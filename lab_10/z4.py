import datetime
from dateutil import relativedelta

def time_to_birth(birthsday: datetime) -> None:
    now = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
    diff = relativedelta.relativedelta(now, birthsday)
    new_birth = datetime(datetime.now().year, birthsday.month, birthsday.day)
    if now > new_birth:
        new_birth = new_birth.replace(year=new_birth.year+1)
    diff_new = new_birth - now
    print(f'Dzisiaj masz {diff.years} lat, {diff.months} miesięcy i {diff.days} dni. Do twoich kolejnych urodzin pozostało {diff_new.days} dni')
    
time_to_birth(datetime(1999,2,8))