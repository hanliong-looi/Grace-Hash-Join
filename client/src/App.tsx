import React from 'react';
import { Button } from 'antd';
import './App.css';

const App = () => {
    function onclick(){
        fetch("/api/get_query")
        .then(response => response.json())
        .then(data => console.log(data));
    }

    return (
        <div className="App">
            <Button onClick={onclick} type="primary">Button</Button>
            With Antd
        </div>
)};

export default App;