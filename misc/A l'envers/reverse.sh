#!/bin/bash

# Création de pipes temporaires
PIPE_IN=$(mktemp -u)
PIPE_OUT=$(mktemp -u)
mkfifo "$PIPE_IN" "$PIPE_OUT"

# Démarre netcat en arrière-plan avec redirection via les FIFOs
nc localhost 4000 <"$PIPE_IN" >"$PIPE_OUT" &
NC_PID=$!

# File descriptor pour écrire dans PIPE_IN
exec 3>"$PIPE_IN"
# File descriptor pour lire dans PIPE_OUT
exec 4<"$PIPE_OUT"

while true; do
    if ! read -r next_line <&4; then
        echo "Connexion fermée par le serveur."
        break
    fi
    echo "Reçu: $next_line"
    
    if [ "$next_line" == "Congratulations!! Here is your flag:" ]; then
        read -r next_line <&4
        echo $next_line
    fi


    next_line=$(echo ${next_line:4})
    reversed=$(echo "$next_line" | rev)
    echo "Envoi: $reversed"
    echo "$reversed" >&3

    if ! read -r reward <&4; then
        echo "Connexion fermée par le serveur."
        break
    fi

    echo "Réponse: $reward"


    if [ "$reward" != "Well done, continue!" ]; then
        break
    fi

done

# Nettoyage
kill $NC_PID 2>/dev/null
exec 3>&-
exec 4<&-
rm -f "$PIPE_IN" "$PIPE_OUT"
