def statsSecuence(numberList):  
    respuesta = []
    cantidad = 0
    max = 0
    sum = 0
    min = 0
    if not numberList.strip():
        cantidad = 0
        respuesta.append(cantidad)
        respuesta.append(min)
        respuesta.append(max)
        respuesta.append(0)
        return respuesta
    else:
        numberList = numberList.split(" ")
        cantidad = len(numberList)
        min = float(numberList[0])
        i = 0
        while i < cantidad:
            numberList[i] = float(numberList[i])
            if numberList[i] >= max:
                max = numberList[i]
            if numberList[i] <= min:
                min = numberList[i]
            sum += numberList[i]
            i += 1
        respuesta = []
        respuesta.append(cantidad)
        respuesta.append(min)
        respuesta.append(max)
        respuesta.append(sum/cantidad)
        return respuesta

