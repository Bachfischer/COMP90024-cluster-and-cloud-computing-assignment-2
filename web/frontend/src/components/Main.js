import React from 'react';
import { Switch, Route } from 'react-router-dom'

import HomePage from '../containers/HomePage'
import MembersPage from '../containers/MembersPage'
import Suburbs from '../containers/Suburbs'
import Analytics from '../containers/Analytics'
import Word_Cloud from '../containers/Word_Cloud'

const Main = () => {
  return (
      <Switch>
          <Route 
            exact path='/' component={HomePage}>
          </Route>
          <Route exact path='/Members' component={MembersPage}></Route>
          <Route exact path='/Suburbs' component={Suburbs}></Route>
          <Route exact path='/Analytics' component={Analytics}></Route>
          <Route exact path='/Word_Cloud' component={Word_Cloud}></Route>
      </Switch>
  );
}

export default Main