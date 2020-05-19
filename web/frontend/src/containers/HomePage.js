import React from 'react';
import { compose, withProps } from "recompose"
import * as Nano from 'nano'
import { useAsync } from 'react-async'
import {View} from 'react-native-web'
import { 
  Polygon,
  GoogleMap,
  withScriptjs,
  withGoogleMap
  } from "react-google-maps"

let counter = 0
class MapSetup extends React.Component {
  constructor(props) {
    super(props)      
    this.state = { 
      counter: 0,
      regions: null};
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
      if(coordArrOuter[0] instanceof(Array)){
        return (
          coordArrOuter.map(coord => (
          <Polygon
            key = {counter++}
            paths ={coord}
            options={{
              strokeColor: '#fc1e0d',
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
              strokeColor: '#fc1e0d',
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
  async callAPI() {
    let message = await fetch("http://backend:8000/test")
    let text = await message.json()
    console.log(text)
    //this.setState({regions: text})
  }
  async get_all(){
    let message = await fetch("http://backend:8000/get_all")
    let text = await message.json()
    console.log(text)
    this.setState({regions: text})
  }


  async componentDidMount() {
      this.callAPI();
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
    <div>{this.state.regions && <this.Map/>}</div>
    )
  }

}
export default MapSetup;