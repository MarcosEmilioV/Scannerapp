from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug = True)


@app.after_request
def cors_headers(whatever):
    whatever.headers['Access-Control-Allow-Origin'] = '*'
    whatever.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    whatever.headers['Access-Control-Allow-Headers'] = "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
    return whatever


@app.route('/', methods=['POST', "OPTIONS"])
def get_image():

    if request.method =="OPTIONS":
        response = app.make_response('')
        response.headers['Access-Control-Allow-Headers'] = "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        return response
    
    if request.method == "POST":
        user_id = 1
        upload_folder = "uploads"
        os.makedirs(upload_folder, exist_ok=True)

        if 'photo' not in request.files:
            return jsonify({"Error" : "No photo provided"})

        photo = request.files['photo']
        print("REQUESTED:", request.files)
        if photo.filename == '':
            return jsonify({"Error": "No photo selected"})

        
        file_path = os.path.join(upload_folder, photo.filename)
        photo.save(file_path)

        try:
            db = sqlite3.connect("test.db")
            print("Connection susccesful")
        except sqlite3.Error as e:
            print(f"Database connection error {e}")
            return jsonify({"Error": "Connection failed"}), 500

        cursor = db.cursor()
        cursor.execute("INSERT INTO image (user_id, image) VALUES (?,?)", (1, file_path))

        db.commit()
        db.close()

        return jsonify({"navaesgay:" : "Photo saved successfully ", "file_path": file_path}), 200

    



    


