## SOpt *telegram bot*
*Bot* do Telegram para o *StackOverFlow* em português (SOpt) 

#### Funcionalidades básicas
* Consulta  e notificação de questões por `tags` e palavras-chaves, exibição no formato:
	* Título, *tag*, e *link* para acesso.

#### Implementações futuras
* Autenticação via *OAuth*, usando a API oficial, para notificação de comentários e votos do usuário logado.

#### Instalação e configuração
1. Instalação das dependências:
`pip install -r requirements.txt`

2. Configuração do *token* de acesso ao *bot*:
	* Criar o diretório `config/`, com o arquivo `token.json`, no formato:
	
	`{"token": "seu_token_aqui"}`
    
    obs: o *token* é gerado quando o *bot* é criado no [*@botfather*](https://telegram.me/BotFather)
3.  Executar o arquivo `src/bot.py`:
                
     `python3 bot.py`
     
Para deixar executando em *background* e independente da sessão do *tty*:

     `nohup python3 bot.py &`
