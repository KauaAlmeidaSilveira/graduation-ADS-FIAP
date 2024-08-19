fun main(){

    val par = arrayOf(0,2,4,6);
    val impar = arrayOf(1,3,5,7);

    var num = mutableListOf<Int>();

    for(i in 0..3){
        num.add(par[i])
        num.add(impar[i])
    }

    for (num in num){
        println(num)
    }

}