function addToSearch(e){
    var search=document.getElementById("search")
    search.value=e.target.innerHTML
    console.log(search.innerHTML)
}

function filter_hist(){
    var list=document.querySelectorAll("small.search_h")
    word=document.getElementById("search").value.toLowerCase()
    list.forEach(elm=>{
        var s_string=elm.innerHTML.toLowerCase()
        if(s_string.indexOf(word)==-1){
            elm.style.display="none"
        }else{
            elm.style.display="block"
        }
    })
}

new Vue({
    el:"#sEngine",
    data:{
        search:[
            "Typescript","Duct tape programmer","Formula 1 championship","ReactJs for beginners","James Bond"
        ],
        user_search:""
    },
    methods:{
        match_search:()=>{
            filter_hist()
        }
    }
});