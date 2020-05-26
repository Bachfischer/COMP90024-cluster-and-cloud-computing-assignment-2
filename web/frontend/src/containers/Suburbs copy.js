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
import React, { useState } from 'react';
import { compose, withProps } from "recompose"
import { 
  Polygon,
  GoogleMap,
  withScriptjs,
  withGoogleMap
  } from "react-google-maps"

import ColourBar from '../components/Colourbar'
import DataTable from '../components/DataTable'
import '../components/Home.css'

let locations = [
  ["Sydney",-33.87,151.20,0],
  ["Melbourne", -38.0,145.1,2],
  ["Adelaide",-34.92,138.6,3],
  ["Canberra",-35.28,149.13,1],
  ["Brisbane",-27.46,153.02,4]
]
let counter = 0
class MapSetup extends React.Component {
  constructor(props) {
    super(props)      
    this.state = { 
      counter: 0,
      regions: null,
      cities: null,
      initial: null,
      centre:{coord:{ lat:  -38.0,lng: 145.1},area:2} ,
      change: false
    };
  }
  Map = compose(
      withProps({
        googleMapURL: "https://maps.googleapis.com/maps/api/js?key=AIzaSyCQ1Ys3Sw7bLIhLhtIoTSB2vupL1ZjZOko&v=3.exp&libraries=geometry,drawing,places",
        loadingElement:<div style ={{height: '800px' }}/>,
        containerElement: <div style ={{height: '800px' }}/>,
        mapElement: <div style ={{height: '100%' }}/>,
      }),
      withScriptjs,
      withGoogleMap
      )((props) => 
        <GoogleMap
          defaultZoom={9}
          center={this.state.centre.coord}
        >
          {console.log(this.state.centre.coord)}
          {this.renderRegions()}
        </GoogleMap>
      )
  renderRegions(){
    return this.state.cities[this.state.centre.area].map(regionJ =>{
      console.log(this.state.centre.area)
      //let region = JSON.parse(JSON.stringify(regionJ))
      let coordinates = regionJ.geometry.coordinates
      let coordArrOuter = []
      let coordArrInner = []
      coordinates.map((coordinate) => {
        coordArrInner = []
        if(coordinate[0] instanceof(Array)){
          if(coordinate[0][0] instanceof(Array)){
            coordinate[0].map((coordinner) => {
              coordArrInner.push({lat:coordinner[1],lng:coordinner[0]})
            })
          }
          else{
            coordinate.map(coord => coordArrInner.push({lat:coord[1],lng:coord[0]}))
          }
        }
        else{
          coordArrInner.push({lat:coordinate[1],lng:coordinate[0]})
        }
        coordArrOuter.push(coordArrInner)
      })
      
      let num = Math.floor(regionJ.properties.ratio)
      num = 255 -num
      let red,blue,green = 0
      if(num < 16){
        green = '0'.concat(num.toString(16))
        blue = '0'.concat(num.toString(16))
      }
      else{
        green = num.toString(16)
        blue = num.toString(16)
      }
      red = 'ff'
      let colour = '#'.concat(red).concat(green).concat(blue)
      console.log(colour)
      if(coordArrOuter[0] instanceof(Array)){
        return (
          coordArrOuter.map(coord => (
          <Polygon
            key = {counter++}
            paths ={coord}
            options={{
              strokeColor: '000000',
              strokeOpacity: 5,
              strokeWeight: 1,
              fillColor: colour,
              fillOpacity: 0.8,
              icons: [{
                icon: "hello",
                offset: '0',
                repeat: '10px'
              }]
            }}
          />
          ))
          
        )
      }
      else{
        let coord = coordArrOuter
        return (
          <Polygon
            key = {counter++}
            paths ={coord}
            options={{
              strokeColor: '000000',
              strokeOpacity: 5,
              strokeWeight: 1,
              fillColor: colour,
              fillOpacity: 0.8,
              icons: [{
                icon: "hello",
                offset: '0',
                repeat: '10px'
              }]
            }}
          />
        )
      }
      }
    )

  }
  async get_all(){
    let message = await fetch("http://localhost:4000/get_all_suburbs")
    let text = await message.json()
    console.log(text)
    this.find_ratio(text)
    let init = JSON.parse(JSON.stringify(text))
    this.setState({initial: init})
  }

