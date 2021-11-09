import React from 'react';
import { Typography} from 'antd';
import Container from './container'
import './App.css';

// const test_input = 'select * from customer C, orders O where C.c_custkey = O.o_custkey;'
const { Title } = Typography;
const App = () => {

    return (
        <div className="App" style={{padding: 20}}>
            <Title>Query Execution Plan Annotator - Group 41</Title>
            <Container/>
        </div>
)};

export default App;