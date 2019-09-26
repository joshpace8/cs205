import dbCreate
# from dbCreate import connect_database
# # dbCreate.connect_database()
import QueryFunctions as qf

k = 'montbello'
c = 'fld_neighborhood_id'
rc = 'fld_offense_category'
data = qf.QueryTop10(k, c, rc)

print(data)
