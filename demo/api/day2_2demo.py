from openai import OpenAI
# pip install openai==1.40.3
import os
# 从环境变量中读取OPENAI_BASE_URL
print(os.getenv('OPENAI_BASE_URL'))
# 初始化 OpenAI 服务。
client = OpenAI()   #使用环境变量 OPENAI_API_KEY 和 OPENAI_BASE_URL 进行配置
completion = client.chat.completions.create(    #调用 chat.completions 接口 的 create 方法
    model="gpt-4o",     #指定使用的模型

    response_format={"type": "json_object"}, #指定响应格式为 JSON 对象
    seed = 40,    #设置随机种子以确保结果可重复
    n = 3,   #要生成的回答数量

    messages=[
        {"role": "system", "content": "assistant"},     #系统角色消息
        {"role": "user", "content": "Hello"}        #用户角色消息
    ]
)
print(completion.choices[0].message.content)