anne = int ( input ( "Donne une anne : " ) )

if anne % 4 == 0 and anne % 100 == 0 or anne % 400 == 0:
    print (f"L'anne {anne} est bissextile ")
else:
    print(f"L'anne {anne} n'est pas bissextile ")