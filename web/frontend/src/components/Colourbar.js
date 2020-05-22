import React from 'react'
import './Colourbar.css'

const ColourBar = () => {
    return (
        <div>
            <div id='bar_container'>
                <p id='title'>Tweet to installation</p>
                <div id='gradient'></div> 
                <p id='lower'>Lower</p>
                <p id='higher'>Higher</p>
            </div>
        </div>
    )
}


export default ColourBar;