import sqlite3


connection = sqlite3.connect('weather.db')

cursor = connection.cursor()

cursor.executescript('''
create table if not exists users(
    id integer primary key autoincrement,
    username text
);

create table if not exists weather(
    id integer primary key autoincrement,
    text text,
    temp_c float,
    wind_kph float,
    feelslike_c float,
    name text,
    country text,
    localtime text,
    user_id integer,
    foreign key(user_id) references users(id)
);
''')







connection.commit()
connection.close()