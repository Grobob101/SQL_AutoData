# SQL模拟数据生成小能手，你可以下载.exe文件直接在你的电脑中运行
## **注意**：
- 如果选择了序列，那么随机数据只会从你写的序列中生成，比如你输入了(直接输入就行不用加“”,同时注意用英文逗号隔开):王,明,飞，那么只会生成下面的数据：王明，王飞飞。。。
  ![image](https://github.com/user-attachments/assets/5ea01643-0983-4642-93aa-3c816f7b46c7)

- 如果是int，double类型的话，可以指定范围数据。

下面演示生成学生信息表 学生姓名，年龄，年级，专业
这是最终生成结果
  ![image](https://github.com/user-attachments/assets/87f69782-5e84-4e92-a193-ef05e5163009)
  
1.输入表名student，确定行数：
![image](https://github.com/user-attachments/assets/f9b65ca4-e869-4a7c-a284-1f1fd6aa033a)

2.点击添加name字段，设置类型varchar(这里varchar和char都可以选择varchar类型)，设置序列，设置名字长度
![image](https://github.com/user-attachments/assets/2518a7c4-b3bb-40da-8099-301a89fae99c)
![image](https://github.com/user-attachments/assets/5ac19625-8fee-49f5-8169-ca92de30d3f0)
3.添加age字段，如果是int数据的话就不要选随机序列了，设置范围就行，添加年级和这里的一样
![image](https://github.com/user-attachments/assets/fd3e40ed-6b0d-4590-a81f-f03d44e27491)
4.添加专业，专业这里需要选随机序列，不过是把每个专业隔开同时字段长度设为1
![image](https://github.com/user-attachments/assets/2897ad29-dfbb-4822-a525-bb42eadb89f4)

![image](https://github.com/user-attachments/assets/6d490e29-8af7-42ed-ba9d-7e3f0f743d5f)
运行结果如下：
![image](https://github.com/user-attachments/assets/b43da7d2-d44b-4b4b-a1d2-6b1f27b27569)






