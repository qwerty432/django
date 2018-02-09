import pymongo

# Open the MongoDB connection
conn = pymongo.MongoClient('mongodb://localhost:27017')

# Print the available MongoDB databases
databases = conn.database_names()
for database in databases:
    print(database)

# Close the MongoDB connection
conn.close()