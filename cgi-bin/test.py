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
    g = ((8 * b) + 13) // 25
    h = ((19 * a) + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + (11 * h)) // 319
    r = ((2 * e) + (2 * j) - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32

    return n, p



print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title> Result of finding easter </title>  </head>')
print('<body>')
print('<p>')
print(f"The selected year is {year}.")
print('</p>')
print('</body>')
print('</html>')