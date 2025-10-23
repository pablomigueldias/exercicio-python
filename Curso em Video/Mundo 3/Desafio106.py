#faça um mini sistema que utilize o interactive help do python. o usuario vai digitar o comando e o manual
# vai aparecer quando o usuario digitar a palavra 'fim' o programa se encerrará.
#obs: use cores

# Mini sistema de ajuda interativa com cores
# Digite o nome de uma função, classe ou módulo (ex.: print, len, str, list, math)
# Digite 'fim' para encerrar.

from time import sleep

C = {
    "limpa": "\033[m",
    "titulo": "\033[1;44m",   
    "sub": "\033[1;45m",     
    "erro": "\033[1;41m",     
    "texto": "\033[0;97m",    
    "help": "\033[7;97m",     
}

def barra(msg: str, cor_inicio: str) -> None:
    print(cor_inicio + " " * (len(msg) + 4) + C["limpa"])
    print(cor_inicio + f"  {msg}  " + C["limpa"])
    print(cor_inicio + " " * (len(msg) + 4) + C["limpa"])

def ajuda(comando: str) -> None:
    barra(f"Acessando o manual do '{comando}'", C["sub"])
    sleep(0.3)
    print(C["help"], end="")  
    help(comando)
    print(C["limpa"], end="") 

def pyhelp() -> None:
    while True:
        barra("SISTEMA DE AJUDA PyHELP", C["titulo"])
        cmd = input(C["texto"] + "Função ou Biblioteca > " + C["limpa"]).strip()
        if cmd.lower() in ("fim", "exit", "quit"):
            barra("Até logo!", C["titulo"])
            break
        if cmd == "":
            barra("Entrada vazia. Tente novamente.", C["erro"])
            sleep(0.6)
            continue
        ajuda(cmd)

# Programa principal
if __name__ == "__main__":
    pyhelp()
