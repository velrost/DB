import cx_Oracle

username = 'velrost'
password = 'Richbitch8228'
database = 'localhost:1521/xe'

connection = cx_Oracle.connect(username, password, database)

cursor = connection.cursor()

print("Вивести скільки кожен бомбардир найбільше забивав голів.\n")
query1 = """
   SELECT
        top_scorer_name,
        max(goals) as most_goals
    FROM season
    GROUP BY top_scorer_name
"""
cursor.execute(query1)

for row in cursor:
    print(row)


print("Вивести відсоток перемог кожної команди від  загальної кількості.\n")
query2 = """
   SELECT winner_name, round((count(winner_name))/(select count(*) from season)*100, 2) percent
   FROM season
   GROUP BY winner_name
   ORDER BY percent DESC, winner_name
"""
cursor.execute(query2)

for row in cursor:
    print(row)

print("Вивести динаміку голів бомбардирів по сезонам.\n")
query3 = """
   SELECT season_year, max(goals) as goals
   FROM season
   GROUP BY season_year
   ORDER BY season_year
"""
cursor.execute(query3)

for row in cursor:
    print(row)

cursor.close()
connection.close()