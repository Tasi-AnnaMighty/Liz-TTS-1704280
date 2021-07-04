function speak(){
    var data = document.getElementById("type").value;
   // var file =document.getElementById("file").value;
    //eel.tokenize(data)(callBack);
    eel.speak(data)();

}

function getUrl(){
    var article = document.getElementById("link").value;
            eel.urlspeak(article)();
}

function filespeak(){
    
    var file= document.getElementById("ans").value;
    ///console.log(upload);
    eel.speak(file)();
}

function read()
{
    var files= document.getElementById("file").files;
    var file=files[0];
    var reader= new FileReader();
    reader.onload=function(evt){
        //Prints contents of first file to the console
        document.getElementById("ans").value=(evt.target.result)
    }
    reader.readAsBinaryString(file);
}

async function getFolder(){
    var dosya_path = await eel.open_file()();
        if (dosya_path) {
            console.log(dosya_path);
        }
    }

// function callback(data){
//      var audio = new Audio(data)
//      audio.play()
// }