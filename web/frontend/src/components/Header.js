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

const Header = () => {
    return (
        <div className='header'>
            <Link id="heading" to='/'>
                <h1>CCC Assignment</h1>
            </Link>  
            <div className='header-buttons'>
            <Link to='/Suburbs'>
                <Button text="Suburbs" />
            </Link>
            <Link  to='/Members'>
                <Button text="Members" />
            </Link>
            </div> 
        </div>
    )
}


export default Header;