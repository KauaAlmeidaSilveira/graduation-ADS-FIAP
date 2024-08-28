fun main () {
    val idade = 30
    val possuiCnh = true;

    if ( idade >= 18 && possuiCnh ){
        println("Esta habilitado!!")
    } else {
        println("Não esta habilitado!!")
    }

    val temIngresso = false;
    val estaComCamisa = true;

    if ( temIngresso || estaComCamisa ) {
        println("Pode entrar")
    } else {
        println("Não pode entrar")
    }
}