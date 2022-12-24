from datetime import date

def dob(birtdate):
    pdate = date.today()
    day = pdate-birtdate
    year=month=d=0
    d = int(day.days)
    if pdate.year >= birtdate.year:
        year = d // 365
        lp_yr = year//4 # for leap yr
        nday = (d+lp_yr)%365
        if nday >= 30:
            month = nday//30
            d=nday%30

    if year!=0:
        return f"{year} years {month} months and {d} days"
    elif month!=0:
        return f"{month} months and {d} days"
    else:
         return f"{d} days"
