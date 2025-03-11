# euComida Backend

## Visão Geral
Este repositório contém a implementação do backend do **euComida**, um serviço de entrega de comida concorrente do iFood. O objetivo é oferecer um backend escalável, seguro e bem documentado, seguindo boas práticas de desenvolvimento.

## Tecnologias Utilizadas
- **Linguagem**: Python
- **Framework**: FastAPI
- **Banco de Dados**: PostgreSQL
- **Autenticação**: JWT (JSON Web Tokens)
- **Documentação**: Swagger (via FastAPI)
- **Containerização**: Docker & Docker Compose

## Arquitetura do Sistema
O sistema segue a arquitetura **MVC** e utiliza padrões **Clean Architecture** e princípios **SOLID** para garantir escalabilidade e manutenibilidade.

### Estrutura do Banco de Dados
O banco de dados é relacional (PostgreSQL) e possui as seguintes tabelas:
- **Usuários**: Tabela que armazena informações dos clientes e entregadores.
- **Pedidos**: Tabela que armazena informações dos pedidos, incluindo o status do pedido (`Em andamento`, `Entregue`, `Cancelado`).
- **Restaurantes**: (opcional para expansão futura) Tabela que pode ser adicionada para armazenar dados de restaurantes parceiros.

### Estratégia de Autenticação
A autenticação será baseada em **JWT**, garantindo que os usuários e entregadores possam acessar os endpoints protegidos de forma segura. Os tokens JWT são gerados no momento do login e enviados para o cliente, que os utiliza em requisições subsequentes.

### Estratégia de Escalabilidade e Segurança
- **Rate Limiting**: Implementação de limites de requisições para prevenir abusos do sistema.
- **CORS Policy**: Configuração para permitir apenas domínios confiáveis, garantindo maior segurança.
- **Logs estruturados**: Usados para monitorar e auditar a aplicação, facilitando a detecção de falhas e comportamentos indesejados.
- **Cache (Redis)**: Usado para armazenar em cache consultas frequentes e melhorar a performance do sistema.

## Decisões Técnicas Tomadas

### 1. Framework FastAPI
A escolha do **FastAPI** foi feita devido à sua alta performance, simplicidade de uso e suporte nativo à documentação interativa via **Swagger**. Além disso, o FastAPI suporta de forma eficiente a validação de dados com **Pydantic** e integra-se bem com **SQLAlchemy** para interagir com bancos de dados relacionais.

### 2. Banco de Dados Relacional (PostgreSQL)
Optamos pelo **PostgreSQL** devido à sua robustez, confiabilidade e excelente suporte para dados relacionais. Ele é amplamente utilizado em sistemas de produção, o que garante estabilidade e escalabilidade.

### 3. Autenticação com JWT
A autenticação será feita utilizando **JWT (JSON Web Tokens)**, uma escolha comum para sistemas modernos. O JWT permite que os usuários e entregadores sejam autenticados de maneira segura, evitando a necessidade de armazenar informações sensíveis como senhas diretamente no servidor. Além disso, o uso de tokens JWT facilita a escalabilidade da aplicação.

### 4. Containerização com Docker
A aplicação foi containerizada utilizando **Docker** e **Docker Compose** para garantir que o ambiente de desenvolvimento e produção seja o mais consistente possível. Isso permite que a aplicação seja facilmente executada em qualquer máquina com Docker instalado, além de garantir isolamento e controle de versões das dependências.

### 5. Padrões de Desenvolvimento
- **Clean Architecture**: A arquitetura do sistema segue o princípio de **Clean Architecture**, o que ajuda a manter o código bem estruturado e fácil de testar, além de garantir que a aplicação seja facilmente escalável no futuro.
- **Princípios SOLID**: A aplicação foi construída seguindo os princípios SOLID, garantindo que o código seja modular, fácil de manter e expandir.

### 6. Escalabilidade e Segurança
- **Rate Limiting**: Implementação de **Rate Limiting** para prevenir abusos da API. Embora não tenha sido configurado de forma explícita no código atual, a configuração está prevista para ser implementada em um futuro próximo.
- **CORS Policy**: A configuração do **CORS** foi feita para permitir apenas domínios confiáveis, garantindo que apenas clientes autorizados possam consumir a API.
- **Logs estruturados**: **Logs estruturados** serão utilizados para monitorar a aplicação e garantir que as falhas possam ser rastreadas de forma eficiente.

## Como Rodar o Projeto

### Requisitos
Antes de rodar o projeto, verifique se você tem os seguintes requisitos em sua máquina:

- **Docker**: O Docker deve estar instalado para permitir a criação e execução dos containers.
- **Docker Compose**: Ferramenta para definir e rodar aplicações multi-container, que facilita a configuração e execução do ambiente de desenvolvimento.
  
### Instalação do Docker
Se você ainda não tem o Docker instalado, siga as instruções abaixo de acordo com seu sistema operacional:

- **[Instalar Docker no Windows](https://docs.docker.com/desktop/install/windows-install/)**
- **[Instalar Docker no macOS](https://docs.docker.com/desktop/install/mac-install/)**
- **[Instalar Docker no Linux](https://docs.docker.com/desktop/install/linux-install/)**

Após a instalação, verifique se o Docker está funcionando corretamente executando o seguinte comando no terminal:
docker --version

1. Clone este repositório:
   ```sh
   git clone https://github.com/LucasSantosReis/ecomida.git
   cd eucomida
2. docker-compose up --build

3. Acesse a documentação da API em:
http://localhost:8000/docs


### Como Contribuir

Faça um fork deste repositório.
Crie uma branch para a sua feature:
git checkout -b feature/nome-da-feature
Faça suas alterações e comite-as:
git commit -am "Adiciona nova feature"
Envie a branch para o repositório remoto:
git push origin feature/nome-da-feature
Abra um Pull Request no GitHub para revisar suas alterações.
Documentação Interativa

Você pode acessar a documentação da API através do Swagger:

Acesse: http://localhost:8000/docs para uma interface interativa que permite testar as rotas diretamente no navegador.