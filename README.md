# Instalador de Drivers geral 

## Indice

- [Motivo da Criação](#motivo-da-criação)
- [Status do Projeto](#status-do-projeto)
- [Técnologias utilizadas](#técnologias-utilizadas)
- [Como Atualizar o executavel](#como-atualizar-o-executavel)
- [Contribuidores](#contribuidores)

## Status do Projeto

![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Finalizado-green)

## Motivo da criação: 
Criado instalador para executar varios arquivos .exe de uma unica vez. 
Pois muitas vezes não tem como identificar o modelo do Cartão/Leitor. Para garantir o sucesso no cartão A3
o interessante é intalar todos os drivers.

## Técnologias utilizadas:

* Python
* Pyinstaller

## Como Atualizar o executavel: 

1. Clonar o repositorio:

```git
    git clone https://github.com/patricklohn/instalador-drivers-a3.git
```

2. Ter python instalado na maquina e abrir o terminal do projeto.

3. Instalar o Pyinstaller:

```pip
    pip install pyinstaller
```

4. Efetuar alterações no codigo. 

5. Executar o comando no terminal para atualizar o executavel dentro da pasta dist:

```python
    pyinstaller --onefile install.py
```
6. Pronto arquivo executavel atualizado. 

## Contribuidores

- [Patrick Lohn](https://github.com/patricklohn)



