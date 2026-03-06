def v_media(media: int | float) -> str:
    """essa função retorna se o aluno passou ou nao de ano"""
    #verificando se é uma string. O raise faz ele dar erro direto
    if not isinstance(media,(int,float)):
        raise TypeError("Tipo inválido, a entrada deve ser numerica")
    
    #verificando se o numero é menor que 0, se for ele vai printar um erro de valor
    if media <0:
        raise ValueError("Valor invalido, entrada tem que ser maior que 0")
    
    #verificando se o numero é maior que 10, se for printa erro de valor
    if media >10:
        raise ValueError("Valor invalido, entrada tem que ser menor que 10")
    
    #verificando se maior que 7 aprovado
    if media >= 7:
        return "aprovado"
    
    #verificando se menor que 4 é reprovado
    elif media <=4:
        return "reprovado"
    #se nao estiver nos criterios acima vai pra recuperação
    else:
        return "recuperação"      
    
   
if __name__ == "__main__":
    print(v_media(7))
