
conversion = [
	[ ["a", "A"], 0 ],
	[ ["b", "B"], 1 ],
	[ ["c", "C"], 2 ],
	[ ["d", "D"], 3 ],
	[ ["e", "E"], 4 ],
	[ ["f", "F"], 5 ],
	[ ["g", "G"], 6 ],
	[ ["h", "H"], 7 ],
	[ ["i", "I"], 8 ],
	[ ["j", "J"], 9 ],
	[ ["k", "K"], 10 ],
	[ ["l", "L"], 11 ],
	[ ["m", "M"], 12 ],
	[ ["n", "N"], 13 ],
	[ ["ñ", "Ñ"], 14 ],
	[ ["o", "O"], 15 ],
	[ ["p", "P"], 16 ],
	[ ["q", "Q"], 17 ],
	[ ["r", "R"], 18 ],
	[ ["s", "S"], 19 ],
	[ ["t", "T"], 20 ],
	[ ["u", "U"], 21 ],
	[ ["v", "V"], 22 ],
	[ ["w", "W"], 23 ],
	[ ["x", "X"], 24 ],
	[ ["y", "Y"], 25 ],
	[ ["z", "Z"], 26 ]
]

def cifrado():
	mensaje = input("Escribe un mensaje: ")
	clave = int(input("Introduce la clave: "))
	decisión = input("¿Deseas encriptar (e) o desencriptar (d)?: ")
	longitud = len(mensaje)
	traduccion = [] 

	for j in range(longitud):
		c = mensaje[j]
		for k in range(27):
			if c in conversion[k][0]:
				if decisión == 'e':
					num = (conversion[k][1] + clave) % 27
					for m in range(27):
						if num == conversion[m][1] and conversion[k][0].index(mensaje[j])==1:
							traduccion.append(conversion[m][0][1])
						elif num == conversion[m][1] and conversion[k][0].index(mensaje[j])==0:
							traduccion.append(conversion[m][0][0])
				elif decisión == 'd':
					num = (conversion[k][1] - clave) % 27
					for m in range(27):
						if num == conversion[m][1] and conversion[k][0].index(mensaje[j])==1:
							traduccion.append(conversion[m][0][1])
						elif num == conversion[m][1] and conversion[k][0].index(mensaje[j])==0:
							traduccion.append(conversion[m][0][0])
			elif c==' ':
				traduccion.append(' ')



	print("Resultado:", "".join(traduccion))

cifrado()