def v_media(media: int | float) -> str:
    """essa função retorna se o aluno passou ou nao de ano                         """
    if media >= 7:
        return("aprovado")
    elif media <5:
        return("reprovado")
    elif media >= 5 and media < 7:
        return("recuperação")          
    elif media <0 and media > 10:
        return("digite um numero entre 0 a 10")
    
if __name__ == "__main__":
    print(v_media(7))
