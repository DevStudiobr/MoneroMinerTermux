#!/bin/bash

# Atualizar Termux e instalar dependências
pkg update && pkg upgrade -y
pkg install git cmake make clang -y
pkg install termux-exec

# Clonar e instalar o XMRig
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake ..
make

echo "XMRig instalado com sucesso!"
