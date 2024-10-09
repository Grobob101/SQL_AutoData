import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import random
import string

def generate_random_string(length=10):
    """生成随机字符串"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_number(min_value, max_value):
    """生成指定范围内的随机整数"""
    return random.randint(min_value, max_value)

def generate_random_float(min_value, max_value):
    """生成指定范围内的随机浮点数"""
    return round(random.uniform(min_value, max_value), 2)

def generate_random_date():
    """生成随机日期"""
    year = random.randint(2000, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month:02d}-{day:02d}"

def generate_random_bool():
    """生成随机布尔值"""
    return random.choice([True, False])

def generate_random_data(data_type, length=None, sequence=None, min_value=None, max_value=None):
    """根据数据类型生成随机数据"""
    if sequence and length:
        # 从序列中随机选择字符，直到达到指定长度
        return f"'{''.join(random.choices(sequence, k=length))}'"
    if data_type.lower() == 'varchar' or data_type.lower() == 'text':
        return f"'{generate_random_string(length)}'"
    elif data_type.lower() == 'int':
        if min_value is not None and max_value is not None:
            return str(generate_random_number(min_value, max_value))
        return str(generate_random_number())
    elif data_type.lower() == 'float' or data_type.lower() == 'decimal':
        if min_value is not None and max_value is not None:
            return str(generate_random_float(min_value, max_value))
        return str(generate_random_float())
    elif data_type.lower() == 'date':
        return f"'{generate_random_date()}'"
    elif data_type.lower() == 'bool' or data_type.lower() == 'boolean':
        return str(generate_random_bool()).lower()

def add_field():
    field_name = simpledialog.askstring("输入字段名", "请输入字段名:")
    if not field_name:
        return
    data_type = simpledialog.askstring("输入数据类型", "请输入字段的数据类型 (varchar, int, float, date, bool):")
    if not data_type:
        return
    use_sequence = messagebox.askyesno("使用随机序列", "是否使用随机序列?")
    sequence = None
    if use_sequence:
        sequence_input = simpledialog.askstring("输入随机序列", "请输入随机序列 (英文逗号分隔):")
        if sequence_input:
            sequence = [item.strip() for item in sequence_input.split(',')]
    length = None
    if data_type.lower() in ['varchar', 'text']:
        if sequence:
            length = simpledialog.askinteger("指定长度", "请输入字段的长度:")
            if length is None or length <= 0:
                messagebox.showerror("错误", "长度必须大于0")
                return
    min_value = None
    max_value = None
    if data_type.lower() in ['int', 'float', 'decimal']:
        min_value = simpledialog.askinteger("最小值", "请输入最小值:", initialvalue=0)
        max_value = simpledialog.askinteger("最大值", "请输入最大值:", initialvalue=100)
        if min_value is None or max_value is None or min_value > max_value:
            messagebox.showerror("错误", "最小值必须小于或等于最大值")
            return

    # 将字段信息添加到列表
    fields.append((field_name, data_type, length, sequence, min_value, max_value))
    # 更新列表框显示
    display_text = f"{field_name} ({data_type})"
    if sequence:
        display_text += " (使用随机序列)"
    if length:
        display_text += f" (长度: {length})"
    if min_value and max_value:
        display_text += f" (范围: {min_value}-{max_value})"
    fields_listbox.insert(tk.END, display_text)

def delete_field():
    try:
        index = fields_listbox.curselection()[0]
        fields.pop(index)
        fields_listbox.delete(index)
    except IndexError:
        messagebox.showerror("错误", "请选择一个字段进行删除")

def generate_sql_file():
    """生成SQL文件"""
    table_name = table_name_entry.get().strip()  # 获取表名
    if not table_name:
        messagebox.showerror("错误", "表名不能为空")  # 如果表名为空，显示错误消息
        return

    num_rows = int(rows_entry.get().strip())  # 获取数据行数
    if num_rows <= 0:
        messagebox.showerror("错误", "数据行数必须大于0")  # 如果数据行数无效，显示错误消息
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".sql", filetypes=[("SQL files", "*.sql"), ("All files", "*.*")])  # 选择保存路径
    if not output_path:
        return  # 如果没有选择路径，返回

    with open(output_path, 'w', encoding='utf-8') as file:
        for _ in range(num_rows):
            # 生成每个字段的随机数据
            values = [generate_random_data(field[1], field[2], field[3], field[4], field[5]) for field in fields]
            # 构建字段名和值的字符串
            field_names = ', '.join([field[0] for field in fields])
            value_str = ', '.join(values)
            sql = f"INSERT INTO {table_name} ({field_names}) VALUES ({value_str});\n"  # 构建SQL插入语句
            file.write(sql)  # 将SQL语句写入文件

    messagebox.showinfo("成功", f"数据已生成并保存到 {output_path}")  # 显示成功消息

# 创建主窗口
root = tk.Tk()
root.title("SQL数据生成器")

# 表名输入
tk.Label(root, text="表名:").grid(row=0, column=0, padx=10, pady=10)
table_name_entry = tk.Entry(root)
table_name_entry.grid(row=0, column=1, padx=10, pady=10)

# 数据行数输入
tk.Label(root, text="数据行数:").grid(row=1, column=0, padx=10, pady=10)
rows_entry = tk.Entry(root)
rows_entry.grid(row=1, column=1, padx=10, pady=10)

# 字段列表
fields = []
tk.Label(root, text="字段列表:").grid(row=2, column=0, padx=10, pady=10)
fields_listbox = tk.Listbox(root, height=10, width=50)
fields_listbox.grid(row=2, column=1, padx=10, pady=10)

# 添加字段按钮
add_field_button = tk.Button(root, text="添加字段", command=add_field)
add_field_button.grid(row=3, column=1, padx=10, pady=10)

# 删除字段按钮
delete_field_button = tk.Button(root, text="删除字段", command=delete_field)
delete_field_button.grid(row=4, column=1, padx=10, pady=10)

# 生成SQL文件按钮
generate_button = tk.Button(root, text="生成SQL文件", command=generate_sql_file)
generate_button.grid(row=5, column=1, padx=10, pady=10)

# 运行主循环
root.mainloop()