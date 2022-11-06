#!/usr/bin/python3
import cgi, datetime
form = cgi.FieldStorage()
year = form.getvalue('year')
choice = form.getvalue('format')

def FindEaster(y):
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    return n, p

year = int(year)
EasterDay = FindEaster(year)
(month, day) = EasterDay
Easter = datetime.datetime(year, month, day)
month_string = Easter.strftime("%B")

daysuffix = {
    1:"st",
    2:"nd",
    3:"rd",
    4:"th",
    5:"th",
    6:"th",
    7:"th",
    8:"th",
    9:"th",
}

dayremainder = day % 10
if day == 11:
    suffix = "th"
else:
    suffix = daysuffix[dayremainder]

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print(f"<title>In the year {year} when does Easter fall?</title>")
print("""<style>
* {
    font-family: Georgia, 'Times New Roman', Times, serif;
    background-color: aquamarine;
    color: palevioletred
}

p {
    font-size: 75pt;
    margin-left: 10px;
}

h1 {
    text-align: center;
    font-size: 40pt;
    border: 4pt dotted black;
    width: 40%;
    margin: auto;
}
</style>
""")
print('</head>')
print('<body>')
print(f'<h1>When does Easter fall in {year}?</h1>')
print('<p>')
if choice == 'numerical':
    print(f"In the year {year}, Easter falls on {day}/{month}/{year}.")
elif choice == 'verbose':
    print(f"In the year {year}, Easter falls on {day}<sup>{suffix}</sup> {month_string} {year}.")
elif choice == 'both':
    print(f"In the year {year}, Easter falls on {day}/{month}/{year}.<br/>")
    print(f"In the year {year}, Easter falls on {day}<sup></sup> {month_string} {year}.")
print('</p>')
print('</body>')
print('</html>')