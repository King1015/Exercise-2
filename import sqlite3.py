import sqlite3
# Read the file and copy its content to a list
with open('stephen_king_adaptations.txt', 'r') as file:
    stephen_king_adaptations_list = file.readlines()
# Establish a connection with the SQLite database
conn = sqlite3.connect('stephen_king_adaptations.db')
cursor = conn.cursor()
# Create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table
                  (movieID INTEGER PRIMARY KEY,
                  movieName TEXT,
                  movieYear INTEGER,
                  imdbRating REAL)''')
# Insert data into the table
for line in stephen_king_adaptations_list:
    movie = line.strip().split(',')
    cursor.execute("INSERT INTO stephen_king_adaptations_table (movieName, movieYear, imdbRating) VALUES (?, ?, ?)",
                   (movie[0], movie[1], movie[2]))
# Save the changes
conn.commit()
# Search for movies in the database
while True:
    print("Choose an option:")
    print("1. Search by movie name")
    print("2. Search by movie year")

    print("3. Search by movie rating")
    print("4. STOP")
    option = input("Enter your choice: ")
    if option == '1':
        movie_name = input("Enter the name of the movie: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?", (movie_name,))
        result = cursor.fetchone()
        if result:
            print("Movie Name:", result[1])
            print("Movie Year:", result[2])
            print("IMDB Rating:", result[3])
        else:
            print("No such movie exists in our database")
    elif option == '2':
        movie_year = int(input("Enter the year of the movie: "))
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?", (movie_year,))
        result = cursor.fetchall()
        if result:
             for movie in result:
                print("Movie Name:", movie[1])
                print("Movie Year:", movie[2])
                print("IMDB Rating:", movie[3])
        else:
            print("No movies were found for that year in our database.")
    elif option == '3':
        movie_rating = float(input("Enter the minimum rating: "))
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (movie_rating,))
        result = cursor.fetchall()
        if result:
            for movie in result:
                print("Movie Name:", movie[1])
                print("Movie Year:", movie[2])
                print("IMDB Rating:", movie[3])
        else:
            print("No movies with a rating equal to or above", movie_rating, "were found in the database.")
    elif option == '4':
        break
    else:
        print("Invalid option. Please try again.")
# Close the connection
conn.close()