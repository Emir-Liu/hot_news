from duckduckgo_search import DDGS
import json
from typing import List


def duck_search(query:str) -> List[dict]:

    # 使用duckduckgo搜索引擎
    search_res_list = []
    print(f'开始搜索')
    try:
        ddgs_generator = DDGS().news(keywords=query, max_results=5)
        for ans_id, tmp_ans in enumerate(ddgs_generator):
            print(f'{tmp_ans}')
            # add http prefix
            url = tmp_ans['url']
            if 'http' in url:
                pass
            else:
                new_url = 'http://' + url
                tmp_ans['url'] = new_url
            print(f'{tmp_ans}')
            search_res_list.append(tmp_ans)
    except Exception as e:
        print(f'搜索引擎接口使用超过限制')
        search_res_list = []

    print(f'搜索结果:{search_res_list}')

    return search_res_list

def save_search_res(query:str, data:List[dict]):
    file_name = f'{query}.json'
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print(f"数据已成功写入到 {file_name} 文件中。")


if __name__ == '__main__':
    # query = '纺织'
    query = 'AI科技'
    search_res = duck_search(query=query)
    save_search_res(query=query, data=search_res)

    
