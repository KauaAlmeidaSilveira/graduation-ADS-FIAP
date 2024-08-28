fun main (){

    println("________________________________")
    println("Bem vindo a Lanchonete do Vinny")
    val precoCoxinha = 5.00 
    val qntCoxinha = 3
    val precoCerveja = 15.00
    val qntCerveja = 2

    var somaCoxinhas = precoCoxinha * qntCoxinha
    var somaCervejas = precoCerveja * qntCerveja
    var somatorio = somaCervejas + somaCoxinhas
    val taxa = (somaCervejas + somaCoxinhas) * 0.1
    var total = somaCervejas + somaCoxinhas + taxa

    println("________________________________")
    println("Comanda:")
    println("________________________________")
    println("3 Coxinhas \t\t\t R$ %.2f".format(somaCoxinhas))
    println("2 Cervejas \t\t\t R$ %.2f".format(somaCervejas))
    println("Total Produtos \t\t R$ %.2f".format(somatorio))
    println("Taxa \t\t\t\t R$ %.2f".format(taxa))
    println("________________________________")
    println("Total \t\t\t\t R$ %.2f".format(total))
    

}