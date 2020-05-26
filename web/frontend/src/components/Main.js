import React from 'react';
import { Switch, Route } from 'react-router-dom'

import HomePage from '../containers/HomePage'
import MembersPage from '../containers/MembersPage'
import Suburbs from '../containers/Suburbs'

const Main = () => {
  return (
      <Switch>
          <Route 
            exact path='/' component={HomePage}>
          </Route>
          <Route exact path='/Members' component={MembersPage}></Route>
          <Route exact path='/Suburbs' component={Suburbs}></Route>
      </Switch>
  );
}

export default Main