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
import { Link } from 'react-router-dom'
import './Header.css'

const Button = (props) => (
    <button >{props.text}</button>
)
//<h1>E</h1><h4>nvironmental </h4><h1>S</h1><h4>ustainability </h4><h1>T</h1><h4>weet </h4><h1>A</h1><h4>nalysis</h4>
const Header = () => {
    return (
        <div className='header'>
            <Link id="heading" to='/'>
                <h1>ESTA</h1><h5>Environmental Sustainability Tweet Analysis</h5>
            </Link>  
            <div className='header-buttons'>
            <Link to='/'>
                <Button text="Home" />
            </Link>
            <Link to='/Suburbs'>
                <Button text="Suburbs" />
            </Link>
            <Link  to='/Analytics'>
                <Button text="Analytics" />
            </Link>
            <Link  to='/Word_Cloud'>
                <Button text="Word Cloud" />
            </Link>
            <Link  to='/Members'>
                <Button text="Members" />
            </Link>
            </div> 
        </div>
    )
}


export default Header;