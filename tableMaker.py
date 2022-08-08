#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rich.console import Console
from rich.table import Table

class TableMaker:
    def __init__(self) -> None:
        self.console = Console()
        self.tabela = Table(show_header=True , show_lines= True , style= 'bold')

    def Header(self,nomes_das_colunas:list):
        for n in nomes_das_colunas:
            self.tabela.add_column(f"{n}")
        self.console.print(self.tabela)
        return self.tabela

    def Print(self,content,colour="white"):
        self.console.print(f'''[{colour}] {content} [/{colour}]''')

if __name__ == "__main__":
    lista2 = ["[green]Nome[/green]","Idade","Classe","Raça"]
    tabela = TableMaker().Header(lista2)
