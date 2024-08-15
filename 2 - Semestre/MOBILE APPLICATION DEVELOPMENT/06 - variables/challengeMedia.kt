fun main(){

    println("Digite a 1º nota: ");
    val n1 = readLine()!!.toDouble();

    println("Digite a 2º nota: ");
    val n2 = readLine()!!.toDouble();

    println("Digite a 3º nota: ");
    val n3 = readLine()!!.toDouble();

    val media = (n1+n2+n3)/3;

    println(String.format("%.2f", media));

}