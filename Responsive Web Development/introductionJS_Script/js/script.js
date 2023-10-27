function validar (){
    let nome = document.getElementById("nome")
    let senha = document.getElementById("senha")
    let erroNome = document.getElementById("erroNome")

    if (nome.value == ""){
        nome.focus()
        erroNome.innerText = "O nome é obrigatório"
        return false;
    }
}