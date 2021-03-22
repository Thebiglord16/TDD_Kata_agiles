def statsSecuence(numberList):
    numberList = numberList.split(" ")
    cantidad = len(numberList)
    i = 1
    max = float(numberList[0])
    min = float(numberList[0])
    sum = float(numberList[0])
    while i < cantidad:
        numberList[i] = float(numberList[i])
        if numberList[i] > max:
            max = numberList[i]
        if numberList[i] < min:
            min = numberList[i]
        sum += numberList[i]
        i += 1
    respuesta = []
    respuesta.append(cantidad)
    respuesta.append(min)
    respuesta.append(max)
    respuesta.append(sum/cantidad)
    return respuesta


