function populateColors(){
    //color:rrggbb
    const hexTerm=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'];
    var genColor=""
    for(var i=0;i<3;i++){
        var last=hexTerm[Math.floor(Math.random()*10)]
        var first="";
        var notDull=false
        while(notDull==false){
            var r=Math.floor(Math.random()*100)
            if(r>5 && r<16){
                notDull=true
                first=hexTerm[r]
            }
        }
        genColor+=first+""+last
    }
    appendColor(genColor)
}
function gen_Color(index,curr){
    const hexTerm=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'];
    var colConf=""
    if(index<2){

    }else if(index<4){

    }else{

    }
}
function appendColor(genColor){
    var container=document.getElementById('colors')
    var divColor=document.createElement('div')
    divColor.classList.add('color')
    divColor.style.background="#"+genColor
    divColor.id=genColor;
    divColor.addEventListener('click',(e)=>{
        var id=e.target.id
        color_selected(id)
    });
    divColor.innerHTML="<h4>#"+genColor+"</h4>";
    h3=document.createElement('h3')
    h3.innerHTML="Copied!"
    divColor.appendChild(h3)
    container.appendChild(divColor)
}
function color_selected(gen_Color){
    var selected=document.getElementById(gen_Color)
    selected.classList.add('selected')
    setTimeout(()=>{remove_selected()},1000)
}
function remove_selected(){
    var colors=document.querySelectorAll('.selected')
    colors.forEach((div)=>{
        div.classList.remove('selected')
        console.log("removed")
    })
}
for(var i=0;i<200;i++){
populateColors()
}





function revealPallete(){
    var pal=document.getElementById('colorPallete')
    pal.classList.remove('hidden')
    pal.classList.add('reveal_from_right')
}