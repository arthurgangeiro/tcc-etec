__author__ = "Arthur Grangeiro de Souza"
__credits__ = ["Arthur Grangeiro de Souza"]
__version__ = "0.9.1"
__maintainer__ = "Arthur Grangeiro de Souza"
__email__ = "arthurgrangeiro@outlook.com"
__status__ = "Prototype"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_project import Base, Cartao, DadosBancarios, Usuario, Organizacao 

engine = create_engine('sqlite:///projeto.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Organizacao cadastradas inicialmente na base de dados
organizacao1 = Organizacao(ativo = "1", 
							cnpj = "Ainda nao cadastrado", 
							razaosocial = "Ainda nao cadastrada", 
							nomefantasia = "Cursinho Popular Vira Mundo",
							representante = "Amanda Ventura", 
							endereco = "Rua Valter Souza Costa, 147 - Jardim Primavera, Ferraz de Vasconcelos", 
							telefone = "11 - 23874113", 
							email = "cpviramundo@gmail.com",
							site = "https://cpviramundo.wixsite.com/viramundo",
							facebook = "https://www.facebook.com/cpviramundo/",
							doacao = "#",
							logo = "images/logo_viramundo.png",
							imagem = "images/imagem_viramundo.png",
							sobre = "Cursinho Popular para os moradores de Ferraz.",
							descricao = "O Cursinho Popular Vira Mundo e constituido por voluntarios, realizamos uma importante missao de preparar estudantes de escolas publicas para a carreira universitaria, preparando para os vestibulares e ENEM, e para alem disso realizamos debates, eventos culturais e visitas tecnicas. Acreditamos na educacao como mecanismos de transformacao social.")
session.add(organizacao1);
session.commit();

organizacao2 = Organizacao(ativo = "1", 
							cnpj = "Ainda nao cadastrado", 
							razaosocial = "Ainda nao cadastrada", 
							nomefantasia = "Casa Boto Rosa",
							representante = "Thaina", 
							endereco = "Rua santa Marcelina, 586 - Carmosina, Sao Paulo", 
							telefone = "11 - 23857559", 
							email = "casabotorosa.thaiana@gmail.com",
							site = "https://www.casabotorosa.org/",
							facebook = "https://www.facebook.com/casaabrigobotorosa/",
							doacao = "https://www.casabotorosa.org/",
							logo = "images/logo_botorosa.png",
							imagem = "images/imagem_botorosa.png",
							sobre = "Abrigo para criancas com cancer.",
							descricao = "Hoje queremos uma casa com a cara do Norte, pois acreditamos fielmente que o conforto e aconchego proporcionados pelo sentimento de lar e essencial para um tratamento de sucesso no caso de cancer.")
session.add(organizacao2);
session.commit();

organizacao3 = Organizacao(ativo = "1",
							cnpj = "Ainda nao cadastrado",
							razaosocial = "Ainda nao cadastrada", 
							nomefantasia = "Casa do Cristo",
							representante = "Mariana Laferreira", 
							endereco = "Rua Agrimenso Sugaya, 00 - Colonia, Sao Paulo", 
							telefone = "11 - 25236222", 
							email = "contato@casadocristoredentor.org.br",
							site = "http://www.casadocristo.org.br/",
							facebook = "https://www.facebook.com/casadocristo",
							doacao = "http://www.casadocristo.org.br/doar-agora",
							logo = "images/logo_casadocristo.png",
							imagem = "images/imagem_casadocristo.png",
							sobre = "Assistencia para toda a comunidade.",
							descricao = "A Casa do Cristo e uma instituicao assistencial sem fins lucrativos, instalada em uma area de 170.000 metros quadrados com ruas asfaltadas, rede  eletrica e de esgoto,  reservatorio de agua,  possuindo  um belo  bosque,  horta e pomar. Dentro desta pequena cidade existem varios projetos para atender a comunidade local.")
session.add(organizacao3);
session.commit();

usuario1 = Usuario(cpf = "12345678910", nome = "Elizabete dos Santos Lima", email= "lisbeth.santos@gmail.com",
					senha = "securepassword", telefone = "1146796145", endereco = "Av. Gov. Janio Quadros, 2000 - Parque Sao Francisco, Ferraz de Vasconcelos")
session.add(usuario1);
session.commit();

print "A little confuse DB created..."