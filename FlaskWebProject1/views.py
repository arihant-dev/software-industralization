"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import jsonify, render_template
from FlaskWebProject1 import app, get_db_connection

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/db')
def db():
    """Returns the database time."""
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT CURRENT_TIMESTAMP()")
        result = cursor.fetchone()
        db_time = result[0].isoformat() if result else None
        return jsonify({"db_time": db_time, "message": "This was updated for docker-compose assignment on date 2024-06-08."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()
        
@app.route('/version')
def version():
    """Returns the application version."""
    return jsonify({"version": "3.0.0"})