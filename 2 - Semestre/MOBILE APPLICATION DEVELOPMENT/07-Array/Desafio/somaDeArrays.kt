fun main(){

    val par = arrayOf(2,4,6);
    val impar = arrayOf(1,3,5);

    var num = mutableListOf<Int>();

    for(i in 0..2){
        num.add(impar[i])
        num.add(par[i])
    }

    for (num in num){
        println(num)
    }

}