casa = float(input('Digite o valor do imóve R%'))
salário = float(input('Digite o valor do seu salário R%'))
prazo = float(input('Digite o prazo em anos: '))
prestação = casa / (prazo * 12)
if prestação > salário / 100 * 30:
    print(f'\n\033[31m===EMPRÉSTIMO NEGADO===\033[m\n\nO valor da prestação ficaria R${prestação:.2f}. A mensalidade não pode ultrapassar 30% do seu salário.')
else:
    print(f'\n\033[34m==EMPRÉSTIMO APROVADO===\033[m\n\nA prestação será de R${prestação:.2f}.')