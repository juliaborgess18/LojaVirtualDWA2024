<<<<<<< HEAD
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from repositories.categoria_repo import CategoriaRepo
=======
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
>>>>>>> aae658d356c8ba08adc33219f8cb390ce4cb0981
from repositories.usuario_repo import UsuarioRepo
from repositories.item_pedido_repo import ItemPedidoRepo
from repositories.pedido_repo import PedidoRepo
from repositories.produto_repo import ProdutoRepo
<<<<<<< HEAD
from routes import auth_routes, main_routes, cliente_routes, admin_routes
from util.auth_jwt import (
    checar_autorizacao,
    checar_autenticacao,
    configurar_swagger_auth,
)
from util.exceptions import configurar_excecoes

load_dotenv()
CategoriaRepo.criar_tabela()
CategoriaRepo.inserir_categorias_json("sql/categoria.json")

=======
from routes import main_routes, cliente_routes, admin_routes
from util.auth import checar_permissao, middleware_autenticacao
from util.exceptions import configurar_excecoes

>>>>>>> aae658d356c8ba08adc33219f8cb390ce4cb0981
ProdutoRepo.criar_tabela()
ProdutoRepo.inserir_produtos_json("sql/produtos.json")
UsuarioRepo.criar_tabela()
UsuarioRepo.inserir_usuarios_json("sql/usuarios.json")
PedidoRepo.criar_tabela()
ItemPedidoRepo.criar_tabela()
<<<<<<< HEAD
app = FastAPI(dependencies=[Depends(checar_autorizacao)])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware("http")(checar_autenticacao)
configurar_excecoes(app)
app.include_router(main_routes.router)
app.include_router(cliente_routes.router)
app.include_router(admin_routes.router)
app.include_router(auth_routes.router)
configurar_swagger_auth(app)
=======
app = FastAPI(dependencies=[Depends(checar_permissao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware(middleware_type="http")(middleware_autenticacao)
configurar_excecoes(app)
app.include_router(main_routes.router)
app.include_router(cliente_routes.router)
app.include_router(admin_routes.router)
>>>>>>> aae658d356c8ba08adc33219f8cb390ce4cb0981
