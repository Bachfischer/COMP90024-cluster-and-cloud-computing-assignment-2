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
  
const images = importAll(require.context('../images/analytics', false, /\.(png|jpe?g|svg)$/));
let image_collection = images.map(image => {
    return {original: image, thumbnail: image}
})

class Gallery extends React.Component{
    render () {
        return (
            <div>
                <ImageGallery id="image" items={image_collection}/>
                <p>*Polarization is in the range -1 to 1 and subjectiveity 0 to 1. These are calculated using the TexTBlob python library where -1 means negative statement and 1 means positive statment, and where 0.0 is very objective and 1.0 is very subjective respectively.</p>

            </div>
        )
    }
}


export default Gallery;