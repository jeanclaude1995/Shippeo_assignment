import psycopg2
import sys
import zlib
def find_common_character(list):
    total=0
    for i in list:
        half=len(i)//2
        #find the common character
        common=set(i[:half]).intersection(set(i[half:]))
        common=common.pop()
        if common.islower():
            total+=ord(common)-96
        else:
            total+=ord(common)-38
    return total

def write_log_to_db(result,data):
    # database connections
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
        
#main function
if __name__ == '__main__':
    filePath=sys.argv[1]
    list=[]
    with open(filePath,'r') as file:
        text=file.read()
        var=text.replace('\n', ',')
        list=var.split(',')
    result=find_common_character(list)
    print("The sum of the value of the common characters is: "+ str(result))
    #compress the text
    data=zlib.compress(text.encode('utf-8'))
    print("The compressed text is: "+ str(data))
    write_log_to_db(result,data)
    
