from flask import Blueprint, render_template
from database.produto import PRODUTOS

product_route = Blueprint('produto', __name__)

'''
Rotas
    - /produtos/ (GET) - listar os produtos
    - /produtos/ (POST) - inserir o produto no servidor
    - /produtos/new (GET) - formulario para inserir produtos
    - /produtos/<id> (GET) - obter os dados de um produto
    - /produtos/<id>/edit/ (GET) - formulario para editar um produto 
    - /produtos/<id>/update (PUT)- atualizar dados do produto
    - /produtos/<id>/delete (DELETE) - deleta os registros do produto
'''

@product_route.route('/')
def listar_produtos():
    return render_template('listar_produtos.html', produtos=PRODUTOS)

@product_route.route('/', methods=['POST'])
def inserir_produtos():
    pass

@product_route.route('/new')
def novo_produto():
    return render_template('novo_produto.html')

@product_route.route('/<int:product_id>')
def detalhe_produto(product_id):
    return render_template('detalhe_produto.html')

@product_route.route('/<int:product_id>/edit')
def editar_produto(product_id):
    return render_template('editar_produto.html')

@product_route.route('/<int:product_id>/update', methods=['PUT'])
def update_produto(product_id):
    pass

@product_route.route('/<int:product_id>/delete', methods=['DELETE'])
def deletar_produto(product_id):
    pass
