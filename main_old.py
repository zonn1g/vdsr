from flask import Flask, render_template,jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def db_connection(sql):
    try:
        cnx = mysql.connector.connect(
            host='localhost',
            user='root3',
            password='P@$$w0rd',
            database='prof'
        )
        cur = cnx.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None
#блок для employs
@app.route('/employs', methods=['GET','POST'])
def get_employs():   
    '''метод get_employs() вызывается с помощью /employs  выводит таблицу employs'''
    data = db_connection('SELECT * FROM `employs` WHERE 1;')
    return jsonify(data)

@app.route('/employs/insert', methods=['POST'])
def add_employs():
    new_employs = request.json
    #print(new_employs)
    sql = f'''INSERT INTO `employs` (`full_name`, `deportament_id`, `position`, `work_phone`, `office`, `email`, `birth_date`, `manager_id`, `assistant_id`, `personal_phone`, `info`) 
    VALUES ("{new_employs[1]}",{new_employs[2]},"{new_employs[3]}","{new_employs[4]}","{new_employs[5]}","{new_employs[6]}","{new_employs[7]}","{new_employs[8]}",{new_employs[9]},"{new_employs[10]}","{new_employs[11]}");'''
    print(sql)    
    #sql='INSERT INTO `employs` (`full_name`, `deportament_id`, `position`, `work_phone`, `office`, `email`, `birth_date`, `manager_id`, `assistant_id`, `personal_phone`, `info`) VALUES ("Байдин Семен Агафонович", 3, "Административный директор-руководитель аппарата", "+7 (179) 370-26-88", "402А", "белоусов@гкдр.ру", "1971-04-25",0, 0, "0", "0");'
    print(sql)    
    print(db_connection(sql))
    return jsonify(new_employs)


#блок для calendars
@app.route('/calendars', methods=['GET','POST'])
def get_calendars():   
    data = db_connection('SELECT * FROM `calendars` WHERE 1;')
    return jsonify(data)
#блок для departments
@app.route('/departments', methods=['GET','POST'])
def get_departments():   
    data = db_connection('SELECT * FROM `departments` WHERE 1;')
    return jsonify(data)
@app.route('/')
def index():
    
    print(db_connection('show tables;'))
    return 'Rest'


if __name__ == '__main__':
    app.run(debug=True)