import React from 'react';
import Header from './Header';
import { default as Main } from './Main'
import './App.css'

const App = () => {
  return (
    <div>
      <Header/>
      <div className='site-content'>
        <Main/>
      </div>
    </div>
  );
}

export default App;
