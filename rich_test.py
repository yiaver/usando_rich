#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rich.table import Table
from rich.console import Console
########
console = Console()

#tabela 
tabela = Table(show_header = True , header_style = 'bold',show_lines= True)
tabela.add_column ("Nome:",style="red",header_style= "red")
tabela.add_column ("Idade:",style="blue",header_style= "blue")
tabela.add_column ("Raça:",style="green",header_style= "green")
tabela.add_column ("Classe:",style="magenta",header_style= "magenta")

def cria_table_rpg(Nome = str , idade = str, raça =str ,classe = str):
    tabela.add_row(Nome,idade,raça,classe)
    return console.print(tabela)

while True:
    console.print('''
[blue]Comandos:[/blue]
[red]sair : Sai do progama.[/red]
[green]criar: Cria um Personagem.[/green]''')
    
    comandos = input("< ")
    
    if comandos == "sair" or comandos == "Sair":
        break
    
    elif comandos == "Criar" or comandos == "criar":
        nome=console.input("Digite o [red]Nome[/red] do jogador: ")
        idade=console.input("[blue]Idade[/blue] do jogador: ")
        race=console.input("[green]Raça[/] do jogador: ")
        classe=console.input("[magenta]Classe[/magenta] do jogador: ")
        a = cria_table_rpg(f"{nome}",f"{idade}",f"{race}",f"{classe}")
    
    else:
        console.print("Algo de errado Não esta certo!")


