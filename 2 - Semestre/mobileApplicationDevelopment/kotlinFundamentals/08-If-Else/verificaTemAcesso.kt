
val User = {
    
}

fun main(){


    println("Nome: ")
    val name = readLine();
    println("Senha: ")
    val senha = readLine();

    if(name == "vinny" && senha == "123456"){
        println("Você esta autorizado !!")
    } else {
        println("Você não esta autorizado !!") 
    }

}