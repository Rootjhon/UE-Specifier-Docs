#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   yaml2Markdown.py
@Time    :   2024/01/05 10:07:18
@Author  :   JunQiang
@Contact :   junqiang.mail@qq.com
@Desc    :   
"""

# here put the import lib
import os
import yaml

def read_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        yaml_str = file.read()
    return yaml_str

def yaml_to_markdown(yaml_path):
    try:
      yaml_str = read_yaml_file(yaml_path)
      fragments = yaml_str.split("###############################################################################")
      for fragment in fragments:
          if not fragment.strip():
              continue
          data = yaml.safe_load(fragment)
          if type(data) == list:
              items = data
          else:
              items = data.get('specifiers',[])
              pass
          
          # specifiers = data['specifiers']

          for item in items:
              name = item['name']
              position = item['position']
              prop_type = item['type']
              related = ', '.join(item.get('related', []))
              doc_text = item['documentation']['text']
              doc_source = item['documentation']['source']
              sample = str(item.get('samples', "")).strip()

              markdown_str = f"""### $UPROPERTY(meta=($ {name} $))$

      **Position:** ${position}$

      **Type:**  ${prop_type}$

      **Related:**  ${related}$

      > {doc_text}
      >
      > - [Unreal Documentation]({doc_source})

      ```cpp
      {sample}
      ```

      """ 
          print(markdown_str,flush=True)
          pass
      
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        pass
    pass

if __name__ == "__main__":
    yaml_to_markdown(f"{os.path.dirname(__file__)}/yaml/uproperty.yml")
    pass
