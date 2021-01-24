var lmode=null;var dmode=null;
const colors=[
    //accent colors box shadows
    {mode:"dark",lcontainers:"#3e3e3e",containers:"#303030",title:"#4040ef",font:"#efefef"},
    {mode:"light",lcontainers:"white",containers:"white",title:"lightseagreen",font:"#797979"},
]

window.onload=function(){
     lmode=document.getElementById("lightmode")
     dmode=document.getElementById("darkmode")
     lmode.addEventListener('click',(e)=>change_mode({mode:"light"}))
     dmode.addEventListener('click',(e)=>change_mode({mode:"dark"}))
     
}

function change_mode({mode}){
    var containers=["body","div","small"]
    var titles=["h1","h2","h3"]
    var lcontainers=["div.auto_predict","input"]
    //special classes var classes=["bright","dull",'accent']
    var m=null
    if(mode=="light"){m=colors[1]}
    else{m=colors[0]}
    change_elements_colors({elements:containers,aspect:"bg",bg:m.containers,fg:m.font})
    change_elements_colors({elements:titles,aspect:"fg",color:m})
    change_elements_colors({elements:lcontainers,aspect:"bg",bg:m.lcontainers,fg:m.font})
}

function change_elements_colors({elements,aspect,color,bg,fg}){
    elements.forEach(c=>{
        var elem=document.querySelectorAll(c)
        elem.forEach(e=>{
            if(aspect=="bg"){
                e.style.background=bg
                e.style.color=fg
            }else{
                e.style.color=color.title
            }
        })
    })
}
