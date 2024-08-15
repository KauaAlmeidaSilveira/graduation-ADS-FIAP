fun main() {

    println("Qual o tipo de temperatura ? (C - Celsius, K - Kelvin, F - Fahrenheit)")
    val typeTemp = readLine()!!

    println("Digite a temperatura: ")
    val temp = readLine()!!.toDouble()

    println("Deseja converter para que tipo ? (C - Celsius, K - Kelvin, F - Fahrenheit)")
    val typeTempToConvert = readLine()!!

    val resultConvert = convertTemp(temp, typeTemp[0].toUpperCase(), typeTempToConvert[0].toUpperCase())

    println(resultConvert)
}

fun convertTemp(temp: Double, typeActualTemp: Char, typeToConvert: Char): Double {
    return if (typeActualTemp == 'C') {
        if (typeToConvert == 'F') {
            temp * 9 / 5 + 32
        } else{
            temp + 273.15
        }
    } else if (typeActualTemp == 'K') {
        if (typeToConvert == 'F') {
            1.8 * (temp - 273) + 32
        } else{
            temp - 273.15
        }
    } else {
        if (typeToConvert == 'K') {
            (temp + 459.67) * 5 / 9
        } else{
            (temp - 32) / 1.8
        }
    }
}
