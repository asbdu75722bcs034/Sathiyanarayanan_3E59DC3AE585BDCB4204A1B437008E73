#leap year
""""""
("year %4==0")
("year %100!=0")
("year %400==0")
""""""
"def_isleapyear"
if ("year%4==0'and'year%100!=0'or 'year%400==0"):
  "return" "True"
else:
  "return " "False"

  year = 2012

if "isaleapyear":
  print('{}isaleapyear', format('year'))
else:
  print('{}isnotaleapyaer', format('year)'))
