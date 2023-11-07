var emailField = document.getElementById('email');
var passwordField = document.getElementById('password');

function checkFieldsLogin(){
    if (emailField.value.trim() === '') {
        alert('O campo de email está vazio. Preencha-o antes de enviar.');
        emailField.focus();
        return false
    }else if (passwordField.value.trim() === '') {
        alert('O campo de senha está vazio. Preencha-o antes de enviar.');
        passwordField.focus();
        return false
    }else{
        return true
    }
}

// Listener que verifica a integridade dos dados
document.getElementById('login').addEventListener('submit', function(event) {

    event.preventDefault()

    let checked = checkFieldsLogin()

    if(checked){
        if(emailField.value.trim() === localStorage.getItem("emailUser") && 
        passwordField.value.trim() === localStorage.getItem("passwordUser")){
            window.location = "./perfil.html"
        }else{
            alert("Login incorreto")
        }
    }
    
});

function logout(){
    localStorage.clear()
    window.location = "./index.html"
}

function exibirDados(){
    let nameStorage = localStorage.getItem("nameUser")
    let emailStorage = localStorage.getItem("emailUser")
    let passwordStorage = localStorage.getItem("passwordUser")
    if(nameStorage){
        alert(nameStorage + " " + emailStorage + " " + passwordStorage)
    }else{
        alert("Não encontrado")
    }
}

