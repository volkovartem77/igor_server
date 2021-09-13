import simplejson
from flask import Flask, request, jsonify
from flask_cors import cross_origin, CORS

from utils import mem_get_users, mem_set_users, mem_get_user_by_id, mem_get_user_by_name, mem_remove_user_by_id, \
    mem_add_user, mem_update_user_by_id

if mem_get_users() is None:
    mem_set_users([])

app = Flask(__name__)
CORS(app)


@app.route('/')
@cross_origin(origin='*')
def index():
    return jsonify({'status': 'ok'})


@app.route('/get_users', methods=['GET'])
@cross_origin(origin='*')
def get_users():
    """
    http://127.0.0.1:5000/get_users
    """
    try:
        users = mem_get_users()
        if users is not None:
            return jsonify({'status': 'ok', 'result': users})
        else:
            return {'status': 'fail'}
    except Exception:
        return {'status': 'fail'}


@app.route('/get_user', methods=['GET'])
@cross_origin(origin='*')
def get_user():
    """
    http://127.0.0.1:5000/get_user?user_id=0
    http://127.0.0.1:5000/get_user?user_name=Andrey
    """
    try:
        user_id = request.args.get('user_id')
        if user_id is not None:
            user = mem_get_user_by_id(int(user_id))
            if user is not None:
                return jsonify({'status': 'ok', 'result': user})
            else:
                return {'status': 'fail'}
        else:
            user_name = request.args.get('user_name')
            if user_name is not None:
                user = mem_get_user_by_name(str(user_name))
                if user is not None:
                    return jsonify({'status': 'ok', 'result': user})
                else:
                    return {'status': 'fail'}
            else:
                user = mem_get_user_by_id(0)
                if user is not None:
                    return jsonify({'status': 'ok', 'result': user})
                else:
                    return {'status': 'fail'}
    except Exception:
        return {'status': 'fail'}


@app.route('/remove_user', methods=['GET'])
@cross_origin(origin='*')
def remove_user():
    """
    http://127.0.0.1:5000/remove_user?user_id=0
    """
    try:
        user_id = request.args.get('user_id')
        if user_id is not None:
            mem_remove_user_by_id(int(user_id))

            users = mem_get_users()
            if users is not None:
                return jsonify({'status': 'ok', 'result': users})
            else:
                return {'status': 'fail'}
        else:
            return {'status': 'fail'}
    except Exception:
        return {'status': 'fail'}


@app.route('/remove_all_users', methods=['GET'])
@cross_origin(origin='*')
def remove_all_users():
    """
    http://127.0.0.1:5000/remove_all_users
    """
    try:
        mem_set_users([])
        users = mem_get_users()
        if users is not None:
            return jsonify({'status': 'ok', 'result': users})
        else:
            return {'status': 'fail'}
    except Exception:
        return {'status': 'fail'}


@app.route('/add_user', methods=['POST'])
@cross_origin(origin='*')
def add_user():
    """
        http://127.0.0.1:5000/add_user
        application/json
        {
            "name": Andrey"
        }
    """
    if request.data:
        data = simplejson.loads(request.data)
        try:
            users = mem_get_users()
            if users is not None:
                user_id = len(users)
                data.update({"id": user_id})
                mem_add_user(data)

                users = mem_get_users()
                if users is not None:
                    return jsonify({'status': 'ok', 'result': users})
                else:
                    return jsonify({'status': 'fail'})
        except Exception:
            return jsonify({'status': 'fail'})
    else:
        return jsonify({'status': 'fail'})


@app.route('/update_user', methods=['POST'])
@cross_origin(origin='*')
def update_user():
    """
        http://127.0.0.1:5000/update_user
        application/json
        {
            "id": 2
            "name": Andrey Ivanov"
        }
    """
    if request.data:
        data = simplejson.loads(request.data)
        try:
            mem_update_user_by_id(int(data['id']), data)
            users = mem_get_users()
            if users is not None:
                return jsonify({'status': 'ok', 'result': users})
            else:
                return jsonify({'status': 'fail'})
        except Exception:
            return jsonify({'status': 'fail'})
    else:
        return jsonify({'status': 'fail'})


if __name__ == '__main__':
    app.run(debug=True)


# GET
# get users (default sort ID, by ID, by Name) {'status': 'ok', {'result': list]}} {status: fail}
# get user (by ID, by Name) {'status': 'ok', {'result': dict]}} {status: fail}
# remove user (by ID) {status: ok} {status: fail}
# remove all

# POST
# add user {status: ok} {status: fail}
# update user {status: ok} {status: fail}

