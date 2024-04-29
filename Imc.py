def imc():
    try:
     peso = float(input("Peso (em kg): "))
     altura = float(input("Altura (em metros): ")) 
     if peso <= 0 and altura <= 0:
        raise ValueError("Os valores tem que ser positivos") 
     imc = peso/(altura**2)
     return imc
    except ValueError as e:
        print(f"Erro: {e}") 
        return None
        
def interpretar_imc(imc):
    if imc is None :
        return "Não foi possível calcular o imc pois os valores são inválidos. "
        
    elif imc < 18.5:
        return "Você está abaixo do peso. "    
        
    elif imc < 25:
        return "Seu peso está normal. " 
        
    elif imc < 30:
        return "Você está acima do peso. " 
        
    else:
        return "Você está obeso. "         
 
def main() :
  resultado = imc() 
  if resultado is not None:
    print(f"Seu imc é : {resultado:.1f}")
    print(interpretar_imc(resultado)) 
    
main()    
