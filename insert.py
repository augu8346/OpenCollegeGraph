import ocgparser
import MySQLdb

def sanitize(lists):
	for item in lists[:-1]:
		lists[lists.index(item)] = item.encode('utf-8') if item.isdigit() else '0'
	return lists

#print parser.parser()
db = MySQLdb.connect(host='localhost',user='ocgadmin',passwd='mecocg',db='OpenCollege')
cur = db.cursor()
cur.execute("select * from Students where RegNo!=0")
batchResults = ocgparser.parser()
# for row in cur.fetchall():
# 	print batchResults[str(row[1])]														#row[1]: RegNo

for row in cur.fetchall():
	result = sanitize(batchResults[str(row[1])])
	if(len(result)!=14):
		continue
	cur.execute("update Students set `601`=" + result[1] + ", `602`=" +result[1] + ", `603`=" +result[2]  + ", `604`=" +result[3] + ", `605`=" +result[4] +", `606`=" +result[5] +", `607`=" +result[6] +", `608`=" +result[7]+ ", `6Tot`=" +result[12] +", `6Res`=\"" +result[13] + "\" where `RegNo`=" + str(row[1]))
	#print result
db.commit()
cur.close()
db.close()