var lmode=null;var dmode=null;
const colors=[
    //accent colors box shadows
    {mode:"dark",containers:"#303030",title:"#4040ee",font:"#efefef"},
    {mode:"light",containers:"white",title:"lightseagreen",font:"#a9a9a9"},
]

window.onload=function(){
     lmode=document.getElementById("lightmode")
     dmode=document.getElementById("darkmode")
     lmode.addEventListener('click',(e)=>change_mode({mode:"light"}))
     dmode.addEventListener('click',(e)=>change_mode({mode:"dark"}))
     
}

function change_mode({mode}){
    var containers=["body","div"]
    var titles=["h1","h2","h3"]
    //special classes var classes=["bright","dull",'accent']
    var m=null
    if(mode=="light"){m=colors[1]}
    else{m=colors[0]}
    change_elements_colors({elements:containers,aspect:"bg",color:m.containers})
    change_elements_colors({elements:titles,aspect:"fg",color:m.title})
}

function change_elements_colors({elements,aspect,color}){
    elements.forEach(c=>{
        var elem=document.querySelectorAll(c)
        elem.forEach(e=>{
            if(aspect=="bg"){
                e.style.background=color
            }else{
                e.style.color=color
            }
        })
    })
}
