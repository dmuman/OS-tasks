#!/bin/bash

if [ $# -lt 1 ]
then 
  echo "Erro: falta pelo menos um argumento"
  exit 1
fi

POS=0
ZERO=0
NEG=0

sinal(){
    if [ $1 -lt 0 ]
    then
      echo "$1 é um número inteiro negativo"
      let "NEG=NEG+1"
    elif [ $1 -eq 0 ]
    then 
      echo "$1 é o número zero"
      let "ZERO=ZERO+1"
    else
      echo "$1 é um número inteiro positivo"
      let "POS=POS+1"
    fi
}


for i in $@
do
  sinal $i
done

echo $NEG $ZERO $POS