# AeroTweet

AeroTweet é um clone simplificado do Twitter desenvolvido com fins educacionais.

O projeto permite cadastro de usuários, login, edição de perfil, criação de tweets, curtidas, comentários, sistema de seguir usuários e feed personalizado com tweets das pessoas seguidas.

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- HTML
- CSS
- Render
- Cloudinary

## Funcionalidades

- Cadastro de usuário
- Login e logout
- Edição de perfil
- Upload de foto de perfil
- Alteração de senha
- Exclusão de conta
- Criação de tweets
- Edição e exclusão de tweets
- Curtidas em tweets
- Comentários em tweets
- Sistema de seguir e deixar de seguir usuários
- Lista de seguidores
- Lista de seguindo
- Feed com tweets dos usuários seguidos e do próprio usuário
- Interface responsiva
- API REST


## Como executar o projeto

### 1. Clone o repositório

```bash
git clone git@github.com:maluucodes/twitter-clone-ebac.git
cd twitter-clone-ebac
```

### 2. Crie e ative um ambiente virtual

**Windows**

```bash
python -m venv env
env\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para um novo arquivo chamado `.env` e preencha os valores necessários.

### 5. Inicie o banco de dados

```bash
docker compose up -d
```

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. Crie um superusuário (opcional, para acessar o painel administrativo)

```bash
python manage.py createsuperuser
```

Informe:

```text
Username:
Email:
Password:
Password (again):
```

### 8. Inicie o servidor

```bash
python manage.py runserver
```

### 9. Acesse a aplicação

Aplicação:

```text
http://127.0.0.1:8000/
```

Painel administrativo:

```text
http://127.0.0.1:8000/admin/
```