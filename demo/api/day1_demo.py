import os   
import http.client
import json


conn = http.client.HTTPSConnection("api.openai-hk.com")  #建立 HTTPS 连接
payload = json.dumps({  #将python字典转换为 JSON 字符串
   "model": "gpt-3.5-turbo",  #指定使用的模型
   "messages": [   #对话消息列表
      {
         "role": "system",    #系统角色消息
         "content": "You are a helpful assistant."  #系统消息内容
      },
      {
         "role": "user",    #用户角色消息
         "content": "Hello!"  #用户消息内容
      }
   ]
})
headers = {  #请求头信息
   'Accept': 'application/json',  #接受的响应格式
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',  #用户代理信息
   'Content-Type': 'application/json',  #请求体格式
   'Authorization': 'Bearer ' + os.getenv('OPENAI_API_KEY'),  #授权信息，使用环境变量中的 API 密钥
   'Host': 'api.openai-hk.com',  #主机名
   'Connection': 'keep-alive'  #连接类型
}
conn.request("POST", "/v1/chat/completions", payload, headers)    #发送 POST 请求
res = conn.getresponse()  #获取响应
data = res.read()  #读取响应数据
print(data.decode("utf-8"))  #解码并打印响应数据

