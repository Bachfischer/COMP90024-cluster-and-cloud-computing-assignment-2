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
  withGoogleMap,
  InfoWindow
  } from "react-google-maps"

import ColourBar from '../components/Colourbar'
import DataTable from '../components/DataTable'
let counter = 0
class MapSetup extends React.Component {
  constructor(props) {
    super(props)      
    this.state = { 
      counter: 0,
      regions: null,
      initital: null,
      selectedCentre: false,
      centre:{ lat:  -35.037633,lng: 144.739408} 
    }
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
          defaultZoom={7}
          defaultCenter={this.state.centre}
        >
          {this.renderRegions()}
        </GoogleMap>
      )

  renderRegions(){
    return this.state.regions.map(regionJ =>{
      if(regionJ._id < 10000){
        return(<Polygon key={counter++}/>)
      }
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
      console.log(regionJ._id,regionJ.properties.ratio)
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
      console.log(regionJ._id,regionJ.properties.ratio)
      console.log(colour)
      if(coordArrOuter[0] instanceof(Array)){
        return (
          coordArrOuter.map(coord => (
          <Polygon
            onMouseOver={this.setState({selectedCentre: true})}
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
          >
            {
              this.state.selectedCentre && (<InfoWindow
                onCloseClick={() =>{
                  this.setState({selectedCentre:false})
                }}
                position={{
                  lat:  -35.037633,lng: 144.739408
                }}
                >
              </InfoWindow>)
            }
          </Polygon>
          ))
          
        )
      }
      else{
        let coord = coordArrOuter
        return (
          <Polygon
            onMouseOver={this.setState({selectedCentre: true})}
            key = {counter++}
            paths ={coord}
            onClick={this.setState({selectedCentre:true})}
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
          >
            {
              this.state.selectedCentre && (<InfoWindow
                onCloseClick={() =>{
                  this.setState({selectedCentre:false})
                }}
                position={{
                  lat:  -35.037633,lng: 144.739408
                }}
                >
              </InfoWindow>)
            }
          </Polygon>
        )
      }
      }
    )

  }
  async get_all(){
    let message = await fetch("http://172.26.130.40:8000/get_all_cities")
    let text = await message.json()
    console.log(text)
    this.find_ratio(text)
    let init = JSON.parse(JSON.stringify(text))
    this.setState({initial: init})}

  async find_ratio(pcs){
    let suburbs = await pcs
    let min_ratio = 1000000
    let max_ratio = 0
    let pc_ratio = []
    suburbs.forEach(suburb =>{
      let temp = JSON.parse(JSON.stringify(suburb))
      console.log(temp._id,temp.properties.ratio)
      let temp_ratio = suburb.properties.ratio
      if(temp_ratio > max_ratio){
        max_ratio = temp_ratio 
      }
      if(temp_ratio < min_ratio){
        min_ratio = temp_ratio 
      }
    pc_ratio.push([suburb._id,suburb.properties.ratio])
    })
    pc_ratio.forEach(pc =>{
      let top = pc[1] - min_ratio
      let bottom = max_ratio - min_ratio
      let z = (top/bottom)
      console.log("pc",pc[0],z,"top",top,"bottom",bottom)
      pc[1] = 255*z
    })
    console.log(pc_ratio)
    suburbs.forEach(suburb =>{
      pc_ratio.forEach(pc =>{
        let id = suburb._id
        if(id === pc[0]){
          suburb.properties.ratio = pc[1]
        }
      })
    })
    console.log(suburbs)
    this.setState({regions: suburbs})
  }

  async componentDidMount() {
      this.get_all();
  }

  render(){
    if(this.state.regions && this.state.initial){
      return(
        <div>
          <div>
            <div>{this.state.regions && <this.Map/>}</div>
          </div>
          <div>
            <ColourBar/>
            <DataTable regions={ this.state.initial}/>
          </div>
        </div>
      )
    }
    else{
        return(
          <div id="big-body">
            <div id='loader-div'>
              <div class='loader'></div>
            </div>
            <ColourBar/>
          </div>
        )
    }
  }

}

export default MapSetup;