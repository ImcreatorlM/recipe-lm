import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ZAI_API_KEY")

URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
MODEL = "glm-4-flash"


def get_recipe(dish: str) -> dict:
    """输入菜名，返回解析好的菜谱 dict。失败时抛异常。"""
    if not API_KEY:
        raise RuntimeError("没有读到 ZAI_API_KEY，请检查项目文件夹里的 .env")

    dish = dish.strip() or "番茄炒蛋"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "你是一个家常菜谱助手。请只输出一个 JSON 对象，不要输出任何解释、不要用 markdown 代码块。",
            },
            {
                "role": "user",
                "content": (
                    f"请为「{dish}」生成一道适合新手的家常菜谱。"
                    "JSON 必须包含字段：title（菜名）、time（耗时）、difficulty（难度）、"
                    "ingredients（数组，每项含 name 和 amount）、steps（字符串数组）。"
                ),
            },
        ],
        "temperature": 0.3,
    }

    resp = requests.post(URL, headers=headers, json=data, timeout=30)
    if resp.status_code != 200:
        raise RuntimeError(f"接口返回状态码 {resp.status_code}：{resp.text[:200]}")

    content = resp.json()["choices"][0]["message"]["content"]

    # 清洗：去掉可能存在的 markdown 代码块标记
    content = content.strip()
    if content.startswith("```"):
        content = content.strip("`")
        if content.startswith("json"):
            content = content[4:]
        content = content.strip()

    try:
        recipe = json.loads(content)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"模型没有返回纯 JSON：{e}\n原始输出：{content[:300]}")

    return recipe


def _print_recipe(recipe: dict) -> None:
    print("菜名:", recipe["title"])
    print("耗时:", recipe["time"])
    print("难度:", recipe["difficulty"])
    print("食材:")
    for item in recipe["ingredients"]:
        print(f"  - {item['name']}: {item['amount']}")
    print("步骤:")
    for i, step in enumerate(recipe["steps"], 1):
        print(f"  {i}. {step}")


if __name__ == "__main__":
    dish = input("想吃什么？输入菜名或现有食材（直接回车默认：番茄炒蛋）：").strip()
    try:
        recipe = get_recipe(dish)
    except Exception as e:
        print("\n--- 失败 ---")
        print(e)
    else:
        print("\n--- 解析成功 ---")
        _print_recipe(recipe)
