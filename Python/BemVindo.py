_Olha meu programa em Python feito para esse repositório_
```
from time import sleep
nome_do_gafanhoto = str(input("Digite seu nome, gafanhoto(a): ")).strip().upper()
sleep(2)
frase = f"{nome_do_gafanhoto.title()}, seja bem-vindo ao meu primeiro arquivo de Python no meu Repositório do GitHub. Aqui começo a minha jornada!"
print("=" * len(frase))
print(frase)
print("=" * len(frase))
sleep(4)
while True:
    choice = str(input(f"Gafanhoto(a) {nome_do_gafanhoto.title()}, você gostaria de saber mais sobre mim? [S/N]: ")).strip()[0]
    sleep(2)
    if choice in "Ss":
        print(f"{nome_do_gafanhoto.title()}, eu me chamo Carlos Alberto da Silva Neto. Você pode me chamar de Neto. Sou apaixonado por qualquer coisa sobre Inteligência Artificial e Python. Outrossim, tenho uma grande ambição e sonho. Ser conhecido nesse mundo da programação e ser o melhor de mim.")
        break
    elif choice in "Nn":
        print(f"{nome_do_gafanhoto.title()}, que pena gafanhoto(a). Quem sabe na próxima! :)")
        break
    else:
        print("Opa, escorregou no botão? Não tem problema! Tente novamente.")
sleep(4)
print("<< Programa finalizado! Obrigado por ser compreensivo e se interessar um pouco por mim >> ")
```
