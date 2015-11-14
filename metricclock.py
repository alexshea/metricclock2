

def checktime(normaltime):
  if len(normaltime) != 4:
    print("Invalid number of digits. Add a 0 to the front if necessary.")
    return 0
  if normaltime > "2359":
    print("Invalid time")
    return 0
  if normaltime < "0":
    print("Invalid time")
    return 0
  if int(normaltime[2:]) > 59:
    print("Invalid time")
    return 0

def convertminutes(normaltime):
  normalmin = int(normaltime[2:])
  normalhour = int(normaltime[:2])
  modmin = float((normalhour%2.4)*60)
  metricmodmin = modmin * (100/144)
  metricnonmodmin = float(normalmin * (100/144))
  newmin = int(metricnonmodmin + metricmodmin)
  return(newmin)

def converthours(normaltime, newmin):
  normalhour = int(normaltime[:2])
  newhour = int(normalhour/2.4)  
  if newmin > 99:
    newmin = newmin - 100
    newhour = newhour + 1
  return newhour

def main():
  normaltime = input('Enter a time in military format (e.g. 2145, 0713): ')
  checktime(normaltime)
  convertminutes(normaltime)
  converthours(normaltime, newmin)

  metrichour = "0"+str(newhour)
  if newmin < 10:
    metricmin = "0"+str(newmin)
  else:
    metricmin = str(newmin)

  print("Normal time is " + normaltime)
  print("Metric time is " + metrichour+metricmin)

main()

#0000 0100 0200 0300 0400 0500 0600 0700 0800 0900
#0000 0224 0448 0712 0936 1200 1424 1648 1912 2136
