import server from './configs.js';
import Ajax from './util/ajax.js'
new Vue({
    el:"#sEngine",
    delimiters:['[{','}]'],
    data:{
        search:[
            "Typescript","Duct tape programmer","Formula 1 championship","ReactJs for beginners","James Bond"
        ],
        user_search:"",
        server_call:false,
    },
    methods:{
        match_search(){
            if(this.filter_hist()==false){
                console.log("Consulting server")
                this.consult_server()
            }
        },
        consult_server(){
            console.log(this.user_search)
           ServerSearch.fetch_search(server.baseUrl+"/search/"+this.user_search)
        },
        addToSearch(e){
            var search=document.getElementById("search")
            search.value=e.target.innerHTML
            //console.log(search.innerHTML)
        },
        filter_hist(){
            var found_match=false
            var list=document.querySelectorAll("small.search_h")
            var word=document.getElementById("search").value.toLowerCase()
            list.forEach(elm=>{
                var s_string=elm.innerHTML.toLowerCase()
                if(s_string.indexOf(word)==-1){
                    elm.style.display="none"
                }else{
                    elm.style.display="block"
                    found_match=true
                }
            })
            return found_match
        }
    }
});


class ServerSearch{
    static fetch_search(url){
        var a=new Ajax(url)
        a.fetch_json((data)=>{
            console.log(data.sentence)
        })
    }
}