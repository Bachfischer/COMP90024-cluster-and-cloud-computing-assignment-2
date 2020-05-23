import React from 'react'
import { Link } from 'react-router-dom'
import './Header.css'

const Button = (props) => (
    <button >{props.text}</button>
)

const Header = () => {
    return (
        <div className='header'>
            <Link to='/'>
                <h1>CCC Assignment</h1>
            </Link>  
            <Link className='header-buttons' to='/Members'>
                <Button text="Members" />
            </Link>
            <Link className='header-buttons' to='/Suburbs'>
                <Button text="Suburbs" />
            </Link>
        </div>
    )
}


export default Header;