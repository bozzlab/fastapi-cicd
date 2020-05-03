import databases
import os 

DATABASE_URL = "postgresql://%s:%s@%s/%s" % (os.environ['PG_USER'], os.environ['PG_PASSWORD'], os.environ['PG_HOST'], os.environ['PG_DATABASE'])
database = databases.Database(DATABASE_URL)