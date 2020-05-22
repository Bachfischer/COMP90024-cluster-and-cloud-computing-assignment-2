import React from 'react';
import { compose, withProps } from "recompose"
import { useAsync } from 'react-async'
import { 
  Polygon,
  GoogleMap,
  withScriptjs,
  withGoogleMap
  } from "react-google-maps"

import ColourBar from '../components/Colourbar'
let counter = 0
class MapSetup extends React.Component {
  constructor(props) {
    super(props)      
    this.state = { 
      counter: 0,
      regions: null,
      min_ratio: 0,
      max_ratio: 0};
  }
  Map = compose(
      withProps({
        googleMapURL: "https://maps.googleapis.com/maps/api/js?key=AIzaSyCQ1Ys3Sw7bLIhLhtIoTSB2vupL1ZjZOko&v=3.exp&libraries=geometry,drawing,places",
        loadingElement:<div style ={{height: '100%' }}/>,
        containerElement: <div style ={{height: '800px' }}/>,
        mapElement: <div style ={{height: '100%' }}/>,
      }),
      withScriptjs,
      withGoogleMap
      )((props) => 
        <GoogleMap
          defaultZoom={9}
          defaultCenter={{ lat:  -38.0,lng: 145.1}}
        >
          {this.renderRegions()}
        </GoogleMap>
      )

  renderRegions(){
    return this.state.regions.map(regionJ =>{
      //let region = JSON.parse(JSON.stringify(regionJ))
      let coordinates = regionJ.geometry.coordinates
      let coordArrOuter = []
      let coordArrInner = []
      coordinates.map(coordinate => {
        coordArrInner = []
        if(coordinate[0] instanceof(Array)){
          if(coordinate[0][0] instanceof(Array)){
            coordinate[0].map(coordinner => {
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
      let colour = regionJ.properties.ratio.toString(16).join('0000')
      if(coordArrOuter[0] instanceof(Array)){
        return (
          coordArrOuter.map(coord => (
          <Polygon
            key = {counter++}
            paths ={coord}
            options={{
              strokeColor: colour,
              strokeOpacity: 1,
              strokeWeight: 2,
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
              strokeColor: colour,
              strokeOpacity: 1,
              strokeWeight: 2,
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
  /*
  async callAPI() {
    let message = await fetch("http://172.26.130.163:8000/test")
    let text = await message.json()
    console.log(text)
    //this.setState({regions: text})
  }
  */
  async get_all(){
    let message = await fetch("http://172.26.130.163:8000/get_all")
    let text = await message.json()
    console.log(text)
    this.find_ratio(text)
  }

  find_ratio(suburbs){
    let min_ratio = 1000000
    let max_ratio = 0
    let pc_ratio = []
    for(let i = 0; i=suburbs.length();i++){
      let temp_ratio = suburbs[i].properties.ratio
      if(temp_ratio > max_ratio){
        max_ratio = temp_ratio 
      }
      if(temp_ratio < min_ratio){
        min_ratio = temp_ratio 
      }
      pc_ratio.push([suburbs._id,temp_ratio])
    }
    for(let i = 0; i=pc_ratio.length();i++){
      pc_ratio[i][1] = 255 *((pc_ratio[i][1] - min_ratio)/(max_ratio-min_ratio))
    }
    for(let i = 0; i=suburbs.length();i++){
      for(let j = 0; i=suburbs.length();i++){
        if(suburbs[i]._id === pc_ratio[j][0]){
          suburbs[i].properties.ratio = pc_ratio[j][1]
          break 
        }
      }
    }
    this.setState({regions: suburbs})
  }


  async componentDidMount() {
      //this.callAPI();
      this.get_all();
  }

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
    return(
      <div>
        <div>{this.state.regions && <this.Map/>}</div>
        <ColourBar/>
      </div>
    )
  }

}
export default MapSetup;