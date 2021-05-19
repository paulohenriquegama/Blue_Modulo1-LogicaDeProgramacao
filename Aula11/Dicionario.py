familia1 = [('Paulo',29),('Morgania',24),('Hadassa',3)]

familia = dict(familia1)
pais = {'Pai':'Iremi','Mãe':'Odalesa','Irmã':'Alana'}
toda= {}
'''
print(familia1[1][1])
print()
print(familia)
print(familia.get('Hadassa'))'''

for (k,v),(k2,v2) in zip(familia.items(),pais.items()):
    print(k,'-',v)
    print(k2,'-',v2)

print()
    
dele = pais.pop("Irmãa","Não encontrado")
print(pais)
print(f'Deletamos o {dele}')

familia.update(pais)
toda = familia

print(familia)
print(pais)
print(toda)