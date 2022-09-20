A aplicação consiste no cadastro de clientes, empresas, ofertas e lances. Onde é possível realizar o cadastro e visualização deles através de uma página html ou por
outro aplicativo como o insomnia.

De início, me preocupei mais em entender a parte relacionado ao Django buscando referências para poder desenvolver a solução e em seguida estudo mais relacionado
ao JavaScript.

É possível fazer diversas melhorias, principalmente, em relação a parte de tratamento de erros. Como, por exemplo, retornar com mais clareza para o usuário onde está 
o erro. Poderia também ser desenvolvido um algoritmo para relacionar os melhores lances em relação as ofertas, visto que ambos recebem diversos parâmetros.
Poderia ser desenvolvida uma interface para visualizar cada oferta separada com os lances realizados para cada uma.
No algoritmo, a visualização ficou simples e resumida a uma tabela.

Ao executar o comando "python manage.py runserver" no terminal, será possível acessar os seguintes endereços.

Visualizar (get):
http://localhost:8000/offert
http://localhost:8000/bid
http://localhost:8000/client
http://localhost1:8000/company

Cadastrar (post):
http://localhost:8000/offert/post
http://localhost:8000/bid/post
http://localhost:8000/client/post
http://localhost:8000/company/post

Atenciosamente, Rafael Fontenele
