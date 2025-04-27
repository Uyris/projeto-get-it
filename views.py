from utils import load_data, load_template, load_note
from database import get_connection
from dotenv import load_dotenv
from flask import session
import psycopg2
import os



def index():
    note_template = load_template('components/notes.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'], id=dados['id'], color=dados['color'])
        for dados in load_data('notes')
    ]
    notes = '\n'.join(notes_li)
    return load_template('index.html').format(notes=notes)

def error404():
    return load_template('404.html')

def submit(titulo, detalhes, selected_color):
    conn = get_connection()
    cursor = conn.cursor()

    user_id = session['user_id']

    # Obtém a maior posição atual
    cursor.execute("SELECT MAX(position) FROM notes")
    max_position = cursor.fetchone()[0]  # Pega o valor máximo encontrado

    if max_position is None:
        max_position = 0

    new_position = max_position + 1

    # Insere a nova nota
    cursor.execute(
        "INSERT INTO notes (Title, Details, position, color, user_id) VALUES (%s, %s, %s, %s, %s)",
        (titulo, detalhes, new_position, selected_color, user_id)
    )

    
    conn.commit()
    conn.close()

def update_order(request):
    data = request.json
    new_order = data.get("order")

    conn = get_connection()
    cursor = conn.cursor()

    # Atualiza a ordem
    for index, note_id in enumerate(new_order):
        cursor.execute("UPDATE notes SET position = %s WHERE id = %s", (index, note_id))

    conn.commit()
    conn.close()

def delete_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()

    user_id = session['user_id']

    cursor.execute("DELETE FROM notes WHERE id = %s AND user_id = %s", (note_id, user_id))
    
    conn.commit()
    conn.close()

def edit_note(note_id, titulo, detalhes, cor):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE notes SET title = %s, details = %s, color = %s WHERE id = %s",
        (titulo, detalhes, cor, note_id)
    )

    conn.commit()
    conn.close()
