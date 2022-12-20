import psycopg2
def find_common_character(list):
    value_priority=[]
    for i in list:
        total=len(i)
        half=total//2
        first=i[:half]
        second=i[half:]
        #find the common character
        common=""
        for i in first:
            if i in second and i not in common:
                common+=i
        if common.islower():
            value_priority.append(ord(common)-96)
        else:
            value_priority.append(ord(common)-38)
    return sum(value_priority)

filePath="input_file.txt"
list=[]
with open(filePath,'r') as file:
    var=file.read().replace('\n', ',')
    list=var.split(',')
result=find_common_character(list)
print("The sum of the value of the common characters is: "+ str(result))


with open(filePath, 'r') as f:
    data=f.read().rstrip()


# Connect to the database
conn = psycopg2.connect(host="postgres", user="postgres", password="mypassword", dbname="postgres")

# Create a cursor
cur = conn.cursor()

#Creating a table in the database with execution date of the script ,content and the result of the script
cur.execute("CREATE TABLE IF NOT EXISTS logs (id SERIAL PRIMARY KEY, date TIMESTAMP,content TEXT,result VARCHAR(255))")

#Insert the execution date of the script ,data and the result of the script into the table 
cur.execute("INSERT INTO logs (date,content,result) VALUES (now(), %s,%s)", (data, result,))

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
