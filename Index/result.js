function detector(parameter){
    result = ""
    if(parameter === 0){
        result = "Hate speech detected";
    }else if(parameter === 1){
        result = "Text is neutral";
    }
    document.getElementById("decission").innerHTML = result;
}
