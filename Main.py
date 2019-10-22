import CommandLine as CL
import database as db


conn = db.create_connection()
db.create_if_not_exists(conn)
db.close_connection(conn)

CLParser = CL.CommandLineParser()
CLParser.parseit()
# CLaction.begin()





