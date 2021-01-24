export default class Ajax{
    url=null
    constructor(url){
        this.url=url
    }
    fetch_json(callback){
        fetch(this.url)
        .then(res=>res.json())
        .then(data=>callback(data))
        .catch(e=>{console.log(e)})
    }
    // post_json(data){
        // fetch(this.url,
        // {method:"POST",data:data}
        // )
    // }
}