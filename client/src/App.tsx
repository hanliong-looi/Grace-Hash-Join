import React, {useState} from 'react';
import {Button, Layout, Typography, Modal, Collapse} from 'antd';
import Container from './container'
import './App.css';

// const test_input = 'select * from customer C, orders O where C.c_custkey = O.o_custkey;'
const { Title, Paragraph } = Typography;
const { Header } = Layout;
const { Panel } = Collapse;

const App = () => {
    const [isModalVisible, setIsModalVisible] = useState(false);

    const showModal = () => {
        setIsModalVisible(true);
    };

    const handleOk = () => {
        setIsModalVisible(false);
    };

    const handleCancel = () => {
        setIsModalVisible(false);
    };
    return (
        <div className="App">
            <Header style={{display: 'flex', alignItems:'center', backgroundColor:'#fff', boxShadow: "0 2px 8px #f0f1f2"}}>
                <Title style={{marginBottom: 0}} level={2}>QEP Annotator - Group 41</Title>
                <Button style={{marginLeft: 21, marginTop: 3}} onClick={showModal} size="middle">Database Schema</Button> 
            </Header>
            <div style={{padding: '20px 40px'}}>
                <Container/>
            </div>
            <Modal cancelButtonProps={{style: {visibility:'hidden'}}} title="TPC-H Database Schema" visible={isModalVisible} onOk={handleOk} onCancel={handleCancel}>
            <Collapse>
                <Panel header="customer" key="1">
                    <Paragraph>c_custkey (integer)</Paragraph>
                    <Paragraph>c_name (character varying)</Paragraph>
                    <Paragraph>c_address (character varying)</Paragraph>
                    <Paragraph>c_nationkey (integer)</Paragraph>
                    <Paragraph>c_phone (character)</Paragraph>
                    <Paragraph>c_acctbal (numeric)</Paragraph>
                    <Paragraph>c_mktsegment (character)</Paragraph>
                    <Paragraph>c_comment (character varying)</Paragraph>
                </Panel>
                <Panel header="lineitem" key="2">
                    <Paragraph>l_orderkey (integer)</Paragraph>
                    <Paragraph>l_partkey (integer)</Paragraph>
                    <Paragraph>l_suppkey (integer)</Paragraph>
                    <Paragraph>l_linenumber (integer)</Paragraph>
                    <Paragraph>l_quantity (numric)</Paragraph>
                    <Paragraph>l_extendedprice (numeric)</Paragraph>
                    <Paragraph>l_discount (numeric)</Paragraph>
                    <Paragraph>l_tax (numeric)</Paragraph>
                    <Paragraph>l_returnflag (character)</Paragraph>
                    <Paragraph>l_linestatus (character)</Paragraph>
                    <Paragraph>l_shipdate (date)</Paragraph>
                    <Paragraph>l_commitdate (date)</Paragraph>
                    <Paragraph>l_receiptdate (date)</Paragraph>
                    <Paragraph>l_shipinstruct (character)</Paragraph>
                    <Paragraph>l_shipmode (character)</Paragraph>
                    <Paragraph>l_comment (character varying)</Paragraph>
                </Panel>
                <Panel header="nation" key="3">
                    <Paragraph>n_nationkey (integer)</Paragraph>
                    <Paragraph>n_name (character)</Paragraph>
                    <Paragraph>n_regionkey (integer)</Paragraph>
                    <Paragraph>n_comment (character varying)</Paragraph>
                </Panel>
                <Panel header="orders" key="4">
                    <Paragraph>o_orderkey (integer)</Paragraph>
                    <Paragraph>o_custkey (integer)</Paragraph>
                    <Paragraph>o_orderstatus (character)</Paragraph>
                    <Paragraph>o_totalprice (numeric)</Paragraph>
                    <Paragraph>o_orderdate (date)</Paragraph>
                    <Paragraph>o_orderpriority (character)</Paragraph>
                    <Paragraph>o_clerk (character)</Paragraph>
                    <Paragraph>o_shippriority (integer)</Paragraph>
                    <Paragraph>o_comment (character varying)</Paragraph>
                </Panel>
                <Panel header="part" key="5">
                    <Paragraph>p_partkey (integer)</Paragraph>
                    <Paragraph>p_name (character varying)</Paragraph>
                    <Paragraph>p_mfgr (character)</Paragraph>
                    <Paragraph>p_brand (character)</Paragraph>
                    <Paragraph>p_type (character varying)</Paragraph>
                    <Paragraph>p_size (integer)</Paragraph>
                    <Paragraph>p_container (character)</Paragraph>
                    <Paragraph>p_retailprice (numeric)</Paragraph>
                    <Paragraph>p_comment (character varying)</Paragraph>
                </Panel>
                <Panel header="partsupp" key="6">
                    <Paragraph>ps_partkey (integer)</Paragraph>
                    <Paragraph>ps_suppkey (integer)</Paragraph>
                    <Paragraph>ps_availqty (integer)</Paragraph>
                    <Paragraph>ps_supplycost (numeric)</Paragraph>
                    <Paragraph>ps_comment (character varying)</Paragraph>
                </Panel>
                <Panel header="region" key="7">
                    <Paragraph>r_regionkey (integer)</Paragraph>
                    <Paragraph>r_name (character)</Paragraph>
                    <Paragraph>r_comment (character varying)</Paragraph>
                </Panel>
                <Panel header="supplier" key="8">
                    <Paragraph>s_suppkey (integer)</Paragraph>
                    <Paragraph>s_name (character)</Paragraph>
                    <Paragraph>s_address (character varying)</Paragraph>
                    <Paragraph>s_nationkey (integer)</Paragraph>
                    <Paragraph>s_phone (character)</Paragraph>
                    <Paragraph>s_acctbal (numeric)</Paragraph>
                    <Paragraph>s_mktsegment (character)</Paragraph>
                    <Paragraph>s_comment (character varying)</Paragraph>
                </Panel>
            </Collapse>
            </Modal>
        </div>

)};

export default App;