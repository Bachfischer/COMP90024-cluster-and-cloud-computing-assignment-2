/*
*    
* Part of Assignment 2 - COMP90024 course at The University of Melbourne     
*    
* Cluster and Cloud Computing - Team 24     
*     
* Authors:     
*    
*  * Liam Simon (Student ID: 1128453)    
*  * Rejoy Benjamin (Student ID: 1110935)    
*  * Parikshit Diwan (Student ID: 1110497)    
*  * Colin McLean (Student ID: 1139518)    
*  * Matthias Bachfischer (Student ID: 1133751)    
*    
* Location: Melbourne    
*   
*/
import React from 'react'
import '../components/Analytics.css'
import ImageGallery from 'react-image-gallery'

function importAll(r) {
    return r.keys().map(r);
}
  
const images = importAll(require.context('../images/cloud', false, /\.(png|jpe?g|svg)$/));
let image_collection = images.map(image => {
    console.log(image)
    let title = image.toString()
    title = title.substring(0,title.length -13)
    title = title.replace("/static/media/","").replace("_"," ").replace("_"," ").toUpperCase()
    return {original: image, thumbnail: image, description:title}
})

class Gallery extends React.Component{
    render () {
        return <ImageGallery items={image_collection}/>
    }
}


export default Gallery;