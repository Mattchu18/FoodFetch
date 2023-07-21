import React from 'react';
// import { Link } from 'react-router-dom';
import "./index.css"

const Footer = ({ isLoaded }) => {


    return (
        <div className='footer-container'>
            <div className='footer-icons'>
                <li><a href="https://github.com/Mattchu18"><i class="fa-brands fa-github"></i><span class="label"> GitHub</span></a></li>
                <li><a href="https://www.linkedin.com/in/matt-aung/"><i class="fa-brands fa-linkedin"></i><span class="label"> Linkedin</span></a></li>

            </div>
        </div>
    )
}

export default Footer
