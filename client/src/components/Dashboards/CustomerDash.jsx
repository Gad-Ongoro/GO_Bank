import React from 'react';
import { Routes, Route } from 'react-router-dom';
import AnimatedYPage from '../AnimatedYPage';
import SideNav from './SideNav';
import NavBar from './NavBar';
import DashView from './DashView';
import Settings from './Settings';

function CustomerDash() {
	return (
		<AnimatedYPage>
		<div className='container h-screen grid grid-cols-12'>
			<div className='sticky top-10 col-start-2 col-end-13 backdrop-blur'>
				<NavBar></NavBar>
			</div>
			<div className='sticky top-20 sm:top-10 bg-gray-900 rounded col-start-1 col-end-13 row-start-1 row-end-2 md:fixed md:top-1/2 md:-translate-y-1/2 md:row-start-2 md:row-end-13'>
				<SideNav></SideNav>
			</div>
			<div className='row-start-2 row-end-13 col-start-1 md:col-start-2 col-end-13'>
				<Routes>
					<Route path='/dashview' element={<DashView></DashView>}></Route>
					<Route path='/settings' element={<Settings></Settings>}></Route>
				</Routes>
			</div>
		</div>
		</AnimatedYPage>
	)
}

export default CustomerDash;