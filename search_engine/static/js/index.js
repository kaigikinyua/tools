loadHistory()

function loadHistory(){
    var history=["Typescript","Duct tape programmer","Formula 1 championship","ReactJs for beginners","James Bond"]
    var parent=document.getElementById("auto_predict")
    history.forEach((h)=>{
        var capsule=document.createElement("small")
        capsule.innerHTML=h
        capsule.addEventListener('click',(e)=>{addToSearch(e);console.log(e.target.innerHTML)})
        parent.appendChild(capsule)
    })
}

function addToSearch(e){
    var search=document.getElementById("search")
    search.value=e.target.innerHTML
    console.log(search.innerHTML)
}