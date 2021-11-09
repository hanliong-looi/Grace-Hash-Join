import React, {useState} from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { PostgreSQL, sql } from '@codemirror/lang-sql';
import { Typography, Button } from 'antd';
import './index.css'

const {Title} = Typography

const Container:React.FC = () => {
    const [query, setQuery] = useState('')

    const onclick = () => {
        fetch("/api/get_query",{
            method: 'POST',
            cache:'no-cache',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({query}) 
        })
        .then(response => response.json())
        .then(data => console.log(data));
    }
   
    return (
        <div className="main-container">
            <div className="schema-container"> Database Schema </div>
            <div className="sql-container">
                <Title style={{margin:'auto'}} level={3}>SQL Query</Title>
                <CodeMirror
                    value={query}
                    height={'300px'}
                    onChange={value => setQuery(value)}
                    extensions={[sql({dialect: PostgreSQL})]}
                    />
                <Button onClick={onclick}>Annotate Query</Button>
            </div>
            <div className="plan-container">
                <Title level={3}>Execution Plan</Title>
            </div>

        </div>
    )
}
export default Container