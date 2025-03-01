#!/bin/bash

# Ativar o ambiente virtual
source /home/leugim/Documentos/GitHub/DynamicAssist/chatbot/rasa_env/bin/activate

# Verificar se a ativação do ambiente foi bem-sucedida
if [ $? -ne 0 ]; then
    echo "Falha ao ativar o ambiente virtual."
    exit 1
fi

# Rodar o servidor do Rasa
rasa run --enable-api --cors "*" > rasa.log 2>&1 &
echo "Rasa está rodando..."
