class Ajax{
    constructor(){}
    static get=(url,callback)=>{
        fetch(url)
        .then(res=>{res.json()})
        .then(data=>{callback(data)})
        .catch(err,()=>{
            callback("error")
            console.error(err)
        });
    }
    static post=({url,post_data,callback})=>{
        fetch(url,
            {
                method:"POST",
                data:post_data
            }    
        ).then(res=>{res.json()})
        .then(res=>{callback()})
        .catch((err)=>{
            callback("error")
            console.warn("Error while posting to "+url+" data: ")
            console.warn(post_data)
            console.error(err)
        })
    }
}
export {Ajax}

