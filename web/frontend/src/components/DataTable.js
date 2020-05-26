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
import React from 'react'
import { makeStyles } from '@material-ui/core/styles'
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import './DataTable.css'

const useStyles = makeStyles({
    table: {
        maxWidth: 900,
    },
});

export default function DataTable(props){
    const classes = useStyles
        let regions = props.regions;
        for(var i = 0; i < regions.length; i++){
            if(!regions[i].properties.hasOwnProperty('tweet_count')){
                regions.splice(i,1);i--;
            }
            if(regions.length === 0){
                break;
            }
        }
        for(i = 0; i < regions.length; i++){
            if(regions[i]._id > 10000){
                if(regions[i]._id == "12000"){
                    regions[i]._id = 'Sydney'
                }
                if(regions[i]._id === "12601"){
                    regions[i]._id = 'Canberra'
                }
                if(regions[i]._id === "13000"){
                    regions[i]._id = 'Melbourne'
                }
                if(regions[i]._id === "15000"){
                    regions[i]._id = 'Adelaide'
                }
            }
        }
        let counter =0
        return (
            <div id='table_container'>
            <TableContainer>
                <Table className={classes.table}>
                    <TableHead>
                        <TableRow>
                            <TableCell>Area</TableCell>
                            <TableCell >Installations</TableCell>
                            <TableCell >Tweets</TableCell>
                            <TableCell >Ratio</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {regions.map((region) =>(
                            <TableRow key={counter++}>
                                <TableCell>{region._id}</TableCell>
                                <TableCell>{Math.trunc(region.properties["0total_ins"])}</TableCell>
                                <TableCell>{region.properties["tweet_count"]}</TableCell>
                                <TableCell>{region.properties["ratio"].toFixed(2)}</TableCell>
                            </TableRow>
                        )
                        )}
                    </TableBody>
                </Table>
            </TableContainer>
            </div>
        )
}





