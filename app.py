from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuration de la base de données MySQL
app.config['MYSQL_HOST'] = '10.0.221.219'  # Nom du conteneur MySQL
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'     # Mot de passe défini lors de la création du conteneur MySQL
app.config['MYSQL_DB'] = 'test'      # Nom de la base de données

mysql = MySQL(app)

# Route POST pour ajouter un utilisateur
@app.route("/add_user", methods=['POST'])
def add_user():
    print("Requête POST reçue sur /add_user")
    data = request.json  # Supposons que le nom de l'utilisateur soit envoyé en JSON
    name = data.get('name')
    if not name:
        return jsonify({"error": "Le nom est requis"}), 400

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user (name) VALUES (%s)", (name,))
    mysql.connection.commit()
    cur.close()

    return jsonify({"success": "Utilisateur ajouté avec succès"}), 201

# Route pour afficher les données de la table "user"
@app.route("/")
def display_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    users = cur.fetchall()
    cur.close()
    
    # Affichage des données dans une liste non ordonnée
    user_list = "<ul>"
    for user in users:
        user_list += "<li>{} - {}</li>".format(user[0], user[1])  # Supposons que la table a deux colonnes : id et name
    user_list += "</ul>"
    
    return "<h1>Utilisateurs</h1>" + user_list

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
