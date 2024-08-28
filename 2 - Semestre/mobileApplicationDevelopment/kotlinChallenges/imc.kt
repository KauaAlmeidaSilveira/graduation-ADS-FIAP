import java.util.*

val scanner = Scanner(System.`in`)

fun main() {
    while (true) {
        println(coletarDados())
        println("Deseja calcular novamente? Sim ou Não")
        val resp = scanner.next()[0]

        if (resp.uppercase() != "S") {
            break
        }
    }
}

fun coletarDados(): String {
    println("Insira o peso: ")
    val peso = scanner.nextDouble()
    println("Insira a altura: ")
    val altura = scanner.nextDouble()

    return "Seu IMC é: " + imc(peso, altura)
}

fun imc(peso: Double, altura: Double): String {
    val imc = peso / (altura * altura)
    
    return when {
        imc < 16.9 -> "Muito abaixo do peso"
        imc in 17.0..18.4 -> "Abaixo do peso"
        imc in 18.5..24.9 -> "Peso normal"
        imc in 25.0..29.9 -> "Acima do peso"
        imc in 30.0..34.9 -> "Obesidade grau 1"
        imc in 35.0..40.0 -> "Obesidade grau 2"
        else -> "Obesidade grau 3"
    }
}
