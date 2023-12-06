import pandas as pd
from chatgpt_api import analyze_text_with_chatgpt
import logging

# 设置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)

# set version of chatgpt
# chatgpt_version = "gpt-3.5-turbo-1106"
chatgpt_version="gpt-4-1106-preview"

# set system_prompt for chatgpt
prompt_path = './interview_system_prompt.txt'
with open(prompt_path, 'r') as f:
    system_prompt = f.read()

# 读取 Excel 文件
input_file_path = './data/input_file_1.xlsx'
output_file_path = './data/output_file_1_gpt4.xlsx'

df = pd.read_excel(input_file_path)

# 在 DataFrame 中添加一个新列用于保存分析结果
df['AI_Analysis'] = df['Transcription'].apply(lambda transcription:
    analyze_text_with_chatgpt(transcription, system_prompt, chatgpt_version)
)

# 保存为新的 Excel 文件
logging.info("保存数据到 %s", output_file_path)
df.to_excel(output_file_path, index=False)
