import mysql.connector, os, re

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="miriani"
)

mycursor = mydb.cursor()
#mycursor.execute("DELETE FROM words WHERE word IN (და, რომ, თუ, არ, ამ, ეს, კი, ისე, ან, მაგრამ, რაც, იმ, სხვა, იყო, რადგან, უფრო, ასე, მე, მისი, არც, მერე, არა, ამიტომ, რა, ვინც, სულ, თავისი, მეტად, რომელიც, ის, იყო, ძალიან, აქ, ჩვენი, ხოლო, რამ, ჩვენს, წმინდა, ერთი, მის, რომელსაც, ახლა, ჯერ, ჩემი, )")

with open('text.txt','r', encoding="utf8") as f:
    for line in f:
        for word in line.split():
            word = re.sub(r"[\Wa-zA-Z1-9]", "", word, flags=re.I)
            try:    
                mycursor.execute("SELECT rank FROM words WHERE word=" + "'" + word + "'")
                myresult = mycursor.fetchall()
                if mycursor.rowcount >= 1:
                    mycursor.execute("UPDATE words SET rank=rank+1 WHERE word=" + "'" + word + "'")
                    mydb.commit()
                    print("updated")
                else:
                    sql = "INSERT INTO words (word, rank) VALUES (%s, %s)"
                    val = (word, "1")
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("added")
            except:    
                print("OKAY")