from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
   { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
   request_body = request.get_json(force=True)
   if request_body is None:
      return 'The request body is None', 400
   if 'label' not in request_body:
            return 'You need to specify the label',400
   if 'done' not in request_body:
            return 'You need to specify the done', 400
   todos.append(request_body)
   json_text = jsonify(todos)
   return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_text = jsonify(todos)
    return json_text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)