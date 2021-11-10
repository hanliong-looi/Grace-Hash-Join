import React, {useState} from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { PostgreSQL, sql } from '@codemirror/lang-sql';
import { Typography, Button, Input, message } from 'antd';
import ReactFlow from 'react-flow-renderer';
import './index.css'

const {Title} = Typography
const {TextArea} = Input
const Container:React.FC = () => {
    const [query, setQuery] = useState('')
    const [plan, setPlan] = useState('')
    const [graph, setGraph] = useState<any[]>([])
    const [graphVisible, setGraphVisible] = useState(false)

    const buildGraphElements = (graphPlan: any) => {
        let elements: any[] = []
        const edges: { id: string; type: string; source: string; target: string; }[] = []
        let root = graphPlan.Plan
        let id = 0 
        const xOffset = Math.floor(window.innerWidth / 2) - 115 
        function dfs(root:any, x: number, y: number, parent?:number):void{
            let node_id = id
            id++
            const type = 'default'
            elements.push({
                id: `${node_id}`,
                data: {label: root['Node Type']},
                position: {x: x + xOffset, y},
                draggable: false,
                type
            })
            if(parent !== undefined){
                edges.push({
                    id: `${parent}-${node_id}`,
                    type: 'straight',
                    source: `${parent}`,
                    target: `${node_id}`,
                })
            }

            if(root.Plans !== undefined){
                if (root.Plans.length === 1){
                    dfs(root.Plans[0], x, y + 100, node_id)
                } else if (root.Plans.length === 2){
                    dfs(root.Plans[0], x - 125, y + 100, node_id)
                    dfs(root.Plans[1], x + 125, y + 100, node_id)
                }
            }
        }
        console.log(graphPlan)
        dfs(root, 0, 10)
        console.log('created graph', [...elements, ...edges])
        setGraph([...elements, ...edges])
    }
    const onclick = () => {
        if(query.length < 1){
            message.error('SQL Query must not be empty')
            return
        }
        
        fetch("/api/get_query",{
            method: 'POST',
            cache:'no-cache',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({query}) 
        })
        .then(response => response.json())
        .then(data => {
            setPlan('')
            setGraphVisible(false)
            setGraph([])
            if(data.error !== 0){
                message.error(data.error_message)
                return
            }
            const plan_raw = data.instructions
            let temp = ""
            console.log(data.instructions)
            for(let i = 0; i < plan_raw.length; i++){
                temp += `Step ${i+1}: ${plan_raw[i]} \n`
            }
            setPlan(temp)
            buildGraphElements(data.plan)
        });
    }
    const onclear = () => {
        setQuery('')
        setPlan('')
        setGraph([])
        setGraphVisible(false)
    }
    return (
        <>
        <div className="main-container">
            <div className="sql-container">
                <Title level={3}>SQL Query</Title>
                <CodeMirror
                    value={query}
                    height={'300px'}
                    onChange={value => setQuery(value)}
                    extensions={[sql({dialect: PostgreSQL})]}
                    placeholder={'Input SQL Query here'}
                    />
                <div style={{display: 'flex', justifyContent:'flex-end', marginTop: 20}}>
                    <Button type="primary" onClick={onclick}>Annotate Query</Button>
                    <Button style={{marginLeft: 10}} onClick={onclear}>Clear</Button>
                </div>
                
            </div>
            <div className="plan-container">
                <Title level={3}>Execution Plan</Title>
                <TextArea value={plan} style={{height: 300}}/>
                {graph.length !== 0 && <Button type="primary" style={{marginTop: 20}} onClick={() => {setGraphVisible(true)}}>Visualise</Button>}
            </div>

        </div>
        {graphVisible && (<div>
            <ReactFlow elements={graph} style={{height: 400, marginTop: 20}} />
        </div>)}
      </>
    )
}
export default Container