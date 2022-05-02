#  Projeto Backend para a emissão de certificados na DEX.

---

#### Neste projeto será utilizado o ``django`` e o ``Django REST framework``, para a criação da api,
o banco de dados conterá duas tabelas além da padrão denominadas ``Eventos`` e ``Nomes``, no qual o 
evento armazena os dados que será mostrado no certificado e a de nome armazenará os nomes e sua relação 
com a tabela de Eventos através de uma chave primária. Com o django rest framework, foi criado duas rotas 
para o acesso aos dados pelo front end, as mesmas denominadas de eventos e nomes.

Para acessar o deploy [clique aqui!](https://dexbackend.herokuapp.com/).
