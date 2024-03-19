import React, {useState} from "react";

const ExampleComponent2 : React.FC = () => {

    const [text, setText] = useState('')
    const [text2, setText2] = useState('')

    const handleChange = (setValue: React.Dispatch<React.SetStateAction<string>>) => 
        (event: React.ChangeEvent<HTMLInputElement>) => {
            setValue(event.target.value)
    }

    return (
        <>
            <p><b>Digite um texto: </b><input type="text" onBlur={ handleChange(setText) }/></p>
            <p><b>Conteudo Digitado: {text}</b></p>
            <p><b>Digite um texto: </b><input type="text" onBlur={ handleChange(setText2) }/></p>
            <p><b>Conteudo Digitado: {text2}</b></p>
        </>
    )
}

export default ExampleComponent2