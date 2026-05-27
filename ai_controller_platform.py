#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI中控平台 - API调用演示脚本
功能: 模拟AI智能体管理平台的API调用功能
作者: [你的名字]
用途: 面试演示 - 展示Python编程、API调用、JSON处理能力
"""

import json
import requests
from datetime import datetime

class AIControllerPlatform:
    """AI中控平台核心类"""
    
    def __init__(self, api_base_url="https://api.openai.com/v1"):
        self.api_base_url = api_base_url
        self.agents = []  # 智能体列表
        self.tools = []   # 工具列表
        
    def call_api(self, endpoint, method="GET", data=None):
        """
        通用API调用方法
        展示HTTP请求处理和JSON数据解析能力
        """
        url = f"{self.api_base_url}/{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer your-api-key-here"
        }
        
        try:
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=data)
            elif method == "PUT":
                response = requests.put(url, headers=headers, json=data)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers)
                
            # 处理JSON响应
            if response.status_code == 200:
                return response.json()  # 解析JSON数据
            else:
                return {"error": f"HTTP {response.status_code}", "message": response.text}
                
        except requests.exceptions.RequestException as e:
            return {"error": "网络请求失败", "details": str(e)}
    
    def create_agent(self, name, description, model="gpt-3.5-turbo"):
        """创建AI智能体 - 对应岗位要求的'搭建智能体Demo'"""
        agent = {
            "id": f"agent_{len(self.agents) + 1}",
            "name": name,
            "description": description,
            "model": model,
            "status": "active",
            "created_at": datetime.now().isoformat(),
            "tools": [],
            "permissions": ["read", "write"]
        }
        self.agents.append(agent)
        return agent
    
    def manage_tools(self, action, tool_name=None, tool_config=None):
        """
        工具管理功能 - 对应岗位要求的'工具管理'
        action: add/remove/list
        """
        if action == "add" and tool_config:
            tool = {
                "name": tool_name,
                "config": tool_config,
                "status": "enabled",
                "added_at": datetime.now().isoformat()
            }
            self.tools.append(tool)
            return {"status": "success", "tool": tool}
            
        elif action == "list":
            return {"status": "success", "tools": self.tools}
            
        elif action == "remove" and tool_name:
            self.tools = [t for t in self.tools if t["name"] != tool_name]
            return {"status": "success", "message": f"工具 {tool_name} 已移除"}
    
    def monitor_api_calls(self):
        """
        API调用监控 - 对应岗位要求的'调监控'
        模拟监控数据返回
        """
        return {
            "timestamp": datetime.now().isoformat(),
            "metrics": {
                "total_calls": 1250,
                "success_rate": 98.5,
                "avg_response_time": "0.45s",
                "error_count": 19,
                "active_agents": len(self.agents),
                "enabled_tools": len(self.tools)
            }
        }
    
    def generate_prd_template(self, product_name):
        """
        生成PRD模板 - 对应岗位要求的'写PRD'
        """
        prd = {
            "product_name": product_name,
            "version": "1.0.0",
            "author": "[你的名字]",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "overview": {
                "background": "产品背景说明",
                "objective": "产品目标",
                "target_users": "目标用户群体"
            },
            "features": [
                {
                    "feature_name": "核心功能1",
                    "description": "功能描述",
                    "priority": "P0",
                    "status": "规划中"
                }
            ],
            "technical_requirements": {
                "api_endpoints": [],
                "data_models": [],
                "security": "权限控制要求"
            }
        }
        return prd

# 演示使用
if __name__ == "__main__":
    print("=== AI中控平台功能演示 ===\n")
    
    # 1. 初始化平台
    platform = AIControllerPlatform()
    print("1. 平台初始化完成")
    
    # 2. 创建智能体
    agent1 = platform.create_agent("客服助手", "处理客户咨询的智能客服")
    agent2 = platform.create_agent("内容生成器", "自动生成营销内容的AI")
    print(f"2. 创建智能体: {agent1['name']}, {agent2['name']}")
    
    # 3. 工具管理
    platform.manage_tools("add", "web_search", {"api_key": "xxx", "max_results": 10})
    platform.manage_tools("add", "image_gen", {"model": "dall-e-3", "size": "1024x1024"})
    tools = platform.manage_tools("list")
    print(f"3. 工具管理: 已添加 {len(tools['tools'])} 个工具")
    
    # 4. API监控
    metrics = platform.monitor_api_calls()
    print(f"4. API监控: 成功率 {metrics['metrics']['success_rate']}%")
    
    # 5. PRD生成
    prd = platform.generate_prd_template("AI智能体管理平台")
    print(f"5. PRD模板生成: {prd['product_name']}")
    
    # 6. JSON数据处理演示
    json_data = json.dumps(platform.agents, indent=2, ensure_ascii=False)
    print(f"\n6. JSON数据处理演示:")
    print(json_data[:200] + "...")  # 只打印部分内容
    
    print("\n=== 演示完成 ===")
    print("这个脚本展示了:")
    print("- Python编程能力")
    print("- HTTP API调用")
    print("- JSON数据处理")
    print("- 类和方法设计")
    print("- 异常处理")
    print("- 面向对象编程")