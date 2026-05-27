# 智能体Demo配置 - 客服助手

## 智能体基本信息
- **名称**: 客服助手
- **描述**: 一个能够处理客户咨询的AI客服智能体
- **版本**: V1.0
- **创建者**: [你的名字]

## 基于Coze/Dify的配置

### 1. 基础设置
```json
{
  "agent_name": "客服助手",
  "description": "处理客户咨询的智能客服",
  "model": "gpt-3.5-turbo",
  "temperature": 0.7,
  "max_tokens": 1000,
  "language": "zh-CN"
}
```

### 2. Prompt模板
```
你是一个专业的客服助手,负责回答客户的问题并提供帮助。

你的能力包括:
1. 回答产品相关问题
2. 处理订单查询
3. 提供技术支持
4. 收集客户反馈

回答要求:
- 使用友好、专业的语气
- 回答要准确、简洁
- 如果遇到无法回答的问题,引导客户联系人工客服
- 始终保持积极的态度

客户问题: {user_question}
```

### 3. 工具配置

#### 3.1 知识库工具
```json
{
  "tool_name": "knowledge_base",
  "type": "search",
  "config": {
    "index_name": "product_faq",
    "top_k": 5,
    "similarity_threshold": 0.8
  }
}
```

#### 3.2 订单查询工具
```json
{
  "tool_name": "order_query",
  "type": "api",
  "config": {
    "endpoint": "/api/v1/orders",
    "method": "GET",
    "parameters": ["order_id", "user_id"]
  }
}
```

#### 3.3 工单创建工具
```json
{
  "tool_name": "ticket_create",
  "type": "api",
  "config": {
    "endpoint": "/api/v1/tickets",
    "method": "POST",
    "parameters": ["user_id", "issue_type", "description"]
  }
}
```

### 4. 工作流设计

```
用户提问
  |
  v
[意图识别]
  |
  +-----> [产品咨询] -----> [查询知识库] -----> [生成回答]
  |
  +-----> [订单查询] -----> [调用订单API] -----> [返回订单信息]
  |
  +-----> [技术问题] -----> [查询技术文档] -----> [提供解决方案]
  |
  +-----> [投诉建议] -----> [创建工单] -----> [返回工单号]
  |
  v
[生成最终回答]
  |
  v
返回给用户
```

### 5. 测试用例

| 测试场景 | 输入 | 预期输出 |
|----------|------|----------|
| 产品咨询 | "这个产品多少钱?" | 返回产品价格信息 |
| 订单查询 | "查询订单12345" | 返回订单状态和详情 |
| 技术问题 | "如何安装软件?" | 提供安装步骤指南 |
| 投诉建议 | "我要投诉" | 创建工单并返回工单号 |
| 未知问题 | "天气怎么样?" | 引导联系人工客服 |

### 6. 部署配置

#### 6.1 环境变量
```bash
OPENAI_API_KEY=your-api-key
DATABASE_URL=your-database-url
REDIS_URL=your-redis-url
```

#### 6.2 启动命令
```bash
# 使用Dify部署
dify deploy --config agent_config.yaml

# 使用Coze部署
coze publish --agent-id agent_123
```

### 7. 监控指标

- **响应时间**: < 2秒
- **准确率**: > 85%
- **用户满意度**: > 4.0/5.0
- **日均处理量**: 1000+ 对话

### 8. 迭代计划

#### V1.1 (下周)
- 增加多语言支持
- 优化响应速度
- 增加更多知识库内容

#### V1.2 (下下周)
- 增加语音识别功能
- 集成更多外部工具
- 优化意图识别准确率