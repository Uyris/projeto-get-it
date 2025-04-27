from database import get_connection
from flask import session

def load_data(table_name):
    # CONECTANDO AO BANCO DE DADOS PARA ACESSAR AS INFORMAÇÕES
    conn = get_connection() # FUNÇÃO QUE RETORNA A CONEXÃO COM O BANCO DE DADOS
    cursor = conn.cursor() #FUNCIONA COMO PONTEIRO PARA USAR OUTROS COMANDOS DA BIBLIOTECA

    user_id = session['user_id']
    
    # SELECIONANDO TODAS AS TABELAS
    cursor.execute(f"""
            SELECT * FROM {table_name}
            WHERE user_id = %s OR user_id IS NULL
            ORDER BY position
        """, (user_id,))
    data_format = []
    data = cursor.fetchall()
    for note in data:
        data_format.append({'id': note[0], 'titulo': note[1], 'detalhes': note[2], 'position': note[3], 'color': note[4]})

    # FECHANDO CONEXÃO
    conn.close()
    
    return data_format

def load_template(template_path):
    with open('static/templates/'+ template_path, 'r', encoding='utf-8') as template:
        data = template.read()
        return f'''{data}'''

def load_note(note_data):
    data = note_data
    for note in data:
        data_format = {'id': note[0], 'titulo': note[1], 'detalhes': note[2]}
    return data_format
