#!/bin/bash
alacritty -e bash -c "python3 /home/leugim/Documentos/GitHub/DynamicAssist/test.py; exec bash"

sleep 1  # Espera o terminal abrir

# Move o terminal para o canto inferior direito (ajuste os valores conforme sua tela)
wmctrl -r "Alacritty" -e 0,1300,750,400,300