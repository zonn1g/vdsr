from flask import Flask, render_template, jsonify, request
import mysql.connector
from mysql.connector import Error
from datetime import datetime

app = Flask(__name__)

def db_connection(sql):
    try:
        cnx = mysql.connector.connect(
            host='192.168.1.163',
            user='root3 ',
            password='P@ssw0rd',
            database='prof'
        )
        cur = cnx.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cnx.commit()
        return rows
    except Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None
#блок для employs
@app.route('/employs', methods=['GET'])
def get_employs():   
    '''метод get_employs() вызывается с помощью /employs  выводит таблицу employs'''
    data = db_connection('SELECT * FROM `employs`  WHERE 1;')
    return jsonify(data)

@app.route('/employs/insert', methods=['POST'])
def add_employs():
    new_employs = request.json
    
    date_str = new_employs[7]
    
    date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %z %Y")
    formatted_date = date_obj.strftime("%Y-%m-%d")

    sql = f'''INSERT INTO `employs` (`full_name`, `deportament_id`, `position`, `work_phone`, `office`, `email`, `birth_date`, `manager_id`, `assistant_id`, 
    `personal_phone`, `info`) 
    VALUES ("{new_employs[1]}",{new_employs[2]},"{new_employs[3]}","{new_employs[4]}","{new_employs[5]}","{new_employs[6]}","{formatted_date}","{new_employs[8]}",
    {new_employs[9]},"{new_employs[10]}","{new_employs[11]}");'''
  
    db_connection(sql)
    return jsonify(new_employs)


@app.route('/employs/update', methods=['POST'])
def update_employs():
    new_employs = request.json
    # Исходная строка даты
    date_str = new_employs[7]
    date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %z %Y")
    formatted_date = date_obj.strftime("%Y-%m-%d")

    sql = f'''UPDATE `employs` SET `full_name`="{new_employs[1]}", `deportament_id`={new_employs[2]}, `position`="{new_employs[3]}", `work_phone`="{new_employs[4]}",
    `office`="{new_employs[5]}", `email`="{new_employs[6]}", `birth_date`="{formatted_date}", `manager_id`="{new_employs[8]}", `assistant_id`={new_employs[9]},
    `personal_phone`="{new_employs[10]}", `info`="{new_employs[11]}" WHERE `employs_id`={new_employs[0]};'''

    db_connection(sql)
    return jsonify(new_employs)

#блок для calendars
@app.route('/calendars', methods=['GET'])
def get_calendars():   
    data = db_connection('SELECT * FROM `calendars` WHERE 1;')
    return jsonify(data)

@app.route('/calendars/insert', methods=['POST'])
def add_calendars():
    new_calendars = request.json
    
    date_str = new_calendars[7]
    
    date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %z %Y")
    formatted_date = date_obj.strftime("%Y-%m-%d")

    sql = f'''pip ;'''
  
    db_connection(sql)
    return jsonify(new_calendars)

#блок для departments
@app.route('/departments', methods=['GET'])
def get_departments():   
    data = db_connection('SELECT * FROM `departments` WHERE 1;')
    return jsonify(data)
@app.route('/')
def index():
    
    print(db_connection('show tables;'))
    return 'Rest'


if __name__ == '__main__':
    app.run(debug=True)