  async find_ratio(pcs){
    let suburbs = await pcs
    let split_suburbs = [[],[],[],[],[]]
    suburbs.forEach(suburb=>{
      let id = suburb._id
      if((id >=2000 && id <=2599)||(id >= 2619 && id<=2899)||(id >= 2921 && id<=2999)){
        split_suburbs[0].push(suburb)
      }
      else if((id >= 2600 && id<=2618)||(id >= 2900 && id<=2920)){
        split_suburbs[1].push(suburb)
      }
      else if((id >= 3000 && id<=3999)){
        split_suburbs[2].push(suburb)
      }
      else if((id >= 4000 && id<=4999)){
        split_suburbs[3].push(suburb)
      }
      else if((id >= 5000 && id<=5999)){
        split_suburbs[4].push(suburb)
      }
    })
    let counter = 0
    split_suburbs.forEach(city =>{
      console.log(city)
      let min_ratio = 1000000
      let max_ratio = 0
      let pc_ratio = []
      city.forEach(suburb =>{
        let temp_ratio = suburb.properties.ratio
        if(temp_ratio > max_ratio){
          max_ratio = temp_ratio 
        }
        if(temp_ratio < min_ratio){
          min_ratio = temp_ratio 
        }
        pc_ratio.push([suburb._id,temp_ratio])
      })
      pc_ratio.forEach(pc =>{
        let z = 255 *((pc[1]/(max_ratio)))
        pc[1] = z
      })
      split_suburbs[counter].forEach(suburb =>{
        pc_ratio.forEach(pc =>{
          let id = suburb._id
          if(id === pc[0]){
            suburb.properties.ratio = pc[1]
          }
        })
      })
    })
    this.setState({cities: split_suburbs},console.log(this.setState.cities))
  }

  async componentDidMount() {
      //this.callAPI();
      this.get_all();
  }
  /*
  changeCentre = (update_lat,update_lng) => {
    console.log(update_lat,update_lng)
      this.setState({
        centre:{ lat:  update_lat,lng: update_lng} ,
        change: true
      },() => 
      console.log(this.state.centre))
  }
  */
  delayedShowMarker = () => {
    setTimeout(() => {
      this.setState({ isMarkerShown: true })
    }, 3000)
  }

  handleMarkerClick = () => {
    this.setState({ isMarkerShown: false })
    this.delayedShowMarker()
  }
  render(){
    if(this.state.initial && this.state.cities){ 
      if(this.state.change === false){
        return(
          <div>
            <div id='wrapper'>
            <div id="map">{ this.state.cities && <this.Map/>}</div>
            <div id="loc-buttons">
              {locations.map(location =>{
                return(
                  <button id="move" onClick={() =>{
                    this.setState({centre:{coord:{ lat:  location[1],lng: location[2]},area: location[3]} ,change: true,})}}
                  >
                    {location[0]}
                  </button>
                )
              })}
            </div>
            </div>
            <ColourBar/>
            <DataTable regions={this.state.initial}/>
          </div>
        )
      }
      else{
        this.setState({change: false})
        return(
          <div>

            <div id = "map"><this.Map/></div>
            <div id="loc-buttons">
              {locations.map(location =>{
                return(
                  <button id={location[0]} onClick={() =>{
                    this.setState({centre:{ lat:  location[1],lng: location[2]} ,change: true,})}}
                  >
                    {location[0]}
                  </button>
                )
              })}
            </div>
            <ColourBar/>
            <DataTable regions={this.state.initial}/>
          </div>

        )
      }
    }
    else{
        return(
          <div id="big-body">
          </div>
        )
    }
  }

}

export default MapSetup;