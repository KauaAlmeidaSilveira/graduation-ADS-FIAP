fun main() {
    var result = somaDosQuadrados(5f, 10f)
    println("A soma dos quadrados e igual a = $result")
}

fun somaDosQuadrados(a:Float, b:Float): Float{
    var sum = ((a*a) + (b*b));
    return sum;
}

