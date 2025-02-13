from flask import Flask, jsonify, request, render_template
import hashlib
app = Flask(__name__)

@app.route('/')
def hello():
    return "REST Python"

@app.route('/docs/list', methods=['GET'])
def get_docs():
    return jsonify(data["Doc"])

@app.route('/cases/list', methods=['GET'])
def get_cases():
    return jsonify(data["Case"])

@app.route('/jobs/list', methods=['GET'])
def get_jobs():
    return jsonify(data["Job"])

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/docs/name/<name>', methods=['GET'])
def get_doctor_by_name(name):
    doctors = [doctor for doctor in data["Doc"] if doctor["name"] == name]
    return jsonify(doctors)


@app.route('/docs/id/<int:id>', methods=['GET'])
def get_doctor_by_id(id):
    doctor = next((d for d in data["Doc"] if d["id"] == id), None)
    if doctor is None:
        return jsonify({"error": "Doctor not found"}), 404
    return jsonify(doctor)


@app.route('/jobs/name/<patient_name>', methods=['GET'])
def get_job_by_patient_name(patient_name):
    jobs = [job for job in data["Job"] if job["patient_name"] == patient_name]
    return jsonify(jobs)


@app.route('/jobs/id/<int:id>', methods=['GET'])
def get_job_by_id(id):
    job = next((j for j in data["Job"] if j["id_J"] == id), None)
    if job is None:
        return jsonify({"error": "Job not found"}), 404
    return jsonify(job)

@app.route('/cases/name/<case_name>', methods=['GET'])
def get_case_by_name(case_name):
    cases = [case for case in data["Case"] if case["name"] == case_name]
    return jsonify(cases)


@app.route('/cases/id/<int:id>', methods=['GET'])
def get_case_by_id(id):
    case = next((c for c in data["Case"] if c["id_C"] == id), None)
    if case is None:
        return jsonify({"error": "Case not found"}), 404
    return jsonify(case)


@app.route('/cases', methods=['POST'])
def add_case():
    new_case = request.json
    data["Case"].append(new_case)
    return jsonify(new_case), 201


def reg():
    ip = request.remote_addr
    token = hashlib.sha256()
    token.update(b"1")
    token.digest()
    token_hex = token.hexdigest()
    mass_users.append({"id": len(mass_users) + 1, "name": "", "token": token_hex})
    print(mass_users)
    return f'Ваш токен: {token_hex}'

if __name__ == '__main__':
    app.run(debug=True)













INSERT INTO `employs` (`full_name`, `deportament_id`, `position`, `work_phone`, `office`, `email`, `birth_date`, `manager_id`, `assistant_id`, `personal_phone`, `info`) VALUES ("Байдин Семен Агафонович",3,"Административный директор-руководитель аппарата","+7 (179) 370-26-88","402А","белоусов@гкдр.ру","Sun, 25 Apr 1971 00:00:00 GMT","None",0,"0","0");

INSERT INTO `employs` (`full_name`, `deportament_id`, `position`, `work_phone`, `office`, `email`, `birth_date`, `manager_id`, `assistant_id`, `personal_phone`, `info`) VALUES ("Байдин Семен Агафонович",3,"Административный директор-руководитель аппарата","+7 (179) 370-26-88","402А","белоусов@гкдр.ру","Sun, 25 Apr 1971 00:00:00 GMT","None",0,"0","0"); 


