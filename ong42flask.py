__author__ = "Arthur Grangeiro de Souza"
__credits__ = ["Arthur Grangeiro de Souza"]
__version__ = "0.9.1"
__maintainer__ = "Arthur Grangeiro de Souza"
__email__ = "arthurgrangeiro@outlook.com"
__status__ = "Prototype"


import os

#import componentes do framework Flask
from flask import Flask, render_template, request, redirect, url_for, flash

#import elementos sqlalchemy para integracao com a base de dados
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_project import Base, Usuario, Organizacao, Cartao, DadosBancarios, Mensagem

#definicao da aplicacao flask
app = Flask(__name__)


#configuracao dos componentes de acesso ao banco de dados
engine = create_engine('sqlite:///projeto.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession() 

#Configuracao dos metodos responsaveis por cada uma das paginas da aplicacao

#pagina inicial do site
@app.route('/')
@app.route('/index/', methods = ['POST', 'GET'])
def frontPage():
	#grava mensagem enviada pelo usuario
	if request.method == 'POST':
		mensagem = Mensagem()
		mensagem.nome = request.form['name']
		mensagem.email = request.form['email']
		mensagem.message = request.form['message']

		session.add(mensagem)
		session.commit()

		flash("Mensagem enviada com sucesso!")

	return render_template('index.html')

#lista as organizacoes cadastradas na base de dados
@app.route('/organizacoes/', methods = ['POST', 'GET'])
def listaOrganizacoes():
	#grava mensagem enviada pelo usuario
	if request.method == 'POST':
		mensagem = Mensagem()
		mensagem.nome = request.form['name']
		mensagem.email = request.form['email']
		mensagem.message = request.form['message']

		session.add(mensagem)
		session.commit()

		flash("Mensagem enviada com sucesso!")

	#busca as organizacoes no banco de dados
	organizacoes = session.query(Organizacao)
	#envia a lista de organizacoes para a pagina organizacoes.html que as exibe
	return render_template('organizacoes.html', organizacoes = organizacoes)

#lista as informacoes sobre uma determinada organizacao
@app.route('/organizacao/<int:organizacao_id>/')
def sobreOrganizacao(organizacao_id):
	#busca uma organizacao especifica e envia os dados
	organizacao = session.query(Organizacao).filter_by(id = organizacao_id).one()
	#envia os dados de uma organizacao para a pagina detalhes_org.html que as exibe
	return render_template('detalhes_org.html', organizacao = organizacao)

#lista as organizacoes cadastradas na base de dados
@app.route('/23567489/messages')
def listaMessages():
	#busca as organizacoes no banco de dados
	mensagens = session.query(Mensagem)
	#envia a lista de organizacoes para a pagina organizacoes.html que as exibe
	return render_template('mensagens.html', mensagens = mensagens)



#lista as informacoes sobre um determinado usuario
@app.route('/usuario/<int:usuario_id>/', methods=['POST','GET'])
def sobreUsuario(usuario_id):
	#busca no banco de dados um usuario com base no id passado na url
	usuario = session.query(Usuario).filter_by(id = usuario_id).one()
	#se ha dados sendo enviados para o servidor...
	if request.method == 'POST':
		#o metodo verifica os campos que estao sendo alterados e os altera no objeto usuario
		if request.form['email']:
			usuario.email = request.form['email']
		if request.form['senha']:
			usuario.senha = request.form['senha']
		if request.form['telefone']:
			usuario.telefone = request.form['telefone']
		if request.form['endereco']:
			usuario.endereco = request.form['endereco']
		if request.form['nome']:
			usuario.nome = request.form['nome']
		if request.form['cpf']:
			usuario.cpf = request.form['cpf']
		if request.form['nascimento']:
			usuario.nascimento = request.form['nascimento']
		if request.form['genero']:
			usuario.genero = request.form['genero']
		#o usuario atualizado e armazenado no banco de dados
		session.add(usuario)
		session.commit()
		#retorno para o usuario
		flash("Dados atualizados com sucesso!")
		#o usuario e redirecionado para a mesma pagina com os dados atualizados
		return redirect(url_for('sobreUsuario', usuario_id = usuario_id))
	#se nao ha dados...
	else:
		#retorna as informacoes do usuario para a pagina detalhes_user.html que ira exibir esses dados
		return render_template('detalhes_user.html', usuario = usuario)

#cria um novo usuario - essa deve cadastrar um novo usuario no sistema
@app.route('/usuario/new', methods=['GET','POST'])
def createUsuario():
	#Se dados estao sendo enviados...
	if request.method == 'POST':
		#um novo usuario e criado com os dados passados via formulario...
		newUser = Usuario(nome = request.form['nome'], email = request.form['email'], senha = request.form['senha'])
		#e adicionado ao banco de dados
		session.add(newUser)
		session.commit()
		#mensagem de confirmacao para o usuario
		flash("Usuario Criado com Sucesso. Bem Vindo!")
		return redirect(url_for('sobreUsuario', usuario_id = newUser.id))
	#se nao ha dados...
	else:
		#a pagina de cadastro e mostrada normalmente
		return render_template('cadastro.html')

#lista as organizacoes cadastradas no site e da a opcao de editar ou excluir
@app.route('/adm/organizacoes/')
def admOrganizacoes():
	#busca as organizacoes no banco de dados
	organizacoes = session.query(Organizacao)
	#envia a lista de organizacoes para a pagina adm_organizacoes.html que as exibe
	return render_template('adm_organizacoes.html', organizacoes = organizacoes)

#metodo para adicionar uma nova organizacao ao sistema
@app.route('/organizacoes/new', methods=['GET','POST'])
def newOrganizacao():
	#se dados estao sendo enviados...
	if request.method == 'POST':
		#um novo objeto Organizacao e criado...
		newOrg = Organizacao()
		#e preenchido com os dados que estiverem no formulario
		if request.form['cnpj']:
			newOrg.cnpj = request.form['cnpj']
		if request.form['razaosocial']:
			newOrg.razaosocial = request.form['razaosocial']
		if request.form['nomefantasia']:
			newOrg.nomefantasia = request.form['nomefantasia']
		if request.form['representante']:
			newOrg.representante = request.form['representante']
		if request.form['email']:
			newOrg.email = request.form['email']
		if request.form['telefone']:
			newOrg.telefone = request.form['telefone']
		if request.form['site']:
			newOrg.site = request.form['site']
		if request.form['facebook']:
			newOrg.facebook = request.form['facebook']
		if request.form['endereco']:
			newOrg.endereco = request.form['endereco']
		if request.form['sobre']:
			newOrg.descricao = request.form['sobre']
		if request.form['descricao']:
			newOrg.descricao = request.form['descricao']

		#a nova organizacao e adicionada ao banco de dados
		session.add(newOrg)
		session.commit()
		#retorno para o usuario
		flash("Nova Organizacao criada")
		#o usuario e redirecionado para a pagina que lista as organizacoes
		return redirect(url_for('listaOrganizacoes'))
	#se nao ha dados e mostrada a tela para cadastrar uma nova organizacao
	else:
		return render_template('nova_organizacao.html')

#editar informacoes sobre uma organizacao cadastrada
@app.route('/adm/organizacao/<int:organizacao_id>/edit', methods=['GET','POST'])
def editOrganizacao(organizacao_id):
	#recupera as informacoes sobre a organizacao do banco de dado
	editOrg = session.query(Organizacao).filter_by(id = organizacao_id).one()
	#se dados estao sendo enviados...
	if request.method == 'POST':
		#sao adicionados ao objeto editOrg
		if request.form['razaosocial']:
			editOrg.razaosocial = request.form['razaosocial']
		if request.form['cnpj']:
			editOrg.cnpj = request.form['cnpj']
		if request.form['nomefantasia']:
			editOrg.nomefantasia = request.form['nomefantasia']
		if request.form['representante']:
			editOrg.representante = request.form['representante']
		if request.form['email']:
			editOrg.email = request.form['email']
		if request.form['endereco']:
			editOrg.endereco = request.form['endereco']
		if request.form['telefone']:
			editOrg.telefone = request.form['telefone']
		if request.form['descricao']:
			editOrg.descricao = request.form['descricao']
		if request.form['missao']:
			editOrg.missao = request.form['missao']
		if request.form['visao']:
			editOrg.visao = request.form['visao']
		if request.form['valores']:
			editOrg.valores = request.form['valores']
		#os novos valores sao passados para o banco
		session.add(editOrg)
		session.commit()
		#mensagem para o usuario informando que os dados foram alterados
		flash("Os dados foram alterados.")
		#a pagina e recarregada com as informacoes atualizadas
		redirect(url_for('editOrganizacao', organizacao_id = organizacao_id))
	#se nao ha dados sendo enviados, a pagina com as informacoes da organizacao e exibida
	else:
		return render_template('edit_organizacao.html', organizacao_id = organizacao_id)

#metodo para excluir um organizacao do banco de dados
@app.route('/adm/organizacao/<int:organizacao_id>/delete', methods=['GET','POST'])
def deleteOrganizacao(organizacao_id):
	#seleciona a organizacao, recuperando-a do banco de dado
	orgToDelete = session.query(Organizacao).filter_by(id=organizacao_id).one()
	#se a solicitacao para deletar e enviada...
	if request.method == 'POST':
		#a organizacao e excluida do banco de dado
		session.delete(orgToDelete)
		session.commit()
		#retorno para o usuario
		flash("Organizacao deletada do banco de dados.")
		#depois de deletar a organizacao o usuario e redirecionado para a lista de organizacoes
		return redirect(url_for('admOrganizacoes'))
	#se o usuario nao confirmou a operacao a pagina delete_organizacao.html e chamada para confirmar
	#a intencao do usuario de deletar a organizacao
	else:
		return render_template('delete_organizacao.html', organizacao_id = organizacao_id)		

#metodo para listar os usuarios cadastrados no site
@app.route('/adm/usuarios')
def admUsuarios():
	#recupera todos os usuarios da base de dados
	usuarios = session.query(Usuario)
	#envia os usuarios encontrados para a pagina que os exibe
	return render_template('adm_usuarios.html', usuarios = usuarios)


#metodo para deletar uma usuario do banco de dados
@app.route('/adm/usuario/<int:usuario_id>/delete', methods=['GET','POST'])
def deleteUsuario(usuario_id):
	#recupera o usuario a ser deletado do banco de dados
	usuarioToDelete = session.query(Usuario).filter_by(id=usuario_id).one()
	#se a solicitacao para deletar e enviada...
	if request.method == 'POST':
		#o usuario e excluido do banco de dados
		session.delete(usuarioToDelete)
		session.commit()
		#informa que a opercacao foi realizada
		flash("Usuario excluido do banco de dados.")
		#o usuario e redirecionado para a lista de usuarios
		return redirect(url_for('admUsuarios'))
	#se o usuario ainda nao confirmou a operacao de deletar a pagina delete_usuario.html
	#e exibida para confirmar a operacao
	else:
		return render_template('delete_usuario.html', usuario_id = usuario_id)

if __name__ == '__main__':
	app.secret_key = '55551993'
	#app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host = '0.0.0.0', port = port)