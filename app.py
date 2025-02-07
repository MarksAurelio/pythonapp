from flask import Flask, request
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Flask"

@app.route('/item', methods=['POST'])
def post_item():
    data = request.get_json()
    sql = f"INSERT INTO todolist(item, status) VALUES('{data['item']}','{data['status']}')"
    banco(sql)
    return data

def banco(sql):
    resultado = ""
    try:
        # Conexão com o banco de dados PostgreSQL
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        cursor = conn.cursor() # cursor vai ser a variável para executar os comandos SQL.
        cursor.execute(sql) # executa o comando sql seja insert, select.. etc
        cursor.close() # finaliza o cursor
        conn.commit() # confirma o comando SQL
        conn.close() # finaliza a conexão
    except psycopg2.Error as e:
        print("Erro na conexão do banco de dados")

host = "dpg-cuhulfij1k6c73fe8f10-a.oregon-postgres.render.com"
port = "5432"
dbname = "senaidb_r6cv"
user = "senaidb_r6cv_user"
password = "hv1B0Brq0jHXiAgB7lP6NLpaXbsv6U3V"

if __name__ == '__main__':
    app.run(debug=True)
