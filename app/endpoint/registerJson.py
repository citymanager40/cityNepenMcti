import ast
from ..database import db
from validate_docbr import CPF
from ..models.userModel import User
from flask import jsonify, request
from ..rotas.registerJsonRout import registerJson_bp

class registerJson():

    @registerJson_bp.route('/registrarUsuario', methods=["POST"])
    def registrarUsuario():

        data = request.get_json()

        nome = data['nome']
        email = data['email']
        cpf = data['cpf']
        senha = data['senha']
        senha_confirmar = data['senha_confirmar']
        flg_admin = data['flg_admin']
        flg_governo = data['flg_governo']

        if not nome:
            return jsonify({"Status": "Campo 'nome' ausente no JSON"}), 400

        if not email:
            return jsonify({"Status": "Campo 'email' ausente no JSON"}), 400

        if not cpf:
            return jsonify({"Status": "Campo 'cpf' ausente no JSON"}), 400

        if not senha:
            return jsonify({"Status": "Campo 'senha' ausente no JSON"}), 400

        if not senha_confirmar:
            return jsonify({"Status": "Campo 'senha_confirmar' ausente no JSON"}), 400

        if senha != senha_confirmar:
            return jsonify({"Status": "As senhas informadas estão divergentes"}), 400

        obj = CPF()
        if not obj.validate(cpf): 
            return jsonify({'Status: {}'.format('Ops. Não nos parece um CPF válido')}), 401

        try:

            user = User(nome, email, cpf, senha, ast.literal_eval(flg_governo), ast.literal_eval(flg_admin))

            db.session.add(user)
            db.session.commit()
            return jsonify({"Status:": "Usuário cadastrado com sucesso!"}) 

        except Exception as e:
            db.session.rollback()
            return jsonify({"Status:" : str(e)}), 400
