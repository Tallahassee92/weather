import requests

from settings import API_TOKEN, BASE_URL
import sqlite3

connection = sqlite3.connect('weather.db')
cursor = connection.cursor()


while True:
    username = input('username: ')

    cursor.execute('select id from users where username = ?;', [username])
    user = cursor.fetchone()
    if not user:
        cursor.execute('insert into users(username) values (?) returning id;', [username])
        user = cursor.fetchone()
        connection.commit()
        print(f'user created: {user}')
    else:
        print(f'user received: {user}')

    city = input('city: ')

    response = requests.get(f'{BASE_URL}/current.json',
                            params={'q': city, 'key': API_TOKEN})
    data = response.json()
    text = data['current']['condition']['text']
    temp_c = data['current']['temp_c']
    wind_kph = data['current']['wind_kph']
    feelslike_c = data['current']['feelslike_c']
    name = data['location']['name']
    country = data['location']['country']
    localtime = data['location']['localtime']


    cursor.execute('''
    insert into weather(text, temp_c, wind_kph, feelslike_c, name, country, localtime, user_id)
    values (?,?,?,?,?,?,?,?)
    ''', [text, temp_c, wind_kph, feelslike_c, name, country, localtime, user[0]])
    connection.commit()
    print(f'weather added to db')

    print(f'''
{text=}
{temp_c=}
{wind_kph=}
{feelslike_c=}
{name=}
{country=}
{localtime=}
''')




