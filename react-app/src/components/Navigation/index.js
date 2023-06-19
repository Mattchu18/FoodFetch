import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
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
							<div>
								<ProfileButton user={sessionUser} />
							</div>
						)}
					</nav>
					<div className='home-button'>
						<NavLink exact to="/"><img src={homeButtonImage}/> <span style={{ fontFamily: 'Bebas Neue', fontWeight: 'bold' }}>FOODFETCH</span></NavLink>
					</div>
				</div>
				<div className='nav-right'>
					<div className='search-bar'>
							Search bar
					</div>
					<div className='cart'>
						Cart
					</div>
				</div>
			</div>
		</header>
	);
}

export default Navigation;
