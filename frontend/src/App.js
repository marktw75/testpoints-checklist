import React, { useState, useEffect } from 'react';
import { Layout, Menu, Card, Form, Input, Button, List, Checkbox } from 'antd';
import { PlusOutlined } from '@ant-design/icons';
import axios from 'axios';

const { Header, Content, Sider } = Layout;

function App() {
  const [modules, setModules] = useState([]);
  const [selectedModule, setSelectedModule] = useState(null);
  const [testItems, setTestItems] = useState([]);
  const [selectedItems, setSelectedItems] = useState([]);
  const [testPoints, setTestPoints] = useState([]);

  useEffect(() => {
    fetchModules();
  }, []);

  const fetchModules = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/modules');
      setModules(response.data);
    } catch (error) {
      console.error('Error fetching modules:', error);
    }
  };

  const fetchTestItems = async (moduleId) => {
    try {
      const response = await axios.get(`http://localhost:5000/api/modules/${moduleId}/test-items`);
      setTestItems(response.data);
    } catch (error) {
      console.error('Error fetching test items:', error);
    }
  };

  const handleModuleSelect = (module) => {
    setSelectedModule(module);
    fetchTestItems(module.id);
  };

  const handleItemSelect = (item) => {
    setSelectedItems(prev => {
      const exists = prev.find(i => i.id === item.id);
      if (exists) {
        return prev.filter(i => i.id !== item.id);
      }
      return [...prev, item];
    });
  };

  const generateTestPoints = async () => {
    try {
      const points = [];
      for (const item of selectedItems) {
        const response = await axios.get(`http://localhost:5000/api/test-items/${item.id}/test-points`);
        points.push(...response.data);
      }
      setTestPoints(points);
    } catch (error) {
      console.error('Error generating test points:', error);
    }
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header style={{ background: '#fff', padding: 0 }}>
        <h1 style={{ margin: '0 20px' }}>測試點檢查清單</h1>
      </Header>
      <Layout>
        <Sider width={300} style={{ background: '#fff' }}>
          <Menu
            mode="inline"
            selectedKeys={selectedModule ? [selectedModule.id.toString()] : []}
          >
            {modules.map(module => (
              <Menu.Item
                key={module.id}
                onClick={() => handleModuleSelect(module)}
              >
                {module.name}
              </Menu.Item>
            ))}
          </Menu>
        </Sider>
        <Content style={{ margin: '20px' }}>
          {selectedModule && (
            <Card title={selectedModule.name}>
              <List
                dataSource={testItems}
                renderItem={item => (
                  <List.Item>
                    <Checkbox
                      checked={selectedItems.some(i => i.id === item.id)}
                      onChange={() => handleItemSelect(item)}
                    >
                      {item.name}
                    </Checkbox>
                  </List.Item>
                )}
              />
              <Button
                type="primary"
                onClick={generateTestPoints}
                disabled={selectedItems.length === 0}
                style={{ marginTop: '20px' }}
              >
                生成測試點
              </Button>
            </Card>
          )}
          {testPoints.length > 0 && (
            <Card title="生成的測試點" style={{ marginTop: '20px' }}>
              <List
                dataSource={testPoints}
                renderItem={point => (
                  <List.Item>
                    {point.content}
                  </List.Item>
                )}
              />
            </Card>
          )}
        </Content>
      </Layout>
    </Layout>
  );
}

export default App; 