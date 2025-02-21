```
 _____                              _                       _     _   
|  __ \                            (_)        /\           (_)   | |     Tecnlogias: Framework Rasa, Ollama Gamma
| |  | |_   _ _ __   __ _ _ __ ___  _  ___   /  \   ___ ___ _ ___| |_    Sistema Operacional: feito no Linux
| |  | | | | | '_ \ / _` | '_ ` _ \| |/ __| / /\ \ / __/ __| / __| __|   Python: 3.10.12
| |__| | |_| | | | | (_| | | | | | | | (__ / ____ \\__ \__ \ \__ \ |_ 
|_____/ \__, |_| |_|\__,_|_| |_| |_|_|\___/_/    \_\___/___/_|___/\__|
         __/ |                                                        
        |___/          
```
Este projeto implementa um chatbot utilizando o framework Rasa. O chatbot é capaz de responder perguntas e interagir com os usuários de forma dinâmica, tendo iterface para minimizar quando a conversa acabar.

---

### Funcionalidades
- Recebe entradas de texto e gera respostas automatizadas.
- Pode ser integrado com diferentes plataformas de comunicação.
- Permite treinamento de modelos de linguagem personalizados.
- Funciona por `systemd` sendo iniciado pelo `start_assistente.sh` assim que sua maquina estiver ligada.

### Configuração de Icone
Para o meu monitor que de 1024x768 60hz, o `root.geometry` encontrado no `widget` é de ("50x50+970+718"), mais pode variar de monitor.

![personaliz](https://github.com/user-attachments/assets/a094a6c3-7197-4177-8a9a-3d900ee1f80a)

### Configuração no systemd
Assim que instalar lembrar de reiniciar:
```bash
sudo systemctl daemon-reload
```

```bash
sudo systemctl restart assistente.service
```


### Instalação
1. Clone este repositório:

```bash 
git clone https://github.com/1mperador/DynamicAssist.git
```

2. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```
3. Treine o modelo do Rasa:

```bash
rasa train
```
4. Inicie o servidor do Rasa:

```bash
rasa run
```

# Teste o Chatbot
Para testar o chatbot localmente, execute o seguinte comando:
```bash
rasa shell
```
Isso permitirá que você interaja com o chatbot diretamente no terminal.

# Use para ligar a assistente
```bash
rasa run --enable-api

```
Assim ele permitira que a rasa funcione por api


# Contribuições
Sinta-se à vontade para contribuir com melhorias ou corrigir bugs. Abra um pull request com suas alterações.

---
