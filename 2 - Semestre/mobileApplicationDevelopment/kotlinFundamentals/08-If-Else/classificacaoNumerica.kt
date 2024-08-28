fun main(){
    println("Digite sua idade:")
    val num = readLine();

    var numConverted = num?.toIntOrNull();

    if (numConverted != null) {
        if (numConverted > 0){
            println("O número é positivo.")
        } else if (numConverted < 0){
            println("O numero é negativo")
        } else {
            println("O numero é zero")
        }
    }
}