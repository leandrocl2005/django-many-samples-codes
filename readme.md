# Django tutoriais

## Como configurar o ambiente
- Criar ambiente virtual: `python -m venv env`
- Ativar ambiente virtual: `. env/Scripts/activate`
- Instalar o django: `pip install django`

## Como criar um projeto
- Criar o projeto: `django-admin startproject core .`

## Configurando os templates

- Criar a pasta *templates* na raíz do projeto
- Apontar templates para essa pasta no settings.

## Configurando os arquivos estáticos

- Criar a pasta *templates/static* na raíz do projeto
- Apontar estáticos para essa pasta no settings.

## Migrações iniciais

- Fazer migrações: `python manage.py migrate`
- Criar superuser: `python manage.py createsuperuser`

## APP HOME

Este app tem a finalidade de servir como um redirecionador para outros apps. 

- Criar o app: `python manage.py startapp home`
- Adicionar app no arquivo *core/settings.py*
- Criar o arquivo *home/urls.py*
- Incluir o path para *home/urls.py* em *core/urls.py*
- Criar a url para home em *home/urls.py*
- Criar a view para home em  *home/views.py*
- Criar o template *templates/home.html*
- Criar o css *templates/static/home/css/home.css*
- Linkar template com css

## APP Quotes Crud

Este app tem a finalidade de estudar o CRUD.

- Criar o app: `python manage.py startapp quotescrud`
- Adicionar app no arquivo *core/settings.py*

- Criar o modelo de citações
- Fazer as migrações

- Adicionar modelo ao admin

- Criar o arquivo *quotescrud/urls.py*
- Incluir o path para *quotescrud/urls.py* em *core/urls.py*

- Criar a view para lista de citações em  *home/views.py*
- Criar a url para lista de citações em *quotescrud/urls.py*

- Criar a view para deleção de citações em  *home/views.py*
- Criar a url para deleção de citações em *quotescrud/urls.py*

- Criar a view para criação de citações em  *home/views.py*
- Criar a url para criação de citações em *quotescrud/urls.py*

- Criar a view para edição de citações em  *home/views.py*
- Criar a url para edição de citações em *quotescrud/urls.py*

- Criar o template *templates/quotescrud/index.html*
- Criar o css *templates/static/quotescrud/css/main.css*
- Linkar template com css