import React from 'react';
import {Layout, Typography} from 'antd';
import Container from './container'
import './App.css';

// const test_input = 'select * from customer C, orders O where C.c_custkey = O.o_custkey;'
const { Title } = Typography;
const { Header } = Layout
const App = () => {

    return (
        <div className="App">
            <Header style={{display: 'flex', alignItems:'center', backgroundColor:'#fff', boxShadow: "0 2px 8px #f0f1f2"}}>
                <Title style={{marginBottom: 0}} level={2}>QEP Annotator - Group 41</Title>
            </Header>
            <div style={{padding: '20px 40px'}}>
                <Container/>
            </div>
        </div>
)};

export default App;