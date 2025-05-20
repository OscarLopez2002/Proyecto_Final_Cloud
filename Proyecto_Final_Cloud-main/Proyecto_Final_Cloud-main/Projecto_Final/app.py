from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv
import pyodbc
import urllib

app = Flask(__name__)

# Load environment variables
load_dotenv()

try:
    # Configure database connection with Azure SQL
    params = urllib.parse.quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('SQL_SERVER')};"
        f"DATABASE={os.getenv('SQL_DATABASE')};"
        f"UID={os.getenv('SQL_USER')};"
        f"PWD={os.getenv('SQL_PASSWORD')};"
    )
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Test connection
    with pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('SQL_SERVER')};"
        f"DATABASE={os.getenv('SQL_DATABASE')};"
        f"UID={os.getenv('SQL_USER')};"
        f"PWD={os.getenv('SQL_PASSWORD')};"
    ) as conn:
        print("Conexión exitosa a Azure SQL Database")
        
except Exception as e:
    print(f"Error al conectar a la base de datos: {str(e)}")
    exit(1)

db = SQLAlchemy(app)

@app.route('/test')
def test_connection():
    try:
        db.session.execute('SELECT 1')
        return jsonify({'status': 'success', 'message': 'Conexión exitosa'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Error handling
@app.errorhandler(500)
def handle_internal_error(error):
    return jsonify({
        'error': 'Internal server error',
        'message': str(error)
    }), 500

# Health check endpoint
@app.route('/health')
def health_check():
    try:
        db.session.execute('SELECT 1')
        return jsonify({'status': 'healthy'}), 200
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(error)
        }), 503

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'created_at': task.created_at.isoformat()
    } for task in tasks])

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        completed=False
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'}), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
