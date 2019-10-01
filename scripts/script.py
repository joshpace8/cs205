import dbCreate
import QueryFunctions as q

k = 'speer'
c='fld_neighborhood_id'
d = q.QueryNumCrimes(k,c)
print(d)
dbCreate.connect_database()


