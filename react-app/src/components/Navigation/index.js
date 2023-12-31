import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import Search from "../Search/Search"
import homeButtonImage from "../../imgs/homeButtonImage.png"
import './Navigation.css';

function Navigation({ isLoaded }) {
	const sessionUser = useSelector(state => state.session.user);

	return (
		<header>
			<div className='nav-row'>
				<div className='nav-left'>
					<nav>
						{isLoaded && (
							<div className='profile-dropdown-div'>
								<ProfileButton user={sessionUser} />
							</div>
						)}
					</nav>
					<div className='home-button'>
						<NavLink exact to="/"><img src={homeButtonImage}/> <span style={{ fontFamily: 'Bebas Neue', fontWeight: 'bold' }}>FOODFETCH</span></NavLink>
					</div>
				</div>
				<div className='nav-right'>
					<Search/>
					{/* <div className='cart'>
						Cart
					</div> */}
				</div>
			</div>
		</header>
	);
}

export default Navigation;
