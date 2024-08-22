#!/bin/bash

if [ $# -ne 1 ]
then 
  echo "Erro: inserir exatamento um argumento"
  exit 1
fi

SOMA=0

for ((i = 0; i<$1; i++ ))
do
  echo -n "Insira um número: "
  read N
  let "SOMA=SOMA+N"
done

echo "Soma: $SOMA"