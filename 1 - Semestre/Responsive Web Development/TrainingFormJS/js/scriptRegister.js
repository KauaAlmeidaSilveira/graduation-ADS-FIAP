var nameField = document.getElementById('name');
var emailField = document.getElementById('email');
var passwordField = document.getElementById('password');

function checkFieldsCadastro(){
    if (nameField.value.trim() === '') {
        alert('O campo de nome está vazio. Preencha-o antes de enviar.');
        nameField.focus();
        return false
    }else if (emailField.value.trim() === '') {
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
document.getElementById('register').addEventListener('submit', function(event) {
    let checked = checkFieldsCadastro()
    
    if(checked){
        localStorage.setItem("nameUser",nameField.value);
        localStorage.setItem("emailUser",emailField.value);
        localStorage.setItem("passwordUser",passwordField.value);
    }
});

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


