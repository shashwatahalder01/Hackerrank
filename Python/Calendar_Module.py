import calendar


a=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
b=str(input())
c=list(b.split(" "))
mm,dd,yy=c
print(a[calendar.weekday(int(yy),int(mm),int(dd))])
